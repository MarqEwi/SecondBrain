# CLAUDE.md

Dieses Repo ist ein persönlicher Obsidian-Vault (Second Brain) nach der PARA-Methode. Sprache der Notizen: Deutsch. Antworten und Commit-Messages ebenfalls auf Deutsch.

## Struktur

- `00 Inbox` ungesortiert · `10 Projects` Vorhaben mit Ende · `20 Areas` dauerhafte Bereiche · `30 Resources` Wissen · `40 Archive` erledigt
- `Journal/Daily/YYYY-MM-DD.md`, `Journal/Weekly/YYYY-Www.md`
- `Templates/` Templater-Vorlagen, `Attachments/` Anhänge, `Home.md` Dashboard
- `30 Resources/Personen/` Personennotizen (`type: person`)
- `.claude/commands/` Kurzbefehle für den Nutzer, siehe unten
- Jeder Ordner hat eine gleichnamige Übersichtsnotiz (`Projects.md`, `Areas.md`, ...) mit Dataview-Abfragen. Diese Notizen haben `type: moc`.

## Konventionen

- Jede Notiz beginnt mit YAML-Frontmatter und mindestens `type`. Werte: `project`, `area`, `resource`, `note`, `meeting`, `person`, `daily`, `weekly`, `moc`, `steckbrief`, `inventar`.
- Projekte: `status: active | on-hold | done`, optional `deadline` (ISO-Datum) und `area` als Wikilink in Anführungszeichen, z. B. `area: "[[Finanzen]]"`.
- Links immer als Wikilinks `[[Notizname]]`, nie als Markdown-Links auf Pfade.
- Dateinamen sind der Notiztitel, mit Leerzeichen und Umlauten, ohne Präfixe. Keine Sonderzeichen wie `: / \ # ^ [ ] |`.
- Daten im Format `YYYY-MM-DD`. Aufgaben im Tasks-Format: `- [ ] Text 📅 YYYY-MM-DD`.
- Neue Notizen entstehen aus der passenden Vorlage in `Templates/`. Templater-Syntax `<% ... %>` nur in Vorlagen verwenden; beim manuellen Anlegen einer Notiz die Werte direkt einsetzen.
- Bestehende Notizen behutsam ändern: Frontmatter erhalten, Abschnitte nicht umbenennen, Inhalte des Nutzers nicht umformulieren, außer er bittet darum.

## Nicht anfassen

- `.obsidian/workspace*.json` (ist gitignored, gerätespezifisch)
- `.obsidian/plugins/*/main.js`, `manifest.json`, `styles.css` (Plugin-Code, kommt von Obsidian)
- Nichts löschen, was nach Nutzerinhalt aussieht. Archivieren heißt verschieben nach `40 Archive`.

## Typische Aufgaben

- Notizen zusammenfassen, verlinken, in die PARA-Struktur einsortieren
- Dataview- oder Tasks-Abfragen schreiben und in Übersichtsnotizen einbauen
- Vorlagen erweitern (Templater-Syntax, siehe bestehende Vorlagen)
- Inhalte aus PDFs oder Web in Resource-Notizen überführen
- Wochenrückblicke vorbereiten: offene Aufgaben und Projekte ohne nächsten Schritt auflisten

## Kurzbefehle

Der Nutzer arbeitet meist über Kurzbefehle statt langer Anweisungen: `/notiz`, `/idee`, `/aufgabe`, `/link`, `/person`, `/projekt`, `/heute`, `/aufraeumen`, `/woche`, `/suche`. Die Definitionen liegen in `.claude/commands/`. Gemeinsame Regeln:

- Der Nutzer will nichts formatieren. Titel, Frontmatter, Tags, Links und Ablageort sind deine Aufgabe.
- Inhalte nur säubern, nie erweitern oder interpretieren. Nichts erfinden, nur auf Notizen verlinken, die existieren.
- Antworten nach einem Kurzbefehl sind ein bis drei Zeilen. Keine Erklärungen, keine Rückfragen, außer etwas ist wirklich mehrdeutig.
- Keine Passwörter oder Zugangsdaten in den Vault, auch nicht auf Wunsch. Stattdessen auf den Passwortmanager verweisen.
- Freie Eingaben wie "Notiz: ..." oder "merk dir ..." wie `/notiz` behandeln, "Aufgabe: ..." wie `/aufgabe`.

## Drive-Ablage (Unterlagen aufräumen)

Parallel zum Vault liegen Unterlagen (Nebengewerbe, Kapitalanlage-Immobilie u. a.) auf Google Drive, lokal gespiegelt über "Google Drive für Desktop". Sie werden Thema für Thema aufgeräumt und im Vault als Steckbriefe abgebildet. Projektnotiz: `10 Projects/Google Drive aufräumen.md`.

Feste Regeln, gelten für jeden Durchlauf:
- **Nichts löschen.** Auch keine leeren Dateien, keine offensichtlichen Kopien. Duplikate (gleiche SHA-256-Prüfsumme) werden nach `_zu_pruefen/` im jeweiligen Themenordner verschoben, das Original bleibt am neuen Platz. Über Löschen entscheidet der Nutzer.
- **Phasen, nach jeder Phase stoppen** und auf das Wort des Nutzers warten:
  1. Reiner Lese-Durchlauf: Inventar mit Pfad, Größe, Datum, Prüfsumme, Dokumenttyp (`/inventar`, Skript `scripts/inventar.py`). Nichts verändern.
  2. Auf Basis des Inventars Namensschema und Zielstruktur vorschlagen. Nichts verändern.
  3. Erst nach ausdrücklicher Freigabe umbenennen und einsortieren. Vorher eine Zuordnungsliste (alt → neu) als Datei ablegen, damit alles rückverfolgbar ist.
  4. Steckbriefe im Vault anlegen (`Templates/Steckbrief.md`) und melden, welche Felder aus den Dateien nicht zu füllen sind.
- Vor Phase 1 sicherstellen: Drive steht auf "gespiegelt" (sonst nur Platzhalter lesbar), Vault liegt außerhalb des Drive-Ordners, gescannte PDFs ohne Textebene sind per `ocrmypdf` aufbereitet oder werden als Lücke gemeldet.
- Steckbriefe verlinken auf den Ablageort im Drive (Pfad als Code, kein Wikilink) und nennen zu jeder Angabe die Quelldatei. Keine Zahlen oder Fakten ohne Quelle. Persönliche Daten Dritter sparsam.
- Keine Zugangsdaten, Kontonummern nur maskiert (letzte vier Stellen).

Namensschema und Zielstruktur: **noch offen**, werden in Phase 2 je Thema festgelegt und danach hier eingetragen, damit spätere Durchläufe sich daran halten.

## Git

- Arbeiten auf dem vorgegebenen Branch, klare Commit-Messages auf Deutsch.
- **Cloud-Session** (kein Obsidian auf diesem Rechner, Repo frisch geklont): zu Beginn `git pull`, nach jeder abgeschlossenen Änderung `git add -A && git commit && git push`. Sonst kommt nichts beim Nutzer an.
- **Lokale Session** (Vault-Ordner auf dem Gerät des Nutzers): Dateien einfach schreiben. Das Plugin Obsidian Git committet und pusht alle zehn Minuten selbst. Kein eigenes `git push` nötig, `git pull` vor größeren Umbauten schadet nicht.
- Vor größeren Umbauten darauf hinweisen, dass der Nutzer auf seinen anderen Geräten vorher pushen und danach pullen soll.
