# Landing Page — Install & Customise

> **⚠️ Rebrand needed before use.** This install guide is the **generic template** as it exists
> in Drive (`INSTALL-landing-page.md`). It still uses placeholder branding ("Lumen LED Mask",
> £129/£189) and references files named `landing-page.html` / `hero-product-landing.liquid`. The
> WakeWave brand doc (03) refers to `wakewave-landing.html` / `wakewave-pdp.liquid`. **Reconcile
> the file names and rebrand all copy/pricing to WakeWave (£34.99 / £54.99 / £89.99) before
> publishing.** See changelog item 9.

Two deliverables, same design:

| File | What it's for |
|---|---|
| `landing-page.html` | A complete, standalone page. Double-click to preview in any browser. Host it anywhere, or use it to get sign-off on the design before building in Shopify. |
| `hero-product-landing.liquid` | A native Shopify **section** — fully editable in the theme customizer (no code edits to launch). |

The placeholder product is **"Lumen LED Mask."** Swap it for WakeWave (see "Make it yours").
All stats, press mentions, and reviews are illustrative — replace them with genuine, verifiable
figures before publishing.

## A) Preview the HTML now
1. Open `landing-page.html` in your browser (double-click).
2. Resize the window narrow to see the sticky mobile buy bar appear.
3. The Add-to-cart buttons show a demo alert — they're wired up for real in the Liquid version.

## B) Install the Shopify section
**Back up first: Online Store → Themes → ⋯ → Duplicate. Work on the copy.**
1. Theme code editor → **Sections → Add a new section** → name it `hero-product-landing`.
2. Delete the default scaffold and paste the entire contents of `hero-product-landing.liquid`. Save.
3. Create a page to host it: **Online Store → Pages → Add page** (e.g. title "WakeWave"). Save.
4. Add the section to a template: **Themes → Customize** → top-bar dropdown → **Pages → [your
   page]** (or **Home page**) → **Add section → Hero Product Landing**. It loads with 3 benefit
   cards + 3 review cards pre-filled.
5. In the section settings:
   - Set **Linked product** to your real product → auto-drives price and live-variant ATC.
   - Upload a **Hero image**, edit the headline/eyebrow/assurance text.
   - Adjust **Accent color** / **Text color** to the WakeWave palette (navy `#161B2E` / amber `#F4A93C`).
   - Add or remove **Benefit** and **Review** blocks freely.
6. **Preview**, then **Publish** the duplicated theme when happy.

## Make it yours (find & replace)
In `landing-page.html`, replace:
- Lumen → WakeWave
- £129 / £189 / Save £60 → WakeWave pricing (£34.99 / £54.99 / £89.99)
- The hero glyph block / `.hero__media` → your product photo (`<img src="...">`)
- Reviews, "92% saw smoother skin", "As seen in Vogue" → your genuine, substantiated claims

In the Liquid section, all of this is editable in the customizer — no code needed. Linking a real
product overrides the placeholder price automatically.

## Rollback
- **Section:** in the customizer, hide or remove the "Hero Product Landing" section, or revert by
  re-publishing your original (un-duplicated) theme.
- **HTML:** it's a standalone file — just don't deploy it.

## Compliance note
UK consumer law (CMA / ASA) requires that savings claims, "as seen in" press mentions, review
counts, and any health-adjacent benefit claims be truthful and substantiated. The placeholder
copy is a template only — replace every figure with something you can evidence before going live.
