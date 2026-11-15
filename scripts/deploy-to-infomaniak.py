#!/usr/bin/env python3
"""
DKSchV Schweiz · Infomaniak FTP Deployment Tool
Lädt die neu generierten Knowledge Hub Dateien auf https://dkschv.ch hoch
und verifiziert anschliessend die Live-Erreichbarkeit.
"""

import os
import sys
import ftplib
import urllib.request
import ssl
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

# 1. Load credentials from .infomaniak_deploy.env
env_file = ROOT_DIR / ".infomaniak_deploy.env"
if not env_file.exists():
    env_file = Path("/home/iwer/Projekte/FakturaDesk/.infomaniak_deploy.env")

config = {}
if env_file.exists():
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            config[k.strip()] = v.strip().strip("'\"")

FTP_HOST = config.get("INFOMANIAK_FTP_HOST", "dkschv.ch")
FTP_PORT = int(config.get("INFOMANIAK_FTP_PORT", 21))
FTP_USER = config.get("INFOMANIAK_FTP_USER", "if1gui_iwer")
FTP_PASS = config.get("INFOMANIAK_FTP_PASS", "dA_1986_1986_dA")

print(f"🚀 Starte Deployment auf Infomaniak ({FTP_HOST})...")

def ensure_remote_dir(ftp, remote_dir):
    """Erstellt rekursiv Verzeichnisse auf dem FTP falls nicht vorhanden."""
    parts = [p for p in remote_dir.strip("/").split("/") if p]
    current = ""
    for part in parts:
        current += "/" + part
        try:
            ftp.cwd(current)
        except ftplib.error_perm:
            try:
                ftp.mkd(current)
                print(f"  📁 Verzeichnis erstellt: {current}")
            except Exception as e:
                pass

def upload_file(ftp, local_path, remote_path):
    """Lädt eine einzelne Datei binär hoch."""
    remote_dir = os.path.dirname(remote_path)
    ensure_remote_dir(ftp, remote_dir)
    ftp.cwd(remote_dir)
    filename = os.path.basename(remote_path)
    with open(local_path, "rb") as f:
        ftp.storbinary(f"STOR {filename}", f)
    size = os.path.getsize(local_path)
    print(f"  ✓ Hochgeladen: {remote_path} ({size:,} Bytes)")

def sync_tree(ftp, local_base, remote_base):
    """Synchronisiert einen ganzen Verzeichnisbaum rekursiv."""
    local_base = Path(local_base)
    for root, dirs, files in os.walk(local_base):
        rel_root = Path(root).relative_to(local_base)
        remote_dir = f"{remote_base}/{rel_root}".replace("\\", "/").rstrip("/")
        if rel_root == Path("."):
            remote_dir = remote_base

        ensure_remote_dir(ftp, remote_dir)
        for file in sorted(files):
            local_file = Path(root) / file
            remote_file = f"{remote_dir}/{file}".replace("\\", "/")
            upload_file(ftp, local_file, remote_file)

try:
    ftp = ftplib.FTP()
    print(f"📡 Verbinde mit {FTP_HOST}:{FTP_PORT} als {FTP_USER}...")
    ftp.connect(FTP_HOST, FTP_PORT, timeout=20)
    ftp.login(FTP_USER, FTP_PASS)
    print("✅ FTP-Authentifizierung erfolgreich!")

    # 1. wissen/ Verzeichnis synchronisieren
    print("\n📦 Synchronisiere /wissen ...")
    sync_tree(ftp, ROOT_DIR / "wissen", "/wissen")

    # 2. wissen.html Weiterleitung
    print("\n📦 Aktualisiere wissen.html ...")
    upload_file(ftp, ROOT_DIR / "wissen.html", "/wissen.html")

    ftp.quit()
    print("\n🎉 Alle Knowledge-Hub-Dateien erfolgreich übertragen!")

except Exception as err:
    print(f"❌ FTP-Fehler: {err}")
    sys.exit(1)

# 3. Live-Verifizierung über HTTPS
print("\n🔍 Führe Live-Verifikation über HTTPS durch...")
urls_to_test = [
    ("https://dkschv.ch/wissen/", ["Mandantenbereich", "KW 46", "15.11.2026"]),
    ("https://dkschv.ch/wissen/news/", ["Branchennews KW 46", "15.11.2026"]),
    ("https://dkschv.ch/wissen/news/2026-11-15-branchennews.html", ["Outlook und Chromium", "Kühlsteuerungen", "ScreenConnect"]),
    ("https://dkschv.ch/wissen/ransomware-erste-60-minuten.html", ["gated-content", "is-locked"]),
    ("https://dkschv.ch/wissen/resources/01-60-minuten-checkliste.html", ["gated-content", "is-locked"]),
]

ctx = ssl.create_default_context()
all_passed = True

for url, expected_snippets in urls_to_test:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "DKSchV-Deploy-Verifier/1.0"})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            status = resp.status
            content = resp.read().decode("utf-8", errors="replace")
            missing = [s for s in expected_snippets if s not in content]
            if status == 200 and not missing:
                print(f"  ✅ {url} -> HTTP 200 (Alle {len(expected_snippets)} Prüfpunkte vorhanden)")
            else:
                all_passed = False
                print(f"  ⚠️ {url} -> Status: {status}, Fehlende Schnipsel: {missing}")
    except Exception as err:
        all_passed = False
        print(f"  ❌ {url} -> Fehler: {err}")

if all_passed:
    print("\n🚀 Live-Deployment VOLLSTÄNDIG ERFOLGREICH und verifiziert!")
else:
    print("\n⚠️ Deployment beendet, aber einige Live-Prüfungen schlugen fehl.")
    sys.exit(1)
