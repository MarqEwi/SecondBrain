---
description: Neues Projekt anlegen, mit Ziel, Area und ersten Schritten
argument-hint: <Projektname, dann Ziel, Area, Deadline und erste Schritte in freier Form>
---
Lege ein neues Projekt an: $ARGUMENTS

Vorgehen:
1. `10 Projects/<Projektname>.md` nach `Templates/Projekt.md` mit echten Werten: `type: project`, `status: active`, `created: <heute>`, `deadline` wenn genannt, `area: "[[<Area>]]"` wenn eine Area aus `20 Areas` passt (bei Unsicherheit die wahrscheinlichste nehmen und in der Antwort nennen).
2. `## Ziel` in ein bis zwei Sätzen aus der Beschreibung. `## Nächste Schritte` mit den genannten Schritten als Tasks, mindestens ein konkreter erster Schritt. `## Log` mit `- <heute>: Projekt angelegt`.
3. Committen und pushen, falls kein Obsidian auf diesem Gerät läuft.
4. Antwort: Pfad, gewählte Area, erster Schritt. Drei Zeilen maximal.
