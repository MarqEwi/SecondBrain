---
type: moc
---
# 🏛️ Areas

Eine Area ist ein **Verantwortungsbereich ohne Enddatum**, den man dauerhaft auf einem gewissen Niveau halten will: Gesundheit, Finanzen, Beruf, Familie, Wohnen, Auto, Hobby.

Jede Area bekommt eine Notiz in diesem Ordner. Projekte verweisen im Feld `area` auf sie.

```dataview
TABLE WITHOUT ID file.link AS "Area", length(filter(file.inlinks, (l) => contains(string(l), "10 Projects"))) AS "Projekte"
FROM "20 Areas"
WHERE file.name != "Areas"
SORT file.name ASC
```
