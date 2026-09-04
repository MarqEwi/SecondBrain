---
type: area
created: 2026-09-04
tags:
  - area
  - privat
---
# Privat

Ich selbst: Gesundheit, Sport, Meditation, Lesen, Hobbys, Reisen.

## Standard
Routinen laufen, und ich habe Zeit für Dinge, die mir guttun.

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
path includes Privat
short mode
```

## Notizen
