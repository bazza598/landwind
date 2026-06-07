# Nexlify — AI Automation Agency Landing Page

> We automate the work. You keep the profit.

A production-ready landing page for an AI automation agency, built on Tailwind CSS and Flowbite. Fully responsive, dark mode supported, no framework required — pure HTML.

---

## Live Sections

| Section | Purpose |
|---|---|
| Hero | Headline, pitch, and two CTAs |
| Features | What we build and how fast we deliver |
| Social Proof | Stats: clients, revenue, delivery time, satisfaction |
| Testimonial | Client quote |
| Pricing | Three one-time packages |
| FAQ | Common client questions answered |
| CTA | Book a free strategy call |
| Footer | Contact and brand |

---

## Pricing Tiers

| Package | Price | Includes |
|---|---|---|
| Starter | $997 one-time | 1 AI automation, 1 tool integration, 2-week delivery, 30-day support |
| Growth | $2,497 one-time | 3 automations, CRM integration, 30-day delivery, 60-day support, analytics dashboard |
| Scale | $4,997 one-time | Full AI stack, unlimited automations, custom agents, 90-day support + account manager |

---

## Tech Stack

- [Tailwind CSS v3](https://tailwindcss.com/) — utility-first styling
- [Flowbite v1.4.7](https://flowbite.com/) — accordion, nav toggle
- Vanilla HTML — no React, no Vue, no build server required

---

## Getting Started

```bash
# Install dependencies
npm install

# Development (watch mode — auto-rebuilds CSS on save)
npm run dev

# Production build (minified)
npm run build
```

Open `index.html` in a browser. To deploy, you only need `index.html` and `output.css`.

---

## Project Structure

```
landwind/
├── index.html              # Main page (all content here)
├── input.css               # Tailwind directives (@tailwind base/components/utilities)
├── output.css              # Compiled & minified CSS (committed, do not edit directly)
├── tailwind.config.js      # Tailwind config — custom primary color palette + Flowbite plugin
├── package.json            # npm scripts: build, dev
├── images/
│   ├── logo.svg
│   ├── hero.png
│   ├── feature-1.png
│   └── feature-2.png
└── .claude/
    ├── settings.json       # Claude Code hook registration
    └── hooks/
        └── session-start.sh  # Auto-runs npm install on remote sessions
```

---

## Customization Guide

### Change the brand name
Search and replace `Nexlify` in `index.html`.

### Change pricing
Edit the three pricing card sections (search for `$997`, `$2,497`, `$4,997`).

### Change the contact email
Replace `hello@nexlify.io` with your email or a Calendly link.

### Change colors
The site uses Tailwind's `purple-*` scale. To switch to a different color:
1. Update `tailwind.config.js` → `theme.extend.colors.primary`
2. Find/replace `purple-` with your chosen color in `index.html`
3. Run `npm run build`

### Add your own images
Replace files in the `images/` directory. The page references:
- `images/hero.png` — hero section (right side)
- `images/feature-1.png` — first feature section
- `images/feature-2.png` — second feature section

---

## Deployment

### Vercel (recommended — free)
1. Push to GitHub
2. Import repo at vercel.com
3. Set build command: `npm run build`
4. Set output directory: `.` (root)
5. Deploy

### Netlify (free)
1. Drag and drop `index.html` + `output.css` into netlify.com/drop
2. Done

### Self-hosted
Upload `index.html` and `output.css` to any static host or server.

---

## Claude Code Setup

This repo includes a session start hook for Claude Code on the web. On every new remote session, `npm install` runs automatically so dependencies are ready before you start working.

```bash
# Hook runs automatically — equivalent to:
npm install
```

To trigger manually:
```bash
CLAUDE_CODE_REMOTE=true CLAUDE_PROJECT_DIR=$(pwd) ./.claude/hooks/session-start.sh
```

---

## LLM Review Notes

This codebase is intentionally simple — one HTML file, one CSS file. Key areas to review:

- **`index.html`** — all content, structure, and copy lives here
- **`tailwind.config.js`** — color palette and Flowbite plugin
- **`output.css`** — generated file, never edit directly
- **`.claude/hooks/session-start.sh`** — runs in remote Claude Code sessions only

Open questions for reviewers:
- Should the "Book a Call" CTA link to a Calendly embed or a separate contact form?
- Should pricing be monthly retainer instead of one-time?
- Should we add a case studies or portfolio section?
- Are the stat numbers (50+ clients, $2.4M) credible for a new agency starting out?

---

## License

MIT — free to use, modify, and resell.
