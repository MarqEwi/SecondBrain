#!/usr/bin/env python3
"""
Inventar eines Ordners (z. B. gespiegelter Google-Drive-Ordner). Reiner Lesezugriff.

Aufruf:
  python scripts/inventar.py "<Pfad zum Ordner>" --thema "Kapitalanlage-Immobilie"

Erzeugt in <Vault>/Attachments/inventar/:
  Inventar <Thema> <Datum>.csv   alle Dateien: Pfad, Größe, Datum, SHA-256, Typ, Hinweise
  Inventar <Thema> <Datum>.md    Zusammenfassung mit Vorprüfungen, Duplikaten, Ordnerbaum

Prüft nebenbei:
  - Google-Drive-Platzhalter (gestreamt statt gespiegelt) und .gdoc/.gsheet-Stubs
  - ob der Vault innerhalb des gescannten Ordners liegt
  - PDFs ohne Textebene (braucht das Paket pypdf, sonst "nicht geprüft")

Es wird nichts im gescannten Ordner verändert.
"""
import argparse
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

try:
    from pypdf import PdfReader  # optional
except Exception:  # pragma: no cover
    PdfReader = None

SKIP_NAMES = {"desktop.ini", "thumbs.db", ".ds_store", ".gitkeep"}
SKIP_PREFIX = ("~$", ".tmp.drive", "._")
SKIP_DIRS = {".git", ".obsidian", ".tmp.driveupload", ".tmp.drivedownload", "@eaDir"}
GOOGLE_STUBS = {".gdoc", ".gsheet", ".gslides", ".gform", ".gdraw", ".gmap", ".gsite", ".glink"}

# Windows-Dateiattribute (Cloud-Platzhalter)
FILE_ATTRIBUTE_OFFLINE = 0x1000
FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS = 0x400000
FILE_ATTRIBUTE_RECALL_ON_OPEN = 0x40000

EXT_TYPES = {
    ".pdf": "PDF", ".docx": "Word", ".doc": "Word", ".odt": "Text", ".rtf": "Text", ".txt": "Text", ".md": "Text",
    ".xlsx": "Tabelle", ".xls": "Tabelle", ".csv": "Tabelle", ".ods": "Tabelle",
    ".pptx": "Präsentation", ".ppt": "Präsentation",
    ".jpg": "Bild", ".jpeg": "Bild", ".png": "Bild", ".heic": "Bild", ".gif": "Bild", ".tif": "Bild", ".tiff": "Bild", ".webp": "Bild",
    ".msg": "E-Mail", ".eml": "E-Mail",
    ".zip": "Archiv", ".rar": "Archiv", ".7z": "Archiv",
    ".mp4": "Video", ".mov": "Video", ".mp3": "Audio", ".m4a": "Audio",
}

# Dokumentart aus dem Dateinamen (Reihenfolge = Priorität)
KEYWORDS = [
    ("Kaufvertrag", r"kaufvertrag|notar|beurkund"),
    ("Grundbuch", r"grundbuch|auflassung|grundschuld"),
    ("Teilungserklärung", r"teilungserkl"),
    ("Darlehen", r"darlehen|kredit|finanzierung|tilgung|zinsbind|annuit"),
    ("Mietvertrag", r"mietvertrag|mieter|übergabeprotokoll|uebergabeprotokoll"),
    ("Hausgeld/WEG", r"hausgeld|weg[-_ ]|eigentümerversammlung|eigentuemerversammlung|wirtschaftsplan|jahresabrechnung|hausverwaltung|verwalter"),
    ("Nebenkostenabrechnung", r"nebenkosten|betriebskosten|nk[-_ ]abrechnung"),
    ("Steuer", r"steuer|elster|anlage v|afa|einkommensteuer|grundsteuer|umsatzsteuer|est[-_ ]"),
    ("Versicherung", r"versicherung|police|gebäudevers|haftpflicht"),
    ("Kontoauszug", r"kontoauszug|umsatz|auszug"),
    ("Rechnung", r"rechnung|invoice|quittung|beleg"),
    ("Exposé", r"expos[ée]|angebot"),
    ("Gutachten", r"gutachten|energieausweis|wertermittlung"),
    ("Protokoll", r"protokoll"),
    ("Vertrag", r"vertrag|agb|vereinbarung"),
    ("Gewerbe", r"gewerbe|handelsregister|ihk|finanzamt|ust[-_ ]id"),
    ("Schriftverkehr", r"schreiben|brief|mail|anschreiben"),
]

DATE_RE = re.compile(r"(20\d{2})[-_. ]?(0[1-9]|1[0-2])(?:[-_. ]?(0[1-9]|[12]\d|3[01]))?")


def sha256(path: Path, chunk=1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def is_placeholder(path: Path) -> bool:
    try:
        st = path.stat()
        attrs = getattr(st, "st_file_attributes", 0)
        return bool(attrs & (FILE_ATTRIBUTE_OFFLINE | FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS | FILE_ATTRIBUTE_RECALL_ON_OPEN))
    except OSError:
        return False


def google_stub_url(path: Path) -> str:
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
        return data.get("url", "")
    except Exception:
        return ""


def pdf_text_status(path: Path) -> str:
    if PdfReader is None:
        return "nicht geprüft (pypdf fehlt)"
    try:
        reader = PdfReader(str(path))
        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception:
                return "verschlüsselt"
        text = ""
        for page in reader.pages[:3]:
            text += page.extract_text() or ""
            if len(text.strip()) > 40:
                return "Text vorhanden"
        return "kein Text (OCR nötig)" if len(text.strip()) <= 40 else "Text vorhanden"
    except Exception as e:  # kaputte oder exotische PDFs
        return f"nicht lesbar ({type(e).__name__})"


def guess_doctype(name: str) -> str:
    low = name.lower()
    for label, pattern in KEYWORDS:
        if re.search(pattern, low):
            return label
    return ""


def guess_date(name: str) -> str:
    m = DATE_RE.search(name)
    if not m:
        return ""
    y, mo, d = m.group(1), m.group(2), m.group(3)
    return f"{y}-{mo}-{d}" if d else f"{y}-{mo}"


def human(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} GB"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root", help="Zu inventarisierender Ordner (nur lesen)")
    ap.add_argument("--thema", default="Ablage", help="Name für die Ausgabedateien")
    ap.add_argument("--vault", default=None, help="Vault-Pfad (Standard: Ordner über scripts/)")
    ap.add_argument("--out", default=None, help="Ausgabeordner (Standard: <Vault>/Attachments/inventar)")
    ap.add_argument("--max-rows-md", type=int, default=400, help="Max. Zeilen der Tabelle in der Markdown-Zusammenfassung")
    args = ap.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        sys.exit(f"Ordner nicht gefunden: {root}")
    vault = Path(args.vault).resolve() if args.vault else Path(__file__).resolve().parent.parent
    out_dir = Path(args.out).resolve() if args.out else vault / "Attachments" / "inventar"
    out_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    safe_thema = re.sub(r'[:/\\#^\[\]|]', "-", args.thema)
    csv_path = out_dir / f"Inventar {safe_thema} {today}.csv"
    md_path = out_dir / f"Inventar {safe_thema} {today}.md"

    # Vorprüfung: Vault im Drive-Ordner?
    vault_inside = False
    try:
        vault.relative_to(root)
        vault_inside = True
    except ValueError:
        pass
    if out_dir.resolve().is_relative_to(root):
        sys.exit("Ausgabeordner liegt im gescannten Ordner. Bitte --out außerhalb wählen.")

    rows = []
    placeholders = 0
    stubs = 0
    pdf_no_text = 0
    pdf_unchecked = 0
    errors = []
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fn in sorted(filenames):
            if fn.lower() in SKIP_NAMES or fn.startswith(SKIP_PREFIX):
                continue
            p = Path(dirpath) / fn
            rel = p.relative_to(root).as_posix()
            ext = p.suffix.lower()
            hints = []
            try:
                st = p.stat()
            except OSError as e:
                errors.append(f"{rel}: {e}")
                continue
            size = st.st_size
            mtime = datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M")
            ftype = EXT_TYPES.get(ext, ext.lstrip(".").upper() or "ohne Endung")
            digest = ""
            if ext in GOOGLE_STUBS:
                stubs += 1
                ftype = "Google-Dokument (nur Link)"
                url = google_stub_url(p)
                hints.append(f"Online-Dokument, nicht lokal lesbar{': ' + url if url else ''}")
            elif is_placeholder(p):
                placeholders += 1
                hints.append("Platzhalter: Drive ist auf 'gestreamt', Inhalt nicht lokal")
            else:
                try:
                    digest = sha256(p)
                except OSError as e:
                    errors.append(f"{rel}: {e}")
                    hints.append("nicht lesbar")
                if size == 0:
                    hints.append("leere Datei")
                if ext == ".pdf" and digest:
                    status = pdf_text_status(p)
                    if status.startswith("kein Text"):
                        pdf_no_text += 1
                    elif status.startswith("nicht geprüft"):
                        pdf_unchecked += 1
                    if status != "Text vorhanden":
                        hints.append(status)
            total_size += size
            rows.append({
                "pfad": rel,
                "ordner": Path(rel).parent.as_posix() if "/" in rel else "",
                "datei": fn,
                "endung": ext,
                "typ": ftype,
                "dokumentart": guess_doctype(fn) or guess_doctype(rel),
                "datum_im_namen": guess_date(fn),
                "groesse_bytes": size,
                "groesse": human(size),
                "geaendert": mtime,
                "sha256": digest,
                "duplikat_von": "",
                "hinweise": "; ".join(hints),
            })

    # Duplikate per Prüfsumme
    by_hash = defaultdict(list)
    for r in rows:
        if r["sha256"]:
            by_hash[r["sha256"]].append(r)
    dup_groups = [g for g in by_hash.values() if len(g) > 1]
    for g in dup_groups:
        g.sort(key=lambda r: (r["geaendert"], r["pfad"]))
        first = g[0]["pfad"]
        for r in g[1:]:
            r["duplikat_von"] = first
    dup_files = sum(len(g) - 1 for g in dup_groups)
    dup_bytes = sum(g[0]["groesse_bytes"] * (len(g) - 1) for g in dup_groups)

    # CSV (Excel-freundlich: Semikolon, BOM)
    fields = list(rows[0].keys()) if rows else ["pfad"]
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter=";")
        w.writeheader()
        w.writerows(rows)

    # Markdown-Zusammenfassung
    by_type = Counter(r["typ"] for r in rows)
    by_doc = Counter(r["dokumentart"] or "(unerkannt)" for r in rows)
    top_folders = Counter()
    for r in rows:
        parts = r["pfad"].split("/")
        top_folders["/".join(parts[:2]) if len(parts) > 2 else (parts[0] if len(parts) > 1 else "(Wurzel)")] += 1
    years = Counter(r["datum_im_namen"][:4] for r in rows if r["datum_im_namen"])

    def ok(flag, good, bad):
        return f"✅ {good}" if flag else f"⚠️ {bad}"

    L = []
    L.append("---")
    L.append("type: inventar")
    L.append(f"thema: {args.thema}")
    L.append(f"quelle: \"{root}\"")
    L.append(f"created: {today}")
    L.append("tags:\n  - inventar\n  - drive")
    L.append("---")
    L.append(f"# Inventar {args.thema} ({today})")
    L.append("")
    L.append(f"Quelle: `{root}`  ")
    L.append(f"Vollständige Liste: `{csv_path.name}` (gleicher Ordner, Semikolon-getrennt, öffnet in Excel)")
    L.append("")
    L.append("## Vorprüfung")
    L.append(f"- Google Drive gespiegelt: {ok(placeholders == 0, 'keine Platzhalter gefunden', f'{placeholders} Platzhalter, Drive steht auf gestreamt oder Dateien sind nicht heruntergeladen')}")
    L.append(f"- Vault außerhalb des Drive-Ordners: {ok(not vault_inside, str(vault), 'Vault liegt IM gescannten Ordner: ' + str(vault))}")
    if pdf_unchecked:
        L.append(f"- PDF-Textebene: ⚠️ {pdf_unchecked} PDFs nicht geprüft, Paket fehlt (`pip install pypdf`), dann erneut laufen lassen")
    else:
        L.append(f"- PDF-Textebene: {ok(pdf_no_text == 0, 'alle PDFs haben Text', f'{pdf_no_text} PDFs ohne Textebene, OCR nötig (Liste unten)')}")
    if stubs:
        L.append(f"- Google-eigene Dokumente (Docs/Sheets): {stubs} Stück, nur als Link vorhanden. Für Steckbriefe müssten sie als PDF/Docx exportiert werden.")
    L.append("")
    L.append("## Überblick")
    L.append(f"- Dateien: **{len(rows)}**, Gesamtgröße **{human(total_size)}**")
    L.append(f"- Duplikate: **{dup_files}** Dateien in {len(dup_groups)} Gruppen, {human(dup_bytes)} doppelt")
    if errors:
        L.append(f"- Nicht lesbar: {len(errors)} (siehe unten)")
    L.append("")
    L.append("### Nach Dateityp")
    L.append("| Typ | Anzahl |\n|---|---|")
    for k, v in by_type.most_common():
        L.append(f"| {k} | {v} |")
    L.append("")
    L.append("### Nach erkannter Dokumentart (aus dem Dateinamen, nur ein Hinweis)")
    L.append("| Dokumentart | Anzahl |\n|---|---|")
    for k, v in by_doc.most_common():
        L.append(f"| {k} | {v} |")
    L.append("")
    if years:
        L.append("### Jahre im Dateinamen")
        L.append("| Jahr | Anzahl |\n|---|---|")
        for k, v in sorted(years.items()):
            L.append(f"| {k} | {v} |")
        L.append("")
    L.append("### Ordner (bis zwei Ebenen)")
    L.append("| Ordner | Dateien |\n|---|---|")
    for k, v in sorted(top_folders.items()):
        L.append(f"| {k} | {v} |")
    L.append("")
    if dup_groups:
        L.append("## Duplikate (gleiche Prüfsumme)")
        for g in sorted(dup_groups, key=lambda g: -g[0]["groesse_bytes"]):
            L.append(f"- **{g[0]['datei']}** ({g[0]['groesse']})")
            for r in g:
                L.append(f"  - `{r['pfad']}` ({r['geaendert']})")
        L.append("")
    no_text = [r for r in rows if "kein Text" in r["hinweise"]]
    if no_text:
        L.append("## PDFs ohne Textebene (OCR nötig)")
        for r in no_text:
            L.append(f"- `{r['pfad']}` ({r['groesse']})")
        L.append("")
    ph = [r for r in rows if "Platzhalter" in r["hinweise"]]
    if ph:
        L.append("## Platzhalter (nicht lokal vorhanden)")
        for r in ph[:100]:
            L.append(f"- `{r['pfad']}`")
        if len(ph) > 100:
            L.append(f"- ... und {len(ph) - 100} weitere")
        L.append("")
    if errors:
        L.append("## Nicht lesbar")
        for e in errors:
            L.append(f"- {e}")
        L.append("")
    L.append("## Alle Dateien")
    if len(rows) > args.max_rows_md:
        L.append(f"Nur die ersten {args.max_rows_md} von {len(rows)} Zeilen, Rest in der CSV.")
    L.append("| Pfad | Typ | Dokumentart | Datum | Größe | Geändert | Hinweise |\n|---|---|---|---|---|---|---|")
    for r in rows[: args.max_rows_md]:
        hint = r["hinweise"]
        if r["duplikat_von"]:
            hint = (hint + "; " if hint else "") + f"Duplikat von {r['duplikat_von']}"
        L.append(f"| `{r['pfad']}` | {r['typ']} | {r['dokumentart']} | {r['datum_im_namen']} | {r['groesse']} | {r['geaendert']} | {hint} |")
    md_path.write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"Dateien: {len(rows)}  Größe: {human(total_size)}  Duplikate: {dup_files}  "
          f"Platzhalter: {placeholders}  PDFs ohne Text: {pdf_no_text}  Stubs: {stubs}")
    print(f"CSV: {csv_path}")
    print(f"MD:  {md_path}")
    if placeholders:
        print("WARNUNG: Platzhalter gefunden. Google Drive für Desktop auf 'Dateien spiegeln' stellen und Sync abwarten.")
    if vault_inside:
        print("WARNUNG: Der Vault liegt im gescannten Ordner.")


if __name__ == "__main__":
    main()
