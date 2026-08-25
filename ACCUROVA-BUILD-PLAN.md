# Accurova Site — Master Build Plan

**Project:** `accurova-site`
**Staging domain:** `https://home.accurova.com/` — live here until the site is polished enough to replace the current Pixieset public marketing site. Pixieset stays in place for client gallery delivery throughout.
**Eventual domain:** `https://www.accurova.com/`
**Purpose:** Replace the current Pixieset public marketing website with a custom, static, search/AI-friendly commercial photography site while retaining Pixieset for client gallery delivery.

---

## 0. Instructions to Claude Code

You are working inside the existing `accurova-site` repository.

**Do not throw away the existing first draft.** Inspect it first, reuse good components/assets/content where appropriate, and evolve it into the architecture below.

The repository already contains:

- a plain HTML/CSS implementation
- a homepage
- `/services/`
- `/portfolio/`
- `/case-studies/`
- a Python case-study generator
- JSON case-study source files
- an existing `site-architecture.md`

The existing architecture document is a useful starting point, but **this document supersedes it where they conflict**.

Before making changes:

1. Inspect the complete repository tree.
2. Read `README.md`, `site-architecture.md`, `README-CASE-STUDIES.md`.
3. Inspect all existing HTML, CSS, JSON, scripts and assets.
4. Run the existing site locally.
5. Identify reusable components and broken/incomplete sections.
6. Do not publish anything to `accurova.com` yet — `home.accurova.com` is the staging domain until cutover.
7. Do not delete existing useful content/assets without recording what was removed and why.
8. Keep all factual claims grounded in known Accurova information. Never invent clients, awards, testimonials, metrics, certifications, locations, pricing, turnaround times or project results.

The current GitHub repository is an **untested first draft**, not a finished specification. Treat it as source material.

---

# 1. Strategic Objective

Accurova is not merely trying to rank for "photographer Singapore."

The website must help establish:

> **Accurova = a credible Singapore photography business for corporate, event, product and portrait photography, supported by real work, real client evidence, transparent commercial information and a coherent online entity.**

The site should support discovery through:

- Google Search
- Google Maps / Business Profile
- ChatGPT Search
- Gemini
- Perplexity
- other answer/search engines

And convert that visibility into measurable:

**visit → enquiry → qualified lead → booking → revenue**

The site is therefore simultaneously:

1. Portfolio
2. Sales site
3. SEO asset
4. AI-readable knowledge source
5. Client-proof repository
6. Lead-generation system
7. Analytics/attribution surface

---

# 2. Core Positioning

Primary positioning:

**Singapore Corporate, Event & Product Photography**

Secondary capabilities:

- Corporate headshots
- Personal branding
- Portrait photography
- Commercial/lifestyle photography
- E-commerce/product imagery
- Campaign photography

Specialist/other work should remain discoverable without confusing the primary business identity.

Avoid positioning Accurova as a generic "photographer who shoots everything."

The hierarchy should communicate:

**Primary:** Corporate / Event / Product
**Secondary:** Corporate Headshots / Portraits / Commercial Content
**Specialist:** Other photographic work where strategically useful

Accurova.AI should be clearly framed as a technology/workflow project by Accurova rather than a competing primary business identity.

---

# 3. Architecture

Use clean directory-based URLs with trailing slashes:

```text
/
├── services/
│   ├── corporate-photography/
│   ├── event-photography/
│   ├── product-photography/
│   ├── corporate-headshots/
│   └── portrait-photography/
│
├── portfolio/
│   ├── corporate/
│   ├── events/
│   ├── products/
│   └── portraits/
│
├── case-studies/
│   └── [project-slug]/
│
├── pricing/
│
├── reviews/
│
├── about/
│
├── resources/
│   ├── guides/
│   ├── articles/
│   └── downloads/
│
├── faq/
│
├── ai-innovation/
│
└── contact/
```

Do **not** mass-produce thin location pages or keyword-stuffed pages.

Do not create pages merely because a keyword exists. Every indexable page must have a useful purpose for a real prospective client.

---

# 4. Homepage

Rebuild the homepage around commercial intent.

Recommended structure:

1. Hero
   - Clear Singapore photography positioning
   - Corporate / Event / Product emphasis
   - Primary CTA: Get a Quote
   - Secondary CTA: View Work

2. Trust / credibility strip
   - Only use factual, verifiable claims
   - Google review count/rating only if dynamically/currently verified or manually maintained
   - Client/partner logos only with permission

3. Services
   - Corporate Photography
   - Event Photography
   - Product Photography
   - Corporate Headshots
   - Portrait Photography

4. Selected work
   - Strong visual work
   - Link into portfolio categories and case studies

5. Why Accurova
   - Professional direction
   - Guided experience
   - Commercial-ready delivery
   - Transparent pricing
   - Human photographer / human creative judgement

6. Case studies
   - Real projects only
   - Highlight challenge → approach → deliverables → outcome

7. Testimonials
   - Relevant reviews with service/category context where known

8. Pricing summary
   - "Starting from..." values must match the canonical pricing source
   - Link to full pricing

9. FAQ summary
   - 4–6 high-intent questions

10. Final CTA
    - Request a quote
    - WhatsApp
    - Contact

---

# 5. Services

Create real commercial landing pages rather than one generic services page.

## Required initial services

### `/services/corporate-photography/`

Target intent examples:

- corporate photographer Singapore
- corporate photography Singapore
- company event photography
- business photography Singapore

Content:

- What corporate photography covers
- Suitable events/use cases
- What clients receive
- Approach
- Sample work
- Relevant case studies
- Relevant testimonials
- Pricing starting point
- FAQs
- CTA

### `/services/event-photography/`

Cover:

- corporate events
- conferences
- seminars
- networking events
- launches
- company functions

### `/services/product-photography/`

Cover:

- product catalogue
- e-commerce
- marketing imagery
- campaign imagery
- lifestyle product photography

### `/services/corporate-headshots/`

Cover:

- executives
- teams
- LinkedIn
- corporate profiles
- company websites
- personal branding

### `/services/portrait-photography/`

Keep this as a secondary service.

---

# 6. Portfolio Architecture

Portfolio is visual evidence, not the main SEO text dump.

## Index

`/portfolio/`

Filter/category links:

- Corporate
- Events
- Products
- Portraits
- Commercial
- Lifestyle
- Other relevant categories supported by actual work

## Category pages

Each category page needs:

- short useful introduction
- gallery
- links to relevant case studies
- links to service page
- clear CTA

Do not create category pages with no meaningful content.

## Individual project pages

Each project should support:

- project title
- client, only where permitted
- industry, where known
- project type
- location, where appropriate
- deliverables
- gallery
- concise project description
- related service
- related case study
- enquiry CTA

---

# 7. Case Studies

This is one of the highest-priority features.

Keep and improve the existing JSON → generated HTML architecture.

Source of truth:

```text
case-studies/data/*.json
```

Generated output:

```text
case-studies/[slug]/index.html
```

Never hand-edit generated case-study pages.

## Case-study structure

1. Hero
2. Project metadata
3. Client / project context
4. Challenge
5. Approach
6. Behind the scenes, if available
7. Final deliverables
8. Results / outcomes, only if supported
9. Client testimonial, only with permission
10. Related service
11. Related portfolio
12. Related resources
13. CTA

Do not use fake placeholder "case studies" on the production site.

Existing placeholder JSON files such as `event-a`, `event-b`, `portrait-a`, etc. must be clearly marked as draft/demo content or replaced with genuine projects before production launch.

---

# 8. Reviews / Testimonials

Create:

`/reviews/`

This becomes the central testimonial/review evidence page.

But do not rely on one giant wall of testimonials.

Where the source permits, associate testimonials with:

- service
- project
- client type
- event/product/portrait category

Relevant testimonials should also appear contextually on service and case-study pages.

Never fabricate or rewrite a client's words into a new testimonial.

---

# 9. Pricing

Create a single canonical pricing source.

Current site has had inconsistent pricing representations. Before launch:

- verify the actual current Accurova pricing
- choose one canonical source
- use the same values everywhere

The site should not expose contradictory prices across homepage/service/pricing pages.

Recommended:

`/pricing/`

Sections:

- Product Photography
- Event Photography
- Corporate / Headshots
- Portraits
- Add-ons / considerations where applicable
- FAQ
- Quote CTA

Use "starting from" where scope varies.

Avoid claiming that a package includes something unless the actual business offering does.

---

# 10. About

`/about/`

Structure:

- Accurova story
- Julian / photographer
- philosophy
- working process
- equipment where useful
- experience
- awards/recognition only when verified
- AI workflow philosophy
- Singapore service context
- CTA

Do not make the equipment list a major selling point.

The buyer should understand:

**who you are → what you do → why clients trust you → how you work.**

---

# 11. AI Innovation

Keep an AI/workflow page, but reposition it.

`/ai-innovation/`

Explain:

- AI-assisted culling
- workflow automation
- asset organisation
- image search
- editing/retouching assistance
- QA
- turnaround optimisation

Clearly state what remains human:

- photography
- creative direction
- client communication
- visual judgement
- final selection/quality control

Do not imply AI-generated photography unless that is actually a service.

The page should reinforce:

> AI improves the workflow; it does not replace the photographer.

Link to it from relevant service pages, but do not make it dominate the core commercial positioning.

---

# 12. Resources

Create a scalable resource system, but do not launch hundreds of articles.

Initial categories:

- Guides
- Articles
- Behind the Scenes
- Photography planning
- Corporate photography advice
- Product photography advice
- Event photography advice
- FAQs

Prioritise genuinely useful buyer questions.

Examples:

- How much does corporate photography cost in Singapore?
- What should a company prepare before a corporate photoshoot?
- How many hours of event photography do I need?
- What should a company wear for corporate headshots?
- What is included in product photography?
- How should businesses prepare products for a shoot?

Do not write articles purely to insert keywords.

---

# 13. FAQ Hub

Create:

`/faq/`

Use semantic HTML:

```html
<details>
  <summary>Question</summary>
  <p>Answer</p>
</details>
```

Group questions:

- Pricing
- Booking
- Preparation
- Events
- Products
- Corporate headshots
- Delivery
- Licensing / usage
- Editing
- AI workflow

Answers should be concise and factually accurate.

---

# 14. Downloads

Optional but useful later:

`/resources/downloads/`

Possible assets:

- Corporate shoot preparation guide
- Product photography preparation checklist
- Corporate headshot preparation guide
- Photography brief template
- Event photography planning checklist
- Pricing guide

Do not gate everything behind email initially.

First establish usefulness and search visibility.

---

# 15. Search / SEO Requirements

Every indexable page must have:

- unique `<title>`
- unique meta description
- canonical URL
- correct H1
- logical H2/H3 hierarchy
- descriptive image alt text
- Open Graph metadata
- Twitter/X card metadata where useful
- internal links
- breadcrumb navigation where appropriate

Generate:

- `sitemap.xml`
- `robots.txt`

Consider an `llms.txt` and `llms-full.txt` only as supplementary resources; do not treat them as a substitute for normal crawlable HTML/content.

Use clean semantic HTML.

Do not hide critical SEO content behind JavaScript.

---

# 16. Structured Data

Implement valid Schema.org structured data where appropriate.

Potential types:

- `LocalBusiness` / appropriate photography business subtype where supported
- `Person` for Julian
- `WebSite`
- `WebPage`
- `BreadcrumbList`
- `Service`
- `Article`
- `ImageObject`

Only include properties that are true and supportable.

Do not create fake:

- aggregate ratings
- reviews
- awards
- prices
- locations
- organisations
- service areas

Structured data must agree with visible page content.

---

# 17. Entity Consistency

Create one canonical business information source in the codebase, for example:

```text
data/business.json
```

Include verified:

- business name
- website
- description
- Singapore location/service area
- contact channels
- social profiles
- founder/photographer information
- service categories

Templates should pull from this source where appropriate.

This reduces contradictions across pages.

---

# 18. Internal Linking System

Create reusable relationships between:

```text
Service
  ↓
Portfolio Category
  ↓
Project
  ↓
Case Study
  ↓
Review
  ↓
Resource
```

Every major service should link to:

- relevant portfolio
- relevant case studies
- relevant FAQs
- relevant resources
- pricing
- contact

Every case study should link back to its service.

Every portfolio project should link to either a service or case study where appropriate.

Avoid orphan pages.

---

# 19. Conversion / Attribution

This is a core requirement, not an afterthought.

Track:

- CTA clicks
- WhatsApp clicks
- email clicks
- enquiry form submissions
- pricing-page CTA clicks
- portfolio interactions where useful
- outbound Pixieset links
- booking actions

Capture lead source where possible:

- Google Search
- Google Maps
- ChatGPT
- Gemini
- Perplexity
- Instagram
- LinkedIn
- referral
- direct
- other

Do not claim that a lead came from an AI engine unless the evidence supports it.

Use UTM parameters for controlled campaigns.

Prepare the site for GA4 and/or another privacy-appropriate analytics system.

Do not put analytics secrets directly in public source code.

---

# 20. WhatsApp

WhatsApp is a major conversion channel.

Use context-aware CTA labels where useful:

- "Ask about corporate photography"
- "Request event photography quote"
- "Ask about product photography"

Do not make every CTA identical.

Where technically practical, include a source/service identifier in the WhatsApp message so enquiries can be attributed.

Do not expose private credentials.

---

# 21. Images / Photography Performance

This is a photography site, so image performance is critical.

Implement:

- responsive images
- `srcset`
- appropriate image dimensions
- modern formats where practical
- lazy loading below the fold
- eager loading for hero/LCP image
- explicit width/height to reduce layout shift
- descriptive filenames
- meaningful alt text
- appropriate compression

Do not destroy image quality merely to chase Lighthouse scores.

Visual quality remains a primary conversion factor.

---

# 22. Accessibility

Target WCAG 2.2 AA where practical.

Requirements:

- keyboard navigation
- visible focus states
- semantic HTML
- sufficient contrast
- accessible mobile menu
- meaningful alt text
- reduced-motion consideration
- proper form labels
- no inaccessible custom widgets
- no interaction dependent solely on hover

Run an automated accessibility audit before launch.

---

# 23. Performance

Target:

- fast first load
- excellent mobile performance
- minimal JS
- no unnecessary dependencies
- optimised fonts
- optimised images
- minimal third-party scripts

Do not introduce a JavaScript framework unless there is a demonstrated benefit.

The current static HTML/CSS approach is acceptable and preferred unless the repository proves that a build system materially improves maintainability.

---

# 24. Design Direction

The existing draft uses:

- void/dark background
- teal
- gold
- Space Grotesk
- JetBrains Mono
- film/contact-sheet motifs

Preserve the strongest parts of this identity unless the implementation review shows a compelling reason to change them.

However:

**Do not let the site look like a developer portfolio or SaaS landing page.**

Accurova is a photography business.

Photography should dominate.

Design priorities:

1. photographs
2. clarity
3. credibility
4. typography
5. conversion
6. technical sophistication

not the reverse.

---

# 25. Technical Architecture

Preferred baseline:

- static HTML/CSS
- minimal vanilla JS
- existing Python generation where useful
- no unnecessary framework
- reusable templates/components through the existing project approach
- data-driven case studies
- central business/service data
- automated validation scripts

If a build system is introduced, document why.

---

# 26. Suggested Data Model

Create structured source data where useful.

Example:

```text
data/
  business.json
  services.json
  portfolio.json
  reviews.json
  redirects.json
  faq.json
```

Case studies remain in:

```text
case-studies/data/
```

This allows future Claude agents to update content safely without manually editing dozens of HTML files.

---

# 27. Migration From Pixieset

Do not switch the live domain until the new site is validated.

First create a migration inventory:

```text
migration/
  old-urls.csv
  redirect-map.csv
  content-inventory.md
```

For every known current URL:

- current URL
- current purpose
- indexed?
- backlinks known?
- keep / redirect / merge / retire
- new URL
- redirect type
- notes

Any old valuable URL that changes should receive a 301 redirect.

Do not blindly redirect everything to the homepage.

Preserve relevant destination intent.

---

# 28. Cloudflare / Staging

Staging domain during the build: `home.accurova.com`. The live public marketing site stays on Pixieset until the new site is validated and ready to take over.

The intended eventual architecture is:

```text
accurova.com
      ↓
Cloudflare DNS/CDN/security
      ↓
Custom static site
```

Pixieset should remain available for client delivery/galleries throughout — it is never removed.

Before DNS cutover from Pixieset to this site:

- test staging deployment (`home.accurova.com`)
- verify HTTPS
- verify redirects
- verify sitemap
- verify robots.txt
- verify analytics
- verify forms
- verify WhatsApp
- verify all images
- verify mobile
- verify 404 page
- verify canonical URLs

---

# 29. Testing / QA

Create a validation script or workflow that checks:

### Every page

- HTTP status
- title
- meta description
- canonical
- H1
- broken internal links
- image alt text
- Open Graph
- structured data presence where required

### Site-wide

- sitemap validity
- robots.txt
- no accidental `noindex`
- no localhost URLs
- no staging URLs
- no placeholder copy
- no fake testimonials
- no fake clients
- no broken images
- no empty pages
- no orphan pages

### Performance

Run Lighthouse/PageSpeed on:

- homepage
- corporate service
- event service
- product service
- one portfolio page
- one case study
- pricing
- contact

### Accessibility

Run an automated WCAG audit.

---

# 30. Content Integrity Rules

Claude must never invent:

- client names
- testimonials
- event results
- business metrics
- awards
- certifications
- review counts
- ratings
- pricing
- turnaround times
- number of photographs delivered
- years of experience
- partnerships
- media appearances

If information is missing:

**use a clearly marked content placeholder and ask the owner to provide it.**

Never turn a placeholder into a production claim.

---

# 31. Build Phases

## Phase 0 — Repository audit

- inspect existing implementation
- run locally
- document current state
- identify reusable code
- identify broken sections
- identify placeholder content
- create content inventory

**Deliverable:** audit report.

## Phase 1 — Foundation

- global CSS/components
- navigation
- footer
- business data
- metadata system
- analytics hooks
- CTA system
- accessibility baseline
- error/404 page

## Phase 2 — Commercial core

Build:

- homepage
- services index
- corporate photography
- event photography
- product photography
- corporate headshots
- portrait photography
- pricing
- contact

This is the minimum viable commercial site.

## Phase 3 — Proof

Build:

- portfolio index
- portfolio category pages
- individual project pages
- case-study generator improvements
- real case studies
- reviews

## Phase 4 — Authority

Build:

- FAQ
- resources
- guides
- about
- AI innovation

## Phase 5 — Technical SEO

- sitemap
- robots
- canonical URLs
- structured data
- Open Graph
- internal-link audit
- image SEO
- performance
- accessibility

## Phase 6 — Migration

- complete old URL inventory
- redirect map
- staging test on `home.accurova.com`
- crawl test
- analytics test
- mobile test
- DNS/Cloudflare cutover plan (Pixieset → this site)

## Phase 7 — Post-launch

Do not immediately mass-publish content.

First monitor:

- indexing
- organic traffic
- queries
- page performance
- enquiries
- referral sources
- AI referral traffic
- broken links
- search visibility

---

# 32. Future AI Agent Layer

The site should be designed so future Claude agents can maintain it.

Potential agents:

### SEO Auditor

Checks technical SEO and reports issues.

### AI Visibility Monitor

Runs a controlled query set across search/answer engines and records whether Accurova appears.

### Competitor Monitor

Tracks competitor visibility, content and authority changes.

### Content Opportunity Agent

Finds useful unanswered buyer questions.

### Case Study Agent

Turns structured project information into draft case studies without inventing facts.

### Lead Attribution Agent

Analyses enquiry sources and reports:

```text
source → enquiries → qualified leads → bookings → revenue
```

### Website QA Agent

Crawls the production site and reports:

- broken links
- missing metadata
- accessibility issues
- image issues
- indexing problems
- content inconsistencies

The website architecture should make these agents possible without requiring them immediately.

---

# 33. Success Metrics

The website project is successful only if it improves both visibility and business outcomes.

Track:

### Search

- branded search visibility
- non-branded commercial queries
- organic impressions
- organic clicks
- Google Maps visibility where measurable

### AI

- AI recommendation frequency
- AI citation frequency
- AI referral traffic
- queries where Accurova is mentioned
- competitor mentions

### Website

- service-page visits
- case-study visits
- pricing visits
- CTA interactions
- WhatsApp clicks
- enquiry submissions

### Business

- enquiries
- qualified enquiries
- bookings
- revenue
- revenue by acquisition source

Primary north-star:

> **Qualified photography enquiries generated per month from search/AI discovery.**

---

# 34. Definition of Done

Do not consider the rebuild complete merely because every page exists.

The production candidate is ready when:

- [ ] all core commercial pages exist
- [ ] real portfolio content is integrated
- [ ] real case studies replace placeholders
- [ ] pricing is internally consistent
- [ ] testimonials are authentic
- [ ] navigation is coherent
- [ ] internal linking is complete
- [ ] metadata is unique
- [ ] canonical URLs are correct
- [ ] structured data validates
- [ ] sitemap works
- [ ] robots.txt works
- [ ] no accidental noindex
- [ ] all internal links work
- [ ] images are optimised
- [ ] accessibility audit passes agreed threshold
- [ ] mobile UX is good
- [ ] analytics works
- [ ] enquiry attribution works
- [ ] WhatsApp CTAs work
- [ ] 404 works
- [ ] old URL redirects are mapped
- [ ] staging crawl succeeds
- [ ] no fabricated content remains
- [ ] Cloudflare deployment is tested
- [ ] Pixieset delivery links remain functional

---

# 35. Important Working Principle

**Build the authority architecture before the content volume.**

Do not spend the project creating dozens of SEO articles.

The first priority is:

```text
Business identity
      ↓
Services
      ↓
Portfolio
      ↓
Case studies
      ↓
Reviews
      ↓
FAQs/resources
      ↓
Internal linking
      ↓
Search/AI visibility
      ↓
Lead attribution
```

The website should make it easy for both a human buyer and a search/answer engine to understand the same thing:

> **Who Accurova is, what Accurova does, where Accurova operates, why Accurova is credible, what Accurova's work looks like, what it costs, and how to engage Accurova.**
