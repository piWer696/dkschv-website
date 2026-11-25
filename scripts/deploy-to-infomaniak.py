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

FTP_HOST = config.get("INFOMANIAK_FTP_HOST") or os.environ.get("INFOMANIAK_FTP_HOST") or "dkschv.ch"
FTP_PORT = int(config.get("INFOMANIAK_FTP_PORT") or os.environ.get("INFOMANIAK_FTP_PORT") or 21)
FTP_USER = config.get("INFOMANIAK_FTP_USER") or os.environ.get("INFOMANIAK_FTP_USER")
FTP_PASS = config.get("INFOMANIAK_FTP_PASS") or os.environ.get("INFOMANIAK_FTP_PASS")

if not FTP_USER or not FTP_PASS:
    print("❌ Fehler: INFOMANIAK_FTP_USER / INFOMANIAK_FTP_PASS nicht in .infomaniak_deploy.env konfiguriert.")
    sys.exit(1)

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

    # 1. Haupt-HTML & SEO / GEO Dateien hochladen
    print("\n📦 Lade Haupt-HTML, SEO- und GEO-Dateien hoch...")
    core_files = [
        ".htaccess",
        "index.html",
        "robots.txt",
        "sitemap.xml",
        "llms.txt",
        "llms-full.txt",
        "sicherheitsanalyse.html",
        "risikomanagement.html",
        "notfallplanung.html",
        "app-entwicklung.html",
        "ueber-uns.html",
        "kontakt.html",
        "datenschutz.html",
        "impressum.html",
        "blueprints/index.html",
    ]
    for rel_f in core_files:
        local_p = ROOT_DIR / rel_f
        if local_p.exists():
            upload_file(ftp, local_p, f"/{rel_f}")

    # 2. Assets (CSS & JS) synchronisieren
    print("\n📦 Aktualisiere Stylesheet & Skripte...")
    if (ROOT_DIR / "assets" / "css" / "style.css").exists():
        upload_file(ftp, ROOT_DIR / "assets" / "css" / "style.css", "/assets/css/style.css")
    if (ROOT_DIR / "assets" / "js" / "portal-auth.js").exists():
        upload_file(ftp, ROOT_DIR / "assets" / "js" / "portal-auth.js", "/assets/js/portal-auth.js")

    # 3. wissen/ Verzeichnis synchronisieren
    print("\n📦 Synchronisiere /wissen ...")
    sync_tree(ftp, ROOT_DIR / "wissen", "/wissen")

    # 4. wissen.html Weiterleitung
    print("\n📦 Aktualisiere wissen.html ...")
    upload_file(ftp, ROOT_DIR / "wissen.html", "/wissen.html")

    ftp.quit()
    print("\n🎉 Alle Website-, SEO- und Knowledge-Hub-Dateien erfolgreich übertragen!")

except Exception as err:
    print(f"❌ FTP-Fehler: {err}")
    sys.exit(1)

# 5. Live-Verifizierung über HTTPS
print("\n🔍 Führe Live-Verifikation über HTTPS durch...")

news_dir = ROOT_DIR / "content" / "news"
news_files = sorted(list(news_dir.glob("*_DKSchV_Branchennews.md")), reverse=True)
latest_date = "22.11.2026"
latest_kw = "KW 47"
latest_slug = "2026-11-22-branchennews.html"

if news_files:
    latest_file = news_files[0]
    import re
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", latest_file.name)
    if m:
        latest_slug = f"{m.group(1)}-branchennews.html"
    with open(latest_file, "r", encoding="utf-8") as f:
        file_text = f.read()
        m_date = re.search(r'datum:\s*["\']?([^"\'\r\n]+)', file_text)
        if m_date:
            latest_date = m_date.group(1).strip()
        m_kw = re.search(r'kalenderwoche:\s*["\']?([^"\'\r\n]+)', file_text)
        if m_kw:
            latest_kw = m_kw.group(1).strip()

urls_to_test = [
    ("https://dkschv.ch/llms.txt", ["DKSchV Dini", "Andreas Dini", "Naters", "6–24 Stunden"]),
    ("https://dkschv.ch/llms-full.txt", ["DKSchV Dini", "Bammattenweg 19", "CHF 1'490", "6–24 Stunden"]),
    ("https://dkschv.ch/robots.txt", ["GPTBot", "PerplexityBot", "sitemap.xml", "llms.txt"]),
    ("https://dkschv.ch/app-entwicklung.html", ["Individuelle Software- & App-Entwicklung", "14", "Offline-First"]),
    ("https://dkschv.ch/sitemap.xml", ["dkschv.ch", "sicherheitsanalyse.html", "llms.txt"]),
    ("https://dkschv.ch/", ["Bammattenweg 19", "Naters", "FAQPage", "IT-Sicherheit &amp; revDSG-Audits in Naters", "6–24"]),
    ("https://dkschv.ch/wissen/", ["Mandantenbereich", latest_kw, latest_date]),
    ("https://dkschv.ch/wissen/news/", [f"Branchennews {latest_kw}", latest_date]),
    (f"https://dkschv.ch/wissen/news/{latest_slug}", [latest_kw, latest_date]),
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
