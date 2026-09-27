# Accurova Site — Master Plan

**Project:** `accurova-site`
**Staging domain:** `https://home.accurova.com/` — live here until the site is ready to replace the current Pixieset public marketing site. Pixieset stays in place for client gallery delivery throughout, and is never removed.
**Eventual domain:** `https://www.accurova.com/`
**Purpose:** Replace the current Pixieset public marketing website with a custom, static, search/AI-friendly commercial photography site, while keeping Pixieset for client gallery delivery.

This document consolidates what were previously three overlapping files (`ACCUROVA-BUILD-PLAN.md`, `site-architecture.md`, `accurova_new_homepage_seo_geo_tasklist.md`) into one. For **what's actually built vs. still outstanding right now**, see [STATUS.md](STATUS.md) — that file tracks current state; this one stays the stable reference for scope, rules and page specs.

---

## 1. Working principles (read first)

**Content integrity — never invent:**
client names, testimonials, event results, business metrics, awards, certifications, review counts, ratings, pricing, turnaround times, number of photographs delivered, years of experience, partnerships, or media appearances. If information is missing, use a clearly marked placeholder and ask the owner to provide it — never let a placeholder quietly become a production claim. The canonical source for verified facts is `data/business.json`, backed by `data/source-content-accurova-com.md`.

**Build order — authority architecture before content volume:**

```text
Business identity → Services → Portfolio → Case studies → Reviews → FAQs/resources → Internal linking → Search/AI visibility → Lead attribution
```

Do not spend the project generating dozens of SEO articles before the commercial core exists. A buyer and a search/answer engine should be able to understand the same thing from the site.

**Technical baseline:** static HTML/CSS, minimal vanilla JS, Python for generation (`scripts/build_includes.py`, `scripts/generate_case_studies.py`) — no framework, no build pipeline, unless a real need is demonstrated and documented. Reuse existing components; don't design a parallel style system per section.

**Before making structural changes:** inspect the current repo, run it locally, identify what's reusable vs. broken, and don't delete existing content without recording what was removed and why.

---

## 2. Positioning — unresolved tension, flag before expanding content

Two positioning directions exist in this project's own history and haven't been reconciled by Julian yet:

- **This plan's original framing:** Accurova as a corporate/B2B commercial studio. Primary: Corporate / Event / Product Photography. Secondary: Corporate Headshots, Portraits, Commercial/Lifestyle content. Accurova.AI framed as an internal workflow tool.
- **What the live site (accurova.com, scraped 2026-08-25, see `data/source-content-accurova-com.md`) actually says:** Julian Cheung, freelance personal-brand photographer. Real nav is Home · About · Testimonials · Astrophotos · Accurova.AI · Contact · Trust & Privacy. Cosplay portraiture is a real, significant part of the business — 4 of the 10 published testimonials are from cosplayers. Accurova.AI is pitched publicly as a product for *other* photographers, not just an internal tool.

**Do not silently pick one.** The current site (this repo) has resolved this pragmatically per Julian's direction as: lead with corporate/commercial credibility for B2B search intent, but keep portrait/cosplay/astro fully visible as real, named categories (see `_positioningNote` in `data/business.json`). Treat any future expansion into the fuller corporate-studio architecture below (10 service pages, 10 industry pages, pillar content) as contingent on this being explicitly confirmed with Julian first — it's a much bigger content commitment than the personal-brand framing needs.

Avoid positioning Accurova as a generic "photographer who shoots everything," but also avoid overclaiming a corporate-studio identity the real testimonials and offering don't support.

---

## 3. Site architecture / URL structure

Clean directory-based URLs with trailing slashes. Current + planned:

```text
/                              homepage
/about/                        ✅ built
/pricing/                      ✅ built
/contact/                      ✅ built
/testimonials/                 ✅ built (was "reviews" in the original plan)
/portfolio/                    ✅ built (index + product category)
/services/                     ✅ built (index + product-photography example)
/services/[slug]/              planned: corporate-photography, event-photography,
                                portrait-photography, cosplay-photography (+ product-photography exists)
/case-studies/[slug]/          ✅ built, generated from case-studies/data/*.json
/resources/                    not built — guides, articles, downloads
/faq/                          not built — accordion FAQ hub
/ai-innovation/                not built as standalone; covered as a homepage section (#ai)
```

Do not mass-produce thin location/keyword pages. Every indexable page needs a real purpose for an actual prospective client.

---

## 4. Page specifications

### Homepage

1. Hero — Singapore photography positioning, primary CTA (quote/book), secondary CTA (view work).
2. Trust/credibility strip — only factual, verifiable claims (currently: real SME500 Award 2026, remaining slots are still placeholder client logos pending permission).
3. Services summary, linking to dedicated service pages.
4. Selected work, linking into portfolio + case studies.
5. Why Accurova — direction, guided experience, commercial-ready delivery, transparent pricing, human judgement.
6. Case studies (real projects only).
7. Testimonials, with service/category context where known.
8. Pricing summary ("starting from," matching the canonical source) linking to `/pricing/`.
9. FAQ summary (4-6 high-intent questions).
10. Final CTA — quote / WhatsApp / contact.

**Conversion funnel to support (not just one path):** `Google/AI/referral/social → homepage → understand Accurova → select service → see real case study → build trust → understand pricing → request quote` — but also let visitors enter via a service page or a case study directly and reach pricing/quote from there. Every page's job is to answer, without excessive scrolling: what does Accurova do, can it handle my type of photography, what does the work look like, roughly how much does it cost, can I trust the business, how do I contact them.

**Not built — quote estimator:** an interactive flow (`what do you need? → event/product/portrait/corporate/property → requirements → estimated package → request detailed quote`), clearly labelled as an estimate, not a guaranteed quotation. Worth considering once the dedicated service pages exist to route into.

### Services — `/services/[slug]/`

One template, real commercial landing pages rather than one generic page. Each needs: what the service covers, suitable use cases, what clients receive, approach, sample work, related case studies, related testimonials, pricing starting point, FAQs specific to that service, CTA.

Planned slugs and target intent:
- **corporate-photography** — corporate photographer/photography Singapore, company event photography, business photography Singapore.
- **event-photography** — corporate events, conferences, seminars, networking events, launches, company functions.
- **product-photography** ✅ built — product catalogue, e-commerce, marketing/campaign imagery, lifestyle product photography.
- **portrait-photography** — personal brand, executive, cosplay (per the real positioning — keep cosplay visible, don't downplay it into a footnote the way the original corporate-studio framing implied).
- **cosplay-photography** — real, significant category per testimonials; worth its own page rather than folding into portraits only, if content depth supports it.

Template sections (from the extended site-architecture spec): Hero (service name + image) → What's included (icon list) → Process (3-5 steps) → Sample gallery pulled from matching portfolio category → Pricing band ("from $X") → FAQ (3-4 Qs specific to that service) → CTA.

### Portfolio — `/portfolio/`

Visual evidence, not the main SEO text dump.

- **Index:** filter/category links — Corporate, Events, Products, Portraits, Cosplay, Astro, and other categories actually supported by real work. Same `.work-grid` masonry component at every scale.
- **Category pages:** short useful intro (100-150 words: what the category covers, typical use cases, typical turnaround), gallery, links to relevant case studies and service page, clear CTA. Don't create a category page with no meaningful content.
- **Individual project pages:** title, client (only where permitted), industry/type where known, location where appropriate, deliverables, gallery, concise description, related service, related case study, enquiry CTA.

**Refinement — don't split "portfolio" and "case studies" into two parallel systems.** A later planning pass concluded portfolio items work better *as* case studies rather than as separate generic category galleries: each real shoot stands alone as a complete page (service category → real case study → photographs → project context → result/deliverable → related service → enquiry CTA), demonstrating actual commercial capability rather than a bare "here are some product photos" gallery. Prefer this over building a separate thin category-page layer once enough real case studies exist to cover each category.

### Case Studies — `/case-studies/[slug]/`

✅ Built and one of the highest-priority features. Keep the JSON → generated-HTML architecture (`case-studies/data/*.json` is the source of truth; never hand-edit the generated `case-studies/[slug]/index.html`). See [CASE-STUDIES-GUIDE.md](CASE-STUDIES-GUIDE.md) for the day-to-day workflow.

Structure per story: Hero → project metadata → client/project context → Challenge → Approach → Behind the scenes (if available) → Final deliverables → Results/outcomes (only if supported) → client testimonial (only with permission) → related service → related portfolio → related resources → CTA.

The 6 current entries (`event-a/b`, `portrait-a/b`, `product-a/b`) are placeholder/demo content and must be clearly marked as such, or replaced with genuine projects, before production launch — never presented as real case studies on the live domain.

### Testimonials — `/testimonials/` (called "Reviews" in the original plan)

✅ Built, using the 10 real verbatim testimonials from `data/source-content-accurova-com.md`. No aggregate rating is published anywhere on the real site, so none is shown — don't add one without a genuine source. Where possible, testimonials should also surface contextually on relevant service/case-study pages (not yet done). Never fabricate or rewrite a client's words into a new testimonial.

### Pricing — `/pricing/`

✅ Built, using the single canonical rate card from `data/business.json` (Standard $250 / Enhanced $450 / Deluxe $850). This value must stay identical everywhere it's shown (homepage teaser, service pages, pricing page) — no contradictory pricing across pages. Use "starting from" since scope varies; don't claim a package includes something the real offering doesn't.

### About — `/about/`

✅ Built: story, Julian/photographer identity, philosophy, real accreditation (SME500 Award 2026, linked to the ATC verification page), CTA. Not yet added: team/studio photos, equipment-with-photos, a fuller AI-workflow-philosophy tie-in. Equipment should stay a supporting detail, not a major selling point — buyer should come away understanding who you are → what you do → why clients trust you → how you work.

### AI Innovation

Currently a homepage section (`#ai`), not a standalone `/ai-innovation/` page. If it becomes standalone: explain AI-assisted culling, workflow automation, asset organisation, image search, editing/retouching assistance, QA, turnaround optimisation — and explicitly state what stays human (photography, creative direction, client communication, visual judgement, final selection). Never imply AI-generated photography unless that's an actual offered service. Per the real site content, Accurova.AI is also a public-facing product pitched to *other* photographers, not just Accurova's internal tool — that distinction should be reflected if this page gets built out.

### Resources / Knowledge Centre — `/resources/` (not built)

Index tabbed/filtered by type: Guides, Articles, Behind the Scenes, Equipment, Lighting, Workflow, Checklists, Downloads, FAQ. Prioritise genuinely useful buyer questions (see the FAQ list in [STATUS.md](STATUS.md)); don't write articles purely to insert keywords, and don't launch hundreds of them at once.

Sub-parts, all currently unbuilt:
- **Pillar pages** — long-form (1,200-2,000 words) cornerstone content with a sticky table of contents; build these last, once supporting articles exist to link into them.
- **Downloads** — card grid of practical guides/checklists/templates; open (not gated) initially.
- **Comparison pages** (`/resources/[a]-vs-[b]/`) — two-column table + short verdict; cheap once the template exists.

### FAQ Hub — `/faq/` (not built)

Semantic `<details>/<summary>` accordion, grouped by category (Pricing, Booking, Preparation, Events, Products, Corporate headshots, Delivery, Licensing/usage, Editing, AI workflow) — good for accessibility and for answer-engine extraction. Answers must be concise and factually accurate.

### Contact — `/contact/`

✅ Built (WhatsApp + email CTA, links to pricing/portfolio). The fuller spec envisions four entry points (Book Consultation calendar, Request Quotation form, Upload a Brief, Studio Location map) plus a condensed FAQ — not yet built; current page is intentionally simpler.

---

## 5. Technical & SEO requirements

**Metadata (every indexable page):** unique `<title>`, unique meta description, canonical URL, correct H1, logical H2/H3 hierarchy, descriptive image alt text, Open Graph metadata, Twitter/X card metadata, internal links, breadcrumb navigation where appropriate.

**Structured data:** valid schema.org, only true/supportable properties — `LocalBusiness`/photography-appropriate subtype, `Person` for Julian, `WebSite`, `WebPage`, `BreadcrumbList`, `Service`, `Article`, `ImageObject`, `FAQPage` where genuinely applicable. Never fake aggregate ratings, reviews, awards, prices, locations, organisations or service areas — structured data must agree with the visible page content.

**Entity consistency:** `data/business.json` is the one canonical business-info source (name, website, description, Singapore service area, contact channels, social profiles, founder info, service categories, accreditations). Templates pull from it rather than repeating values that can drift out of sync.

**Internal linking:** build the relationship chain `Service → Portfolio Category → Project → Case Study → Review → Resource`, both directions. Every major service should link to relevant portfolio, case studies, FAQs, resources, pricing, and contact. Avoid orphan pages.

**Image SEO:** descriptive filenames (not `DSC_49283.jpg`), meaningful non-keyword-stuffed alt text, `srcset`/responsive images, lazy-load below the fold, eager-load the hero/LCP image, explicit width/height to avoid layout shift, modern formats where practical, appropriate compression without sacrificing visual quality (photography quality is a primary conversion factor — don't chase Lighthouse scores at its expense).

**Accessibility:** target WCAG 2.1/2.2 AA where practical — keyboard navigation, visible focus states, semantic HTML, sufficient contrast, accessible mobile menu, meaningful alt text, reduced-motion consideration, proper form labels, nothing hover-only. Run an automated audit before launch.

**Performance:** fast first load, strong mobile performance, minimal JS/third-party scripts, optimised fonts and images. The current static HTML/CSS approach is correct; don't introduce a framework without a demonstrated, documented benefit.

**Design direction:** preserve the existing void/teal/gold identity, Space Grotesk + JetBrains Mono, film/contact-sheet motifs — unless review shows a compelling reason to change. But keep photography dominant: this is a photography business, not a developer portfolio or SaaS landing page. Priority order: photographs → clarity → credibility → typography → conversion → technical sophistication.

Treat marketing pages (homepage, services), case studies, and everything else as three distinct content experiences sharing one design system but different information priorities — a case study should read as proof-of-capability, not another landing page. As a practical navigation test: a visitor should be able to answer "what does Accurova do / can it handle my type of shoot / what does the work look like / roughly how much / can I trust them / how do I contact them" without excessive scrolling or exploration on any given page.

**Data model:** central JSON data files under `data/` (business info; consider `services.json`, `portfolio.json`, `reviews.json`, `redirects.json`, `faq.json` as those sections get built) plus `case-studies/data/` — lets content be updated safely without hand-editing dozens of HTML files.

**GEO / AI discoverability:** repeatedly establish the entity relationship `Accurova → photography business → Singapore → Julian → [service]` in natural, factual language (not keyword lists) as crawlable HTML text, not only inside images. Answer real client questions concisely rather than writing generic SEO filler — see the FAQ list in [STATUS.md](STATUS.md).

---

## 6. Conversion, attribution & WhatsApp

Track (not yet implemented — no analytics access configured): CTA clicks, WhatsApp clicks, email clicks, enquiry form submissions, pricing-page CTA clicks, portfolio interactions, outbound Pixieset links, booking actions. Capture lead source where possible (Google Search, Google Maps, ChatGPT, Gemini, Perplexity, Instagram, LinkedIn, referral, direct, other) — never claim a lead came from a specific AI engine without evidence. Use UTM parameters for controlled campaigns; prepare for GA4 or a privacy-appropriate alternative; never put analytics secrets in public source.

WhatsApp is a major conversion channel — use context-aware CTA labels ("Ask about corporate photography" vs. a generic "Contact us") rather than identical CTAs everywhere, and include a source/service identifier in the message where practical so enquiries can be attributed. Don't expose private credentials.

---

## 7. Migration from Pixieset & launch

**Do not switch the live domain until the new site is validated.** Build a migration inventory (`old-urls.csv` / `redirect-map.csv` / `content-inventory.md`, not yet created — blocked on Search Console / crawl access, see STATUS.md) covering, per known old URL: current purpose, indexed?, backlinks known?, keep/redirect/merge/retire, new URL, redirect type, notes. Every valuable old URL that changes gets a 301; don't blindly redirect everything to the homepage — preserve destination intent.

**Staging → production architecture:**

```text
accurova.com → Cloudflare DNS/CDN/security → this static site (on Zeabur)
```

Pixieset remains available for client delivery/galleries throughout — never removed. Before DNS cutover, verify: staging deployment, HTTPS, redirects, sitemap, robots.txt, analytics, forms, WhatsApp, images, mobile, 404 page, canonical URLs.

**Testing/QA before launch** — per page: HTTP status, title, meta description, canonical, H1, broken internal links, image alt text, Open Graph, structured data presence. Site-wide: sitemap validity, robots.txt, no accidental `noindex`, no localhost/staging URLs, no placeholder copy, no fake testimonials/clients, no broken images, no orphan pages. Performance: Lighthouse/PageSpeed on homepage, each service type, one portfolio page, one case study, pricing, contact. Accessibility: automated WCAG audit.

**Build phases** (original plan's ordering — see STATUS.md for where the project actually is against this):

0. Repository audit → 1. Foundation (nav, footer, business data, metadata system, analytics hooks, CTA system, accessibility baseline, 404) → 2. Commercial core (homepage, services, pricing, contact) → 3. Proof (portfolio, case studies, reviews) → 4. Authority (FAQ, resources, guides, about, AI innovation) → 5. Technical SEO (sitemap, robots, canonical, structured data, OG, internal-link audit, image SEO, performance, accessibility) → 6. Migration (URL inventory, redirect map, staging test, crawl test, analytics test, mobile test, DNS/Cloudflare cutover plan) → 7. Post-launch monitoring (indexing, organic traffic, queries, page performance, enquiries, referral sources, AI referral traffic, broken links, search visibility — don't mass-publish content immediately after launch).

---

## 8. Future AI agent layer (aspirational, not built)

The architecture should make these possible without requiring them immediately: **SEO Auditor** (checks technical SEO, reports issues), **AI Visibility Monitor** (runs a controlled query set across search/answer engines, records whether Accurova appears), **Competitor Monitor**, **Content Opportunity Agent** (finds real unanswered buyer questions), **Case Study Agent** (turns structured project info into draft case studies without inventing facts), **Lead Attribution Agent** (source → enquiries → qualified leads → bookings → revenue), **Website QA Agent** (crawls production, reports broken links/missing metadata/accessibility issues/image issues/indexing problems/content inconsistencies).

---

## 9. Success metrics

The project succeeds only if it improves both visibility and business outcomes.

- **Search:** branded/non-branded search visibility, organic impressions/clicks, Google Maps visibility where measurable.
- **AI:** AI recommendation/citation frequency, AI referral traffic, queries where Accurova is mentioned, competitor mentions.
- **Website:** service-page visits, case-study visits, pricing visits, CTA interactions, WhatsApp clicks, enquiry submissions.
- **Business:** enquiries, qualified enquiries, bookings, revenue, revenue by acquisition source.

**Primary north-star:** qualified photography enquiries generated per month from search/AI discovery.
