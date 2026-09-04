---
description: Schnelle Notiz in die Inbox legen, formatiert und verlinkt
argument-hint: <Text der Notiz, optional mit Bezug auf ein Projekt, eine Area oder eine Person>
---
Lege aus dem folgenden Text eine Notiz im Vault an. Der Nutzer will nichts formatieren, das machst du.

Text: $ARGUMENTS

Vorgehen:
1. Heutiges Datum ermitteln (`date +%F`).
2. Einen kurzen, sprechenden Titel aus dem Text ableiten (3 bis 6 Wörter, keine Sonderzeichen wie `: / \ # ^ [ ] |`). Prüfe mit einer Suche, ob eine Notiz mit sehr ähnlichem Titel schon existiert. Falls ja: den neuen Inhalt dort als Absatz mit Datum anhängen, statt eine Dublette anzulegen, und das sagen.
3. Sonst neue Datei `00 Inbox/<Titel>.md` anlegen, nach dem Muster von `Templates/Notiz.md`, aber mit echten Werten statt Templater-Platzhaltern:
   - Frontmatter: `type: note`, `created: <Datum>`, `source:` leer, `tags:` passende 1 bis 3 Schlagwörter in Kleinbuchstaben.
   - Überschrift `# <Titel>`.
   - Den Text sauber ausformuliert, Rechtschreibung korrigiert, Stichpunkte wo sinnvoll. Inhalt nicht erweitern oder interpretieren.
   - Abschnitt `## Verknüpfungen` mit Wikilinks auf bestehende Notizen, die im Text erkennbar gemeint sind (Projekte in `10 Projects`, Areas in `20 Areas`, Personen in `30 Resources/Personen`). Nur verlinken, was wirklich existiert. Nichts erfinden.
4. Enthält der Text eine Aufgabe ("muss noch", "nicht vergessen", "bis Freitag"), diese zusätzlich als Task-Zeile `- [ ] ... 📅 YYYY-MM-DD` in die Notiz schreiben, Datum nur wenn eines genannt oder klar ableitbar ist.
5. Wenn kein Obsidian auf diesem Gerät läuft (Cloud-Session): `git add -A && git commit -m "notiz: <Titel>" && git push`.
6. Antwort: eine Zeile mit Pfad und Titel, sonst nichts.
