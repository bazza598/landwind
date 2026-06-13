# WakeWave Launch Package — Review & Changelog

**Reviewed:** 2026-06-13 · **Scope:** all package documents + financial model in Google Drive

This revision organises the package into a numbered set, adds a master index with a single
canonical numbers table (doc 00), and **resolves a set of conflicting CPA/ROAS/KPI
thresholds** that — left as they were — could have led to scaling at a loss. Below is every
change, with the reasoning.

---

## A. Material corrections (could affect money)

**1. CPA targets were contradictory across docs.**
- *Before:* `07-launch-sprint` and `04-ad-creative-pack` set "CPA target ≤ £27, red line > £35."
  The financial model sets "target CPA £15, break-even £20.40 (single)."
- *Problem:* £27 is actually the **blended break-even** at a ~50/50 single/kit mix — not a
  *target*. A target at break-even leaves no profit, and a £35 red line means you keep
  spending while losing ~£8/order.
- *After:* All docs now use **target ≤ £15 (profit)**, **break-even £20.40 single / ~£33 kit /
  ~£27 blended**, and treat the blended break-even (~£27) as the hard stop — not £35.

**2. ROAS kill threshold let you bleed below break-even.**
- *Before:* `07-launch-sprint` killed spend only below **1.4x ROAS**; break-even is **1.72x**.
- *Problem:* Between 1.4x and 1.72x you are losing money but the rule keeps the ad set on.
- *After:* Kill threshold aligned to **< 1.7x** (matching `10-meta-automated-rules`, which was
  already correct). Healthy scale gate stays at **≥ 2.0x**; the automated budget-bump trigger
  stays conservative at **≥ 2.5x** (these are complementary, not in conflict — now stated as such).

**3. AOV target harmonised.** `07-launch-sprint` said ≥ £44; financial model says ≥ £45. → **≥ £45** everywhere.

**4. CPM action line harmonised.** The risk register treated **> £12** as the trigger to shift
to TikTok; the financial model uses **£8–18 normal, > £25 sustained = act**. £12 is too tight
for UK auctions. → Watch at > £18, act/shift channel at **> £25 sustained**.

**5. Competitor spend figure dated.** Research (doc 01, June 11) cites Histrips' top creative at
**€40,306**; the ad-creative pack (June 13) cites **€52.8K**. These are the **same creative**,
which grew. → Now labelled as one ad over time; latest figure (€52.8K, June 13) used, with the
June 11 baseline noted.

## B. Housekeeping / hygiene (do in Drive)

**6. Duplicate files in Drive.** Two copies each of `WakeWave-brand-and-install` (keep the
07:22 version) and `product-decision-model` (keep the 06:45 version). Delete the older copies
to avoid editing the wrong one.

**7. Files are loose in Drive root.** The `WakeWave Launch — June 2026` folder exists but is
empty; the package docs sit in the Drive root. Move all package files into the folder. (A
copy of doc 00 has been placed in that folder by this review.)

**8. Numbering.** The originals jumped (brand→04→09 with several un-numbered extras). This
package renumbers them 00–11 in execution order (see doc 00 index).

## C. Gaps to close (not yet built)

**9. Landing-page files don't match / aren't saved.** Doc 03 references `wakewave-landing.html`
and `wakewave-pdp.liquid`, but Drive only contains `INSTALL-landing-page.md`, which still has
**generic "Lumen LED Mask" placeholders and £129/£189 pricing** and points at differently-named
files (`landing-page.html` / `hero-product-landing.liquid`). → Either save the actual
WakeWave-branded HTML/Liquid to Drive, or rebrand the generic template to WakeWave. Doc 11
flags this inline.

**10. "Stages 1–3" never written as standalone docs.** The research (01) and financial model
(02) effectively cover them; no action needed unless you want explicit brand/positioning docs.

---

## What was NOT changed
- All ad copy, scripts, brand voice, compliance language, and the offer structure were kept
  as-is — they are strong and compliant.
- The `updated master prompt` doc in Drive is a **separate YouTube doodle-video engine**,
  unrelated to WakeWave, and was left out of this package.
