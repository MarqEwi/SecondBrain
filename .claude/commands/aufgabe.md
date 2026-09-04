---
description: Aufgabe anlegen, in Tagesnotiz oder Projekt, mit Fälligkeit
argument-hint: <Aufgabe, optional "bis <Datum/Wochentag>" und "für <Projekt>">
---
Lege diese Aufgabe an: $ARGUMENTS

Vorgehen:
1. Heutiges Datum ermitteln (`date +%F`). Fälligkeit aus dem Text ableiten: "bis Freitag" = nächster Freitag ab heute, "morgen", "nächste Woche" = Montag der nächsten Woche, konkrete Daten übernehmen. Keine Angabe = keine Fälligkeit.
2. Task-Zeile im Tasks-Format bauen: `- [ ] <Aufgabe> 📅 YYYY-MM-DD` (das Datum nur mit Fälligkeit). Aufgabe kurz und mit Verb formulieren.
3. Ablageort:
   - Nennt der Text ein Projekt oder ist es eindeutig zuzuordnen (Suche in `10 Projects`): Zeile unter `## Nächste Schritte` des Projekts anhängen.
   - Sonst in die heutige Tagesnotiz `Journal/Daily/<heute>.md` unter `## Aufgaben`. Existiert sie nicht, aus `Templates/Daily Note.md` anlegen und alle Templater-Platzhalter mit echten Werten füllen (Datum, Links auf Vortag, Folgetag und Woche im Format `gggg-[W]ww`, also z. B. `2026-W36`).
4. Wenn im Text eine Person vorkommt, die als Notiz in `30 Resources/Personen` existiert, in der Aufgabe verlinken.
5. Committen und pushen, falls kein Obsidian auf diesem Gerät läuft.
6. Antwort: die fertige Task-Zeile und wo sie liegt, eine Zeile.
