---
description: Phase 1 der Drive-Ablage. Ordner nur lesen und Inventar mit Prüfsummen erstellen
argument-hint: <Pfad zum Drive-Ordner> [Thema]
---
Erstelle ein Inventar für: $ARGUMENTS

Das ist **Phase 1** des Ablage-Projekts (siehe CLAUDE.md, Abschnitt "Drive-Ablage"). Reiner Lesezugriff. Es wird im Quellordner nichts umbenannt, verschoben, gelöscht oder angelegt.

Vorgehen:
1. Pfad und Thema aus der Eingabe nehmen. Fehlt der Pfad, nachfragen. Fehlt das Thema, aus dem Ordnernamen ableiten. Prüfen, dass der Pfad existiert und nicht im Vault liegt.
2. Voraussetzungen prüfen: `python --version` (Windows) bzw. `python3 --version`. Fehlt Python: dem Nutzer `winget install Python.Python.3.12` nennen und stoppen. Dann `python -c "import pypdf"`; schlägt das fehl, `pip install pypdf` ausführen (nur dieses Paket, nichts anderes).
3. Skript starten, Ausgabe kommt in den Vault:
   `python scripts/inventar.py "<Pfad>" --thema "<Thema>"`
4. Die erzeugte Zusammenfassung `Attachments/inventar/Inventar <Thema> <Datum>.md` lesen.
5. Dem Nutzer berichten, knapp und in dieser Reihenfolge:
   - Ergebnis der drei Vorprüfungen (Drive gespiegelt, Vault außerhalb, PDFs ohne Text). Bei Platzhaltern: Drive für Desktop auf "Dateien spiegeln" stellen, Sync abwarten, `/inventar` wiederholen. Bei PDFs ohne Text: Anzahl nennen und ocrmypdf vorschlagen, aber nicht installieren.
   - Zahlen: Dateien, Größe, Duplikatgruppen, Anteil Google-eigener Dokumente.
   - Die fünf häufigsten Dokumentarten und die Ordnerstruktur der obersten Ebene.
   - Was dir beim Lesen der Liste auffällt: uneinheitliche Namen, Jahre, Lücken, offensichtliche Fehlablagen. Maximal fünf Punkte.
   - Link auf die Inventarnotiz als Wikilink.
6. In der Projektnotiz `10 Projects/Google Drive aufräumen.md` den Task für Phase 1 des Themas abhaken und unter `## Log` eine Zeile mit Datum, Thema und Dateianzahl eintragen.
7. **Stoppen.** Keine Vorschläge für Namensschema oder Struktur, das ist Phase 2 und beginnt erst, wenn der Nutzer es sagt.
8. Committen und pushen nur, wenn kein Obsidian auf diesem Gerät läuft.
