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

Pure HTML/CSS site for Accurova, a commercial photography studio, with no build pipeline or JS framework — deployed as static files on Zeabur. It currently runs at the staging domain `home.accurova.com` until it's ready to replace the live Pixieset marketing site; `robots.txt` blocks crawling until that cutover. See [ACCUROVA-BUILD-PLAN.md](ACCUROVA-BUILD-PLAN.md) for the full build plan, phases, and content-integrity rules — most importantly, never inventing business facts (pricing, testimonials, review counts, etc.).

## Features

- Shared header/nav/footer injected into every hand-authored page via `partials/header.html` / `partials/footer.html` and `build_includes.py`, using `<!--INCLUDE:HEADER-->`/`<!--INCLUDE:FOOTER-->` markers
- Case studies generated from JSON source-of-truth files (`case-studies/data/*.json`) via `generate_case_studies.py`, so each story's page is never hand-edited directly
- `data/business.json` as the canonical source for business info, with unverified fields explicitly marked so nothing gets published as fact prematurely
- Design system (`assets/style.css`) built on a void/teal/gold palette with Space Grotesk for display type and JetBrains Mono for labels/data
- Dedicated service, portfolio, and case-study sections, each following a consistent template/component pattern (`.work-grid`, `.meta-row`, `.filter-chip`, `.cta-band`, etc.)
- `robots.txt` blocking crawling on the staging domain until the real cutover

## Tech Stack

| Layer | Choice |
|---|---|
| Markup/Styling | Plain HTML + `assets/style.css` — no framework, no npm |
| Build tooling | Python scripts (`build_includes.py`, `generate_case_studies.py`) — no JS build step |
| Hosting | Zeabur (static files), auto-deployed on push to `main` |

## Screenshots

_Screenshots coming soon._

## Setup / Quick Start

No install needed — this is a static site with two small Python helper scripts.

```bash
git clone https://github.com/TheBooleanJulian/accurova-site
cd accurova-site

# rebuild shared header/footer into every hand-authored page
python build_includes.py

# regenerate case-study pages from case-studies/data/*.json
python3 generate_case_studies.py
```

Then open `index.html` directly, or serve the folder with any static file server.

## Project Structure

```
index.html                  homepage
404.html                    not-found page
robots.txt                  blocks crawling on the staging domain
services/                   service pages (template: services/product-photography.html)
portfolio/                  portfolio index + project pages
case-studies/
  template.html             page shell used to generate each story
  index-template.html       landing page shell (filter chips)
  data/*.json               one JSON file per case study (source of truth)
  <slug>/index.html          <- generated, don't hand-edit
  index.html                 <- generated, don't hand-edit
generate_case_studies.py    regenerates case-studies/*/index.html from data/*.json
partials/header.html        canonical nav, injected into every page
partials/footer.html        canonical footer, injected into every page
build_includes.py           renders partials/*.html into every page's INCLUDE markers
data/business.json          canonical business info — TODO fields are unverified, don't publish as fact
assets/style.css            shared design system
```

Full page-by-page build plan for the rest of the site (industries, resources, FAQ, about, contact, etc.) is in [site-architecture.md](site-architecture.md). The overall project plan, phases, and content-integrity rules are in [ACCUROVA-BUILD-PLAN.md](ACCUROVA-BUILD-PLAN.md).

## Working with case studies

Details in [README-CASE-STUDIES.md](README-CASE-STUDIES.md); short version:

```bash
cp case-studies/data/_TEMPLATE.json case-studies/data/<slug>.json
# fill in the JSON, point images at assets/case-studies/<slug>/
python3 generate_case_studies.py
git add -A && git commit -m "case study: <slug>" && git push
```

## Deploy

Static files served on Zeabur — push to `main` and it deploys automatically.

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
