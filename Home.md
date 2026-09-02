---
type: home
---
# 🧠 Second Brain

> Startseite. Als Standard-Startnotiz in Obsidian festpinnen (Rechtsklick auf den Tab, "Anpinnen") oder per Lesezeichen.

**Schnellzugriff:** [[Inbox]] · [[Projects]] · [[Areas]] · [[Resources]] · [[Archive]] · [[Journal]]

## Heute
```dataview
LIST
FROM "Journal/Daily"
WHERE file.day = date(today)
```

## Aktive Projekte
```dataview
TABLE WITHOUT ID file.link AS "Projekt", area AS "Bereich", deadline AS "Deadline"
FROM "10 Projects"
WHERE type = "project" AND status = "active"
SORT deadline ASC
```

## Fällig in den nächsten 7 Tagen
```tasks
not done
due before in 8 days
sort by due
short mode
```

## Inbox
```dataview
TABLE WITHOUT ID file.link AS "Notiz", file.ctime AS "Angelegt"
FROM "00 Inbox"
WHERE file.name != "Inbox"
SORT file.ctime DESC
```

## Zuletzt bearbeitet
```dataview
TABLE WITHOUT ID file.link AS "Notiz", file.mtime AS "Geändert"
FROM ""
WHERE file.name != "Home" AND !contains(file.folder, "Templates")
SORT file.mtime DESC
LIMIT 10
```
