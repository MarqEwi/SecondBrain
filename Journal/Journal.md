---
type: moc
---
# 📓 Journal

- **Daily:** eine Notiz pro Tag (`YYYY-MM-DD`). Anlegen über das Kalender-Panel rechts oder den Befehl "Open today's daily note".
- **Weekly:** eine Notiz pro Woche (`YYYY-Www`) für den Wochenrückblick. Anlegen über die Wochennummer im Kalender.

## Letzte Tage
```dataview
LIST
FROM "Journal/Daily"
SORT file.name DESC
LIMIT 14
```

## Wochenrückblicke
```dataview
LIST
FROM "Journal/Weekly"
SORT file.name DESC
LIMIT 8
```
