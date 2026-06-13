# WakeWave — Stage 7: Launch Sprint, KPIs & Automation

## 14-day sprint

| Day | Action | Gate |
|---|---|---|
| 1 | Supplier outreach ×3 (template in doc 05); order samples express | Quotes back ≤ 48h |
| 2 | Duplicate theme; install Liquid section; create 3 tier products; publish landing page | Mobile ATC works |
| 3 | Klaviyo flows live (welcome, abandoned ×2, review request, win-back); Judge.me installed | Test order fires all flows |
| 4–5 | Generate 5 videos from prompts; write primary text from scripts; build Advantage+ campaign (paused) | All 5 pass compliance checklist |
| 6–7 | Samples arrive → test vibration/battery/comfort; fill `[verify]` placeholders with real numbers; file evidence | **HARD GATE: samples pass or do not launch** |
| 8 | LAUNCH: campaign live £50/day; n8n daily KPI digest + Histrips watch on | Pixel + conversions firing |
| 9–10 | Kill losers per matrix (CTR < 1.5% @ £30); leave winners alone | ≥ 2 ads surviving |
| 11–12 | First scale: winner +20%/day if ROAS ≥ 2.0; new hook variant of winner | CPA ≤ £15 target (under break-even) |
| 13 | First ops review: delivery times honest? Refund flow smooth? Review requests sending? | Zero broken promises |
| 14 | Sprint retro: full KPI readout; decide scale / iterate / kill | See decision rules |

## KPI dashboard (daily digest)

| KPI | Target | Red line |
|---|---|---|
| CTR | ≥ 1.5% | < 1.0% = creative problem |
| CVR (store) | ≥ 2.5% | < 1.5% = page/offer problem |
| CPA | **≤ £15 (target); break-even £20 single / ~£27 blended** | > break-even = pause, diagnose |
| Blended ROAS | ≥ 2.0 | **< 1.7 (break-even, 3-day avg) = stop spend** |
| AOV | **≥ £45** (kit dominance) | < £38 = tier selector issue |
| Kit take rate | ≥ 50% of orders | — |
| Refund rate | < 5% | > 10% = product/quality problem |

> **Corrected this revision:** CPA target was "£27 / red £35" and ROAS stop was "< 1.4". £27 is
> the **blended break-even**, not a target, and stopping only below 1.4 means bleeding money
> between 1.4 and the 1.72 break-even. Now: target CPA £15, stop spend below break-even ROAS
> (~1.7). AOV harmonised to £45. See changelog items 1–3.

## Decision rules (day 14)
- **SCALE:** ROAS ≥ 2.0 + refunds < 5% → budget to £100/day, +20%/day max; lock backup supplier; brief UK 3PL.
- **ITERATE:** ROAS 1.7–2.0 → page CRO pass, 3 new hooks on best angle, re-test 7 days.
- **KILL:** ROAS < 1.7 after iteration OR refunds > 10% → stop, post-mortem, redeploy budget to
  next pipeline product (desk mat / Android tracker — doc 01).

## Automation hooks (n8n / Hermes / scheduled tasks)
1. Daily 08:00 — KPI digest: spend, ROAS, CPA, orders, refunds → Slack/email.
2. Daily — competitor watch: Histrips active-ad count + new-angle detection (WinningHunter);
   alert if they launch GB-heavy targeting or a partner angle.
3. Weekly — product radar: `find_winning_products` sweep for new sleep-niche entrants.
4. Weekly — review monitor: new Judge.me reviews → flag any complaint theme ≥ 3 mentions.
5. Order flow: AutoDS auto-fulfil; Shopify Flow auto-refund-on-receipt tagging.

## Risk register

| Risk | Trigger | Response |
|---|---|---|
| Histrips UK blitz | Their GB ad share spikes | Double down on partner/2-pack angle they don't run; out-honest them, never out-claim |
| Supplier stockout | Lead time > 10 days | Switch to locked backup; pause scale, not ads |
| Meta account flag | Rejected ads | Claims are conservative; appeal with evidence file |
| CPM inflation | CPM > £25 sustained | Shift budget to TikTok Spark Ads using same scripts (watch from > £18) |
| Copycats undercut | Clone at £24.99 | Hold price; lean on guarantee + reviews + brand voice |

**NEXT ACTION (highest leverage):** Supplier outreach today — samples are the critical path;
everything else is already built.
