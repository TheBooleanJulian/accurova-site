# Accurova Case Studies — how this fits the rebuild

This is dropped straight into your existing `accurova/` build (homepage, services,
portfolio, `assets/style.css`) — it's the **Case Studies** section: the "highly
relatable, shareable portfolio dump" of real event / portrait / product stories,
using your real header/nav/footer and existing component classes
(`.work-grid`, `.meta-row`, `.filter-chip`, `.breadcrumb`, `.eyebrow`, `.cta-band`)
rather than introducing a parallel style system.

## How it works

Nothing dynamic, no server, no database — same static-HTML-on-Zeabur pattern as
juliancheung.com. The only "build step" is a one-command Python script.

```
accurova/
├── assets/
│   └── style.css                case-study CSS appended to the bottom, same tokens
├── case-studies/
│   ├── template.html             the page shell — one template, many stories
│   ├── index-template.html       the portfolio-dump landing page w/ filter chips
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
├── index.html                    nav + footer updated with a Case Studies link
├── portfolio/ , services/        unchanged
└── generate_case_studies.py      run from this root
```

## Adding a real story

1. `cp case-studies/data/_TEMPLATE.json case-studies/data/wedding-launch-2026.json`
2. Fill in the real brief, process, anecdote, and testimonial. Swap the
   `picsum.photos` placeholder URLs for real delivered frames — drop images in
   `assets/case-studies/<slug>/` and point `cover_image` / `gallery` at them.
3. `python3 generate_case_studies.py` — regenerates every page + the index
   (safe to re-run any time, including after editing an old entry).
4. `git add -A && git commit -m "case study: wedding launch 2026" && git push`
   → Zeabur auto-deploys. Live at `accurova.com/case-studies/wedding-launch-2026/`.

Delete a JSON file + re-run the script to remove a case study.

## Why this shape (not a CMS, not a DB)

- **Clean per-page URLs** (`/case-studies/event-a/`) rather than `?slug=` query
  params, because static JS-templated pages don't get crawled properly and the
  whole point of this section is *sharing* — WhatsApp/LinkedIn/IG link previews
  need real per-page `<meta property="og:*">` tags, which only work if the HTML
  is actually generated per page (done — see `template.html` head).
- **One JSON file per story** keeps editing dead simple and diffable in git —
  no HTML wrangling to add a new case study, no risk of breaking shared markup.
- **Zero new stack.** Pure Python stdlib (`json`, `pathlib`, `re`), same as
  most of your tools — no npm install, no build pipeline change on Zeabur,
  since Zeabur is just serving the resulting static files.
- **Reuses your real components**, not a parallel style system: gallery =
  `.work-grid`, meta row = `.meta-row`, filters = `.filter-chip`, related
  cards = a new `.cs-card` sized to match `.t-card`/`.insight-card`. Header,
  nav, and footer are copy-pasted verbatim from `index.html`/`portfolio/product.html`
  with the relative paths adjusted for the extra folder depth.

## Design system used

Your existing tokens, unchanged: `--void:#050508`, `--surface:#0a0e14`,
`--teal:#00D4C8`, `--gold:#F5C842`, Space Grotesk (`--display`) + JetBrains
Mono (`--mono`), 2px border-radius, hairline `--line` borders. The
`01 — Challenge`, `02 — Approach`... numbering mirrors your `.process-step`
pattern from the service pages, since a case study genuinely *is* a sequence —
brief → shoot → edit → delivery → result.

## Next steps

- Swap the 6 placeholder stories for real ones (start with your best BNI or
  product shoot — the structure's already fixed per your original brief).
- `index.html`'s nav and footer now link to `case-studies/index.html` — same
  update is worth making on `services/*.html` and `portfolio/*.html` once you
  regenerate those (they still point Case Studies at `#`).
- Once you've got ~10+ real stories in, consider an "Industries" filter
  alongside category — the JSON schema has room (add `"tags": [...]`, extend
  `index-template.html`'s filter bar to match).
- Give each entry real delivered images instead of picsum placeholders before
  sharing links — the OG image is what shows up in the WhatsApp/LinkedIn preview.
