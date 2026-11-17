# Accurova Case Studies — how this works

The **Case Studies** section: real event/portrait/product stories, using the site's real header/nav/footer and existing component classes (`.work-grid`, `.meta-row`, `.filter-chip`, `.breadcrumb`, `.eyebrow`, `.cta-band`) rather than a parallel style system. See [PLAN.md § Case Studies](PLAN.md#page-specifications) for the content spec each story should follow.

## How it works

Nothing dynamic, no server, no database — same static-HTML-on-Zeabur pattern as the rest of the site. The only "build step" is a one-command Python script.

```text
accurova-site/
├── assets/
│   └── style.css                case-study CSS lives alongside the rest, same tokens
├── case-studies/
│   ├── template.html             the page shell — one template, many stories
│   ├── index-template.html       landing page; two-level filter chips are generated from TAXONOMY in the generator
│   ├── data/
│   │   ├── _TEMPLATE.json        copy this to start a new case study
│   │   ├── event-a.json          placeholder — 6 sample entries pre-loaded
│   │   ├── event-b.json
│   │   ├── portrait-a.json
│   │   ├── portrait-b.json
│   │   ├── product-a.json
│   │   └── product-b.json
│   ├── event-a/index.html        ← generated, don't hand-edit
│   ├── ...                       ← generated, don't hand-edit
│   └── index.html                ← generated, don't hand-edit
├── index.html, portfolio/ (redirect stubs), services/, about/, pricing/, contact/, testimonials/   unrelated to this generator
└── scripts/generate_case_studies.py   run from the repo root
```

## Adding a real story

1. `cp case-studies/data/_TEMPLATE.json case-studies/data/wedding-launch-2026.json`
2. Fill in the real brief, process, anecdote, and testimonial. Drop images in
   `assets/case-studies/<slug>/` and point `cover_image` / `gallery` at them.
3. `python3 scripts/generate_case_studies.py` — regenerates every page + the index
   (safe to re-run any time, including after editing an old entry).
4. `git add -A && git commit -m "case study: wedding launch 2026" && git push`
   → Zeabur auto-deploys. Live at `accurova.com/case-studies/wedding-launch-2026/`.

Delete a JSON file + re-run the script to remove a case study.

If you edit `case-studies/template.html` or `case-studies/index-template.html` directly (e.g. changing nav/footer, layout), always re-run `scripts/generate_case_studies.py` afterward — the generated pages and the index are stale copies until you do.

## Replacing a placeholder story

Every filter chip on `/case-studies/` has at least one placeholder story (32 in total), so
you can fill them in one by one instead of starting from blank JSON. Each one is marked
`[PLACEHOLDER]` (title, copy) or `[X]` / `[Client name]` / `[Month Year]` (facts). Nothing in
them is a real figure, so nothing ships as fact by accident.

1. **Images:** each story's files are already in `assets/case-studies/<slug>/`:
   `cover.jpg` (16:9) and `1.jpg` to `6.jpg` (4:5). Each one is a labelled placeholder
   graphic. Overwrite it with a real frame **using the same filename**, so no JSON
   change is needed. `property-a` uses its own names (`wide-01.jpg`, `360-01.jpg`, …).
   Want more or fewer frames? Edit the `gallery` list.
2. **Copy:** open `case-studies/data/<slug>.json` and replace every `[PLACEHOLDER]` /
   `[X]` / `[...]` value. Rename `slug` (and the file and image folder) if you want a nicer URL.
3. Run `python scripts/generate_case_studies.py`, then commit.

Won't have a real story for a chip any time soon? Delete its JSON (and image folder)
and re-run the script. The chip then shows the "being added" empty state. PLAN/STATUS
call for one strong story per category, so deleting the extras is expected.

To check what's still placeholder: `grep -l PLACEHOLDER case-studies/data/*.json`.

| Slug | Card title | Category → sub-filters |
|---|---|---|
| `anniversary-a` | Anniversary Shoot | events → anniversaries |
| `astro-a` | Astrophotography | creative → astrophotos |
| `baby-a` | Baby Session | people → babies |
| `birthday-a` | Birthday Celebration | events → birthdays |
| `bts-a` | Behind the Scenes | events → bts |
| `comedy-channel-a` | ChuckleClips | video → comedy-channel |
| `community-event-a` | Community Event | events → community-events |
| `cosplay-a` | Cosplay Shoot | people → cosplay |
| `drone-a` | Drone Aerials | aerial → drone |
| `event-a` | BNI Crescendo Gala | corporate → galas, corporate-events |
| `event-b` | Product Launch Party | corporate → corporate-events |
| `event-video-a` | Event Highlight Reel | video events → event-videography |
| `fashion-a` | Fashion Lookbook | commercial → fashion |
| `furkid-a` | Furkid Portraits | people → furkids |
| `graduation-a` | Graduation Portraits | events → graduation |
| `hologram-a` | Hologram Capture | aerial → holograms |
| `influencer-a` | GraceYuki Content | video people → influencer-marketing |
| `lifestyle-a` | Lifestyle Session | people → lifestyle |
| `macro-a` | Macro Study | creative → macro |
| `mice-a` | MICE Conference | corporate → mice, corporate-events |
| `motorsports-a` | Motorsports Shoot | sports → motorsports |
| `portrait-a` | Executive Headshots | corporate → corporate-headshots, team-shoots |
| `portrait-b` | Founder Branding Session | people → portraiture |
| `product-a` | E-commerce Catalogue | commercial → product |
| `product-b` | F&B Lifestyle Shoot | commercial → product, fb, marketing-campaigns |
| `product-video-a` | Product Video | video commercial → product-videography, product |
| `property-a` | Residential Property Shoot | commercial aerial → property, virtual-tours, 360 |
| `property-video-a` | Property Walkthrough | video commercial → property-videography, property |
| `proposal-a` | Surprise Proposal | events → proposals |
| `sports-a` | Sports Coverage | sports → sports |
| `underwater-a` | Underwater Shoot | sports → underwater |
| `wedding-a` | Wedding Day | events → weddings |

The homepage reel/bento images are the same kind of labelled placeholders in
`assets/home/` (e.g. `reel-cosplay.jpg`, `bento-product.jpg`, `behind-the-scenes.jpg`), and the
Product Photography service page uses `assets/services/product-hero.jpg` /
`product-sample.jpg`. Overwrite those the same way.

## Why this shape (not a CMS, not a DB)

- **Clean per-page URLs** (`/case-studies/event-a/`) rather than `?slug=` query
  params, because static JS-templated pages don't get crawled properly and the
  whole point of this section is *sharing* — WhatsApp/LinkedIn/IG link previews
  need real per-page `<meta property="og:*">` tags, which only work if the HTML
  is actually generated per page (see `template.html`'s `<head>`).
- **One JSON file per story** keeps editing dead simple and diffable in git —
  no HTML wrangling to add a new case study, no risk of breaking shared markup.
- **Zero new stack.** Pure Python stdlib (`json`, `pathlib`, `re`) — no npm
  install, no build pipeline change on Zeabur, since Zeabur just serves the
  resulting static files.
- **Reuses real components**, not a parallel style system: gallery =
  `.work-grid`, meta row = `.meta-row`, filters = `.filter-chip`, related
  cards = `.cs-card` sized to match `.t-card`/`.insight-card`.

## Design system used

Same tokens as the rest of the site, unchanged: `--void:#050508`, `--surface:#0a0e14`, `--teal:#00D4C8`, `--gold:#F5C842`, Space Grotesk (`--display`) + JetBrains Mono (`--mono`), 2px border-radius, hairline `--line` borders. The `01 — Challenge`, `02 — Approach`... numbering mirrors the `.process-step` pattern from the service pages, since a case study genuinely *is* a sequence — brief → shoot → edit → delivery → result.

## Status / next steps

See [STATUS.md](STATUS.md) for the current up-to-date checklist. As of the last update:

- Nav/footer across the whole site (including case-studies) are in sync — done.
- All 32 case studies are placeholder scaffolds (see *Replacing a placeholder story* above). None may go live as real case studies. Replace them with genuine projects or delete them before the `accurova.com` cutover.
- Once ~10+ real stories exist, consider an "Industries" filter alongside category (the JSON schema has room — add `"tags": [...]`, extend `index-template.html`'s filter bar to match).

## Categories & filters

The landing page filter is two-level (category chips, then sub-chips), defined once in `TAXONOMY` in `scripts/generate_case_studies.py`. Each story JSON carries `cat` (one or more top-level slugs, space-separated) and `tags` (sub-filter slugs); `category` (event/portrait/product/property) is still used for the card label and "related" matching. Deep links: `case-studies/index.html#video`, `#events`, etc. This supersedes the old single-level "Industries" filter idea above.
