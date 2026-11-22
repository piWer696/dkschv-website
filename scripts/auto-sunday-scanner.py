#!/usr/bin/env python3
"""
DKSchV Schweiz · Vollautomatischer Sonntags-Scanner & Publisher
Sucht sonntags auf allen Geräten (Handy/Galaxy S25, uConsole, Laptop, Kali-Tower)
nach dem neuen Manus-Sonntagspaket, importiert es und lädt es auf die Website hoch.
"""

import os
import sys
import time
import json
import hashlib
import zipfile
import subprocess
import shutil
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT_DIR / ".last_published_package.json"
UCONSOLE_SSH_HOSTS = ["100.124.185.110", "192.168.1.118"]
UCONSOLE_USER = "kali"

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)

def compute_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def is_valid_sunday_package(filepath):
    """Prüft, ob die Datei ein echtes DKSchV-Sonntagspaket ist."""
    try:
        if not zipfile.is_zipfile(filepath):
            return False
        with zipfile.ZipFile(filepath, "r") as z:
            names = z.namelist()
            has_news = any("Branchennews" in n or "Laufstatus" in n for n in names)
            has_blog = any("blog-paket" in n or "articles" in n for n in names)
            return has_news or has_blog
    except Exception:
        return False

def get_kdeconnect_devices():
    """Gibt eine Liste von verfügbaren KDE Connect Device-IDs und Namen zurück."""
    try:
        res = subprocess.run(["kdeconnect-cli", "-a", "--id-name-only"], capture_output=True, text=True, timeout=5)
        devices = []
        for line in res.stdout.strip().splitlines():
            line = line.strip()
            if not line:
                continue
            parts = line.split(maxsplit=1)
            dev_id = parts[0]
            dev_name = parts[1] if len(parts) > 1 else dev_id
            devices.append((dev_id, dev_name))
        return devices
    except Exception as e:
        log(f"⚠️ KDE Connect Abfrage fehlgeschlagen: {e}")
        return []

def mount_and_scan_kde_device(dev_id, dev_name):
    """Mountet ein KDE Connect Gerät und sucht nach Sonntagspaketen."""
    found = []
    log(f"📱 Prüfe KDE Connect Gerät: {dev_name} ({dev_id})...")
    try:
        subprocess.run(["kdeconnect-cli", "-d", dev_id, "--mount"], capture_output=True, text=True, timeout=10)
        time.sleep(1)

        mount_res = subprocess.run(["kdeconnect-cli", "-d", dev_id, "--get-mount-point"], capture_output=True, text=True, timeout=5)
        mp = mount_res.stdout.strip()
        if not mp or not os.path.exists(mp):
            mp = f"/run/user/{os.getuid()}/{dev_id}"

        if not os.path.exists(mp):
            log(f"  ℹ️ Kein Mount-Punkt für {dev_name} vorhanden.")
            return found

        search_dirs = [
            Path(mp) / "storage" / "emulated" / "0" / "Download",
            Path(mp) / "storage" / "emulated" / "0" / "Documents",
            Path(mp) / "storage" / "emulated" / "0",
            Path(mp) / "Download",
            Path(mp)
        ]

        for s_dir in search_dirs:
            if s_dir.exists() and s_dir.is_dir():
                try:
                    for f in s_dir.iterdir():
                        if f.is_file() and f.name.endswith(".zip"):
                            if "DKSchV" in f.name or "News" in f.name or "KW" in f.name or "Blogpflege" in f.name or "Laufstatus" in f.name:
                                if is_valid_sunday_package(f):
                                    found.append(f)
                except (PermissionError, OSError):
                    pass
    except Exception as e:
        log(f"  ⚠️ Fehler beim Durchsuchen von {dev_name}: {e}")
    return found

def scan_local_dirs():
    """Durchsucht lokale Verzeichnisse auf Kali-Tower."""
    found = []
    home = Path.home()
    search_dirs = [
        home / "Downloads",
        home / "Dokumente",
        home / "Dokumente" / "Firma DKSchV",
        home / "Schreibtisch",
        home / "Desktop",
        ROOT_DIR
    ]
    for s_dir in search_dirs:
        if s_dir.exists() and s_dir.is_dir():
            try:
                for f in s_dir.iterdir():
                    if f.is_file() and f.name.endswith(".zip"):
                        if "DKSchV" in f.name or "News" in f.name or "KW" in f.name or "Blogpflege" in f.name or "Laufstatus" in f.name:
                            if is_valid_sunday_package(f):
                                found.append(f)
            except (PermissionError, OSError):
                pass
    return found

def scan_uconsole():
    """Prüft uConsole (kali-raspberrypi) via SSH und lädt gefundene Pakete herunter."""
    found = []
    host = None
    for h in UCONSOLE_SSH_HOSTS:
        check = subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=2", f"{UCONSOLE_USER}@{h}", "echo ok"],
            capture_output=True, text=True
        )
        if check.returncode == 0:
            host = h
            break

    if not host:
        return found

    log(f"💻 uConsole erreichbar über {host}, prüfe dortige Verzeichnisse...")
    find_cmd = 'find /home/kali/Downloads /home/kali/Desktop /home/kali -maxdepth 2 -name "*DKSchV*.zip" -o -name "*KW*.zip" 2>/dev/null'
    res = subprocess.run(
        ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=5", f"{UCONSOLE_USER}@{host}", find_cmd],
        capture_output=True, text=True
    )
    remote_files = [line.strip() for line in res.stdout.strip().splitlines() if line.strip()]
    dest_dir = Path.home() / "Downloads"
    for rf in remote_files:
        filename = os.path.basename(rf)
        local_dest = dest_dir / filename
        log(f"  📥 Lade Paket von uConsole herunter: {filename}")
        subprocess.run(["scp", "-o", "BatchMode=yes", f"{UCONSOLE_USER}@{host}:{rf}", str(local_dest)], capture_output=True)
        if local_dest.exists() and is_valid_sunday_package(local_dest):
            found.append(local_dest)
    return found

def notify(title, message, kde_devices=None):
    """Sendet Benachrichtigungen an Desktop und alle verbundenen Handys/KDE Connect Geräte."""
    try:
        subprocess.run(["notify-send", "-a", "DKSchV Website", title, message], timeout=3)
    except Exception:
        pass

    if kde_devices:
        for dev_id, dev_name in kde_devices:
            try:
                subprocess.run(["kdeconnect-cli", "-d", dev_id, "--ping-msg", f"{title}: {message}"], timeout=5)
                log(f"📲 Benachrichtigung an {dev_name} gesendet.")
            except Exception as e:
                log(f"⚠️ Benachrichtigung an {dev_name} fehlgeschlagen: {e}")

def main():
    log("🔍 Starte DKSchV Sonntags-Scanner...")

    last_state = {}
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                last_state = json.load(f)
        except Exception:
            pass

    last_hash = last_state.get("hash", "")
    all_candidates = []

    # 1. Lokale Verzeichnisse prüfen (Kali-Tower)
    local_found = scan_local_dirs()
    if local_found:
        log(f"  📁 {len(local_found)} Paket(e) lokal auf Kali-Tower gefunden.")
        all_candidates.extend(local_found)

    # 2. Handy & KDE Connect Geräte prüfen
    kde_devices = get_kdeconnect_devices()
    for dev_id, dev_name in kde_devices:
        dev_found = mount_and_scan_kde_device(dev_id, dev_name)
        if dev_found:
            log(f"  📱 {len(dev_found)} Paket(e) auf {dev_name} gefunden.")
            for remote_file in dev_found:
                target_copy = Path.home() / "Downloads" / remote_file.name
                try:
                    if not target_copy.exists() or target_copy.stat().st_size != remote_file.stat().st_size:
                        log(f"  📥 Übertrage {remote_file.name} vom Handy nach ~/Downloads ...")
                        shutil.copy2(remote_file, target_copy)
                    all_candidates.append(target_copy)
                except Exception as e:
                    log(f"  ⚠️ Fehler beim Kopieren von {remote_file.name}: {e}")

    # 3. uConsole prüfen
    uconsole_found = scan_uconsole()
    if uconsole_found:
        log(f"  💻 {len(uconsole_found)} Paket(e) von uConsole übernommen.")
        all_candidates.extend(uconsole_found)

    if not all_candidates:
        log("ℹ️ Keine Sonntags-ZIP-Pakete auf Handy, uConsole, Laptop oder Kali-Tower gefunden.")
        sys.exit(0)

    unique_candidates = {}
    for c in all_candidates:
        unique_candidates[c.name] = c

    sorted_candidates = sorted(unique_candidates.values(), key=lambda f: f.stat().st_mtime, reverse=True)
    best_candidate = sorted_candidates[0]
    candidate_hash = compute_sha256(best_candidate)

    log(f"🎯 Neuestes Paket: {best_candidate.name} (Grösse: {best_candidate.stat().st_size:,} Bytes, SHA256: {candidate_hash[:12]}...)")

    if candidate_hash == last_hash:
        log(f"✅ Dieses Paket ({best_candidate.name}) wurde bereits veröffentlicht (SHA256 stimmt überein). Keine Aktion erforderlich.")
        sys.exit(0)

    log(f"🚀 NEUES SONNTAGSPAKET ENTDECKT! Starte automatische Veröffentlichung...")

    project_zip = ROOT_DIR / best_candidate.name
    shutil.copy2(best_candidate, project_zip)

    log("🔨 Führe Import und HTML-Generierung aus...")
    import_cmd = ["node", str(ROOT_DIR / "scripts" / "import-sunday-package.mjs"), str(project_zip)]
    import_res = subprocess.run(import_cmd, cwd=str(ROOT_DIR), capture_output=True, text=True)
    print(import_res.stdout)
    if import_res.returncode != 0:
        log(f"❌ Fehler beim Import: {import_res.stderr}")
        notify("DKSchV Veröffentlichungsfehler", f"Fehler beim Generieren von {best_candidate.name}", kde_devices)
        sys.exit(1)

    log("📡 Lade Seiten auf Infomaniak (dkschv.ch) hoch...")
    deploy_cmd = ["python3", str(ROOT_DIR / "scripts" / "deploy-to-infomaniak.py")]
    deploy_res = subprocess.run(deploy_cmd, cwd=str(ROOT_DIR), capture_output=True, text=True)
    print(deploy_res.stdout)
    if deploy_res.returncode != 0:
        log(f"❌ Fehler beim Deployment: {deploy_res.stderr}")
        notify("DKSchV Deployment-Fehler", "FTP-Upload oder HTTPS-Prüfung fehlgeschlagen", kde_devices)
        sys.exit(1)

    new_state = {
        "filename": best_candidate.name,
        "hash": candidate_hash,
        "published_at": datetime.now().isoformat(),
        "file_mtime": best_candidate.stat().st_mtime
    }
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(new_state, f, indent=2)

    log("🎉 SONNTAGS-PUBLIKATION ERFOLGREICH ABGESCHLOSSEN!")
    notify(
        "DKSchV Website aktualisiert! 🚀",
        f"{best_candidate.name} wurde erfolgreich auf dkschv.ch/wissen/ veröffentlicht.",
        kde_devices
    )

if __name__ == "__main__":
    main()
