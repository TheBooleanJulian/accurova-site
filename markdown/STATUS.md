# Accurova Site — Status

**Last updated:** 2026-09-28. This is a living tracker — update it whenever a chunk of [PLAN.md](PLAN.md) gets built, not just at milestones. Where something is blocked, the reason is the point — don't just mark it "todo."

---

## Done

**Branding & metadata**
- Real logo (not text) in header/footer, favicon, and social-share `og:image` sitewide.
- Unique `<title>`/description/OG/canonical on every real page (previously 5+ pages had none).
- `sitemap.xml` covering all 16 real pages, ready for the `accurova.com` cutover.
- `robots.txt` correctly blocks staging crawling with the swap-over instructions already written in as a comment.

**Structured data**
- `LocalBusiness` (homepage + About), `Person` (Julian, About), `BreadcrumbList` (Pricing/About/Testimonials/Contact), `FAQPage` (Pricing), `ContactPage` (Contact), `Service` (product-photography). Real UEN (`53483334M`) and the verified Singapore SME 500 Award 2026 are in the `LocalBusiness` data — linked to the ATC verification page, not stated as a bare claim.

**Core pages**
- Homepage, Portfolio (index + product), Services (index + product-photography), Case Studies (index + 6 generated stories), 404/error page — all pre-existing, now updated.
- **New this cycle:** `/about/`, `/pricing/`, `/contact/`, `/testimonials/` promoted from homepage anchors to real dedicated pages with their own URLs, matching the old Pixieset structure for eventual 301 continuity. Content is verbatim from `data/source-content-accurova-com.md`, not invented.
- Homepage's pricing/testimonials sections trimmed to teasers linking out, to avoid duplicate content with the new pages.

**Internal linking & content integrity**
- Nav/footer rewired site-wide (including case-studies, which had its own stale copy diverged from the real footer).
- Removed a fabricated "SME500 Award 2026" line from the case-studies footer, then correctly reinstated it once confirmed real (see `data/source-content-accurova-com.md`'s correction note) — same footer/business.json now agree everywhere.
- Full sitewide link-check script run twice; zero broken internal links across all real pages.
- Fixed several dead `#pricing`/`#about` anchors left over from before the dedicated pages existed.

**Infra**
- Fixed a real production bug: Zeabur's Caddy buildpack auto-detects a root-level `404.html` as an MPA-fallback marker, which was silently 404-ing every request including `/`. Renamed to `errors/not-found.html` (root-absolute links, since a Caddy error page is served under whatever URL was actually requested) and shipped a custom `Caddyfile` that explicitly wires it up correctly.
- Repo decluttered: `build_includes.py` / `generate_case_studies.py` → `scripts/`, planning docs → `markdown/`.

---

## Partial / in progress

- **URL inventory (PLAN.md §7 / migration)** — live `accurova.com` blocks WebFetch with a 403 (Pixieset bot protection) and this environment has no outbound `curl`. Only `/` and `/testimonials/` confirmed indexed via search; `/about/`, `/pricing/`, `/portfolio/`, `/contact/`, `/accurova-ai/` are believed to exist (per the tasklist's own list) but unconfirmed. **Needs:** Google Search Console export from Julian, or connector access.
- **Service pages (PLAN.md §4)** — only `product-photography.html` exists as a worked example. `corporate-photography`, `event-photography`, `portrait-photography`, `cosplay-photography` are specced but not built.
- **Testimonials contextual placement** — the 10 real testimonials live on `/testimonials/` and 3 appear on the homepage; not yet cross-linked onto relevant service/case-study pages.
- **About page** — story + accreditation done; team/studio photos and equipment-with-photos not added.

---

## Not started — homepage/case-study architecture brief (not yet executed)

[HOMEPAGE-CASESTUDY-ARCHITECTURE.md](HOMEPAGE-CASESTUDY-ARCHITECTURE.md) is a full implementation brief Julian dropped in and hasn't executed yet. None of it is built. Before starting it, two conflicts need resolving with Julian (flagged in that file's status note): its pricing figures contradict the verified real rate card, and its "Property Photography" category isn't confirmed as a real offering. Once resolved, it covers:

- Case-study taxonomy fields (category/subcategories/client/location/project_type/services/duration/deliverables/featured/related_service/related_case_studies) — richer than the current `case-studies/data/*.json` schema.
- Standalone case-study page structure (hero → project overview → brief → approach → results gallery → deliverables → testimonial → related service → CTA) and the service-page-vs-case-study distinction.
- Quote estimator (interactive package-estimate flow — this also appears as a lighter mention in PLAN.md §4).
- Reusable component list (`ServiceCard`, `CaseStudyCard`, `PricingCard`, `FAQ`, `CTA`, `ClientLogo`, `ProcessStep`, etc.) so new case studies don't require redesigning the site.
- Breadcrumbs on deeper pages (Home → Portfolio → Category → Project, and Home → Services → Category) — visible + structured data. Currently only Pricing/About/Testimonials/Contact have `BreadcrumbList` JSON-LD; portfolio and services pages don't.
- Its own FAQ topic list (cost, booking lead time, travel within Singapore, delivery time, RAW files, corporate packages, custom shot requests, night events, custom commercial quotes) — overlaps with but isn't identical to PLAN.md's FAQ list; reconcile into one list when the FAQ hub gets built.
- "Future scalability" categories (commercial, branding, food, real estate, videography, corporate content packages, workshops, photowalks, studio rental, overseas assignments) — explicitly not to build now, just don't architect against them.

## Not started

- **Resources hub, FAQ hub, pillar content, downloads, comparison pages** (PLAN.md §4) — none built. Homepage's "Insights" section is still explicitly placeholder card copy.
- **Quote estimator** (PLAN.md §4 Homepage) — interactive package-estimate flow, not built. Worth doing once dedicated service pages exist to route into.
- **Image SEO** (PLAN.md §5) — nearly every image on the site is still a `picsum.photos` placeholder, not a real delivered photograph. Filenames, alt text, `srcset`, lazy-loading strategy all depend on real images existing first — doing this now would just be optimizing placeholder filenames.
- **Analytics & attribution** (PLAN.md §6) — no GA4 or equivalent configured, no UTM/CTA-click tracking, no lead-source capture. Needs Julian's analytics account access.
- **Migration redirect map** (PLAN.md §7) — can't build `old-urls.csv`/`redirect-map.csv` without the URL inventory above.
- **Domain cutover** (PLAN.md §7) — pointing `accurova.com` at Zeabur, canonical host (`www` vs bare) decision, Cloudflare DNS/CDN config, `gallery.accurova.com` / `pixieset.accurova.com` setup. All Zeabur-dashboard/DNS-registrar actions, not code — needs Julian to action or explicitly delegate dashboard access.
- **Local SEO** (Google Business Profile, physical address/UEN-on-listings consistency) — no address is published anywhere yet (`business.json` still marks it `TODO`); UEN is now known and in place everywhere else.
- **Accessibility audit, performance/Lighthouse pass, mobile UX pass** — not run yet; reasonable to defer until real images replace placeholders (performance numbers on placeholder images aren't representative).
- **AI Innovation as a standalone page** — currently just a homepage section; fine as-is unless/until the business wants to push Accurova.AI as a product to other photographers (per its real public positioning) rather than just an internal-workflow mention.

---

## Blocked on Julian / external access (not something to keep re-flagging — action once, then wait)

1. **Google Search Console + Analytics access** — needed for the URL inventory, baseline traffic numbers, and post-launch monitoring.
2. **DNS/Zeabur dashboard access or action** — domain architecture (§7), actual cutover.
3. **Confirm the positioning question** (PLAN.md §2) — corporate-studio framing vs. the real personal-brand-with-cosplay/astro positioning the live site actually uses. This gates how much of the "10 service pages + 10 industry pages" architecture is worth building at all, and also affects whether HOMEPAGE-CASESTUDY-ARCHITECTURE.md's 5-category list (no cosplay/astro) needs revising before it's executed.
4. **Reconcile HOMEPAGE-CASESTUDY-ARCHITECTURE.md's two flagged conflicts** — its pricing figures vs. the real rate card, and its unconfirmed "Property Photography" category — before building anything from it.
5. **Real portfolio/case-study images** — everything downstream of this (image SEO, real case studies replacing the 6 placeholders, alt text) is blocked on delivered photographs existing in the repo.
6. **Physical address / legal name**, if Julian wants those published (currently correctly left as `TODO` rather than invented).

---

## Quick priority read (borrowed from the original SEO/GEO tasklist's P0/P1/P2 split)

- **P0 (do before any domain cutover):** URL inventory + redirect map, GSC/analytics wired up, real portfolio images in at least the homepage hero and one full case study, accessibility/mobile pass.
- **P1 (strongly recommended, not launch-blocking):** remaining service pages, FAQ hub, real case studies replacing all 6 placeholders, testimonials cross-linked onto service pages.
- **P2 (post-launch growth):** pillar content, comparison pages, downloads, Singapore-specific content expansion, backlink building.
