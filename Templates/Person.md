---
type: person
created: <% tp.date.now("YYYY-MM-DD") %>
role: 
company: 
email: 
phone: 
tags:
  - person
---
# <% tp.file.title %>

## Kontext
Woher kenne ich die Person, was verbindet uns?

<% tp.file.cursor() %>

## Notizen

## Meetings mit dieser Person
```dataview
TABLE date AS "Datum", project AS "Projekt"
FROM "" 
WHERE type = "meeting" AND contains(participants, this.file.link)
SORT date DESC
```
