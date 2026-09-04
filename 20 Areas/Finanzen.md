---
type: area
created: 2026-09-04
tags:
  - area
  - finanzen
---
# Finanzen

Konten, Verträge, Versicherungen, Abos, Steuern. Keine Zugangsdaten, die liegen im Passwortmanager.

## Standard
Verträge und Kündigungsfristen sind bekannt, keine Überraschungen beim Kontoauszug.

## Projekte in dieser Area
```dataview
TABLE WITHOUT ID file.link AS "Projekt", status AS "Status", deadline AS "Deadline"
FROM "10 Projects"
WHERE type = "project" AND contains(area, this.file.link)
SORT status ASC
```

## Offene Aufgaben hier
```tasks
not done
path includes Finanzen
short mode
```

## Notizen
