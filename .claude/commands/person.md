---
description: Personennotiz anlegen oder ergänzen
argument-hint: <Name, dann Rolle, Firma, Kontext, Kontaktdaten in freier Form>
---
Lege eine Personennotiz an oder ergänze sie: $ARGUMENTS

Vorgehen:
1. Existiert `30 Resources/Personen/<Name>.md` schon, die neuen Informationen dort ergänzen (Frontmatter-Felder füllen, Kontext erweitern). Nichts Vorhandenes überschreiben.
2. Sonst neu anlegen nach `Templates/Person.md` mit echten Werten: `type: person`, `created: <heute>`, `role`, `company`, `email`, `phone` soweit genannt, sonst leer. Tag `person` plus Bereich (`arbeit`, `familie`, `privat`) wenn erkennbar.
3. Unter `## Kontext` den Zusammenhang in ein, zwei Sätzen. Verlinke die passende Area aus `20 Areas`, wenn eindeutig.
4. Keine Passwörter oder Zugangsdaten speichern, auch wenn der Nutzer sie mitliefert. Dann darauf hinweisen, dass die in den Passwortmanager gehören.
5. Committen und pushen, falls kein Obsidian auf diesem Gerät läuft.
6. Antwort: eine Zeile mit Pfad.
