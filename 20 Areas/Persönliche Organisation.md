---
type: area
created: 2026-09-02
tags:
  - area
---
# Persönliche Organisation

Alles rund um Notizen, Werkzeuge, Routinen und Systeme, mit denen ich meinen Alltag organisiere.

## Standard
Wöchentlicher Rückblick findet statt, Inbox ist leer, aktive Projekte haben einen nächsten Schritt.

## Projekte in dieser Area
```dataview
TABLE WITHOUT ID file.link AS "Projekt", status AS "Status"
FROM "10 Projects"
WHERE type = "project" AND contains(area, this.file.link)
```

## Notizen
