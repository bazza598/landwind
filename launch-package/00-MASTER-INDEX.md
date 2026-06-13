# WakeWave — Launch Package · Master Index

**Brand:** WakeWave — *the silent alarm for heavy sleepers*
**Compiled:** 2026-06-13 · **Status:** pre-launch (samples not yet tested)

> **Naming note:** This package was requested as "GlowRest_Launch_Package." Every built
> asset — store, ad scripts, financial model, flows — is for the **WakeWave** brand (a
> wrist-vibration silent alarm). There is no separate "GlowRest" product or asset anywhere
> in Drive or the repo, so this index keeps the real brand name (WakeWave) to stay
> consistent with the actual deliverables. Rename throughout only if you genuinely intend
> to relaunch under a new brand.

---

## What's in this package

| # | File | Purpose |
|---|------|---------|
| 00 | `00-MASTER-INDEX.md` | This file — map, canonical numbers, readiness gate |
| 01 | `01-winning-products-research.md` | WinningHunter Top-10 scan that surfaced the vibration alarm (June 1–11) |
| 02 | `02-unit-economics-and-financial-model.md` | **Single source of truth** for COGS, margin, CPA, ROAS, KPIs, 90-day scenarios |
| 03 | `03-brand-offer-and-install.md` | Brand, 3-tier offer, Shopify build steps |
| 04 | `04-ad-creative-pack.md` | Angle bank, 5 scripts, video prompts, campaign structure |
| 05 | `05-operations-and-sourcing.md` | Product spec, supplier process, fulfilment, returns, automation |
| 06 | `06-compliance-pack-uk.md` | ASA/CMA/DMCCA checklist, safe vs risky language |
| 07 | `07-launch-sprint.md` | 14-day sprint, KPI dashboard, decision rules, risk register |
| 08 | `08-wakeup-routine-guide.md` | Customer-facing insert (ships with the product) |
| 09 | `09-klaviyo-flows.md` | Welcome / abandoned cart / post-purchase / win-back copy |
| 10 | `10-meta-automated-rules.md` | Paste-in Ads Manager kill/scale rules + account safety |
| 11 | `11-landing-page-install.md` | HTML + Liquid landing page install & customise guide |
| — | `REVIEW-CHANGELOG-2026-06-13.md` | What was reviewed and corrected in this revision |

**Live source assets in Google Drive (not duplicated here):**
- `product-decision-model` (spreadsheet, 6 sheets) — the live financial model; doc 02 summarises it.
- `wakewave-landing.html` / `wakewave-pdp.liquid` — referenced by doc 03 but **not currently saved in Drive** (see changelog, item 9).

---

## Canonical numbers — single source of truth

These come from the `product-decision-model` financial model. **If any other doc disagrees
with this table, this table wins.** (Conflicts that existed before this revision are listed
in the changelog.)

### Unit economics (single watch, £34.99)

| Line | Value |
|---|---|
| Sell price | £34.99 |
| Product COGS (landed) | £9.00 *(report range $8–12 — VERIFY with supplier)* |
| Pick / pack / ship | £4.50 |
| Payment fees (2.4% + £0.25) | £1.09 |
| **Total variable cost** | **£14.59** |
| **Contribution margin** | **£20.40 (58.3%)** |
| Gross margin (COGS only) | 74.3% |

### Tiers

| Tier | Price | ~Contribution | Break-even CPA |
|---|---|---|---|
| Watch (single) — anchor | £34.99 | ~£20.40 (58%) | ~£20 |
| **Heavy Sleeper Kit ★ default** | **£54.99** | **~£33.40 (61%)** | ~£33 |
| Couples Kit | £89.99 | ~£50.60 (56%) | ~£50 |

### Acquisition & profit gates

| Metric | Value | Meaning |
|---|---|---|
| **Target CPA (profit)** | **≤ £15** | The number to optimise toward |
| Break-even CPA (single) | £20.40 | Above this you lose money on a single-unit order |
| Blended break-even CPA | ~£27 | At a ~50/50 single-to-kit mix |
| **Break-even ROAS** | **1.72x** | Kill ad sets sustained below this |
| Healthy scale ROAS | ≥ 2.0x | 3-day stable → eligible to scale |
| Auto budget-bump trigger | ≥ 2.5x | Conservative trigger for the Meta scale rule |

### KPI dashboard (use these exact thresholds everywhere)

| KPI | Launch target | Red line (act) |
|---|---|---|
| Ad CTR (link) | ≥ 1.5% | < 0.8% |
| CPM (UK) | £8–18 | > £25 sustained |
| Cost per click | < £0.90 | > £1.50 |
| Landing CVR | 2.5–4% | < 1.5% |
| CPA / CAC | ≤ £15 (break-even £20 single) | > blended break-even (~£27) |
| AOV | ≥ £45 | < £35 |
| Blended ROAS (MER) | ≥ 2.0x | < 1.72x (break-even) |
| Refund / return rate | < 5% | > 10% |
| Email capture | ≥ 8% of sessions | < 3% |
| Repeat purchase (90d) | ≥ 12% | < 5% |
| Chargeback rate | < 0.5% | > 1% |
| Contribution margin | ≥ 55% | < 45% |

---

## Launch readiness gate — do NOT spend until all green

These are the open `[verify]` items blocking launch (from docs 03, 05, 06):

- [ ] **Real landed COGS** confirmed by supplier quote (model assumes £9.00)
- [ ] **Battery life** measured on a real sample (number only goes in ads after testing)
- [ ] **UK delivery window** confirmed (must be shown honestly pre-purchase — CMA)
- [ ] **Vibration strength** tested on a genuine heavy sleeper (the core product claim)
- [ ] **CE/UKCA + RoHS** documentation photographed and filed
- [ ] **Returns policy** published in footer + checkout (legal requirement)
- [ ] **Conversions API + domain verification** live in Business Manager
- [ ] `evidence/` folder created; every live claim mapped to its proof

**Highest-leverage next action:** supplier outreach today (doc 05) — samples are the
critical path; everything else is already built.
