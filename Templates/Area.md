---
type: area
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - area
---
# <% tp.file.title %>

Worum geht es in diesem Bereich? Ein, zwei Sätze.

<% tp.file.cursor() %>

## Standard
Woran erkenne ich, dass dieser Bereich "in Ordnung" ist?

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
path includes <% tp.file.title %>
short mode
```

## Notizen
