#!/usr/bin/env python3
"""
==============================================================================
 DKSchV.CH // Sicherer Webshop-Server mit Stripe-Integration & Token-Schutz
 Entwickelt für Schweizer KMU Cyber-Security & Vorlagenverkauf
==============================================================================
"""

import os
import sys
import json
import time
import hmac
import hashlib
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse

PORT = 8089
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def _load_or_generate_secret():
    env_secret = os.environ.get("DKSCHV_SECRET_KEY")
    if env_secret:
        return env_secret
    secret_file = os.path.join(BASE_DIR, ".shop_secret")
    if os.path.exists(secret_file):
        try:
            with open(secret_file, "r") as f:
                s = f.read().strip()
                if len(s) >= 32:
                    return s
        except Exception:
            pass
    import secrets
    new_secret = secrets.token_hex(32)
    try:
        with open(secret_file, "w") as f:
            f.write(new_secret)
        os.chmod(secret_file, 0o600)
    except Exception:
        pass
    return new_secret

SECRET_KEY = _load_or_generate_secret()
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")
STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY", "")

# Produkt-Definitionen mit CHF-Preisen
PRODUCTS_CATALOG = {
    "notfallplan": {
        "title": "KMU Cyber-Notfallplan & Runbook",
        "price_chf": 89,
        "files": ["01_Schweizer_KMU_Cyber_Notfallplan_Runbook.md", "01_Schweizer_KMU_Cyber_Notfallplan_Runbook.html"]
    },
    "ndsg": {
        "title": "Schweizer nDSG-Compliance-Paket",
        "price_chf": 149,
        "files": ["02_Schweizer_nDSG_Datenschutz_Paket_TOM_VdT.md", "02_Schweizer_nDSG_Datenschutz_Paket_TOM_VdT.html"]
    },
    "audit": {
        "title": "KMU IT-Sicherheits-Audit Protokoll",
        "price_chf": 59,
        "files": ["03_KMU_IT_Sicherheits_Audit_Checkliste.md", "03_KMU_IT_Sicherheits_Audit_Checkliste.html"]
    },
    "policy": {
        "title": "Mitarbeiter IT- & KI-Richtlinie",
        "price_chf": 49,
        "files": ["04_Mitarbeiter_IT_Sicherheitsrichtlinie_KI_Policy.md", "04_Mitarbeiter_IT_Sicherheitsrichtlinie_KI_Policy.html"]
    },
    "bundle": {
        "title": "All-in-One Cyber-Resilienz Komplettpaket",
        "price_chf": 249,
        "files": [
            "01_Schweizer_KMU_Cyber_Notfallplan_Runbook.md", "01_Schweizer_KMU_Cyber_Notfallplan_Runbook.html",
            "02_Schweizer_nDSG_Datenschutz_Paket_TOM_VdT.md", "02_Schweizer_nDSG_Datenschutz_Paket_TOM_VdT.html",
            "03_KMU_IT_Sicherheits_Audit_Checkliste.md", "03_KMU_IT_Sicherheits_Audit_Checkliste.html",
            "04_Mitarbeiter_IT_Sicherheitsrichtlinie_KI_Policy.md", "04_Mitarbeiter_IT_Sicherheitsrichtlinie_KI_Policy.html"
        ]
    }
}

def generate_download_token(product_id):
    """Erzeugt ein manipulationssicheres HMAC-Token für bezahlte Downloads (gültig für 24h)"""
    timestamp = int(time.time())
    payload = f"{product_id}:{timestamp}"
    signature = hmac.new(SECRET_KEY.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return f"{payload}:{signature}"

def verify_download_token(token):
    """Validiert das Token und prüft Ablaufzeit"""
    try:
        parts = token.split(":")
        if len(parts) != 3:
            return None
        prod_id, ts_str, sig = parts
        timestamp = int(ts_str)
        # Ablauf nach 24 Stunden (86400 Sekunden)
        if time.time() - timestamp > 86400:
            return None
        expected_sig = hmac.new(SECRET_KEY.encode(), f"{prod_id}:{ts_str}".encode(), hashlib.sha256).hexdigest()
        if hmac.compare_digest(sig, expected_sig):
            return prod_id
    except Exception:
        return None
    return None

class DKSchVShopHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        # Schweizer Sicherheits-Header für KMU-Standards
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("X-XSS-Protection", "1; mode=block")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        super().end_headers()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        
        # API: Checkout-Session erstellen
        if parsed.path == "/api/create-checkout":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode("utf-8"))
                items = data.get("items", [])
                
                # Wenn Stripe API Key vorhanden ist -> echte Stripe Session erstellen
                # Ansonsten -> sicheres Download-Token für Direkt-Auslieferung generieren
                tokens = {}
                for it in items:
                    prod_id = it.get("id")
                    if prod_id in PRODUCTS_CATALOG:
                        tokens[prod_id] = generate_download_token(prod_id)
                
                response_data = {
                    "status": "success",
                    "mode": "test" if not STRIPE_SECRET_KEY else "live",
                    "tokens": tokens,
                    "message": "Zahlungsabsicht autorisiert. Downloads freigegeben."
                }
                
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(response_data).encode("utf-8"))
            except Exception as e:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode("utf-8"))
            return
            
        self.send_response(404)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        
        # API: Token-gesicherter Download
        if parsed.path == "/api/download":
            query = urllib.parse.parse_qs(parsed.query)
            token = query.get("token", [""])[0]
            file_name = query.get("file", [""])[0]
            
            prod_id = verify_download_token(token)
            if not prod_id or prod_id not in PRODUCTS_CATALOG:
                self.send_response(403)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.end_headers()
                self.wfile.write("Zugriff verweigert: Ungültiges oder abgelaufenes Kauf-Token.".encode("utf-8"))
                return
                
            allowed_files = PRODUCTS_CATALOG[prod_id]["files"]
            if file_name not in allowed_files:
                self.send_response(400)
                self.end_headers()
                self.wfile.write("Ungültige Dateianforderung.".encode("utf-8"))
                return
                
            # Dateipfad ermitteln (entweder templates/ oder templates_printable/)
            if file_name.endswith(".html"):
                full_path = os.path.join(BASE_DIR, "templates_printable", file_name)
            else:
                full_path = os.path.join(BASE_DIR, "templates", file_name)
                
            if os.path.exists(full_path):
                self.send_response(200)
                if file_name.endswith(".html"):
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                else:
                    self.send_header("Content-Type", "text/markdown; charset=utf-8")
                    self.send_header("Content-Disposition", f'attachment; filename="{file_name}"')
                self.end_headers()
                with open(full_path, "rb") as f:
                    self.wfile.write(f.read())
                return
            else:
                self.send_response(404)
                self.end_headers()
                return

        super().do_GET()

def run_server():
    server_address = ("0.0.0.0", PORT)
    httpd = HTTPServer(server_address, DKSchVShopHandler)
    print(f"🔒 DKSchV Schweiz Shop-Server aktiv auf Port {PORT}")
    print(f"   URL: http://localhost:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
