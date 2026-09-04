---
type: area
created: 2026-09-04
tags:
  - area
  - arbeit
  - apps
---
# MERCwerk

Meine App-Familie (BFT Tool, PFT Tool, SGT Rechner und Nachfolger): Ideen, Releases, Store, AdMob, Nutzerfeedback.

## Standard
Jede App hat eine aktuelle Version im Store, offene Bugs und Ideen stehen als Aufgaben in den Projekten.

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
path includes MERCwerk
short mode
```

## Notizen
