---
type: moc
---
# 🗄️ Archive

Abgeschlossene Projekte, inaktive Areas und Ressourcen, die nicht mehr relevant sind. Nichts wird gelöscht, alles bleibt durchsuchbar.

**Archivieren:** Notiz oder Ordner hierher verschieben, bei Projekten zusätzlich `status: done` setzen. Obsidian aktualisiert alle Links automatisch.

```dataview
TABLE WITHOUT ID file.link AS "Notiz", type AS "Typ", file.mtime AS "Zuletzt"
FROM "40 Archive"
WHERE file.name != "Archive"
SORT file.mtime DESC
```
