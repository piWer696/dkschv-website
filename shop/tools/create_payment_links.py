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
    ("notfallplan", "price_1Ufa6XFuctZ4rXB3K4ph4WFe", 89),
    ("ndsg", "price_1Ufa8mFuctZ4rXB33KF5HZQx", 149),
    ("audit", "price_1Ufa8mFuctZ4rXB3WdHvsiBo", 59),
    ("policy", "price_1Ufa8nFuctZ4rXB3dWXjXc3p", 49),
    ("bundle", "price_1Ufa8nFuctZ4rXB37gsLtEap", 249)
]

links = {}

for sku, price_id, chf in products:
    try:
        pl = stripe_post("payment_links", {
            "line_items[0][price]": price_id,
            "line_items[0][quantity]": "1",
            "after_completion[type]": "redirect",
            "after_completion[redirect][url]": f"https://dkschv.ch/shop/danke.html?product={sku}"
        })
        pl_url = pl["url"]
        links[sku] = {
            "price_id": price_id,
            "amount_chf": chf,
            "url": pl_url
        }
        print(f"✅ {sku} ({chf} CHF) -> {pl_url}")
    except Exception as e:
        print(f"❌ Fehler bei {sku}: {e}")

out_path = os.path.join(os.path.dirname(__file__), "dkschv_stripe_payment_links.json")
with open(out_path, "w") as f:
    json.dump(links, f, indent=2)

print("\n🎉 Alle Stripe Payment Links gespeichert in:", out_path)
