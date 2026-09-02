# NAS-Spiegel per Docker (Variante B)

Die UGREEN DH2300 zieht selbstständig jede Stunde den aktuellen Stand von GitHub. Läuft ohne PC, braucht nur Docker auf der NAS.

## Einrichtung

1. In UGOS Pro die App **Docker** installieren (App Center).
2. Auf der NAS einen Ordner anlegen, z. B. `docker/secondbrain`, und die Dateien `docker-compose.yml` und `.env.example` aus diesem Ordner dorthin kopieren.
3. `.env.example` in `.env` umbenennen und den GitHub-Token eintragen:
   - GitHub, Settings, Developer settings, Personal access tokens, **Fine-grained tokens**, "Generate new token"
   - Repository access: nur `SecondBrain`
   - Permissions: **Contents: Read-only**
   - Ablauf großzügig wählen und im Kalender notieren
4. Im Docker-Bereich von UGOS das Projekt aus der Compose-Datei anlegen und starten (Compose / Projekt / "Aus Datei erstellen"). Alternativ per SSH:
   ```bash
   cd /volume1/docker/secondbrain
   docker compose up -d
   docker compose logs -f
   ```
5. Nach dem ersten Lauf liegt unter `docker/secondbrain/mirror/SecondBrain.git` ein vollständiges Bare-Repository mit der gesamten Historie.

## Wiederherstellen

```bash
git clone //<NAS>/docker/secondbrain/mirror/SecondBrain.git SecondBrain
```

## Hinweise

- Der Spiegel ist eine Einbahnstraße: NAS liest von GitHub, schreibt nie zurück.
- Der Token steht nur in der `.env` auf der NAS. Sollte er jemals im Repo auftauchen, sofort auf GitHub widerrufen.
- Wer zusätzlich eine Kopie außerhalb des Hauses will: UGOS-Backup-App auf eine externe Platte oder Cloud, den Ordner `mirror` einschließen.
