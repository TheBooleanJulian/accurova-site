<div align="center">

# Accurova Site

**Static site source for accurova.com — a commercial photography studio site.**

![HTML](https://img.shields.io/badge/-HTML-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/-CSS-1572B6?logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-AGPLv3%20%2B%20Commercial-00D4C8.svg)

</div>

---

## What it does

Pure HTML/CSS site for Accurova, a commercial photography studio, with no build pipeline or JS framework — deployed as static files on Zeabur. It currently runs at the staging domain `home.accurova.com` until it's ready to replace the live Pixieset marketing site; `robots.txt` blocks crawling until that cutover. See [markdown/ACCUROVA-BUILD-PLAN.md](markdown/ACCUROVA-BUILD-PLAN.md) for the full build plan, phases, and content-integrity rules — most importantly, never inventing business facts (pricing, testimonials, review counts, etc.).

## Features

- Shared header/nav/footer injected into every hand-authored page via `partials/header.html` / `partials/footer.html` and `scripts/build_includes.py`, using `<!--INCLUDE:HEADER-->`/`<!--INCLUDE:FOOTER-->` markers
- Case studies generated from JSON source-of-truth files (`case-studies/data/*.json`) via `scripts/generate_case_studies.py`, so each story's page is never hand-edited directly
- `data/business.json` as the canonical source for business info, with unverified fields explicitly marked so nothing gets published as fact prematurely
- Design system (`assets/style.css`) built on a void/teal/gold palette with Space Grotesk for display type and JetBrains Mono for labels/data
- Dedicated service, portfolio, and case-study sections, each following a consistent template/component pattern (`.work-grid`, `.meta-row`, `.filter-chip`, `.cta-band`, etc.)
- `robots.txt` blocking crawling on the staging domain until the real cutover
- Custom `Caddyfile` at the repo root, overriding Zeabur's auto-generated one so `errors/not-found.html` is wired up correctly as the 404 handler (see Deploy below)

## Tech Stack

| Layer | Choice |
|---|---|
| Markup/Styling | Plain HTML + `assets/style.css` — no framework, no npm |
| Build tooling | Python scripts (`scripts/build_includes.py`, `scripts/generate_case_studies.py`) — no JS build step |
| Hosting | Zeabur (static files via Caddy), auto-deployed on push to `main` |

## Screenshots

_Screenshots coming soon._

## Setup / Quick Start

No install needed — this is a static site with two small Python helper scripts.

```bash
git clone https://github.com/TheBooleanJulian/accurova-site
cd accurova-site

# rebuild shared header/footer into every hand-authored page
python scripts/build_includes.py

# regenerate case-study pages from case-studies/data/*.json
python3 scripts/generate_case_studies.py
```

Then open `index.html` directly, or serve the folder with any static file server.

## Project Structure

```
index.html                  homepage
robots.txt                  blocks crawling on the staging domain
Caddyfile                   custom Zeabur/Caddy config — see Deploy below
errors/not-found.html       404 page, served via Caddyfile's handle_errors (root-absolute links —
                             it must render correctly no matter what missing URL triggered it)
services/                   service pages (template: services/product-photography.html)
portfolio/                  portfolio index + project pages
case-studies/
  template.html             page shell used to generate each story
  index-template.html       landing page shell (filter chips)
  data/*.json               one JSON file per case study (source of truth)
  <slug>/index.html          <- generated, don't hand-edit
  index.html                 <- generated, don't hand-edit
scripts/build_includes.py         renders partials/*.html into every page's INCLUDE markers
scripts/generate_case_studies.py  regenerates case-studies/*/index.html from data/*.json
partials/header.html        canonical nav, injected into every page
partials/footer.html        canonical footer, injected into every page
data/business.json          canonical business info — TODO fields are unverified, don't publish as fact
assets/style.css            shared design system
markdown/                   planning docs (build plan, site architecture, case-study README)
```

Full page-by-page build plan for the rest of the site (industries, resources, FAQ, about, contact, etc.) is in [markdown/site-architecture.md](markdown/site-architecture.md). The overall project plan, phases, and content-integrity rules are in [markdown/ACCUROVA-BUILD-PLAN.md](markdown/ACCUROVA-BUILD-PLAN.md).

## Working with case studies

Details in [markdown/README-CASE-STUDIES.md](markdown/README-CASE-STUDIES.md); short version:

```bash
cp case-studies/data/_TEMPLATE.json case-studies/data/<slug>.json
# fill in the JSON, point images at assets/case-studies/<slug>/
python3 scripts/generate_case_studies.py
git add -A && git commit -m "case study: <slug>" && git push
```

## Deploy

Static files served on Zeabur via Caddy — push to `main` and it deploys automatically.

Zeabur's static buildpack normally auto-generates its own Caddyfile, and it does something surprising: if it finds a root-level file literally named `404.html`, it switches the whole site into an MPA-fallback mode that ended up 404-ing every request, including `/`. The repo now ships its own [`Caddyfile`](Caddyfile) at the root, which Zeabur uses in place of its auto-generated one — it serves static files normally and explicitly rewrites 404s to `errors/not-found.html` (not `404.html`, to avoid re-triggering that auto-detection). If you ever touch `Caddyfile`, redeploy and confirm `home.accurova.com/` and a deliberately bad URL like `home.accurova.com/does-not-exist` both resolve as expected.

## Status / Roadmap

- [x] Shared nav/footer via include markers and `business.json` as the business-data source
- [x] 404 page and staging `robots.txt`
- [x] Real content pulled from the live accurova.com site, replacing earlier placeholder/fabricated copy
- [x] Case-study generator (JSON → static HTML) with a working example set
- [ ] Full page-by-page build out per [site-architecture.md](site-architecture.md) (industries, resources, FAQ, about, contact)
- [ ] Cutover from the staging domain to replace the live Pixieset site, with `robots.txt` crawling re-enabled

## Changelog

- **2026-08-25** — Replaced fabricated placeholder content with real content pulled from the live accurova.com site
- **2026-08-25** — Phase 1 foundation: shared nav/footer, business data source, 404 page, staging `robots.txt`
- **2026-08-25** — Initial commit of the Accurova site

## License

This project is dual licensed.

- Community Edition — [GNU Affero General Public License v3 (AGPLv3)](LICENSE). Free to use, modify, and self-host. If you distribute a modified version or run it as a network service, you must make the corresponding source available.
- Commercial License — for organisations that want to embed, modify, or distribute this software without AGPLv3's obligations. See [COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md).

---

<div align="center">
<sub>Built by <a href="https://github.com/TheBooleanJulian">@TheBooleanJulian</a></sub>
</div>
