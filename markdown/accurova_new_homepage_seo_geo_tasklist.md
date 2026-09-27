# Accurova New Homepage — SEO + GEO Migration Tasklist

## Objective

Build the new Accurova homepage on Zeabur and migrate the public website from Pixieset while:

- Preserving existing SEO equity and indexed URLs.
- Improving technical SEO and site performance.
- Strengthening GEO (Generative Engine Optimization) and AI discoverability.
- Making Accurova's services and Singapore location explicit to search engines and AI systems.
- Improving conversion from visitors to photography enquiries.
- Keeping the existing Pixieset site available as a controlled legacy/backup resource.

---

# 1. Hosting & Domain Architecture

## Target architecture

```text
accurova.com
└── New Zeabur website
    ├── /
    ├── /about/
    ├── /pricing/
    ├── /portfolio/
    ├── /contact/
    ├── /testimonials/
    ├── /corporate-photography/
    ├── /event-photography/
    ├── /portrait-photography/
    ├── /product-photography/
    └── /cosplay-photography/

gallery.accurova.com
└── Pixieset client galleries

pixieset.accurova.com
└── Optional legacy Pixieset website
    └── NOINDEX if retained publicly
```

## Tasks

- [ ] Build and test the new site on `home.accurova.com` as a staging/development URL.
- [ ] Configure Zeabur to serve the finished site from `accurova.com`.
- [ ] Decide on canonical host: `accurova.com` or `www.accurova.com`.
- [ ] Redirect the alternate host to the canonical host.
- [ ] Ensure HTTPS works correctly.
- [ ] Do not permanently make `home.accurova.com` the main public website.
- [ ] Set up `gallery.accurova.com` for Pixieset client galleries if useful.
- [ ] Optionally retain the old Pixieset website at `pixieset.accurova.com`.
- [ ] If the legacy Pixieset site remains accessible, prevent it from competing with the new site in search (`noindex` and/or appropriate canonical strategy).

---

# 2. Existing URL & SEO Inventory

Before switching domains, document the current site.

## Tasks

- [ ] Crawl/index the current `accurova.com` website.
- [ ] Export all currently indexed URLs.
- [ ] Record existing important pages.
- [ ] Record title tags and meta descriptions.
- [ ] Record existing headings.
- [ ] Record existing image URLs.
- [ ] Record internal links.
- [ ] Identify pages receiving organic traffic.
- [ ] Identify pages with backlinks.
- [ ] Identify URLs currently appearing in Google Search.
- [ ] Record current Google Search Console performance for comparison after migration.

## Known important existing URLs

```text
/
 /about/
 /pricing/
 /portfolio/
 /contact/
 /testimonials/
 /accurova-ai/
```

Verify the complete current URL inventory before migration rather than relying only on this list.

---

# 3. URL Migration Plan

Create a migration map:

| Existing URL | New URL | Action |
|---|---|---|
| `/` | `/` | Retain |
| `/about/` | `/about/` | Retain |
| `/pricing/` | `/pricing/` | Retain |
| `/portfolio/` | `/portfolio/` | Retain |
| `/contact/` | `/contact/` | Retain |
| `/testimonials/` | `/testimonials/` | Retain |
| `/accurova-ai/` | `/accurova-ai/` or relevant new page | Retain/301 |
| Other existing URLs | Closest equivalent | 301 |

## Tasks

- [ ] Preserve important existing URLs wherever practical.
- [ ] Create a complete old → new URL mapping.
- [ ] Use permanent 301 redirects for changed URLs.
- [ ] Redirect each old URL to its closest equivalent new page.
- [ ] Avoid redirecting every old URL to the homepage.
- [ ] Remove unnecessary redirect chains.
- [ ] Ensure old URLs do not produce unexpected 404s.
- [ ] Test every important redirect after launch.

---

# 4. Site Information Architecture

The new site should make Accurova's business structure explicit.

## Core pages

- [ ] Homepage
- [ ] About
- [ ] Pricing
- [ ] Portfolio
- [ ] Testimonials
- [ ] Contact

## Service pages

Create dedicated pages where justified by actual services and content depth:

- [ ] Corporate Photography
- [ ] Event Photography
- [ ] Portrait Photography
- [ ] Product Photography
- [ ] Cosplay Photography
- [ ] Commercial Photography
- [ ] Other high-value/niche services

## Potential supporting content

- [ ] Corporate headshots
- [ ] Personal branding photography
- [ ] Corporate events
- [ ] Community/private events
- [ ] E-commerce/product photography
- [ ] Lifestyle product photography
- [ ] Cosplay photography
- [ ] Singapore photography pricing
- [ ] Photography FAQs

Avoid creating thin pages solely for SEO.

---

# 5. Homepage Content

The homepage should immediately establish:

> **Accurova = Singapore photography business**

## Tasks

- [ ] Clear H1 identifying Accurova and photography.
- [ ] Explicitly mention Singapore.
- [ ] Clearly describe primary photography services.
- [ ] Establish Julian/Accurova as the photographer/business entity.
- [ ] Include strong portfolio imagery.
- [ ] Include concise service summaries with links to dedicated pages.
- [ ] Include pricing starting points or a clear path to pricing.
- [ ] Include testimonials/social proof.
- [ ] Include clear enquiry CTA.
- [ ] Include service/location context naturally throughout the page.
- [ ] Include internal links to important service pages.
- [ ] Avoid keyword stuffing.

## Suggested positioning structure

```text
Accurova
Singapore Photography

Short positioning statement

[Portfolio / Enquire CTA]

Services
├── Corporate
├── Events
├── Portraits
├── Products
└── Cosplay

Why Accurova

Selected Work

Testimonials

Pricing / Starting Rates

FAQ

Contact / Enquire
```

---

# 6. SEO Metadata

For every important page:

- [ ] Unique `<title>`.
- [ ] Unique meta description.
- [ ] One clear H1.
- [ ] Logical H2/H3 hierarchy.
- [ ] Descriptive URL slug.
- [ ] Canonical URL.
- [ ] Open Graph title.
- [ ] Open Graph description.
- [ ] Open Graph image.
- [ ] Twitter/X card metadata where relevant.

Avoid duplicating the same title/description across all pages.

---

# 7. Image SEO

Accurova is an image-heavy photography business, so image implementation is a major SEO consideration.

## Tasks

- [ ] Use descriptive image filenames.
- [ ] Replace generic names such as `DSC_49283.jpg` where practical.
- [ ] Write meaningful alt text.
- [ ] Avoid keyword-stuffed alt text.
- [ ] Add captions where they genuinely provide context.
- [ ] Use WebP/AVIF where appropriate.
- [ ] Compress images without compromising portfolio quality.
- [ ] Serve appropriately sized images.
- [ ] Implement responsive images.
- [ ] Lazy-load below-the-fold images.
- [ ] Prioritize loading of the main hero/LCP image.
- [ ] Ensure important images are crawlable.
- [ ] Consider an image sitemap if useful.
- [ ] Preserve important existing image/portfolio content during migration.

Example:

```text
Filename:
singapore-corporate-headshot-photography.jpg

Alt:
Corporate headshot photography by Accurova in Singapore
```

---

# 8. Structured Data

Implement schema/JSON-LD where appropriate.

## Core entity

- [ ] Organization / LocalBusiness schema.
- [ ] Photography business/service classification where appropriate.
- [ ] Business name: Accurova.
- [ ] Website URL.
- [ ] Logo.
- [ ] Contact information.
- [ ] Singapore location/service area.
- [ ] Social profile links.

## Person

- [ ] Person schema for Julian where appropriate.
- [ ] Photographer role.
- [ ] Relationship to Accurova.
- [ ] Relevant professional links.

## Services

- [ ] Service schema for major photography services where appropriate.

Potential services:

```text
Corporate Photography
Event Photography
Portrait Photography
Product Photography
Commercial Photography
Cosplay Photography
```

## Other

- [ ] BreadcrumbList on relevant pages.
- [ ] FAQPage only where the page genuinely contains qualifying FAQs.
- [ ] Validate structured data before launch.

---

# 9. GEO / AI Discoverability

Design the site so AI systems can clearly understand what Accurova is, where it operates, and what it offers.

## Entity clarity

Repeatedly establish the relationship:

```text
Accurova
→ photography business
→ Singapore
→ Julian
→ photography services
```

## Tasks

- [ ] Explicitly state what Accurova does.
- [ ] Explicitly state the geographic market.
- [ ] Explicitly describe each major service.
- [ ] Connect Julian to Accurova.
- [ ] Maintain consistent business naming across the website and external profiles.
- [ ] Use natural, factual descriptions rather than SEO keyword lists.
- [ ] Ensure important information exists as crawlable HTML text, not only inside images.

---

# 10. Answerable Content

Create concise, useful answers to questions potential clients and AI systems may ask.

Potential FAQ/content topics:

- [ ] What does corporate photography in Singapore cost?
- [ ] How much does an event photographer cost in Singapore?
- [ ] How long does a corporate headshot session take?
- [ ] What should I wear for a corporate headshot?
- [ ] Does Accurova provide corporate event photography?
- [ ] Does Accurova provide product photography for e-commerce?
- [ ] Does Accurova photograph cosplay?
- [ ] Does Accurova travel within Singapore?
- [ ] How does the photography booking process work?
- [ ] How quickly are edited photographs delivered?
- [ ] What is included in Accurova photography packages?

Guideline:

> Build useful answers, not generic SEO articles.

Prioritize topics that directly support real client decisions.

---

# 11. Internal Linking

Build a deliberate internal-link network.

Example:

```text
Homepage
│
├── Corporate Photography
│   └── Pricing
│
├── Event Photography
│   └── Portfolio
│
├── Portrait Photography
│   └── Testimonials
│
├── Product Photography
│   └── Portfolio
│
└── Cosplay Photography
    └── Portfolio
```

## Tasks

- [ ] Homepage links to all major services.
- [ ] Service pages link to relevant portfolio examples.
- [ ] Service pages link to pricing.
- [ ] Service pages link to contact/enquiry.
- [ ] Portfolio pages link back to relevant services.
- [ ] Relevant FAQ answers link to service pages.
- [ ] Avoid orphan pages.

---

# 12. Local SEO

Strengthen the Singapore association.

## Tasks

- [ ] Consistent business name.
- [ ] Consistent Singapore location/service-area information.
- [ ] Link to relevant external profiles.
- [ ] Ensure Google Business Profile information matches the website where applicable.
- [ ] Add relevant Singapore context naturally to service pages.
- [ ] Maintain consistent NAP information where a physical business address is publicly used.
- [ ] Add service-area information where relevant.
- [ ] Link testimonials/reviews to the appropriate review platform where appropriate.

Do not fabricate locations or claim service areas that Accurova does not actually cover.

---

# 13. Technical SEO

## Crawlability

- [ ] Generate `sitemap.xml`.
- [ ] Generate/verify `robots.txt`.
- [ ] Ensure important pages are indexable.
- [ ] Prevent staging pages from being indexed.
- [ ] Prevent duplicate/legacy pages from competing with the main site.
- [ ] Ensure canonical tags are correct.
- [ ] Check for broken links.
- [ ] Check for broken images.

## Performance

- [ ] Optimize Core Web Vitals.
- [ ] Optimize Largest Contentful Paint.
- [ ] Minimize JavaScript where practical.
- [ ] Minimize render-blocking resources.
- [ ] Use caching/CDN appropriately.
- [ ] Compress assets.
- [ ] Optimize fonts.
- [ ] Test mobile performance.

---

# 14. Analytics & Search Monitoring

Before launch:

- [ ] Confirm Google Search Console access.
- [ ] Confirm analytics setup.
- [ ] Record current organic traffic baseline.
- [ ] Record important query rankings where useful.
- [ ] Record indexed-page count.
- [ ] Record top landing pages.
- [ ] Record backlinks if available.

After launch:

- [ ] Submit the new sitemap.
- [ ] Monitor indexing.
- [ ] Monitor crawl errors.
- [ ] Monitor 404s.
- [ ] Monitor redirect errors.
- [ ] Monitor organic impressions/clicks.
- [ ] Monitor important service queries.
- [ ] Compare performance against the pre-migration baseline.
- [ ] Investigate unexpected traffic/ranking drops.

---

# 15. Launch Procedure

## Before DNS/domain switch

- [ ] Finish new site.
- [ ] Test all pages.
- [ ] Test mobile and desktop.
- [ ] Test enquiry forms.
- [ ] Test portfolio galleries.
- [ ] Test all internal links.
- [ ] Test metadata.
- [ ] Test structured data.
- [ ] Test sitemap.
- [ ] Test robots.txt.
- [ ] Test canonical URLs.
- [ ] Test page speed.
- [ ] Complete old → new URL migration map.
- [ ] Prepare 301 redirects.
- [ ] Ensure staging site is not accidentally indexed.

## Domain switch

- [ ] Point `accurova.com` to Zeabur.
- [ ] Configure SSL.
- [ ] Configure canonical host.
- [ ] Activate redirects.
- [ ] Verify homepage.
- [ ] Verify major service pages.
- [ ] Verify old URLs redirect correctly.
- [ ] Verify forms and enquiry flow.

## Immediately after launch

- [ ] Submit sitemap to Google Search Console.
- [ ] Request indexing for the homepage and key pages where appropriate.
- [ ] Check Google Search Console coverage/indexing.
- [ ] Check server logs/crawl activity if available.
- [ ] Check for unexpected 404s.
- [ ] Check redirects.
- [ ] Check canonicalization.
- [ ] Check structured-data validation.
- [ ] Check analytics.

---

# 16. Post-Launch SEO/GEO Expansion

Once the migration is stable:

- [ ] Build dedicated service landing pages.
- [ ] Expand useful FAQs.
- [ ] Publish selected case studies.
- [ ] Add portfolio pages with contextual descriptions.
- [ ] Build Singapore-specific service relevance.
- [ ] Strengthen external entity signals.
- [ ] Earn relevant backlinks/citations.
- [ ] Maintain consistent Accurova descriptions across the web.
- [ ] Monitor which queries generate impressions.
- [ ] Expand content based on real client search intent.

---

# 17. Migration Principles

Keep these rules in mind throughout the rebuild:

1. **`accurova.com` remains the primary public domain.**
2. **`home.accurova.com` is staging/development, not the permanent canonical site.**
3. **Preserve valuable existing URLs whenever possible.**
4. **Use 301 redirects when URLs change.**
5. **Redirect old pages to their closest equivalent, not automatically to the homepage.**
6. **Do not create duplicate indexed copies of the site.**
7. **Treat photography images as important SEO assets.**
8. **Make Accurova's entity, services and Singapore market explicit.**
9. **Write content that answers real client questions.**
10. **Use structured data to reinforce—not replace—clear human-readable content.**
11. **Measure the migration before and after launch.**
12. **Optimize for users first, then search engines and AI systems.**

---

# 18. Definition of Done

The new Accurova website is ready for production when:

- [ ] `accurova.com` resolves to the Zeabur site.
- [ ] HTTPS works.
- [ ] Canonical domain is configured.
- [ ] All important existing URLs are preserved or redirected.
- [ ] No significant redirect chains exist.
- [ ] No important pages return 404.
- [ ] Sitemap is live.
- [ ] Robots.txt is correct.
- [ ] Canonical tags are correct.
- [ ] Metadata is complete.
- [ ] Structured data is implemented and validated.
- [ ] Images are optimized and have meaningful alt text.
- [ ] Core Web Vitals are acceptable.
- [ ] Mobile experience is functional.
- [ ] Google Search Console is configured.
- [ ] Analytics is configured.
- [ ] Major services are clearly represented.
- [ ] Singapore/location context is explicit.
- [ ] Accurova/Julian entity relationships are clear.
- [ ] Key client questions are answered.
- [ ] Legacy Pixieset content is prevented from competing with the new site.
- [ ] Enquiry/booking conversion path works end-to-end.

---

## Priority Order

### P0 — Must do before launch

- Domain architecture
- URL inventory
- URL migration map
- 301 redirects
- Canonicals
- Sitemap
- Robots.txt
- Metadata
- Mobile usability
- Page speed
- Enquiry flow
- Core service content
- Google Search Console
- Analytics

### P1 — Strongly recommended

- Service landing pages
- Structured data
- Image SEO
- Internal linking
- Local SEO signals
- FAQ/answerable content
- Person/Organization entity markup
- Testimonials
- Portfolio contextual descriptions

### P2 — Post-launch growth

- Case studies
- Additional service pages
- Singapore-specific content
- Further GEO content
- Backlink/citation building
- Content expansion based on Search Console data
- Ongoing technical SEO improvements
