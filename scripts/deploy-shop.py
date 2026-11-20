#!/usr/bin/env python3
"""
Deployment script for the Digital Chrüsimüsi Shop to https://dkschv.ch/shop/
"""

import os
import sys
import ftplib
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SHOP_DIR = ROOT_DIR / "shop"

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

print(f"🚀 Starte Shop-Deployment auf Infomaniak ({FTP_HOST})...")

def ensure_remote_dir(ftp, remote_dir):
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
    remote_dir = os.path.dirname(remote_path)
    if remote_dir:
        ensure_remote_dir(ftp, remote_dir)
    print(f"  ⬆️ Upload: {local_path.name} -> {remote_path}")
    with open(local_path, "rb") as f:
        ftp.storbinary(f"STOR {remote_path}", f)

def sync_tree(ftp, local_dir, remote_base):
    for root, dirs, files in os.walk(local_dir):
        rel_path = os.path.relpath(root, local_dir)
        if rel_path == ".":
            target_remote = remote_base
        else:
            target_remote = f"{remote_base}/{rel_path}".replace("\\", "/")
        
        ensure_remote_dir(ftp, target_remote)
        
        for file in files:
            local_file = Path(root) / file
            remote_file = f"{target_remote}/{file}".replace("\\", "/")
            upload_file(ftp, local_file, remote_file)

try:
    ftp = ftplib.FTP()
    print(f"📡 Verbinde mit {FTP_HOST}:{FTP_PORT} als {FTP_USER}...")
    ftp.connect(FTP_HOST, FTP_PORT, timeout=20)
    ftp.login(FTP_USER, FTP_PASS)
    print("✅ FTP-Authentifizierung erfolgreich!")

    print("\n📦 Synchronisiere /shop ...")
    sync_tree(ftp, SHOP_DIR, "/shop")

    ftp.quit()
    print("\n🎉 Shop erfolgreich auf https://dkschv.ch/shop übertragen!")

except Exception as err:
    print(f"❌ FTP-Fehler: {err}")
    sys.exit(1)
