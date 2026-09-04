---
type: area
created: 2026-09-04
tags:
  - area
  - zuhause
---
# Zuhause

Wohnung, Haushalt, Geräte, Reparaturen, Netzwerk und NAS.

## Standard
Alles funktioniert, Ersatzteile und Anleitungen sind auffindbar.

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
path includes Zuhause
short mode
```

## Notizen
