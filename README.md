# 🧠 SecondBrain

Mein persönlicher Obsidian-Vault. Notizen liegen lokal auf jedem Gerät, Git hält sie synchron und versioniert, GitHub ist der zentrale Remote, die UGREEN NAS hält ein Backup.

```
Gerät A (PC) ──┐                    ┌──> UGREEN DH2300 (Backup)
               ├──> GitHub (privat) ┤
Gerät B (Handy)┘                    └──> weitere Geräte
```

## Struktur (PARA)

| Ordner | Inhalt |
|---|---|
| `00 Inbox` | Alles Ungesortierte. Neue Notizen landen automatisch hier. |
| `10 Projects` | Vorhaben mit Ziel und Ende. Eine Notiz pro Projekt. |
| `20 Areas` | Dauerhafte Verantwortungsbereiche (Gesundheit, Finanzen, Beruf, ...). |
| `30 Resources` | Wissen und Interessen: Bücher, Artikel, Werkzeuge, Rezepte. |
| `40 Archive` | Erledigtes. Wird nie gelöscht, bleibt durchsuchbar. |
| `Journal/Daily` | Eine Notiz pro Tag (`2026-09-02`). |
| `Journal/Weekly` | Wochenrückblick (`2026-W36`). |
| `Templates` | Vorlagen für Templater. |
| `Attachments` | Bilder, PDFs und andere Anhänge. |

`Home.md` ist das Dashboard. Jeder Ordner hat eine gleichnamige Übersichtsnotiz (z. B. `Projects.md`), die ihren Inhalt per Dataview auflistet.

### Notiztypen

Jede Notiz hat im Frontmatter ein Feld `type`. Darauf bauen die Dashboards auf.

| `type` | Vorlage | Wo |
|---|---|---|
| `project` | Projekt | `10 Projects` |
| `area` | Area | `20 Areas` |
| `resource` | Ressource | `30 Resources` |
| `note` | Notiz | überall |
| `meeting` | Meeting | Projekt- oder Area-Ordner |
| `person` | Person | `30 Resources/Personen` |
| `daily` / `weekly` | Daily Note / Weekly Review | `Journal` |

Projekte haben zusätzlich `status: active | on-hold | done` und optional `deadline` und `area` (Link auf die Area-Notiz).

## Einrichtung auf einem PC

### 1. Voraussetzungen

- [Obsidian](https://obsidian.md/download)
- [Git](https://git-scm.com/downloads) (Windows: bei der Installation "Git Credential Manager" mitnehmen, dann klappt die GitHub-Anmeldung per Browser)

### 2. Repo klonen

Der Ordnername ist frei, Obsidian zeigt ihn als Vault-Namen an. Hier heißt er `SteveVault`.

```bash
# Windows (PowerShell), Vault landet unter C:\Users\<du>\SteveVault
cd ~
git clone https://github.com/MarqEwi/SecondBrain.git SteveVault

# macOS / Linux
cd ~
git clone https://github.com/MarqEwi/SecondBrain.git SteveVault
```

Das machst du **auf jedem Gerät** (großer PC, Surface). Jedes Gerät hat seine eigene Kopie, Git gleicht sie über GitHub ab. Das funktioniert von überall, auch unterwegs ohne WireGuard.

Wichtig: Den Vault **nicht** auf die NAS-Freigabe legen und auch nicht in einen Ordner, der von OneDrive, iCloud, Dropbox oder einer NAS-Synchronisation überwacht wird. Obsidian über SMB (erst recht über WireGuard von unterwegs) ist langsam, erkennt Änderungen unzuverlässig und geht vom Handy gar nicht. Zwei Sync-Systeme auf demselben Ordner erzeugen Konflikte. Die NAS bekommt ihr Backup über Git, siehe unten.

Falls du in Obsidian schon einen leeren Vault angelegt hast: einfach schließen und löschen, der geklonte Ordner ersetzt ihn.

### 3. In Obsidian öffnen

Obsidian starten, "Ordner als Vault öffnen", den geklonten Ordner `SteveVault` wählen. Die Frage nach "Trust author and enable plugins" mit Ja beantworten.

### 4. Community-Plugins installieren

Die Einstellungen der Plugins liegen schon im Repo, nur der Code muss einmal geladen werden.

Einstellungen, Community-Plugins, Durchsuchen, dann nacheinander installieren **und aktivieren**:

1. **Obsidian Git** (Vinzent03): automatischer Commit, Pull und Push
2. **Templater**: Vorlagen mit Datum und Cursor-Logik
3. **Periodic Notes**: Daily und Weekly Notes
4. **Calendar**: Kalender-Panel in der rechten Seitenleiste
5. **Dataview**: die Tabellen auf `Home.md` und in den Übersichtsnotizen
6. **Tasks**: Aufgaben mit Fälligkeit über alle Notizen hinweg

Danach Obsidian einmal neu laden (Strg+P, "Reload app without saving").

**Templater nachprüfen:** Einstellungen, Community-Plugins, Templater. "Template folder location" muss `Templates` sein und "Trigger Templater on new file creation" muss eingeschaltet sein. Steht der Schalter auf aus, bleiben in neuen Notizen die Platzhalter `<% ... %>` stehen und Tasks meldet "unexpanded template text". Reparatur für eine schon angelegte Notiz: Strg+P, "Templater: Replace templates in the active file".

### 5. Git-Identität setzen (einmalig pro Gerät)

```bash
git config --global user.name "Marq"
git config --global user.email "marq.ewi@gmail.com"
```

### 6. Ersten Sync testen

In Obsidian: Strg+P, "Obsidian Git: Commit all changes", dann "Obsidian Git: Push". Wenn das ohne Fehler durchläuft, ist alles verbunden. Ab jetzt passiert das automatisch:

- alle **10 Minuten** Commit und Push, wenn sich etwas geändert hat
- alle **10 Minuten** Pull
- beim Start Pull

Die Intervalle stehen in `.obsidian/plugins/obsidian-git/data.json` und können in den Plugin-Einstellungen geändert werden.

## Backup auf die UGREEN DH2300

Zwei Varianten. Variante A ist in fünf Minuten fertig und braucht nichts auf der NAS außer einer Freigabe. Variante B läuft ohne PC und braucht Docker auf der NAS (UGOS Pro bringt das mit).

### Variante A: Bare-Repository auf der SMB-Freigabe (empfohlen für den Start)

Auf der NAS im UGOS eine Freigabe anlegen, z. B. `Backup`. Dann auf dem PC das Skript ausführen:

```powershell
# Windows, PowerShell im Vault-Ordner
.\scripts\setup-nas-remote.ps1 -NasPath "\\<NAS-Name-oder-IP>\Backup\SecondBrain.git"
```

```bash
# macOS / Linux, Freigabe muss gemountet sein
./scripts/setup-nas-remote.sh /Volumes/Backup/SecondBrain.git
```

Das Skript legt das Bare-Repository auf der NAS an, registriert es als Remote `nas` und schiebt den aktuellen Stand rüber. Danach sichert

```bash
git push nas --all
```

den Vault auf die NAS. Wer das nicht manuell machen will, hängt die NAS als zweites Push-Ziel an `origin`; dann schiebt Obsidian Git bei jedem Push automatisch auf GitHub **und** NAS:

```bash
git remote set-url --add --push origin https://github.com/MarqEwi/SecondBrain.git
git remote set-url --add --push origin //<NAS-Name-oder-IP>/Backup/SecondBrain.git
```

Nachteil: Ist die NAS nicht erreichbar (Laptop unterwegs), meldet Obsidian Git einen Push-Fehler, obwohl GitHub aktualisiert wurde. Wer viel unterwegs ist, bleibt bei `git push nas` oder nimmt Variante B.

### Variante B: NAS spiegelt GitHub per Docker

Die NAS zieht selbstständig jede Stunde den aktuellen Stand von GitHub. Anleitung und Compose-Datei in [`nas/README.md`](nas/README.md).

### Wiederherstellen von der NAS

```bash
git clone //<NAS-Name-oder-IP>/Backup/SecondBrain.git SecondBrain
```

## Handy (Android)

Obsidian läuft auf dem Handy mit demselben Vault, das Git-Plugin gleicht ihn ab. Einmalige Einrichtung, etwa zehn Minuten:

1. **Token anlegen** (am PC, einmalig): GitHub, Settings, Developer settings, Personal access tokens, Fine-grained tokens, "Generate new token". Repository access nur `SecondBrain`, Permissions "Contents: Read and write". Token kopieren, er wird nur einmal angezeigt.
2. **Obsidian** aus dem Play Store installieren, öffnen, "Neuen Vault erstellen", Name `SteveVault`, Speicherort im Gerätespeicher (nicht auf SD-Karte, das ist deutlich langsamer).
3. Einstellungen, Community-Plugins, eingeschränkten Modus deaktivieren, "Durchsuchen", **Git** installieren und aktivieren.
4. Befehlspalette öffnen (nach unten wischen oder das Symbol oben rechts), `Git: Clone an existing remote repo` wählen. URL `https://github.com/MarqEwi/SecondBrain.git`, als Benutzername `MarqEwi`, als Passwort den Token. Bei "Depth" den Vorschlag lassen, bei der Frage nach dem Ordner den Vault-Root wählen. Danach die App wie verlangt neu starten.
5. Nach dem Neustart sind alle Plugins und Einstellungen da. In den Git-Einstellungen unter "Authentication" Name `Marq` und E-Mail eintragen, sonst lehnt GitHub Commits ab.
6. Test: eine Zeile in eine Notiz schreiben, Befehlspalette, `Git: Commit-and-sync`. Am Surface nach dem nächsten Pull nachschauen.

Hinweise: Das Git-Plugin auf Android ist langsamer als am PC, bei einem großen Vault dauert der erste Klon ein paar Minuten. Auto-Pull und Auto-Push laufen wie am PC alle zehn Minuten, solange Obsidian im Vordergrund ist. Vor dem Schließen der App einmal `Git: Commit-and-sync`, dann ist alles oben.

**Der schnellste Weg vom Handy aus:** Claude-App öffnen, Code, Cloud-Sitzung auf dem Repo `SecondBrain`, dann einfach diktieren: `/notiz Papa hat Donnerstag Arzttermin, Unterlagen mitnehmen`. Claude legt die Notiz an und pusht, ohne dass du Obsidian aufmachen musst. Die Kurzbefehle stehen im nächsten Abschnitt.

## Kurzbefehle für Claude

Liegen in `.claude/commands/` und gelten in jeder Claude-Code-Sitzung auf diesem Vault, lokal wie in der Cloud. Du tippst oder diktierst nur den Inhalt, Claude macht Titel, Ablage, Frontmatter, Tags und Links.

| Befehl | Was passiert |
|---|---|
| `/notiz <Text>` | Notiz in die Inbox, sauber formatiert, verlinkt mit passenden Projekten, Areas, Personen |
| `/idee <Text>` | Wie Notiz, plus "Warum" und "Nächster Schritt", hängt sich an Projekt oder Area |
| `/aufgabe <Text> bis Freitag für <Projekt>` | Task mit Fälligkeit in die Tagesnotiz oder unter "Nächste Schritte" des Projekts |
| `/link <URL> <Kommentar>` | Ressource mit Titel und Kurzfassung in `30 Resources` |
| `/person <Name>, <Rolle>, <Kontext>` | Personennotiz anlegen oder ergänzen |
| `/projekt <Name>, <Ziel>, <Area>, <erste Schritte>` | Neues Projekt mit Ziel, Area und Tasks |
| `/heute` | Tagesnotiz anlegen, fällige Aufgaben und Projekte ohne nächsten Schritt zusammenfassen |
| `/aufraeumen` | Inbox durchgehen, Einsortierung vorschlagen, nach Freigabe verschieben |
| `/woche` | Wochenrückblick vorbereiten: Erledigtes, Überfälliges, Projekte ohne nächsten Schritt |
| `/suche <Frage>` | Frage nur aus dem Vault beantworten, mit Quellen |

Freier Text funktioniert auch: "merk dir, dass ..." wird wie `/notiz` behandelt, "Aufgabe: ..." wie `/aufgabe`.

## Arbeitsweise

1. **Erfassen:** Strg+N, Gedanke rein, fertig. Landet in der Inbox.
2. **Tagesnotiz:** Kalender rechts, heutigen Tag anklicken. Fokus, Aufgaben, Log.
3. **Aufgaben:** überall als `- [ ] Text 📅 2026-09-10` (Tasks-Plugin, das Datum kommt per Autovervollständigung). `Home.md` zeigt alles, was in den nächsten sieben Tagen fällig ist.
4. **Wochenrückblick:** Kalender rechts, Wochennummer anklicken, Checkliste abarbeiten. Dabei die Inbox leeren.
5. **Verlinken statt Ordnen:** `[[Notizname]]` ist wichtiger als der Ordner. Backlinks zeigen, was zusammenhängt.

## Mit Claude Code an diesem Vault arbeiten

Weil der Vault ein Git-Repo ist, kann Claude Code direkt darauf arbeiten: Notizen zusammenfassen, Struktur umbauen, Vorlagen ändern, Dataview-Abfragen schreiben, Inhalte aus PDFs in Notizen überführen. Die Konventionen dafür stehen in `CLAUDE.md`. Vorher in Obsidian einmal pushen, danach einmal pullen, damit nichts kollidiert.
