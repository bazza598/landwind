# WakeWave — Meta Automated Rules (paste-in setup)

Free, native, ban-safe ad automation. Set these in **Ads Manager → Rules → Create rule**. They
handle killing/scaling so you don't babysit the account; the daily-ads-profit-tracker scheduled
task handles the *true-profit* read that Meta can't see.

All thresholds use the WakeWave economics (doc 02): break-even ROAS ≈ **1.72x**, **profit-target
CPA ≤ £15**, single-unit break-even CPA ≈ **£20.40**, blended contribution ≈ 58%. Tune as real
data comes in.

Set attribution to **7-day click / 1-day view** on every rule. Run frequency **every 30 minutes**
for kill rules, **once daily (after midnight)** for scale rules. Apply at **ad set** level unless noted.

## Rule 1 — Kill zero-sale waste (fast)
**Turn off ad sets that spend without converting.**
- Action: **Turn off ad set**
- Condition: Spend (last 2 days) **≥ £20** AND Purchases (last 2 days) **= 0**
- Schedule: every 30 min
- Why: £20 ≈ one single-unit break-even CPA. No sale after a full CPA of spend = cut it.

## Rule 2 — Kill unprofitable CPA (steadier)
- Action: **Turn off ad set**
- Condition: Cost per purchase (last 7 days) **> £20** AND Spend (last 7 days) **≥ £40**
- Schedule: daily
- Why: above £20 CPA you're below break-even on the single unit; needs the bundle to save it —
  cut and reallocate. (If kit take-rate is high, your blended break-even is ~£27, but optimise
  toward the £15 target, not the ceiling.)

## Rule 3 — Kill below break-even ROAS
- Action: **Turn off ad set**
- Condition: Purchase ROAS (last 4 days) **< 1.7** AND Spend (last 4 days) **≥ £50**
- Schedule: daily
- Why: 1.72x is your break-even. Give it enough spend (£50) to judge fairly, then cut.

## Rule 4 — Scale the winners (gently)
- Action: **Increase daily budget by 20%**
- Condition: Purchase ROAS (last 3 days) **≥ 2.5** AND Spend (last 3 days) **≥ £20**
- Schedule: **once daily** · Limit: max one increase per day
- Why: 20%/day is the safe ceiling — bigger jumps reset the learning phase and spike CPMs. The
  ≥ 2.5 trigger is deliberately above the ≥ 2.0 "healthy" line so auto-scaling only fires on
  clear winners.

## Rule 5 — Frequency guardrail (notify, don't act)
- Action: **Send notification only**
- Condition: Frequency (last 7 days) **> 3**
- Schedule: daily
- Why: high frequency = audience fatigue. Your cue to refresh creative, not to cut.

## Optional — Dayparting
If data shows dead hours (e.g. 1am–6am), add a rule to **turn off ad set** during those hours and
back on in the morning. Only after you have 1–2 weeks of hour-of-day data.

## Order of operations
1. Start with **Rules 1–3 (kill)** from day one — they cap downside.
2. Add **Rule 4 (scale)** only once you have a creative consistently above 2.5x.
3. Keep budgets low while the account is new (see safety below).

## Account-safety checklist (the real risk in this business)
- **Warm up the account:** start at £20–30/day total, raise gradually. New accounts get
  restricted by sudden spend spikes.
- **Verify your domain** in Business Manager and set up the **Conversions API** (not just the
  pixel) — improves signal and stability.
- **Keep claims clean:** no "cures insomnia", no fabricated "99%/10,000+" stats in live ads. A
  sleep/health-adjacent policy strike can disable the whole account — this is why every asset
  flags claims as "must substantiate."
- **One ad account, one BM, one payment method.** Don't spin up multiples to dodge limits —
  that's the classic ban trigger.
- **Don't let rules fight each other:** a scale rule and a kill rule on the same metric/window
  can thrash. The windows above (2–4–7 days) are staggered to avoid that.

## How this pairs with the bot brain
- **Meta Automated Rules** = real-time control on *platform* metrics (free, safe).
- **daily-ads-profit-tracker** = once-a-day truth check on *real profit* (Meta spend + Shopify
  revenue − your COGS). Meta optimises to ROAS; this catches the case where ROAS looks fine but
  thin margins mean you're actually losing money.
- Connect **Windsor.ai** or **Supermetrics** so the profit-tracker can read Meta spend automatically.
