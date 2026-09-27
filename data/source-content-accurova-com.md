# Real content pulled from live accurova.com (Pixieset)

Scraped 2026-08-25 from `https://www.accurova.com/` and its subpages (curl with a browser user-agent — direct requests get a 403 from Pixieset's bot protection). This is the source of truth for facts, copy, pricing and testimonials — use it instead of inventing content. Update this file if the live site changes before cutover.

No address or UEN is published anywhere on the live site — `data/business.json` correctly keeps those as `TODO`.

---

## Identity

- Business name: **Accurova**
- Tagline: "Accurova, where Accuracy meets Innovation"
- Photographer: **Julian Cheung** — freelance professional photographer, Singapore, **8+ years** experience
- Real nav structure (this is the actual IA, not the corporate one in the build plan): Home · About · Testimonials · Astrophotos · Accurova.AI · Contact · Trust & Privacy Policy
- Positioning is **personal-brand / freelance photographer**, not a corporate B2B studio: "Look like the professional you already are. No posing experience needed. No awkward silences. Just clean, sharp images ready for LinkedIn, campaigns, and your biggest moments."
- Categories actually shot, per the real portfolio/homepage: **Portrait** (personal brand, executive, cosplay), **Event Coverage** (corporate, community, celebration), **Product Shoots** (e-commerce, lifestyle, campaign), and **Astrophotography** (own nav item, prints for sale).
- **Property/Real Estate photography** — confirmed by Julian 2026-09-28 (not from the original scrape; not visible on the live site at scrape time). Wide-angle DSLR high-resolution stills, rectilinear 360° photos, room virtual tours (4D Kankan), and walkthrough videos. Case-study content is ready but not yet built into the site.
- Cosplay portraiture is a real, significant part of the business — 4 of the 10 published testimonials are from cosplayers. This isn't in the current `markdown/PLAN.md` positioning at all.

**⚠ Strategic note:** `markdown/PLAN.md` positions Accurova as a corporate/B2B "commercial photography studio" (primary: Corporate/Event/Product, secondary: headshots/portraits, no mention of astro or cosplay). The real site is a freelance personal-brand photographer covering portrait/event/product/astro, with cosplay as a visible niche. These two directions don't fully agree — flagged for Julian to reconcile rather than silently resolved.

## About copy (verbatim, from `/about/`)

> Hello! I'm Julian Cheung, a freelance professional photographer with a heart for capturing life's precious moments. Over the past 8 years, I've had the joy of photographing everything from wedding portraits to starry-eyed cosplayers, helping people and businesses alike share their stories through vivid, meaningful images.
>
> Photography, for me, is more than just a skill; it's a way to freeze time, to hold onto the memories that matter most. Whether I'm working in bright sunlight or under the stars, I make sure every shot counts, so you can relive those moments exactly as you remember them. This past year, I've been thrilled to see clients fall in love with their photos, with many seeing incredible increases in how much their audiences engage with them.
>
> At the heart of my work are authentic, high-resolution photos that accurately capture the true spirit of the moment. I believe in keeping things real and natural, that is my artistic flair. I'm on the lookout for new stories to tell, new memories to capture.

## Homepage "Why Accurova" (verbatim)

- **S-Tier Results, Not Guesswork** — "8+ years of upskilling + pro Nikon D850 & Godox lighting means sharp, well-lit images in any environment; indoor, outdoor, or studio."
- **Comfortable, Guided Experience** — "You don't need to know how to pose. I direct patiently so you look natural and confident; camera-ready without awkwardness."
- **Commercial-Ready, Fast + Consistent Delivery** — "Clean, colour-accurate edits (no weird filters) delivered in 1–2 weeks; ready for campaigns, LinkedIn, and social media."

## Equipment (real)

Nikon D850, Godox lighting. (This matches the placeholder draft's equipment claim — that part can stay.)

## Pricing — "Rate card" (real, verbatim)

**Direction from Julian, 2026-09-28 (not scraped, first-party):** this rate card is his real current pricing, deliberately set below market rate. He's planning to raise it to market rate via a new, more robust pricing model, to be delivered as a guest-interactable price calculator on the site — see `data/business.json`'s `pricing._directionNote` and `markdown/STATUS.md`.

All packages include commercial usage rights, optimised colour-accurate post-production, and opt-in photo lab printing.

**Standard (Fast & Focused)** — Starting from $250
- Up to 2 hours coverage
- Guided direction
- Pro lighting kit
- Curated gallery of post-processed best images
- Delivery in 7–14 days (Accurova.AI optimised workflow)
- Best for: quick portraits, small events, compact product sets

**Enhanced (The Sweet Spot)** — Starting from $450
- 3–5 hours coverage
- Pre-shoot planning (mood board)
- Advanced lighting setups
- More selects + deeper edits
- Priority delivery (faster than Standard)
- Best for: brand days, corporate events, bigger cosplay/portrait sets, lifestyle product shoots

**Deluxe (All-Day Takeover)** — Starting from $850
- Full-day reserved
- Maximum variety: multiple locations / outfits
- Lighting mastery
- Hero-image focus
- Fastest turnaround + priority queue
- Optional add-ons: assistant, same-day selects, commercial usage / licensing
- Best for: campaigns, major launches

## Contact (real)

- WhatsApp: **+65 9856 6543**
- Email: **juliancheung@accurova.com**
- Post-shoot feedback form linked from `/contact/`

## Social (real)

- Instagram: https://www.instagram.com/accurova/
- Telegram community: https://t.me/accurova
- Medium.com: articles about photography (URL not found in scraped markup — get from Julian)

## Accurova.AI (real — different from what the build plan assumes)

This is **not** just an internal culling/retouching workflow tool. Per `/accurova-ai/`, it's a public-facing product: "the ultimate AI assistant for photographers," a ChatGPT-based tool "designed by serial AI entrepreneur Alaric Ong and Accurova," pitched to *other* photographers for client engagement (24/7 inquiry responses) and marketing content generation. The rate card does also credit it internally ("Delivery in 7–14 days (Accurova.AI optimised workflow)"), so it's used both ways — but its public page sells it as a product/tool for photographers generally, not as Accurova's internal AI-assisted-culling pitch to photography clients that the build plan's `/ai-innovation/` section assumes.

## Testimonials (real, verbatim — replace the fabricated placeholder ones)

1. "Julian is a long-time photographer of mine, and a friend. Even with his affordable rates, Julian constantly upgrades his equipment, and research on advanced photography techniques to provide even more value for his clients. I've personally seen how his photos have improved in quality as well, while his dedication to his clients have been steadfast. He is also very accommodative of my requests, be it the type of shoot or the location. Highly recommended!" — **Wah Qi Le, Wahsoshiok**
2. "Great communication, super easy to work with. Takes the cosers' opinion into consideration when planning. Perhaps because he does tutoring, very good at explaining things also! Was a great shoot!" — **Babbit, Cosplayer**
3. "Julian was a great photographer to work with. He was very accommodating and followed through our requests. His passion and professionalism can be seen in the quality photos he took. My associates and I will continue to engage his services in the future." — **Abdul Qayyum, NUS Political Assoc**
4. "very epic photog! i love how u send me every raw photo so i can slowly pick to choose and edit!! and also punctual to shoots (bcs im always late) !!!! xoxo not much suggestions or improvements bcs ur vv epic liao hehehe i think ur quality of shoots is vv good too n ur so friendly 🙏🙏 kinda wanna gatekeep u as my own photog liao but i can't stop recommending u to others HAHAHAH 100/10 best photog (istg i need to treat u to bbt or some drink one day)" — **kiri, Cosplayer**
5. "Julian was fun and really nice to work with :) A delight to work with, really nice too thank you sm :)" — **Haru, Cosplayer**
6. "We have engaged Julian on both event days for photography and was very pleasant with what he captured on site. Although he might not be familiar with beauty events, he was very proactive and quick in learning. At the same time, he was meticulous in his work and responsible in keeping the post production work in check. We can also see that he is really passionate in photography, would definitely like to work with him again. Thank you Julian!" — **Xie Jingyi, BREAVACO**
7. "Love the angled shots (the ones taken with more dynamic angles) which provided great storytelling for the photos taken :) A fantastic job at taking dynamic and well timed photographs to really bring out the essence of the character I'm cosplaying as! Very helpful and patient when taking photos, especially since I am very shy and inexperienced behind the camera." — **ZY, Cosplayer**
8. "very good photos taken and very good videos filmed. very professional with the framing and stuff. very high quality stuff. took extra behind the scenes pics too, which i think are kinda fun. very chill and cool guy. would 100% choose him again." — **Sachi, Cosplayer**
9. "Hi Julian... just done going through all the pictures.. they turned out good... some of them are soo beautiful that we want to print and frame them. I know maternity photoshoot is not going to be easy... but you have been really sweet, kind and patient with us as i take my own sweet time to do things 😂. Thank you for all your efforts and See you for another shoot once the baby is out." — **Nilima, mother-to-be**
10. "good grasp of angles and lighting. very nice photog, didn't get to talk to you much but i had an overall good experience at this shoot, especially with the photogs!" — **Jinx, Cosplayer**

## Trust & Privacy Policy (real — legal content, summarised)

- PDPA-compliant: only collects data necessary for project execution/invoicing, never sold/traded/shared.
- Pre-release confidentiality for unreleased merchandise/branding/cosplay debuts — raw files and drafts not published without explicit client consent.
- Responsible AI policy: no commissioned media/proprietary designs/personal likenesses used to train third-party generative AI without explicit written opt-in. AI tools (generative fill, automated masking) used only for localized retouching in Photoshop/Lightroom, to enhance human-directed work, not fabricate the core asset.
- Contracting aligned with the Tripartite Standard on Contracting with Self-Employed Persons (SEPs) — clear milestones, documented deliverables/timelines/revisions before shooting starts.
- Copyright: clients get agreed licensing/usage rights on full payment; Accurova retains the right to display final publicly-released images in its portfolio unless an NDA is active.
- Sells digital products too: Lightroom presets, CapCut templates, educational materials, via an "Accurova store" — final sale, licensed for individual use, no resale/redistribution.

## Correction (2026-09-27): SME500 Award 2026 is real, not fabricated

Julian confirmed via ATC's own verification tool (atc.sg) that ACCUROVA (UEN **53483334M**) holds a real **Singapore SME 500 Award 2026** accreditation, certificate no. **26-44508**, awarded 2026-03-10. It just wasn't published on the live Pixieset site at scrape time, which is why the earlier version of this note called it fabricated — that was wrong. It's now in `data/business.json` under `accreditations`, with the verification URL: https://www.atc.sg/sg-verify-sme-business-award-status-results.php. Safe to reference on the site; link to that verification page rather than restating the certificate number as an unlinked claim.

## What's confirmed fabricated in the current draft (do not keep)

- "900+ shoots delivered" — no such figure appears anywhere on the real site.
- "5.0 Google Rating" / aggregateRating of 5.0 with 900 reviews — not on the real site; no aggregate rating is published.
- "48H Avg. Turnaround" — real delivery is **7–14 days** (Standard tier), faster for Enhanced/Deluxe tiers but no "48 hour" figure is published.
- The 3 fabricated placeholder testimonials ("Placeholder Name, Head of Marketing" etc.) — replace with the 10 real ones above.
- "Featured in Straits Times, Lianhe Zaobao" — not found on the real site; homepage only says "Featured in & Trusted By" with what look like logo placeholders, no outlet named. Don't carry this claim over without confirmation.
