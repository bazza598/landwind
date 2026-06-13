# WakeWave — Brand, Offer & Install

## The brand

| | |
|---|---|
| **Name** | WakeWave |
| **One-liner** | The silent alarm for heavy sleepers |
| **Tagline** | *Wake without waking them.* |
| **Hero angle** (validated by the competitor's high-spend creative) | *"You're not bad at waking up. Your alarm is."* |
| **Palette** | Night navy `#161B2E` + sunrise amber `#F4A93C` + calm periwinkle `#8B9DC3` on warm off-white `#FBFAF7` |
| **Why this name** | Says what it does (a gentle wave that wakes you), brandable, ownable, carries the problem-first ad story |

The amber-on-navy "sunrise over night" metaphor is the whole positioning: gentle dawn instead
of jarring noise.

## The offer — built for margin

The CTA is a **3-tier selector defaulting to the Kit**, because the bundle carries the best
contribution and lifts AOV. Don't lead with the bare watch.

| Tier | Price | Est. contribution | Contribution % | Role |
|---|---|---|---|---|
| WakeWave Watch (single) | £34.99 | ~£20.40 | ~58% | Entry / anchor |
| **Heavy Sleeper Kit ★ default** | **£54.99** | **~£33.40** | **~61%** | **Hero offer — pushed by the CTA** |
| Couples Kit (2 watches + 2 masks) | £89.99 | ~£50.60 | ~56% | AOV maximiser |

Margins use the verified figures from `product-decision-model` (COGS £9 watch, +£6.50 kit
add-ons, £4.50 ship, 2.4% fees). **Confirm COGS with your supplier before publishing.**
Compare-at prices (£44.99 / £74.99 / £129.99) are anchors — **only show a "was" price you have
genuinely sold at**, per UK pricing rules.

**Why default to the Kit:** anchoring on the middle tier with "★ Most popular" is the classic
decoy structure — the single makes the Kit look like value, the Couples Kit makes the Kit look
affordable. It moves the average order toward your highest-contribution SKU.

## Files

| File | Purpose |
|---|---|
| `wakewave-landing.html` | Full branded conversion page. Double-click to preview. Tier selector + sticky bar live. |
| `wakewave-pdp.liquid` | Shopify PDP section with the 3-tier selector wired to AJAX add-to-cart. |

> **Status flag:** these two files are referenced here but are **not currently in Drive**. The
> only landing asset saved is the generic `INSTALL-landing-page.md` (still branded "Lumen"). See
> doc 11 and changelog item 9 — save the real WakeWave HTML/Liquid or rebrand the template
> before building.

These reuse the system already built this session: `cro-sticky-atc.liquid`,
`testimonials.liquid`, and the `review-request-email-flow` (doc 09).

## Build the store (Shopify)

**Duplicate your theme first.** Then:

1. **Create 3 products** (or one product with 3 variants):
   - *WakeWave Watch* — £34.99
   - *Heavy Sleeper Kit* — £54.99
   - *Couples Kit* — £89.99
   Set each compare-at price only if genuine.
2. **Add the section:** theme editor → Sections → Add new → name `wakewave-pdp` → paste `wakewave-pdp.liquid`.
3. Apply it to your product template (Customize → Products → add **WakeWave PDP** section), then
   in settings **link each tier to its product** and set default tier = *Heavy Sleeper Kit*.
4. Add the **sticky ATC** (`cro-sticky-atc.liquid`) and **testimonials** sections.
5. Use `wakewave-landing.html` as your homepage design reference, or rebuild it as native sections.
6. Install Judge.me + turn on the review-request email flow.
7. **Preview → Publish** the duplicated theme.

### Make it yours
- Replace the ⌚ emoji blocks with real product photography.
- Swap all review text + any "10,000+ / 99%" stats for genuine, substantiated figures.

## Compliance (UK) — non-negotiable before launch
- Any performance claim, review count, or health-adjacent benefit must be **truthful and
  evidenced** (ASA/CMA; DMCCA 2024).
- Only show a struck-through "was" price you have actually charged.
- WakeWave is **not a medical device** — don't imply it treats sleep disorders.
- Collect reviews via the post-purchase flow; never incentivise *positive* reviews, only reviews.

## Rollback
Hide/remove the WakeWave PDP section in the customizer, or re-publish your original theme.
