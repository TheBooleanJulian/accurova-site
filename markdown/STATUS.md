# Accurova Site — Status

**Last updated:** 2026-09-28. This is a living tracker — update it whenever a chunk of [PLAN.md](PLAN.md) gets built, not just at milestones. Where something is blocked, the reason is the point — don't just mark it "todo."

---

## Done

**Branding & metadata**
- Real logo (not text) in header/footer, favicon, and social-share `og:image` sitewide.
- Unique `<title>`/description/OG/canonical on every real page (previously 5+ pages had none).
- `sitemap.xml` covering all 18 real indexable pages, ready for the `accurova.com` cutover (`/privacy/` deliberately excluded — noindex, see below).
- `robots.txt` correctly blocks staging crawling with the swap-over instructions already written in as a comment.

**Structured data**
- `LocalBusiness` (homepage + About), `Person` (Julian, About), `BreadcrumbList` (Pricing/About/Testimonials/Contact/FAQ), `FAQPage` (Pricing, FAQ), `ContactPage` (Contact), `Service` (product-photography). Real UEN (`53483334M`), sole-proprietorship registration (per public ACRA lookup, 2024-03-29), and the verified Singapore SME 500 Award 2026 are in the `LocalBusiness` data — linked to the ATC verification page, not stated as a bare claim.

**Core pages**
- Homepage, Portfolio (index + product), Services (index + product-photography), Case Studies (index + 7 generated stories incl. Property), 404/error page — all pre-existing, now updated.
- `/about/`, `/pricing/`, `/contact/`, `/testimonials/` promoted from homepage anchors to real dedicated pages with their own URLs, matching the old Pixieset structure for eventual 301 continuity. Content is verbatim from `data/source-content-accurova-com.md`, not invented.
- **New this cycle:** `/faq/` (10 real Q&As, `<details>`/`FAQPage` schema) and `/privacy/` (Trust & Privacy Policy, summarized from the real live-site policy already captured in `data/source-content-accurova-com.md`, `noindex`'d as boilerplate legal content).
- Homepage's pricing/testimonials sections trimmed to teasers linking out, to avoid duplicate content with the new pages.

**Doctor Clean comparison — copied over (2026-09-28)**
Compared the site against doctorclean.com.sg for good, honestly-applicable conversion patterns:
- Floating WhatsApp button, sitewide (all real pages + case studies) — cheap, high-conversion, no data dependency.
- "How It Works" 4-step process section on the homepage (Tell Us What You Need → Plan → Shoot → Edit & Deliver), matching the spec already written in `HOMEPAGE-CASESTUDY-ARCHITECTURE.md` §16 but never built.
- `/faq/` hub with a footer link (see above).
- Expanded homepage/About "Why Accurova" from 3 points to 5 — added the real production team and the real accreditation as genuine differentiators, matching Doctor Clean's icon-grid pattern without inventing anything (no fake "insured"/"guaranteed" claims added).
- Team section on `/about/` — Julian, Shawn, Damian (confirmed real by Julian 2026-09-28; Accurova is not solo).
- PayNow noted as the accepted payment method on `/pricing/` and in `business.json`.
- Google Business Profile link captured (`business.json.googleBusinessProfile`) — Accurova has a real GBP listing; rating/review count unconfirmed (Maps is JS-rendered, couldn't be scraped in this environment).
- Deliberately **not** copied: team/leadership bios beyond name+role (no more detail given), payment-method badge row (PayNow only, no card/GrabPay gateway), promo/discount banners, date-time booking widget, client logo wall (still no real permissions), press-mention logos (none exist) — see PLAN.md's content-integrity rule.

**Internal linking & content integrity**
- Header simplified 2026-09-28: 4 grouped nav items + single Book Consult CTA, working mobile menu. Portfolio filter rebuilt as two-level categories/sub-filters incl. Video; tiles are still placeholders tagged to the new taxonomy, and empty categories show an empty-state. Portfolio meta/title and footer links updated.
- Nav/footer rewired site-wide (including case-studies, which had its own stale copy diverged from the real footer).
- Removed a fabricated "SME500 Award 2026" line from the case-studies footer, then correctly reinstated it once confirmed real (see `data/source-content-accurova-com.md`'s correction note) — same footer/business.json now agree everywhere.
- Full sitewide link-check script run twice; zero broken internal links across all real pages.
- Fixed several dead `#pricing`/`#about` anchors left over from before the dedicated pages existed.

**Infra**
- Fixed a real production bug: Zeabur's Caddy buildpack auto-detects a root-level `404.html` as an MPA-fallback marker, which was silently 404-ing every request including `/`. Renamed to `errors/not-found.html` (root-absolute links, since a Caddy error page is served under whatever URL was actually requested) and shipped a custom `Caddyfile` that explicitly wires it up correctly.
- Repo decluttered: `build_includes.py` / `generate_case_studies.py` → `scripts/`, planning docs → `markdown/`.

---

## Decisions (2026-09-28)

Four open questions from the previous update, resolved directly by Julian:

1. **Pricing:** the flat $250/$450/$850 rate card is his real current pricing, deliberately below market. He's planning a more robust, category-specific pricing model delivered as a guest-interactable price calculator on the site (this supersedes the simpler "Quote Estimator" idea in HOMEPAGE-CASESTUDY-ARCHITECTURE.md §14). Until that ships: `/pricing/` and the homepage keep the real flat rate card; any category-specific numbers used in case-study copy must be explicitly marked as a placeholder.
2. **Property Photography is a real, current offering** — case-study content is ready (wide-angle DSLR high-res stills, rectilinear 360° photos, room virtual tours via 4D Kankan, walkthrough video). Added to `data/business.json`'s categories. Not yet built — see "Ready to build" below.
3. **Positioning stays corporate-first.** Cosplay and astrophotography remain real, ongoing categories but get their own case-study subpages rather than top-level service pages.
4. **Case studies ARE the portfolio** — one flagship case study per category, not a separate generic gallery layer. Quality over quantity.

`PLAN.md` §2/§4 and `HOMEPAGE-CASESTUDY-ARCHITECTURE.md`'s status note are updated to match.

---

## Ready to build (content exists, just needs handoff)

- **Property Photography case study** — scaffolded: `case-studies/data/property-a.json` + `case-studies/property-a/` (generated), with a new `property` category (filter chip + label). Real image files still needed: `assets/case-studies/property-a/{cover,wide-01..04,360-01,360-02}.jpg` are placeholder graphics (clearly labeled, dark-theme-matching) — overwrite them in place with Julian's real wide-angle stills and 360 photos, same filenames, no JSON changes needed. All copy fields in the JSON are `[PLACEHOLDER]` text — needs the real brief/approach/results/testimonial. The 4D Kankan virtual tour and walkthrough video aren't wired up yet — the case-study template has no embed slot for either; that's a template change, not just a content swap, if wanted.
- **`/services/property-photography/` page** — not built yet, per `PLAN.md` §4.

---

## Partial / in progress

- **URL inventory (PLAN.md §7 / migration)** — live `accurova.com` blocks WebFetch with a 403 (Pixieset bot protection) and this environment has no outbound `curl`. Only `/` and `/testimonials/` confirmed indexed via search; `/about/`, `/pricing/`, `/portfolio/`, `/contact/`, `/accurova-ai/` are believed to exist (per the tasklist's own list) but unconfirmed. **Needs:** Google Search Console export from Julian, or connector access.
- **Service pages (PLAN.md §4)** — only `product-photography.html` exists as a worked example. `corporate-photography`, `event-photography`, `portrait-photography`, `property-photography` are specced but not built.
- **Testimonials contextual placement** — the 10 real testimonials live on `/testimonials/` and 3 appear on the homepage; not yet cross-linked onto relevant service/case-study pages.
- **About page** — story + accreditation done; team/studio photos and equipment-with-photos not added.

---

## Not started — homepage/case-study architecture brief (conflicts resolved, not yet executed)

[HOMEPAGE-CASESTUDY-ARCHITECTURE.md](HOMEPAGE-CASESTUDY-ARCHITECTURE.md) is a full implementation brief Julian dropped in; both flagged conflicts are now resolved (see Decisions above), but none of it is built yet. It covers:

- Case-study taxonomy fields (category/subcategories/client/location/project_type/services/duration/deliverables/featured/related_service/related_case_studies) — richer than the current `case-studies/data/*.json` schema.
- Standalone case-study page structure (hero → project overview → brief → approach → results gallery → deliverables → testimonial → related service → CTA) and the service-page-vs-case-study distinction.
- Price calculator (per Decision 1 above — a fuller build than the brief's original "Quote Estimator" sketch).
- Reusable component list (`ServiceCard`, `CaseStudyCard`, `PricingCard`, `FAQ`, `CTA`, `ClientLogo`, `ProcessStep`, etc.) so new case studies don't require redesigning the site.
- Breadcrumbs on deeper pages (Home → Portfolio → Category → Project, and Home → Services → Category) — visible + structured data. Currently only Pricing/About/Testimonials/Contact have `BreadcrumbList` JSON-LD; portfolio and services pages don't.
- Its own FAQ topic list (cost, booking lead time, travel within Singapore, delivery time, RAW files, corporate packages, custom shot requests, night events, custom commercial quotes) — overlaps with but isn't identical to PLAN.md's FAQ list; reconcile into one list when the FAQ hub gets built.
- "Future scalability" categories (commercial, branding, food, real estate, videography, corporate content packages, workshops, photowalks, studio rental, overseas assignments) — explicitly not to build now, just don't architect against them.

## Not started

- **Resources hub, pillar content, downloads, comparison pages** (PLAN.md §4) — none built. Homepage's "Insights" section is still explicitly placeholder card copy. (FAQ hub is now done — see above.)
- **Price calculator** (PLAN.md §4 Homepage / Decision 1 above) — guest-interactable, category-specific pricing tool meant to bring pricing up to market rate. Not built. Worth doing once dedicated service pages exist to route into.
- **Image SEO** (PLAN.md §5) — nearly every image on the site is still a `picsum.photos` placeholder, not a real delivered photograph. Filenames, alt text, `srcset`, lazy-loading strategy all depend on real images existing first — doing this now would just be optimizing placeholder filenames.
- **Analytics & attribution** (PLAN.md §6) — no GA4 or equivalent configured, no UTM/CTA-click tracking, no lead-source capture. Needs Julian's analytics account access.
- **Migration redirect map** (PLAN.md §7) — can't build `old-urls.csv`/`redirect-map.csv` without the URL inventory above.
- **Domain cutover** (PLAN.md §7) — pointing `accurova.com` at Zeabur, canonical host (`www` vs bare) decision, Cloudflare DNS/CDN config, `gallery.accurova.com` / `pixieset.accurova.com` setup. All Zeabur-dashboard/DNS-registrar actions, not code — needs Julian to action or explicitly delegate dashboard access.
- **Local SEO / GBP-website consistency** — Accurova has a real Google Business Profile (link now in `business.json`), which resolves the earlier "no GBP" gap. Rating/review count couldn't be confirmed (Google Maps is JS-rendered; blocked in this environment). Address is deliberately private (resolved, see Blocked-list history below) — Julian should confirm the GBP listing itself is set to hide the exact address (service-area business setting), since that's a dashboard setting outside what's checkable from here.
- **Accessibility audit, performance/Lighthouse pass, mobile UX pass** — not run yet; reasonable to defer until real images replace placeholders (performance numbers on placeholder images aren't representative).
- **AI Innovation as a standalone page** — currently just a homepage section; fine as-is unless/until the business wants to push Accurova.AI as a product to other photographers (per its real public positioning) rather than just an internal-workflow mention.

---

## Blocked on Julian / external access (not something to keep re-flagging — action once, then wait)

1. **Google Search Console + Analytics access** — needed for the URL inventory, baseline traffic numbers, and post-launch monitoring.
2. **DNS/Zeabur dashboard access or action** — domain architecture (§7), actual cutover.
3. **Real portfolio/case-study images**, including the Property Photography media mentioned in Decisions above — everything downstream (image SEO, real case studies replacing the 6 placeholders, alt text) is blocked on delivered media existing in the repo.
4. ~~Physical/registered address~~ — **resolved 2026-09-28.** Confirmed real (Julian's home, no studio yet) and confirmed private: stays on ACRA only, never published on the site or in structured data. One follow-up still worth Julian checking himself: make sure the Google Business Profile is configured as a service-area business with the exact address hidden from public view — that's a GBP dashboard setting, not something checkable from here (Maps is JS-rendered, blocked in this environment).

---

## Quick priority read (borrowed from the original SEO/GEO tasklist's P0/P1/P2 split)

- **P0 (do before any domain cutover):** URL inventory + redirect map, GSC/analytics wired up, real portfolio images in at least the homepage hero and one full case study, accessibility/mobile pass.
- **P1 (strongly recommended, not launch-blocking):** remaining service pages, FAQ hub, real case studies replacing all 6 placeholders, testimonials cross-linked onto service pages.
- **P2 (post-launch growth):** pillar content, comparison pages, downloads, Singapore-specific content expansion, backlink building.
