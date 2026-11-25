import "dotenv/config";
import Stripe from "stripe";
import express from "express";

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, {
  apiVersion: "2026-03-25.dahlia",
});

const app = express();
app.disable("x-powered-by");

// Sicherheits-Header Middleware
app.use((req, res, next) => {
  res.setHeader("X-Content-Type-Options", "nosniff");
  res.setHeader("X-Frame-Options", "SAMEORIGIN");
  res.setHeader("Referrer-Policy", "strict-origin-when-cross-origin");
  res.setHeader("Strict-Transport-Security", "max-age=31536000; includeSubDomains; preload");
  res.setHeader("Permissions-Policy", "camera=(), microphone=(), geolocation=()");
  next();
});

// Zugriffsschutz gegen Pfad-Traversal und sensible Dateien (.env, .git, .secret, Skripte)
app.use((req, res, next) => {
  const p = req.path.toLowerCase();
  if (
    p.includes("/.") ||
    p.includes("..") ||
    p.endsWith(".env") ||
    p.endsWith(".secret") ||
    p.endsWith(".sh") ||
    p.endsWith(".py") ||
    p.startsWith("/shop/templates") ||
    p.startsWith("/templates")
  ) {
    return res.status(403).type("text/plain").send("Zugriff verweigert: Geschützte Systemressource.");
  }
  next();
});

app.use(express.static("public"));
app.use(express.urlencoded({ extended: true, limit: "32kb" }));
app.use(express.json({ limit: "32kb" }));

app.post("/api/create-checkout-session", async (req, res) => {
  const mode = "payment";

  const sessionParams = {
    ui_mode: "form",
    mode,
    billing_address_collection: "auto",
    phone_number_collection: {
      enabled: false,
    },
    automatic_tax: {
      enabled: false,
    },
    submit_type: "auto",
    integration_identifier: "custom_embedded_web_0002",
    line_items: [{ price: process.env.STRIPE_PRICE_ID || "price_...", quantity: 1 }],
  };

  if (mode === "subscription") {
    sessionParams.payment_method_collection = "always";
  }

  try {
    const session = await stripe.checkout.sessions.create(sessionParams);
    res.json({ client_secret: session.client_secret });
  } catch (error) {
    console.error("Error creating checkout session:", error.message);
    res.status(500).json({ error: "Fehler beim Erstellen der Bezahl-Sitzung." });
  }
});

app.post("/api/webhook", express.raw({ type: "application/json" }), (req, res) => {
  const endpointSecret = process.env.STRIPE_WEBHOOK_SECRET;
  let event = req.body;

  if (endpointSecret) {
    const signature = req.headers["stripe-signature"];
    try {
      event = stripe.webhooks.constructEvent(req.body, signature, endpointSecret);
    } catch (err) {
      console.log("Webhook signature verification failed.", err.message);
      return res.sendStatus(400);
    }
  }

  switch (event.type) {
    case "checkout.session.completed":
      const session = event.data.object;
      console.log("Checkout completed:", session.id);

      if (session.consent?.terms_of_service === "accepted") {
        console.log("Customer accepted terms of service");
      }

      if (session.consent?.promotions === "opt_in") {
        const email = session.customer_details?.email;
        console.log("Customer opted in for promotional emails:", email);
      }
      break;
    default:
      console.log("Unhandled event type:", event.type);
  }

  res.sendStatus(200);
});

const PORT = process.env.PORT || 4242;
app.listen(PORT, () => console.log(`🔒 DKSchV Checkout Server running on port ${PORT}`));
