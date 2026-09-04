---
type: area
created: 2026-09-04
tags:
  - area
  - familie
---
# Familie

Familie und nahe Menschen, darunter alles, was meinen Vater betrifft: Termine, Unterlagen, Absprachen, Dinge, die ich mir merken muss.

## Standard
Ich weiß, was ansteht, und nichts Wichtiges geht zwischen Terminen verloren.

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
path includes Familie
short mode
```

## Notizen
