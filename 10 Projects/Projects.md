---
type: moc
---
# 🎯 Projects

Ein Projekt hat ein **konkretes Ziel** und ein **Ende**. "Wohnung renovieren" ist ein Projekt, "Wohnen" ist eine Area.

Neues Projekt: Notiz in diesem Ordner anlegen, die Vorlage `Projekt` wird automatisch angewendet.

## Aktiv
```dataview
TABLE WITHOUT ID file.link AS "Projekt", area AS "Bereich", deadline AS "Deadline", created AS "Seit"
FROM "10 Projects"
WHERE type = "project" AND status = "active"
SORT deadline ASC
```

## Pausiert
```dataview
TABLE WITHOUT ID file.link AS "Projekt", area AS "Bereich"
FROM "10 Projects"
WHERE type = "project" AND status = "on-hold"
```

## Abgeschlossen (noch nicht archiviert)
```dataview
LIST
FROM "10 Projects"
WHERE type = "project" AND status = "done"
```
