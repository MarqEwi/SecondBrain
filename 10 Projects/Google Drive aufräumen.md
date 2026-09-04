---
type: project
status: active
created: 2026-09-04
deadline: 
area: "[[Finanzen]]"
tags:
  - project
  - drive
---
# Google Drive aufräumen

## Ziel
Die Unterlagen auf Google Drive (Kapitalanlage-Immobilie, Nebengewerbe, weitere) sind einheitlich benannt und einsortiert, und zu jedem Thema gibt es im Vault einen Steckbrief, der auf den Ablageort verlinkt. Nichts wurde gelöscht, Duplikate liegen in `_zu_pruefen`.

Regeln und Phasen stehen in der `CLAUDE.md` unter "Drive-Ablage". Befehl für Phase 1: `/inventar "<Pfad>" <Thema>`.

## Nächste Schritte
### Kapitalanlage-Immobilie
- [ ] Phase 1: Inventar erstellen (`/inventar`)
- [ ] Phase 2: Namensschema und Zielstruktur vorschlagen, Freigabe
- [ ] Phase 3: Umbenennen und einsortieren, Duplikate nach `_zu_pruefen`
- [ ] Phase 4: Steckbrief anlegen, Lücken melden

### Nebengewerbe
- [ ] Phase 1: Inventar erstellen
- [ ] Phase 2: Namensschema und Zielstruktur, Freigabe
- [ ] Phase 3: Umbenennen und einsortieren
- [ ] Phase 4: Steckbrief anlegen, Lücken melden

### Vorbereitung
- [ ] Google Drive für Desktop steht auf "Dateien spiegeln" (Einstellungen, Google Drive, Option "Dateien spiegeln"). Das Inventar prüft das mit.
- [ ] Vault liegt außerhalb des Drive-Ordners (aktuell `C:\Users\marce\Obsidian\SteveVault`, Drive-Ordner meist `G:\Meine Ablage` oder `C:\Users\marce\Google Drive`). Das Inventar prüft das mit.
- [ ] Anzahl der PDFs ohne Textebene aus dem Inventar ablesen, dann entscheiden, ob ocrmypdf eingerichtet wird

## Notizen
- Inventare liegen unter `Attachments/inventar/`, je Thema und Datum eine Markdown-Zusammenfassung und eine CSV.
- Steckbriefe entstehen aus `Templates/Steckbrief.md` und liegen in `30 Resources/<Thema>/` oder direkt in der passenden Area.

## Ressourcen
- [[Finanzen]]

## Log
- 2026-09-04: Projekt angelegt, Inventar-Skript und `/inventar` eingerichtet
