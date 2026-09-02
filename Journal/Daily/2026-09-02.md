---
type: daily
date: <% tp.file.title %>
tags:
  - daily
---
# <% tp.date.now("dddd, D. MMMM YYYY", 0, tp.file.title, "YYYY-MM-DD") %>

« [[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %>|Gestern]] · [[<% tp.date.now("gggg-[W]ww", 0, tp.file.title, "YYYY-MM-DD") %>|Woche]] · [[<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>|Morgen]] »

## Fokus heute
- 

## Aufgaben
- [ ] 

## Notizen
<% tp.file.cursor() %>

## Fällig / überfällig
```tasks
not done
due before <% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>
sort by due
short mode
```

## Heute erledigt
```tasks
done on <% tp.file.title %>
short mode
```
