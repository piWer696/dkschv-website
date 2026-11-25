import urllib.request
import urllib.parse
import json
import base64
import os

key = os.environ.get("STRIPE_SECRET_KEY")
if not key:
    env_file = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            for line in f:
                if line.startswith("STRIPE_SECRET_KEY="):
                    key = line.split("=", 1)[1].strip().strip("'\"")
                    break

def stripe_post(endpoint, data):
    url = f"https://api.stripe.com/v1/{endpoint}"
    encoded = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=encoded, method="POST")
    auth = base64.b64encode(f"{key}:".encode()).decode()
    req.add_header("Authorization", f"Basic {auth}")
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

products = [
    {
        "sku": "ndsg",
        "name": "Schweizer nDSG-Compliance-Paket (KMU & Praxen)",
        "desc": "Verzeichnis der Bearbeitungstätigkeiten (VdT), TOM-Katalog & Auftragsverarbeitungsvertrag nach neuem nDSG",
        "price_chf": 149
    },
    {
        "sku": "audit",
        "name": "KMU IT-Sicherheits-Audit Protokoll",
        "desc": "Strukturierter 80-Punkte Audit-Prüfkatalog für Schweizer KMU-Infrastruktur & Cloud-Dienste",
        "price_chf": 59
    },
    {
        "sku": "policy",
        "name": "Mitarbeiter IT- & KI-Richtlinie (Swiss KMU)",
        "desc": "Verbindliche Betriebsvereinbarung für Mitarbeitende, BYOD, Passwort-Hygiene & ChatGPT/KI-Nutzung",
        "price_chf": 49
    },
    {
        "sku": "bundle",
        "name": "All-in-One Cyber-Resilienz Komplettpaket (4 Fachvorlagen)",
        "desc": "Komplettpaket inkl. Notfallplan, nDSG-Compliance, Audit-Checkliste & Mitarbeiter-Policy",
        "price_chf": 249
    }
]

catalog = {
    "notfallplan": {
        "prod_id": "prod_Vgy2XeF1aTBOco",
        "price_id": "price_1Ufa6XFuctZ4rXB3K4ph4WFe",
        "amount_chf": 89
    }
}

for item in products:
    p = stripe_post("products", {
        "name": item["name"],
        "description": item["desc"],
        "metadata[category]": "cybersecurity_template",
        "metadata[sku]": item["sku"]
    })
    pr = stripe_post("prices", {
        "product": p["id"],
        "unit_amount": str(item["price_chf"] * 100),
        "currency": "chf"
    })
    catalog[item["sku"]] = {
        "prod_id": p["id"],
        "price_id": pr["id"],
        "amount_chf": item["price_chf"]
    }
    p_name = item["name"]
    pr_id = pr["id"]
    p_chf = item["price_chf"]
    print(f"✅ Erstellt: {p_name} -> {pr_id} ({p_chf} CHF)")

catalog_path = os.path.join(os.path.dirname(__file__), "dkschv_stripe_catalog.json")
with open(catalog_path, "w") as f:
    json.dump(catalog, f, indent=2)

print("\n🎉 Alle 5 Produkte & Preise erfolgreich bei Stripe registriert!")
