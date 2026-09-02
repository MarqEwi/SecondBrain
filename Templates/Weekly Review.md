---
type: weekly
week: <% tp.file.title %>
tags:
  - weekly
---
# Wochenrückblick <% tp.file.title %>

« [[<% tp.date.now("gggg-[W]ww", -7, tp.file.title, "gggg-[W]ww") %>|Vorwoche]] · [[<% tp.date.now("gggg-[W]ww", 7, tp.file.title, "gggg-[W]ww") %>|Nächste Woche]] »

## Review-Checkliste
- [ ] Inbox leeren: jede Notiz einsortieren (Projekt, Area, Resource) oder löschen
- [ ] Offene Aufgaben durchgehen, Fälligkeiten anpassen
- [ ] Jedes aktive Projekt: gibt es einen nächsten Schritt?
- [ ] Abgeschlossene Projekte ins Archiv verschieben
- [ ] Daily Notes der Woche überfliegen, Wichtiges in dauerhafte Notizen übernehmen
- [ ] Kalender der nächsten Woche anschauen

## Was lief gut

## Was hakte

## Fokus nächste Woche
- 

## Diese Woche erledigt
```tasks
done after <% tp.date.now("YYYY-MM-DD", -1, tp.date.weekday("YYYY-MM-DD", 0, tp.file.title, "gggg-[W]ww"), "YYYY-MM-DD") %>
done before <% tp.date.now("YYYY-MM-DD", 7, tp.date.weekday("YYYY-MM-DD", 0, tp.file.title, "gggg-[W]ww"), "YYYY-MM-DD") %>
short mode
```

## Noch offen
```tasks
not done
due before <% tp.date.now("YYYY-MM-DD", 7, tp.date.weekday("YYYY-MM-DD", 0, tp.file.title, "gggg-[W]ww"), "YYYY-MM-DD") %>
sort by due
short mode
```
