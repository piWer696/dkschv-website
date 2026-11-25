import os
import urllib.request
import urllib.parse
import json
import base64
import sys

API_KEY = os.environ.get("STRIPE_SECRET_KEY", "")
if not API_KEY:
    env_file = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            for line in f:
                if line.startswith("STRIPE_SECRET_KEY="):
                    API_KEY = line.split("=", 1)[1].strip().strip("'\"")
                    break

def stripe_post(endpoint, data):
    url = f"https://api.stripe.com/v1/{endpoint}"
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=encoded_data, method="POST")
    auth_str = f"{API_KEY}:"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    req.add_header("Authorization", f"Basic {auth_b64}")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        print(f"Stripe API Error on {endpoint}: {err_msg}", file=sys.stderr)
        raise

print("🚀 Erstelle Produkte und Payment Links bei Stripe...")

products = [
    {
        "key": "questbudget",
        "name": "QuestBudget RPG Finance Tracker",
        "desc": "Gamified RPG Budget Tracker für Excel & Google Sheets",
        "amount": 1490, # 14.90 CHF in Rappen
    },
    {
        "key": "freelancer",
        "name": "Swiss Freelancer Starterkit",
        "desc": "Schweizer Rechnungsvorlage mit MwSt 8.1%, 5-Rappen-Rundung & Stundenerfassung",
        "amount": 3900, # 39.00 CHF in Rappen
    },
    {
        "key": "bundle",
        "name": "Das Chrüsimüsi Master-Bundle",
        "desc": "QuestBudget RPG + Swiss Freelancer Starterkit im Sparpaket",
        "amount": 4400, # 44.00 CHF in Rappen
    }
]

created_links = {}

for p in products:
    print(f"\n📦 Erstelle Produkt: {p['name']}...")
    prod = stripe_post("products", {
        "name": p["name"],
        "description": p["desc"]
    })
    prod_id = prod["id"]
    print(f"  ✅ Produkt-ID: {prod_id}")
    
    print(f"  💰 Erstelle Preis: {p['amount']/100:.2f} CHF...")
    price = stripe_post("prices", {
        "product": prod_id,
        "unit_amount": p["amount"],
        "currency": "chf"
    })
    price_id = price["id"]
    print(f"  ✅ Preis-ID: {price_id}")
    
    print(f"  🔗 Erstelle Payment Link...")
    pl = stripe_post("payment_links", {
        "line_items[0][price]": price_id,
        "line_items[0][quantity]": 1,
        "after_completion[type]": "redirect",
        "after_completion[redirect][url]": "https://dkschv.ch/shop/danke"
    })
    pl_url = pl["url"]
    print(f"  🎉 Payment Link URL: {pl_url}")
    created_links[p["key"]] = pl_url

with open("/home/iwer/stripe_links.json", "w", encoding="utf-8") as f:
    json.dump(created_links, f, indent=2)

print("\nAlle Zahlungslinks erfolgreich generiert:")
for k, v in created_links.items():
    print(f"  {k}: {v}")
