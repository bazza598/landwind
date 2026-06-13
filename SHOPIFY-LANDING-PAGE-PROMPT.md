# Shopify Landing Page Builder Prompt

## Role

You are an elite Shopify developer and conversion rate optimization (CRO) specialist with 10+ years building 7-figure e-commerce stores. You understand buyer psychology, A/B testing frameworks, and Shopify's Liquid architecture deeply.

## Objective

Build a high-converting, mobile-first Shopify landing page for **[INSERT PRODUCT NAME]** priced at **[INSERT PRICE]** in the **[INSERT NICHE]** market.

---

## Page Structure (Single-Page Scroller)

### 1. Above-the-Fold Hero Section

- Full-width hero with video background or high-quality lifestyle image (auto-play muted, 5–7 second loop)
- **Headline:** Pain-point agitation + solution promise (max 8 words)
  > *Example: "Finally, [Pain Point] Without [Common Frustration]"*
- **Subheadline:** 1–2 sentences expanding the unique mechanism/technology
- **CTA Button:** Contrasting color (`#FF4757` or `#2ED573`), text: `"Get [Product] – [Discount]% Off"` or `"Claim Your [X]% Discount"`
- **Trust Bar:** Below fold — "Free Shipping | 30-Day Guarantee | 24/7 Support" with icons
- **Urgency Element:** Dynamic stock counter or countdown timer (JavaScript-powered, resets per session)

### 2. Problem Agitation Section

- 3-card layout showing the "before" state
- Each card: Icon + "Tired of [Problem]?" + 1-sentence agitation
- Dark background or subtle gradient to create emotional contrast

### 3. Solution Introduction

- Large product hero shot with floating feature callouts (hover/click to reveal on mobile)
- "Meet [Product Name]" headline
- 3–4 bullet-point benefits (not features — benefits)
- Social proof integration: "Join 10,000+ [target audience] who made the switch" with rotating customer avatars

### 4. Features & Benefits Grid

- Alternating 2-column layout (image left/text right, then reverse)
- Each feature block: Lifestyle image + H3 headline + 2-sentence explanation + micro-CTA
- Include comparison table (Your Product vs. Competitors/Old Way)

### 5. Social Proof & Authority

- Video testimonials: 3 embedded video reviews (auto-play muted, click for sound)
- Star rating aggregate: 4.8/5 from 2,000+ reviews
- Media logos: "As seen in..." bar (Forbes, Health, etc.)
- Trust badges: Secure checkout, SSL, payment icons

### 6. Offer Stack & Pricing

- Value stack visualization: Show total value vs. your price
- Bundle options: 1×, 2×, 3× with progressive savings (anchor 3× as "Best Value")
- Risk reversal: "365-Day Money-Back Guarantee" badge with shield icon
- Scarcity trigger: "Only [X] units left at this price" with real-time inventory connection

### 7. FAQ Section (Accordion)

- 5–7 objections handled: Shipping time, returns, ingredients/materials, compatibility, results timeline
- Each answer ends with a soft CTA

### 8. Final CTA Section

- Repeat hero image from a different angle
- Headline: "Ready to [Desired Outcome]?"
- CTA Button: Larger and more urgent than hero (`"Yes! Send My [Product] Now"`)
- Guarantee reminder directly below button
- Payment options: Shop Pay, Apple Pay, Google Pay, PayPal, credit cards

### 9. Footer

- Minimal: Contact, Privacy, Terms, Shipping Policy links
- Email capture: "Get 10% off your first order" popup trigger (exit-intent)

---

## Technical Specifications

### Shopify Implementation

- Use Shopify 2.0 Dawn theme as base, or PageFly/Shogun for drag-and-drop if non-coder
- **Sections:** Custom Liquid sections for each block above
- **Product integration:** Direct "Add to Cart" buttons that skip cart and go to checkout (Shopify Buy Button API or AJAX cart)
- **Mobile optimization:** 70%+ traffic will be mobile — test thumb-zone placement for CTAs
- **Page speed:** Lazy-load images, WebP format, defer non-critical JavaScript. Target <2.5s load time

### Conversion Optimization

- **Heatmap tracking:** Install Hotjar or Microsoft Clarity
- **A/B testing:** Use Google Optimize or Shopify's native A/B testing for headlines and CTAs
- **Retargeting pixel:** Facebook Pixel, TikTok Pixel, Google Analytics 4 — all firing on page load and purchase events
- **Meta tags:** OG tags for social sharing, SEO-optimized title/description

---

## Copy Framework

| Section | Framework | Purpose |
|---|---|---|
| Hero + Problem | PAS (Problem–Agitate–Solve) | Hook emotional pain |
| Product flow | AIDA (Attention–Interest–Desire–Action) | Guide toward purchase |
| Testimonials | Future Pacing ("I can't imagine going back to...") | Cement transformation |
| All CTAs | Action verb + benefit | Drive clicks |

> **Never use "Submit"** — always use `"Get My Discount"`, `"Claim My Kit"`, etc.

---

## Output Format

Provide the following deliverables:

1. **Complete HTML/CSS/Liquid code** for the page (Shopify 2.0 compatible)
2. **Copy document** with all headlines, body text, and CTAs written out
3. **Image/video brief** specifying exactly what visuals are needed for each section
4. **Technical setup checklist** (apps, integrations, tracking codes)
5. **A/B testing roadmap** — what to test first, second, third for optimization

---

## Tone

Direct, benefit-driven, emotionally resonant but not hypey. The reader should feel understood in their pain and excited about the transformation.

---

## Product Details Input

| Field | Your Input |
|---|---|
| Product name | |
| Price point | |
| Target audience | |
| Main pain point solved | |
| Unique mechanism/differentiator | |
| Current conversion rate (if any) | |
| Traffic source (Facebook, TikTok, Google, organic?) | |

---

## Automation Enhancement: Kimi Claw Integration

For a Business-in-a-Box dropshipping workflow, deploy Kimi Claw to automate ongoing landing page optimization:

| Task | Kimi Claw Setup |
|---|---|
| Competitor page monitoring | Scheduled task: Daily at 9 AM — scrape competitor landing pages for price changes, new offers, and headline swaps. Auto-save to cloud folder. |
| Ad creative sync | Connect to Meta LAL strategy — auto-pull winning ad copy into a "Swipe File" for A/B test ideas. |
| Stock/urgency updates | Link to Shopify inventory API — auto-refresh scarcity counters and "units left" copy when stock thresholds hit. |
| Weekly CRO report | Every Friday at 5 PM — compile heatmap insights, conversion rate changes, and test results into a one-page PDF. |
