# Accurova.com — Site Architecture &amp; Build Guide

Homepage is built (`index.html`). This doc is the pattern to extend into the other 12 sections — same design system (void/teal/gold, Space Grotesk + JetBrains Mono, contact-sheet/filmstrip motif), same placeholder-and-replace approach.

**Design tokens to reuse everywhere:**
`--void:#050508` `--surface:#0a0e14` `--teal:#00D4C8` `--gold:#F5C842` `--text:#E8E8ED` `--muted:#8890A0`
Display: Space Grotesk · Labels/data: JetBrains Mono

---

## The one strategic addition, made concrete

Every portfolio project page ends with a **"Related"** block: 1 case study + 1 resource article, matched by category tag (e.g. a Product shoot links to the Product Photography Guide + a relevant case study). Every resource/guide page ends with a **"See it in practice"** block: 2–3 portfolio thumbnails from that category. Build category tags (`product`, `corporate`, `food`, `industrial`, `hospitality`, `architecture`, `lifestyle`, `ecommerce`, `campaign`) once, and reuse them across Portfolio, Case Studies, and Resources so the linking is automatic rather than hand-curated per page.

---

## 2. Portfolio — `/portfolio/`

Index page: filterable grid (same `.work-grid` masonry component from homepage), filter chips = the 9 categories. Each category has its own sub-page (`/portfolio/product/`) using the same grid at larger scale + a short GEO intro paragraph (100–150 words: what the category covers, typical use cases, typical turnaround).

Each individual project = a **project detail template**:
- Hero image (full-bleed)
- Meta row (Client · Industry · Deliverables · Turnaround) in JetBrains Mono
- 4–8 image gallery
- "Related case study" + "Related guide" block

---

## 3. Services — `/services/[slug]/`

One template, 10 instances (Commercial, Product, Corporate, Event, Video, Drone, 360°/Virtual Tours, Retouching, Content Production, AI Workflow Enhancement).

Template sections: Hero (service name + 1 hero image) → What's included (icon list) → Process (3–5 numbered steps) → Sample gallery (pull from matching portfolio category) → Pricing band (range, not exact — "from $X") → FAQ (3–4 Qs specific to that service) → CTA.

---

## 4. Industries — `/industries/[slug]/`

Same template x10 (Retail, Manufacturing, Healthcare, Food, Hospitality, Real Estate, Finance, Technology, Government, Education).

Template: Hero → "Why [industry] chooses Accurova" (2–3 sentences on sector-specific needs: compliance, access hours, volume) → Relevant services (link out to 2–3 Services pages) → Case study for that industry → Portfolio gallery filtered to that industry.

---

## 5. Case Studies — `/case-studies/[slug]/`

Fixed structure per your brief — build as one template:
1. Challenge (client situation, 2–3 sentences)
2. Approach (methodology)
3. Behind the scenes (BTS photos — different from final deliverables)
4. AI-assisted workflow, where relevant (which parts were AI-accelerated vs. fully manual)
5. Final deliverables (gallery)
6. Results (metrics if available — turnaround time, volume delivered, client-reported outcome)

Index page = filterable card grid, same tag system as Portfolio.

---

## 6. Resources / Knowledge Centre — `/resources/`

Index = tabbed or filtered by type: Guides · Articles · Case Studies (pulls from #5) · Behind the Scenes · Equipment · Lighting · Workflow · Checklists · Downloads · FAQ (pulls from #11).

Each article template: Hero → eyebrow category tag → body (short paragraphs, subheads every 150–200 words for scannability and GEO) → pull-quote or stat callout in gold → "See it in practice" portfolio block → related articles (3).

---

## 7. Pillar Content — `/resources/[pillar-slug]/`

8 pillar pages (Commercial Photography, Product Photography, Corporate Branding Photography, Industrial Photography, Photography for Marketing, Photography Production, AI in Commercial Photography, Visual Content Strategy). Longer-form (1,200–2,000 words), each with a table-of-contents sidebar (JetBrains Mono, sticky) and a grid of 4–6 supporting article links at the bottom. These are your highest-effort SEO/GEO pages — write these last, once supporting articles exist to link into them.

---

## 8. AI Innovation — `/ai-innovation/`

Standalone page, same 4-item structure already on the homepage (`why-list` component) but expanded to 7 (culling, retouching, asset management, image search, workflow automation, turnaround, QA). Add a short "what this isn't" callout box — explicitly states no AI-generated imagery, human photographer on every shoot. This page is your differentiation anchor; link to it from every Service and Industry page's "why Accurova" mention.

---

## 9. Portfolio Resources — `/resources/downloads/`

Simple card grid, 7 items (Pricing Guide, Shoot Prep Checklist, Wardrobe Guide, Brand Photography Guide, Image Licensing Guide, Production Timeline, Creative Brief Template). Each card = title, 1-line description, file type/size, download button (gate behind email capture if you want lead-gen; placeholder as open download for now).

---

## 10. Comparison Pages — `/resources/[a]-vs-[b]/`

6 pages, single fixed template: two-column comparison table + short verdict paragraph ("choose X if... choose Y if..."). High SEO value, cheap to produce once the template exists. Link each comparison page into the relevant pillar page (#7).

---

## 11. FAQ Hub — `/faq/`

Accordion UI, grouped by the 8 categories (Pricing, Licensing, Turnaround, Preparation, Equipment, AI Workflow, Editing, Commercial Usage). Use `<details>/<summary>` semantic HTML — good for both accessibility and GEO/answer-engine extraction.

---

## 12. About — `/about/`

Single long-scroll page: Story → Team (grid of photos + roles) → Studio (space photos) → Equipment (Nikon D850, Godox V860III, Yongnuo RGB, Canon SELPHY CP1500 — list with photos) → Process → Certifications/Awards (SME500 2026) → Sustainability → AI Innovation Philosophy (short version, links to #8).

---

## 13. Contact — `/contact/`

Four entry points as separate tabs or anchored sections: Book Consultation (calendar embed placeholder), Request Quotation (form), Upload a Brief (file upload placeholder), Studio Location (map embed placeholder). End with a condensed FAQ (3–4 most-asked questions, linking to full FAQ Hub).

---

## Build order recommendation

1. ✅ Homepage
2. Services template (10 pages) — highest commercial intent
3. Portfolio index + category pages — needed to link from Services
4. ✅ Case Study template — `case-studies/template.html` + `index-template.html`, generated via `generate_case_studies.py` from `case-studies/data/*.json`. 6 placeholder stories loaded (event-a/b, portrait-a/b, product-a/b) — swap in real ones.
5. Industries template (10 pages)
6. AI Innovation page
7. About + Contact
8. Resources/Guides (start populating once portfolio + case studies exist to link into)
9. Pillar pages (need supporting articles to link to — build last)
10. Comparison pages + FAQ Hub (fast to produce once template exists)
