# Portfolio — Md. Sabbir Hossain Rahat

Personal portfolio website for Md. Sabbir Hossain Rahat (CSE Student & Software Developer), built on Next.js with high-fidelity Framer exports.

```bash
npm install
npm run dev
```

## How It Works

Every page is served via static HTML under `public/`, wired through Next.js rewrites in `next.config.mjs`. This preserves 100% of Framer animations, WebGL canvases, and micro-interactions byte-for-byte.

### Active Routes

- `/` — Home (Hero, Featured Works, Experience)
- `/about` — About (Background, Skills, Philosophy)
- `/projects` — Projects (Detailed showcase)
- `/article` — Articles & Journal
- `/contact` — Contact & Inquiries

## Development & Build

- **Development server**: `npm run dev`
- **Production build**: `npm run build`
- **Production start**: `npm run start`

## Assets & Structure

- `public/assets/` — Self-hosted static assets (fonts, optimized images, Framer runtime modules).
- `public/f2c-sw.js` — Service worker mapping external Framer CDN requests to local self-hosted assets for offline reliability and fast caching.
- `scripts/` — Project personalization and maintenance utility scripts.
