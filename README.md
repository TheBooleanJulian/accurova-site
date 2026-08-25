# Accurova Site

Static site source for accurova.com — a commercial photography studio site. Pure HTML/CSS, no build pipeline, deployed as static files (Zeabur).

## Stack

- Plain HTML + `assets/style.css` (design tokens: void/teal/gold palette, Space Grotesk display font, JetBrains Mono for labels/data)
- Case studies are generated from JSON via a small Python script — see below
- No JS framework, no npm, no server-side code

## Structure

```
index.html                  homepage
services/                   service pages (template: services/product-photography.html)
portfolio/                  portfolio index + project pages
case-studies/
  template.html             page shell used to generate each story
  index-template.html       landing page shell (filter chips)
  data/*.json               one JSON file per case study (source of truth)
  <slug>/index.html          ← generated, don't hand-edit
  index.html                 ← generated, don't hand-edit
generate_case_studies.py    regenerates case-studies/*/index.html from data/*.json
assets/style.css            shared design system
```

Full page-by-page build plan for the rest of the site (industries, resources, FAQ, about, contact, etc.) is in [site-architecture.md](site-architecture.md).

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
