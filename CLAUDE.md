# CLAUDE.md

Dieses Repo ist ein persönlicher Obsidian-Vault (Second Brain) nach der PARA-Methode. Sprache der Notizen: Deutsch. Antworten und Commit-Messages ebenfalls auf Deutsch.

## Struktur

- `00 Inbox` ungesortiert · `10 Projects` Vorhaben mit Ende · `20 Areas` dauerhafte Bereiche · `30 Resources` Wissen · `40 Archive` erledigt
- `Journal/Daily/YYYY-MM-DD.md`, `Journal/Weekly/YYYY-Www.md`
- `Templates/` Templater-Vorlagen, `Attachments/` Anhänge, `Home.md` Dashboard
- Jeder Ordner hat eine gleichnamige Übersichtsnotiz (`Projects.md`, `Areas.md`, ...) mit Dataview-Abfragen. Diese Notizen haben `type: moc`.

## Konventionen

- Jede Notiz beginnt mit YAML-Frontmatter und mindestens `type`. Werte: `project`, `area`, `resource`, `note`, `meeting`, `person`, `daily`, `weekly`, `moc`.
- Projekte: `status: active | on-hold | done`, optional `deadline` (ISO-Datum) und `area` als Wikilink in Anführungszeichen, z. B. `area: "[[Finanzen]]"`.
- Links immer als Wikilinks `[[Notizname]]`, nie als Markdown-Links auf Pfade.
- Dateinamen sind der Notiztitel, mit Leerzeichen und Umlauten, ohne Präfixe. Keine Sonderzeichen wie `: / \ # ^ [ ] |`.
- Daten im Format `YYYY-MM-DD`. Aufgaben im Tasks-Format: `- [ ] Text 📅 YYYY-MM-DD`.
- Neue Notizen entstehen aus der passenden Vorlage in `Templates/`. Templater-Syntax `<% ... %>` nur in Vorlagen verwenden; beim manuellen Anlegen einer Notiz die Werte direkt einsetzen.
- Bestehende Notizen behutsam ändern: Frontmatter erhalten, Abschnitte nicht umbenennen, Inhalte des Nutzers nicht umformulieren, außer er bittet darum.

## Nicht anfassen

- `.obsidian/workspace*.json` (ist gitignored, gerätespezifisch)
- `.obsidian/plugins/*/main.js`, `manifest.json`, `styles.css` (Plugin-Code, kommt von Obsidian)
- Nichts löschen, was nach Nutzerinhalt aussieht. Archivieren heißt verschieben nach `40 Archive`.

## Typische Aufgaben

- Notizen zusammenfassen, verlinken, in die PARA-Struktur einsortieren
- Dataview- oder Tasks-Abfragen schreiben und in Übersichtsnotizen einbauen
- Vorlagen erweitern (Templater-Syntax, siehe bestehende Vorlagen)
- Inhalte aus PDFs oder Web in Resource-Notizen überführen
- Wochenrückblicke vorbereiten: offene Aufgaben und Projekte ohne nächsten Schritt auflisten

## Git

- Arbeiten auf dem vorgegebenen Branch, klare Commit-Messages, danach pushen.
- Der Nutzer synchronisiert den Vault über das Plugin Obsidian Git. Vor größeren Umbauten darauf hinweisen, dass er vorher in Obsidian pushen und danach pullen soll.
