---
type: moc
---
# 📚 Resources

Wissen und Interessen, die nicht an ein Projekt oder eine Area gebunden sind: Bücher, Artikel, Kurse, Werkzeuge, Rezepte, Reiseideen, technische Notizen.

Unterordner nach Thema anlegen, sobald sich mehr als eine Handvoll Notizen zu einem Thema sammeln.

## Nach Art
```dataview
TABLE WITHOUT ID file.link AS "Titel", kind AS "Art", author AS "Autor", status AS "Status", rating AS "Bewertung"
FROM "30 Resources"
WHERE type = "resource"
SORT status ASC, file.name ASC
```

## Alle Notizen hier
```dataview
LIST
FROM "30 Resources"
WHERE file.name != "Resources" AND type != "resource"
SORT file.name ASC
```
