# Stripe Integration TODO

This document is the single source of truth for the Stripe Checkout embedded form integration.

## Values to Replace

The following values are placeholders and must be updated before going live.

**Files containing placeholders:**
- [server.js](server.js)
- [.env](.env)
- [public/checkout.html](public/checkout.html)
- [shop/checkout.html](shop/checkout.html)

| Field | Current Value | What to Set |
|-------|--------------|-------------|
| mode | payment | Set to "payment" for one-time charges or "subscription" for recurring billing. |
| line_items[].price | price_... | Your actual Stripe Price ID from the Dashboard (https://dashboard.stripe.com/prices) or API. |
| STRIPE_SECRET_KEY | sk_test_... | Your Stripe Secret API key from the Dashboard (https://dashboard.stripe.com/apikeys). |
| STRIPE_PUBLISHABLE_KEY | pk_test_... | Your Stripe Publishable API key from the Dashboard (https://dashboard.stripe.com/apikeys). |
| STRIPE_WEBHOOK_SECRET | whsec_... | Your Stripe Webhook Signing Secret from Workbench/Webhooks (https://dashboard.stripe.com/workbench/webhooks). |
| Stripe('<your-publishable-key>') | <your-publishable-key> | Your Stripe Publishable Key (`pk_test_...` or `pk_live_...`) in [public/checkout.html](public/checkout.html) and [shop/checkout.html](shop/checkout.html). |

---

## Configured Parameters

These parameters were configured in Checkout Studio and are already set correctly.

**Files containing these parameters:**
- [server.js](server.js)

| Parameter | Value |
|-----------|-------|
| ui_mode | form |
| billing_address_collection | auto |
| phone_number_collection.enabled | false |
| automatic_tax.enabled | false |
| submit_type | auto |
| integration_identifier | custom_embedded_web_0002 |
| payment_method_collection | always (included conditionally when `mode === "subscription"`) |

---

## Setup and Next Steps

### Setup Instructions
1. **Dependencies:** Ensure the required dependencies are installed:
   ```bash
   npm install stripe dotenv express
   ```
2. **Environment Variables:** Update `.env` with your actual Stripe credentials:
   ```text
   STRIPE_PUBLISHABLE_KEY=pk_test_...
   STRIPE_SECRET_KEY=sk_test_...
   STRIPE_WEBHOOK_SECRET=whsec_...
   DOMAIN=http://localhost:4242
   ```
3. **Start the Server:**
   ```bash
   node server.js
   ```
   The server will start on port 4242 (or the port defined in `PORT`).
4. **Access the Embedded Checkout:**
   Navigate to `http://localhost:4242/checkout.html` or `http://localhost:4242/shop/checkout.html`.

### Project Structure of New Files Created
* `server.js`: Express server providing `POST /api/create-checkout-session` using Stripe API version `2026-03-25.dahlia`, returning `{ client_secret: session.client_secret }`, and `POST /api/webhook` for event handling.
* `.env`: Environment configuration for Stripe secret and publishable keys.
* `public/checkout.html`: Client-side embedded form loading `https://js.stripe.com/dahlia/stripe.js`, initializing Checkout Form SDK with custom appearance, mounting into `#checkout-form`, and wiring confirmation actions.
* `shop/checkout.html`: Shop-specific embedded checkout page matching the client-side specifications.
* `STRIPE_INTEGRATION_TODO.md`: Single source of truth for configuration, parameters, and remaining setup tasks.

### How the Integration Works (Flow Overview)
1. The customer loads `checkout.html` which includes Stripe Dahlia SDK (`https://js.stripe.com/dahlia/stripe.js`).
2. The page sends a POST request to `/api/create-checkout-session`.
3. The server calls `stripe.checkout.sessions.create` with `ui_mode: "form"`, API version `2026-03-25.dahlia`, and configured field intents.
4. The server returns `{ client_secret: session.client_secret }`.
5. The frontend initializes `stripe.initCheckoutFormSdk` and mounts the embedded form into `<div id="checkout-form"></div>`.
6. When the user confirms payment, `loadActionsResult.actions.confirm` processes the transaction inside the embedded form.
7. Upon successful payment, Stripe sends the `checkout.session.completed` event to `/api/webhook` to trigger fulfillment.

### Testing Credit Card Numbers and Test Modes
When using test keys (`sk_test_...` and `pk_test_...`), use Stripe's test payment details:
* **Card number:** `4242 4242 4242 4242`
* **Expiration date:** Any valid future month and year (e.g., `12/34`)
* **CVC:** Any 3 digits (e.g., `123`)
* **Billing ZIP / Postal code:** Any valid postal code (e.g., `8001`)

### Next Steps
1. Replace `price_...` in `server.js` with your real Stripe Price ID (e.g., `price_1UdnCdCC0cKMcRpMYfFxXTxM`).
2. Replace `<your-publishable-key>` in `public/checkout.html` and `shop/checkout.html` with your Stripe Publishable Key.
3. Configure webhook endpoint in Stripe Workbench / Webhooks dashboard pointing to your deployed domain (`https://dkschv.ch/api/webhook`).
4. Implement digital download fulfillment inside `case "checkout.session.completed"` in `server.js`.

### Resources
* Stripe Support: https://support.stripe.com
* Stripe MCP Documentation: https://docs.stripe.com/mcp
