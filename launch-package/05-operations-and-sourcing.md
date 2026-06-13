# WakeWave — Stage 5: Operations & Sourcing

## Product spec (for supplier quotes)

| Spec | Requirement |
|---|---|
| Type | Standalone vibrating alarm wristwatch (no app dependency preferred) |
| Vibration | Multi-level, gradually increasing intensity; strong max setting |
| Battery | Rechargeable, ≥ 7 days real-world (**verify on samples** — this number goes in ads ONLY after testing) |
| Band | Soft silicone, one-size with buckle adjust, sleep-comfortable |
| Display | Simple LED/LCD time + alarm set; no health-tracking claims |
| Cert | CE/UKCA marking required; RoHS; charging cable included |
| Packaging | Plain or branded box (branded from order #2 onward) |

## Bundle components
- Travel case (zip EVA hard case, ~£1.20)
- Spare strap (~£0.80)
- Wake-Up Routine guide — digital PDF (doc 08; zero marginal cost; we write it)

## Supplier criteria & process

1. Pull 3 quotes: **CJ Dropshipping (primary), AutoDS marketplace, 1 AliExpress vendor (backup)**.
2. Demand: landed UK cost (unit + ship + duty), 7–10 day max UK delivery, photo of CE/UKCA mark,
   defect rate, branded packaging MOQ.
3. **Order 3 samples before any ad spend.** Test: vibration wakes a real heavy sleeper, battery
   life, strap comfort, charging.
4. Lock backup supplier at agreed price before scaling past 30 orders/day.

### Outreach template
> Hi — I'm launching a UK brand for a vibrating alarm watch (silent wake-up). Please quote:
> (1) unit price at 50/200/500 units, (2) landed UK shipping cost & days, (3) CE/UKCA
> documentation, (4) branded box MOQ, (5) defect/return rate. Samples to [address] — I'll pay
> sample + express shipping today if specs match. Target first order within 14 days.

## UK fulfilment options

| Option | When |
|---|---|
| CJ UK warehouse stock | From day 1 if SKU available — 2–4 day delivery beats 10-day China ship |
| China direct (ePacket/YunExpress) | Fallback; must state honest delivery window pre-purchase (CMA) |
| UK 3PL (e.g. Huboo) | After 30+ orders/day consistent |

## Returns policy (customer-facing, publish before launch)
- 60-day no-quibble returns, full refund on receipt of item
- Customer pays return postage unless faulty (faulty = we pay, prepaid label)
- Refund within 5 working days of receipt — automate via Shopify Flow
- Policy linked in footer + checkout (legal requirement, not optional)

## Automation stack (the 90%)

| Layer | Tool |
|---|---|
| Order routing | AutoDS auto-fulfil → supplier |
| Email/SMS | Klaviyo: welcome, abandoned cart (1h/24h), post-purchase review request (day 14), win-back (day 45) |
| Reviews | Judge.me — post-delivery request flow only, **never incentivised for positive reviews** |
| Monitoring | n8n/Hermes: daily Histrips ad watch, daily KPI digest, weekly review monitor |

**Numbers still needing verification before launch:** landed COGS, battery life, UK delivery
days, vibration strength on a real heavy sleeper.

**NEXT ACTION:** Send outreach to 3 suppliers today; order samples within 48h.
