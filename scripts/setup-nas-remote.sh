#!/usr/bin/env bash
# Richtet die UGREEN NAS als Git-Backup-Remote "nas" ein.
#
#   ./scripts/setup-nas-remote.sh /Volumes/Backup/SecondBrain.git       # macOS
#   ./scripts/setup-nas-remote.sh /mnt/nas/Backup/SecondBrain.git       # Linux
#
# Die SMB-Freigabe muss vorher gemountet sein.
set -euo pipefail

NAS_PATH="${1:-}"
REMOTE_NAME="${2:-nas}"

if [[ -z "$NAS_PATH" ]]; then
  echo "Aufruf: $0 <Pfad-zum-Bare-Repo-auf-der-NAS> [Remote-Name]" >&2
  exit 1
fi

VAULT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$VAULT"
[[ -d .git ]] || { echo "Kein Git-Repository in $VAULT" >&2; exit 1; }

if [[ ! -d "$NAS_PATH" ]]; then
  echo "Lege Bare-Repository an: $NAS_PATH"
  mkdir -p "$NAS_PATH"
  git init --bare "$NAS_PATH"
else
  echo "Bare-Repository existiert bereits: $NAS_PATH"
fi

if git remote | grep -qx "$REMOTE_NAME"; then
  git remote set-url "$REMOTE_NAME" "$NAS_PATH"
  echo "Remote '$REMOTE_NAME' aktualisiert."
else
  git remote add "$REMOTE_NAME" "$NAS_PATH"
  echo "Remote '$REMOTE_NAME' angelegt."
fi

echo "Schiebe alle Branches auf die NAS..."
git push "$REMOTE_NAME" --all

cat <<MSG

Fertig. Ab jetzt sichert 'git push $REMOTE_NAME --all' den Vault auf die NAS.
Automatisch bei jedem Push mitsichern (optional):
  git remote set-url --add --push origin https://github.com/MarqEwi/SecondBrain.git
  git remote set-url --add --push origin $NAS_PATH
MSG
