<#
.SYNOPSIS
  Richtet die UGREEN NAS als Git-Backup-Remote "nas" ein.
.EXAMPLE
  .\scripts\setup-nas-remote.ps1 -NasPath "\\UGREEN\Backup\SecondBrain.git"
.NOTES
  Die Freigabe muss erreichbar sein (im Explorer einmal öffnen und ggf. anmelden).
#>
param(
  [Parameter(Mandatory = $true)]
  [string]$NasPath,
  [string]$RemoteName = "nas"
)

$ErrorActionPreference = "Stop"
$vault = Split-Path -Parent $PSScriptRoot
Set-Location $vault

if (-not (Test-Path (Join-Path $vault ".git"))) {
  throw "Kein Git-Repository in $vault gefunden."
}

if (-not (Test-Path $NasPath)) {
  Write-Host "Lege Bare-Repository an: $NasPath"
  New-Item -ItemType Directory -Path $NasPath -Force | Out-Null
  git init --bare "$NasPath"
  if ($LASTEXITCODE -ne 0) { throw "git init --bare fehlgeschlagen." }
} else {
  Write-Host "Bare-Repository existiert bereits: $NasPath"
}

# Git will auf Windows Vorwärts-Schrägstriche
$gitPath = $NasPath -replace "\\", "/"

$existing = git remote 2>$null
if ($existing -contains $RemoteName) {
  git remote set-url $RemoteName $gitPath
  Write-Host "Remote '$RemoteName' aktualisiert."
} else {
  git remote add $RemoteName $gitPath
  Write-Host "Remote '$RemoteName' angelegt."
}

Write-Host "Schiebe alle Branches auf die NAS..."
git push $RemoteName --all
if ($LASTEXITCODE -ne 0) { throw "Push auf die NAS fehlgeschlagen." }

Write-Host ""
Write-Host "Fertig. Ab jetzt sichert 'git push nas --all' den Vault auf die NAS."
Write-Host "Automatisch bei jedem Push mitsichern (optional):"
Write-Host "  git remote set-url --add --push origin https://github.com/MarqEwi/SecondBrain.git"
Write-Host "  git remote set-url --add --push origin $gitPath"
