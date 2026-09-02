---
type: moc
---
# 📥 Inbox

Hier landet alles, was schnell festgehalten wird: Gedanken, Links, Ideen, Aufgaben ohne Zuhause. Neue Notizen (Strg+N) landen automatisch hier.

**Regel:** Die Inbox wird beim Wochenrückblick geleert. Jede Notiz wandert in ein Projekt, eine Area oder eine Resource, oder sie wird gelöscht.

```dataview
TABLE WITHOUT ID file.link AS "Notiz", file.ctime AS "Angelegt", tags AS "Tags"
FROM "00 Inbox"
WHERE file.name != "Inbox"
SORT file.ctime DESC
```
