# Accurova Homepage & Case Study Architecture

## Claude Code Implementation Brief

**Project:** Accurova new website
**Domain:** `accurova.com`
**Current platform:** Pixieset
**New platform:** Zeabur
**Primary objective:** Build a conversion-focused photography business website while preserving Accurova's real-world case-study portfolio architecture.

---

# 1. Core Direction

Use the information architecture and conversion logic of `doctorclean.com.sg` as inspiration.

Do **not** copy its branding, visual design, wording, assets, or exact UI.

Instead, adapt the underlying structure:

> Clear proposition → services → proof → explanation → pricing → process → testimonials → FAQ → CTA

The Accurova website should feel like a **professional photography company**, not merely a photographer portfolio.

The site must simultaneously communicate:

1. What Accurova does
2. Who it serves
3. What types of photography are available
4. What the work actually looks like
5. What a client can expect to pay
6. Why a client should trust Accurova
7. How to enquire
8. Evidence from real completed projects

---

# 2. Critical Portfolio Architecture

## Do NOT replace the portfolio with generic category galleries.

Accurova's portfolio should continue using **real shoots as standalone case studies**.

Each case study should represent a category through an actual project.

For example:

```text
/portfolio/
    /corporate-event-example/
    /product-shoot-example/
    /corporate-headshots-example/
    /cosplay-shoot-example/
    /property-shoot-example/
```

Each case study should be a complete standalone page rather than merely a gallery item.

---

# 3. Case Studies as Category Representatives

The website should establish a relationship:

```text
SERVICE CATEGORY
        ↓
REAL CASE STUDY
        ↓
PHOTOGRAPHS
        ↓
PROJECT CONTEXT
        ↓
RESULT / DELIVERABLE
        ↓
RELATED SERVICE
        ↓
ENQUIRY CTA
```

For example:

```text
Product Photography
        ↓
Real Client Product Shoot
        ↓
Case Study
        ↓
Product images
        ↓
What the client needed
        ↓
How Accurova approached it
        ↓
Final deliverables
        ↓
Product Photography service
        ↓
Get a Quote
```

This is preferable to having a generic page saying:

> "Here are some product photos."

The case study should demonstrate actual commercial capability.

---

# 4. Homepage Information Architecture

Build the homepage in this approximate order.

## 4.1 Navigation

Primary navigation:

* Home
* Services
* Portfolio
* About
* Pricing / Packages
* Contact

Primary CTA:

**Get a Quote**

Mobile navigation should preserve the CTA prominently.

---

# 5. Hero Section

Headline should immediately explain the business.

Example direction:

> # Photography that makes your business look the part.

Supporting text:

> Professional photography for businesses, events, products, portraits and people in Singapore.

Primary CTA:

**Get a Quote**

Secondary CTA:

**View Portfolio**

Hero imagery should immediately demonstrate professional-quality Accurova work.

Avoid using a generic stock-style hero image.

---

# 6. Trust / Proof Strip

Immediately after the hero.

Possible metrics:

* Shoots completed
* Clients served
* Years active
* Singapore-based
* Google rating

Only display numbers that are supported by actual data.

Example:

```text
XX+ Shoots
XX+ Clients
Singapore
★★★★★ Google Reviews
```

This section should be visually compact.

---

# 7. Service Discovery

Heading:

> ## What do you need photographed?

Create visually strong service cards.

Initial categories:

### Event Photography

Corporate events, conferences, networking events, dinners, launches and celebrations.

### Corporate Photography

Headshots, team photography, executive portraits and company branding.

### Product Photography

E-commerce, catalogue, advertising, social media and commercial product imagery.

### Portrait Photography

Personal branding, creative portraits, graduation, cosplay and individual sessions.

### Property Photography

Residential property, commercial property, interiors and architecture.

Additional categories can be added later.

Each service card should contain:

* Representative image
* Short description
* Link to relevant service page
* Link or visual reference to one or more relevant case studies

---

# 8. Case Study Showcase

This is one of the most important sections.

Heading:

> ## Real Projects. Real Results.

Subheading:

> Explore how Accurova approaches different photography requirements through actual client projects.

Display selected case studies.

Each card should show:

* Project image
* Client/project name
* Photography category
* Short description
* View Case Study CTA

Example:

```text
[IMAGE]

Corporate Event Photography
BNI Crescendo Gala Dinner

Event coverage for a large networking and corporate event.

View Case Study →
```

Do not present these as generic "portfolio categories".

They are **specific projects**.

---

# 9. Case Study Taxonomy

Every case study should have structured metadata.

Recommended fields:

```yaml
title:
slug:
category:
subcategories:
client:
location:
date:
project_type:
services:
duration:
deliverables:
featured:
hero_image:
gallery:
testimonial:
related_service:
related_case_studies:
```

Example:

```yaml
title: BNI Crescendo Gala Dinner
slug: bni-crescendo-gala-dinner
category: event-photography
subcategories:
  - corporate-event
  - networking
  - gala
client: BNI Crescendo
location: Singapore
project_type: corporate-event
services:
  - event-photography
duration: 4-hours
deliverables:
  - edited-event-photographs
related_service: event-photography
featured: true
```

The actual implementation should use the project's existing data architecture where possible rather than creating unnecessary duplication.

---

# 10. Standalone Case Study Page Structure

Every case study should follow a consistent structure.

## Hero

* Project title
* Category
* Location
* Strong hero image

Example:

> # BNI Crescendo Gala Dinner
>
> Event Photography · Singapore

---

## Project Overview

Explain:

* Who the client/project was
* What the event/shoot was
* What Accurova was engaged to do
* Key requirements

---

## The Brief

Describe the client's photography requirements.

Example:

> Accurova was engaged to document the event while capturing both formal moments and candid networking interactions.

---

## The Approach

Explain the photography approach.

Possible elements:

* Equipment
* Lighting
* Lens selection
* Coverage strategy
* Positioning
* Candid vs posed coverage
* Low-light strategy
* Turnaround

Do not over-technify this section unless the technical details help demonstrate expertise.

---

## The Results

Large photography gallery.

Images should be the primary focus.

Use captions where useful.

---

## Deliverables

Example:

```text
✓ Full event coverage
✓ Professionally edited photographs
✓ Candid networking photographs
✓ Formal group photographs
✓ Highlight images
```

---

## Client Testimonial

If available:

> "..."

Display client name and organisation.

Do not fabricate testimonials.

---

## Related Service

Example:

> ## Looking for event photography?
>
> Accurova provides professional event photography for corporate events, conferences, networking sessions, dinners and launches.

**View Event Photography →**

---

## CTA

> ## Planning a similar shoot?

**Get a Quote**

---

# 11. Service Pages vs Case Studies

Keep these as two separate concepts.

### Service page

Answers:

> "Does Accurova provide this service?"

Example:

`/services/event-photography/`

Contains:

* What the service is
* Who it is for
* Typical use cases
* Packages / starting prices
* Process
* FAQs
* Relevant case studies
* CTA

### Case study

Answers:

> "Can Accurova actually do this?"

Example:

`/portfolio/bni-crescendo-gala-dinner/`

Contains:

* Actual project
* Actual images
* Actual context
* Actual deliverables
* Actual testimonial where available
* Related service
* CTA

This distinction is important.

---

# 12. Case Study → Service Linking

Every case study must link back to its relevant service.

Every service page must link to several relevant real case studies.

Example:

```text
/services/event-photography/
        ↓
/portfolio/bni-crescendo-gala-dinner/
/portfolio/corporate-conference-2026/
/portfolio/networking-event-example/
```

And:

```text
/portfolio/bni-crescendo-gala-dinner/
        ↓
/services/event-photography/
```

This creates a strong internal-linking structure.

---

# 13. Homepage Pricing Section

Introduce pricing without making the homepage feel like a price list.

Heading:

> ## Photography Packages

Show starting package information.

Current Accurova package framework:

### Event Photography

* Standard — S$600 — 2–3 hours
* Enhanced — S$1,000 — 4–6 hours
* Deluxe — S$1,800 — 7–12 hours

### Product Photography

* Standard — S$300 — up to 10 products
* Enhanced — S$600 — 11–25 products
* Deluxe — S$1,100 — 26–50 products

### Portrait Photography

* Standard — S$250 — 2 hours
* Enhanced — S$400 — 3–4 hours
* Deluxe — S$700 — 5–8 hours

Treat these as current working prices and make the pricing architecture easy to update.

Property/corporate/custom commercial work can use:

> **Custom Quote**

rather than forcing every job into a fixed package.

---

# 14. Quote Estimator

Build toward an interactive quote estimator.

Possible flow:

```text
What do you need?
        ↓
Event / Product / Portrait / Corporate / Property
        ↓
Requirements
        ↓
Estimated package
        ↓
Request detailed quote
```

The estimator should clearly state:

> This is an estimate. Final pricing may vary depending on project requirements.

Do not present estimates as guaranteed quotations.

---

# 15. Why Accurova

Heading:

> ## Why Accurova?

Use concrete differentiators rather than generic marketing claims.

Potential points:

### Professional Equipment

High-resolution professional camera systems and professional lighting equipment.

### Commercial-Ready Images

Photography designed for websites, social media, marketing materials and business communications.

### Flexible Coverage

Packages and custom coverage for different project sizes.

### Complete Workflow

Planning → Photography → Editing → Delivery.

### Singapore-Based

Local photographer with familiarity with Singapore venues, events and businesses.

### One Visual Partner

Ability to support businesses across events, portraits, products and other photography requirements.

Only include claims that can be substantiated.

---

# 16. Process Section

Heading:

> ## From Brief to Final Images

Four steps:

### 01 — Tell Us What You Need

Share your project, requirements, date and location.

### 02 — Plan

We discuss the scope, coverage and deliverables.

### 03 — Shoot

Accurova photographs the project.

### 04 — Edit & Deliver

Images are professionally selected, edited and delivered.

Visualise this as a simple four-step process.

---

# 17. Testimonials

Use genuine testimonials.

Prioritise:

1. Corporate clients
2. Commercial clients
3. Event clients
4. Portrait clients
5. Repeat clients

Where possible include:

* Client name
* Company
* Project type
* Google review link/reference

Do not invent reviews.

---

# 18. Client / Organisation Proof

Where permissions allow, show:

> **Trusted by / Worked with**

Possible logos or organisation names.

This section should be factual and should not imply endorsement unless endorsement actually exists.

---

# 19. FAQ

Create FAQ content around real customer questions.

Initial topics:

* How much does photography cost?
* How far in advance should I book?
* Do you travel around Singapore?
* How long does delivery take?
* Do I receive high-resolution files?
* Can you provide RAW files?
* Do you offer corporate packages?
* Can I request specific shots?
* Can you photograph events at night?
* Do you provide product photography?
* Do you offer custom commercial quotes?

FAQ content should support both users and search engines without keyword stuffing.

---

# 20. SEO / GEO Architecture

The website should establish a clear entity hierarchy.

Primary entity:

**Accurova — Photography Business in Singapore**

Service entities:

* Event Photography Singapore
* Corporate Photography Singapore
* Product Photography Singapore
* Portrait Photography Singapore
* Property Photography Singapore

Case studies provide evidence underneath those entities.

Conceptually:

```text
Accurova
│
├── Services
│   ├── Event Photography
│   ├── Corporate Photography
│   ├── Product Photography
│   ├── Portrait Photography
│   └── Property Photography
│
└── Portfolio / Case Studies
    ├── Event Case Study
    ├── Corporate Case Study
    ├── Product Case Study
    ├── Portrait Case Study
    └── Property Case Study
```

Avoid creating dozens of thin pages purely for keywords.

A real project should preferably support the category.

---

# 21. Metadata

Every service and case-study page should have unique:

* `<title>`
* meta description
* canonical URL
* Open Graph title
* Open Graph description
* Open Graph image

Case studies should use their actual project hero image for social sharing.

---

# 22. Structured Data

Implement appropriate Schema.org structured data where valid.

Potential types:

* LocalBusiness
* ProfessionalService
* Organization
* BreadcrumbList
* Service
* FAQPage where appropriate
* ImageObject
* Review / AggregateRating only where requirements are genuinely satisfied

Do not manufacture structured-data ratings or reviews.

---

# 23. Breadcrumbs

Implement breadcrumbs on deeper pages.

Example:

```text
Home
→ Portfolio
→ Event Photography
→ BNI Crescendo Gala Dinner
```

And:

```text
Home
→ Services
→ Event Photography
```

Use both visible breadcrumbs and structured breadcrumb data where appropriate.

---

# 24. Image Strategy

Photography is the primary visual asset.

Priorities:

* Strong hero images
* High-quality thumbnails
* Responsive image sizes
* Modern image formats where practical
* Lazy loading below the fold
* Explicit image dimensions
* Descriptive alt text
* Avoid excessive image payloads

Do not sacrifice image quality to the point that Accurova's portfolio looks weak.

The site should balance:

> Visual quality ↔ Core Web Vitals ↔ SEO

---

# 25. CTA Strategy

Primary CTA throughout the website:

**Get a Quote**

Secondary CTAs:

* View Portfolio
* View Case Study
* Explore Services
* See Packages
* Contact Accurova

Every major page should eventually provide a clear path toward enquiry.

---

# 26. Homepage Conversion Funnel

The intended user journey:

```text
Google / AI / Referral / Social
          ↓
      Homepage
          ↓
 Understand Accurova
          ↓
 Select service
          ↓
 See real case study
          ↓
 Build trust
          ↓
 Understand pricing
          ↓
 Request quote
```

Alternative journey:

```text
Search
  ↓
Service Page
  ↓
Case Study
  ↓
Quote
```

Another:

```text
Search
  ↓
Case Study
  ↓
Related Service
  ↓
Pricing
  ↓
Quote
```

The architecture should support all three.

---

# 27. Important Design Principle

Do not make every page look like a landing page.

Accurova needs three distinct content experiences:

### Marketing pages

Designed to explain and convert.

### Service pages

Designed to answer a specific commercial need.

### Case studies

Designed to prove capability through real work.

They should share the same design system but have different information priorities.

---

# 28. Suggested URL Architecture

```text
/
├── /services/
│   ├── /event-photography/
│   ├── /corporate-photography/
│   ├── /product-photography/
│   ├── /portrait-photography/
│   └── /property-photography/
│
├── /portfolio/
│   ├── /case-study-1/
│   ├── /case-study-2/
│   ├── /case-study-3/
│   └── ...
│
├── /about/
├── /pricing/
├── /contact/
└── /guides/
```

Use clean, permanent URLs.

Avoid unnecessary dates or technical IDs in URLs.

---

# 29. Navigation Philosophy

The visitor should never need to understand Accurova's internal organisation.

They should be able to answer these questions immediately:

1. What does Accurova do?
2. Can Accurova handle my type of photography?
3. What does the work look like?
4. How much does it roughly cost?
5. Can I trust the business?
6. How do I contact them?

If any of these answers require excessive scrolling or exploration, simplify the page.

---

# 30. Implementation Priority

Implement in this order.

## Phase 1 — Foundation

* New homepage
* Global navigation
* Global footer
* CTA system
* Responsive layout
* SEO metadata framework
* Image optimisation

## Phase 2 — Services

* Service index
* Event Photography
* Corporate Photography
* Product Photography
* Portrait Photography
* Property Photography

## Phase 3 — Case Studies

Build reusable case-study template.

Then migrate/create real projects.

Each case study should automatically support:

* Category
* Hero image
* Gallery
* Description
* Deliverables
* Testimonial
* Related service
* Related projects
* CTA
* SEO metadata

## Phase 4 — Conversion

* Pricing section
* Quote estimator
* Contact/quote form
* Tracking
* Conversion events

## Phase 5 — SEO/GEO

* Schema
* Breadcrumbs
* Internal linking
* Sitemap
* robots.txt
* canonicalisation
* Search Console verification
* Analytics
* Service/location content
* Guides

---

# 31. Migration Considerations

The existing Pixieset website must remain available during development.

Proposed architecture:

```text
accurova.com
      ↓
NEW ZEABUR WEBSITE

pixieset.accurova.com
      ↓
OLD PIXIESET WEBSITE / BACKUP
```

When the new website launches:

* Redirect old canonical URLs where appropriate.
* Preserve existing valuable URLs when possible.
* Create 301 redirects for changed URLs.
* Do not blindly redirect everything to `/`.
* Maintain equivalent page-to-page redirects.
* Preserve image/content URLs where practical.
* Submit the new sitemap.
* Monitor indexing and traffic after migration.

The migration should be treated as an SEO migration, not simply a domain switch.

---

# 32. Technical Requirement: Content-Driven Architecture

Do not hard-code every case study into the homepage.

Create reusable components/templates.

For example:

```text
ServiceCard
CaseStudyCard
CaseStudyPage
Testimonial
PricingCard
FAQ
CTA
ClientLogo
ProcessStep
```

This should allow Julian to add another case study without redesigning the website.

---

# 33. Future Scalability

The architecture should support future expansion into:

* Commercial photography
* Branding photography
* Food photography
* Real estate photography
* Videography
* Corporate content packages
* Photography workshops
* Photowalks
* Studio rental
* Overseas photography assignments

Do not build all of these pages now.

Build the architecture so they can be added later.

---

# 34. Final Product Goal

The finished Accurova website should feel like:

> **A professional Singapore photography company with the visual credibility of a strong photographer portfolio and the conversion architecture of a modern service business.**

The homepage sells the business.

The service pages explain the offering.

The case studies prove the capability.

The pricing reduces uncertainty.

The quote system converts interest into leads.

The SEO/GEO architecture makes the entire system discoverable.

Most importantly:

> **Every major photography category should ideally be represented by a real Accurova project rather than an artificial generic portfolio category.**

That real-project-first philosophy should remain central to the implementation.
