---
description: Link als Ressource speichern, mit Titel und Kurzfassung
argument-hint: <URL, optional ein Kommentar dahinter>
---
Speichere diesen Link als Ressource: $ARGUMENTS

Vorgehen:
1. Wenn Web-Zugriff möglich ist, Seite abrufen und Titel sowie eine Zusammenfassung in drei Sätzen erstellen. Sonst Titel aus der URL ableiten und die Zusammenfassung leer lassen, das ist in Ordnung.
2. Datei `30 Resources/<Titel>.md` nach dem Muster von `Templates/Ressource.md` mit echten Werten: `type: resource`, `kind: artikel` (oder `video`, `tool`, `kurs`, wenn erkennbar), `url`, `status: to-read`, `created: <heute>`, passende Tags.
3. Den Kommentar des Nutzers, falls vorhanden, unter `## Was ich damit mache` eintragen. Bezug zu Projekt oder Area als Wikilink unter `## Verknüpfungen`.
4. Committen und pushen, falls kein Obsidian auf diesem Gerät läuft.
5. Antwort: eine Zeile mit Pfad und Titel.
