# Accurova Site

Static site source for accurova.com — a commercial photography studio site. Pure HTML/CSS, no build pipeline, deployed as static files (Zeabur).

**Staging domain:** `home.accurova.com`, until the site is ready to replace the live Pixieset marketing site. `robots.txt` blocks all crawling until that cutover — see [ACCUROVA-BUILD-PLAN.md](ACCUROVA-BUILD-PLAN.md) for the full build plan, phases, and content rules (never invent business facts — pricing, testimonials, review counts, etc.).

## Stack

- Plain HTML + `assets/style.css` (design tokens: void/teal/gold palette, Space Grotesk display font, JetBrains Mono for labels/data)
- Case studies are generated from JSON via a small Python script — see below
- No JS framework, no npm, no server-side code

## Structure

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
  <slug>/index.html          ← generated, don't hand-edit
  index.html                 ← generated, don't hand-edit
generate_case_studies.py    regenerates case-studies/*/index.html from data/*.json
partials/header.html        canonical nav, injected into every page
partials/footer.html        canonical footer, injected into every page
build_includes.py           renders partials/*.html into every page's INCLUDE markers
data/business.json          canonical business info — TODO fields are unverified, don't publish as fact
assets/style.css            shared design system
```

Full page-by-page build plan for the rest of the site (industries, resources, FAQ, about, contact, etc.) is in [site-architecture.md](site-architecture.md). The overall project plan, phases, and content-integrity rules are in [ACCUROVA-BUILD-PLAN.md](ACCUROVA-BUILD-PLAN.md).

## Editing nav/footer

Nav and footer are shared across every hand-authored page via include markers:

```html
<!--INCLUDE:HEADER--> ... <!--/INCLUDE:HEADER-->
<!--INCLUDE:FOOTER--> ... <!--/INCLUDE:FOOTER-->
```

Edit `partials/header.html` / `partials/footer.html` (use `{{ROOT}}` for the relative path prefix — the script fills in `../` per directory depth), then run:

```
python build_includes.py
```

This rewrites every page's markers in place. It skips `case-studies/` (that section has its own generator) and is safe to re-run any time. To add nav/footer to a new hand-authored page, wrap its `<header>`/`<footer>` blocks in the same markers and run the script.

## Working with case studies

Case studies are the one part of the site with a generation step. Details in [README-CASE-STUDIES.md](README-CASE-STUDIES.md); short version:

```
cp case-studies/data/_TEMPLATE.json case-studies/data/<slug>.json
# fill in the JSON, point images at assets/case-studies/<slug>/
python3 generate_case_studies.py
git add -A && git commit -m "case study: <slug>" && git push
```

Everything else is hand-authored HTML — copy an existing page in the same section as a starting template and keep the shared header/nav/footer and component classes (`.work-grid`, `.meta-row`, `.filter-chip`, `.cta-band`, etc.) consistent.

## Deploy

Static files served on Zeabur — push to `main` and it deploys automatically.
