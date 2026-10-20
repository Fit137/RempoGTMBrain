# Source: GTM-BRIEF.md

Original path: `sources/raw/research/GTM-BRIEF.md`
Type: md
Size: 19,150 bytes
# Rempo, GTM Builder Discovery Brief (Run 2)

The filled discovery input for the `gtm-builder` skill, second run. This is what the skill's REQUIRED INPUTS checklist asks for, answered for Rempo after the second briefing on 2026-10-19.

**What changed since Run 1 (2026-10-16).** Run 1 was a consultation: it answered five founder decisions and recommended two motions split by number of locations. The founder has since decided the shape of the business, and this run builds the full go-to-market on those decisions:

- Rempo is a **hybrid of service and product, service-dominated.** The done-for-you service is the front-end offer. Software features are upsells later in the same funnel.
- **One ICP, one funnel, one message.** No separate go-to-market for the product, and no separate sales-led lane.
- **The funnel is optimized for self-serve purchase, with sales bumpers:** a VSL at the front, FAQs, a purchase flow, and several calls to action. One goes to a sales call for buyers who need more information. One goes to a middle-of-funnel asset with an opt-in, so non-buyers join the email list and keep being nurtured.
- **The funnel is not built in this run.** This run defines it at go-to-market level: stages, calls to action, assets, metrics.
- **The founder's ratings are assumptions, not facts.** The two matrices in `sources/founder-matrices.md` are a starting point. Every rating is checked against research in `research/step-0d-service-outcomes.md`.

**Global rules, unchanged from Run 1.** If a metric is unknown it stays `{TBD}`; no number is invented. No customer, result, or testimonial is on file, so the proof set is empty and closed. `{DEFERRED: product}` marks anything that depends on how a feature behaves, and each one resolves to a line in `dashboards/gtm-requirements-for-product.md`.

## Sources

1. **The pricing page,** `sources/pricing-page.md`, the source of truth for what is live today: Starter $197/month plus $299 setup, Growth $297/month plus $499 setup, Pro "Call for price", a 15-Day Free Trial, "Start Free" and "Book a Demo". This run recommends changes to it (Phase 9); until they ship, the live page is what a buyer sees.
2. **The founder's first brief,** `sources/founder-brief.md`: the business, stack, team, budget ($15,000), and the founder's hypotheses.
3. **The second briefing,** `sources/founder-matrices.md`, with the two CSV exports beside it: the Service Offer Matrix and the Product Features Matrix, and the instructions that came with them.
4. **Research,** `research/step-0d-service-outcomes.md` (2026-10-19) for this run, plus Run 1's research files (2026-10-16), which still hold for competitor facts and compliance unless superseded.

## Classification

| | |
|---|---|
| Archetype | Hybrid, service-dominated. A done-for-you review service sold online as a monthly subscription, delivered by Rempo's team on GoHighLevel. Software capabilities from the same platform are sold later as add-ons to existing clients |
| Audiences | One ICP (Phase 4). The skill's two ICP levels are read as two maturity stages of the same buyer, moving through the same funnel |
| Evidence state | Pre-launch for proof. Customer count `{TBD}` |
| Motion | Self-serve purchase with sales bumpers. Primary call to action: buy online. Bumper 1: book a call. Bumper 2: a middle-of-funnel asset with an opt-in, then nurture |
| Funnel role of the product | Upsells after purchase, inside the same funnel, under rules set in `dashboards/11-offer-architecture.md` |

## Fixed by the founder for this run

| # | Decision | Consequence for the skill |
|---|---|---|
| F1 | Service-dominated hybrid; the service is the front end | Phase 1 starts from the services (Phase 0, added), then scores features |
| F2 | One ICP, one funnel, one message | Phase 4 picks one ICP; Phase 5 runs for that ICP's two maturity levels; Phase 7 maps one journey |
| F3 | Self-serve purchase, optimized, with sales bumpers | Phase 7 maps the calls to action and where each bumper catches a buyer; Phase 9 prices for a checkout, not a sales call |
| F4 | VSL at the front, FAQs, purchase flow, a sales-call CTA, a middle-of-funnel opt-in | Phase 8 specifies these as assets; the Lead Magnet is the middle-of-funnel asset |
| F5 | Product upsells later, in the same funnel | Phase 9 prices them as add-ons; Phase 11 sets when they are offered |
| F6 | Do not build the funnel now | No page copy, VSL script, or email copy beyond what the skill's own templates require (copy drills, lead magnet sequence) |
| F7 | Treat the matrices' options and choices as assumptions | Phase 0 redesigns what is measured and re-rates every service from research |

## What this run decides

1. What to measure on each service, and what each service actually produces (Phase 0)
2. Which features lead, which are table stakes, which to drop from the pitch (Phase 1)
3. The competitive set for a done-for-you offer, and where Rempo can lead (Phases 2 and 3)
4. The single ICP and its buying roles (Phases 4 and 5)
5. The message (Phase 6)
6. The funnel at go-to-market level: stages, calls to action, bumpers, metrics (Phase 7)
7. The offer, packaging, and prices: front end, order bump, upsells, product add-ons (Phase 9)
8. Channels, assets, and the hire (Phase 8)
9. The 90-day test of all of it on the $15,000 budget (Phase 10)
10. When and how product upsells enter the funnel without turning Rempo into two companies (Phase 11)

## What this run does not decide

The funnel build (pages, VSL script, checkout configuration, email copy beyond the scorecard sequence), the product requirements and user flows, which CRMs connect and how, and legal review. Each gap is marked and listed in `dashboards/gtm-requirements-for-product.md`.

---

# 1. PROJECT INFORMATION

| Field | Value |
|---|---|
| Project name | Rempo |
| Project website | https://rempo.io (did not resolve from this environment on 2026-10-16 or 2026-10-19) |
| Category name | Done-for-you Google review management for local service businesses |
| Niche focus | Owner-led home-service businesses that already keep customer records in a CRM or field-service software (Phase 4) |
| One-liner, founder's words | "a done-for-you reputation management service that helps businesses consistently generate Google reviews without learning software, manually following up, or relying on staff to remember to ask" |
| One-liner, working form | Rempo connects to the software you already log jobs in, asks every customer for a Google review after every job, follows up, and answers every review, so your profile stays current without anyone at the shop running it |
| Business model | A monthly service with a one-time setup, bought online. Service upsells (Google Business Profile, website) and product add-ons (software) sold after purchase |
| Delivery | The founder runs onboarding and raises upsells; a technical assistant does setup. Stack: GoHighLevel, Zapier, NiftyImages (the brief writes "Neftyimage"), WordPress |
| GTM budget | $15,000 for a 90-day experiment, including external help and advertising |

# 2. COMPETITORS

Selection rule from Run 1, unchanged: a competitor earns a slot only if this buyer actually weighs it. Run 2 changes the slate, because Rempo now sells a done-for-you service online and the buyer is a single-ICP home-service owner.

| Slot | Name | Why |
|---|---|---|
| 1. Closest self-serve substitute | NiceJob | Review software at $75 to $125 a month, bought without a call. Sets the price a buyer expects for a tool |
| 2. Already paid for | Jobber Reviews (standing for the review feature in field-service software; Housecall Pro has the same) | The ICP keeps jobs in this software, and its review switch is already there |
| 3. Category leader | Podium | The name owners know; sold by demo on annual terms at about $399 to $599 a month |
| 4. Done-for-you alternative (new) | Footbridge Media | Contractor marketing at $249 a month with website, profile optimization, and review management included, no contract, 90-day money-back guarantee. The sharpest comparison for a service sold online |
| 5. Status quo | Google Business Profile, used by hand | The free review link plus someone remembering to send it |

**Out of the slate in Run 2:** Birdeye, which positions on multi-location brands outside the single ICP; agencies on GoHighLevel, noted as a market rather than one competitor; Scorpion, a sales-led agency on long contracts.

# 3. FEATURES LIST

The new feature list combines the founder's Product Features Matrix (the source for what the offer is now) with the pricing page items it does not cover. Numbers are Phase 1 row numbers.

| # | Feature | Group | Source |
|---|---|---|---|
| 1 | Automated review requests from CRM job data | Core service | Matrix (founder: needs an existing CRM) |
| 2 | Automated follow-ups | Core service | Matrix |
| 3 | Personalized visual request (owner or team photo, customer's first name in the image) | Core service | Matrix, founder's brief |
| 4 | Review replies, AI-drafted, written for each review | Core service | Matrix, pricing page (AI Review Reply Assistant) |
| 5 | Reviews repurposed into social posts | Core service | Matrix, pricing page (AI Social Post Generator) |
| 6 | Review widget on the website | Core service | Matrix, pricing page (Auto-Display 5★ Reviews; Google Review Widget) |
| 7 | Done-for-you implementation (CRM connection, setup) | Core service | Matrix (Custom Implementation) |
| 8 | Review monitoring, negative review alerts, monthly report | Core service | Pricing page (Negative Review Alerts, Review Dashboard, Monthly Performance Report) |
| 9 | Google Business Profile optimization | Upsell 1 | Matrix |
| 10 | Autoposting to Google Business Profile | Upsell 1 | Matrix |
| 11 | Autoposting to major social media | Upsell 1 | Matrix |
| 12 | Geotagged images | Upsell 1 | Matrix |
| 13 | Website FAQ auto-updated from what customers ask | Upsell 1 | Matrix |
| 14 | Website gallery widget, auto-updated | Upsell 1 | Matrix |
| 15 | Website build and occasional updates (home services) | Upsell 2 | Matrix, founder's brief |
| 16 | Unified inbox (Facebook, Instagram, Google, SMS, email) | Product layer | Matrix ("prefer not, to reduce support"), pricing page (Client Inbox) |
| 17 | Social media scheduler | Product layer | Matrix, pricing page (Social Media Manager) |
| 18 | AI voice receptionist | Product layer | Pricing page (Pro) |
| 19 | Smart booking calendars | Product layer | Pricing page (Pro) |
| 20 | Sales pipeline and workflow automation | Product layer | Pricing page (Pro) |
| 21 | Reactivation campaigns | Product layer | Pricing page (Pro) |
| 22 | Website chat and AI chat widget | Product layer | Pricing page (Growth, Pro) |
| 23 | Customer surveys | Product layer | Pricing page (Growth) |
| 24 | Referral and testimonial requests | Product layer | Pricing page (Growth) |
| 25 | Listings sync across directories | Product layer | Pricing page (Growth) |
| 26 | Video testimonial requests | Candidate, not built | Founder's brief |

"Google Search Boost" (pricing page) is read as the GBP optimization in row 9. "24/7 Support" and "Multi-User Access" are terms of service, not features, and are handled in Section 5 and Phase 9.

**Deliberately not offered, and named as such in the FAQ:** review gating, incentives for reviews, fake or bought reviews, asking customers to name staff or use given wording, removing negative reviews, guaranteed review counts, and guaranteed rankings.

# 4. BUSINESS CONTEXT

Unchanged from Run 1 except where noted.

```
Team:               Founder, working full-time elsewhere; runs onboarding and upsells.
                    One technical assistant does setup. Hire options: media buyer plus research
                    strategist ($900/month) or plus creative agency ($2,400/month combined).
Burn rate:          {TBD}
Budget:             $15,000 for 90 days, including external help and advertising
Channels tried:     {TBD}; treated as none
Working CAC:        $350, the founder's figure, not validated
Customers today:    {TBD}
Cost to serve:      {TBD} per account. Public inputs for the structure in Phase 9 (research Step 0D, section 6)
```

## Open decisions that change the output

| # | Decision | Blocks | Proposed default |
|---|---|---|---|
| 1 | Geography | Phases 4, 8 | United States, English |
| 2 | Which CRMs and field-service systems the setup connects to, and the fallback for shops without one | Phases 4, 7, the checkout qualifier | Housecall Pro and Jobber first (both expose a completed-job trigger), CSV upload as fallback, `{DEFERRED: product}` |
| 3 | Whether the 15-day free trial stays | Phases 7, 9 | Replace with a paid start and a process guarantee (Phase 9). Founder to confirm |
| 4 | The process guarantee's terms: days to go live, refund scope | Phases 6, 9 | "First requests out within 7 days of your CRM connection, or your setup fee back", counsel to review |
| 5 | Customers today and any result the founder may cite | Phases 2, 6 | None; the proof set stays empty |
| 6 | Cost to serve per account | Phases 9, 10 | `{TBD}`; structure built with blanks |

# 5. POSITIONING AND CLAIM CONSTRAINTS

Governing sensitivity, unchanged: every claim about reviews sits under Google's review policies and the FTC Consumer Review Rule. Claim the process, never a result. Never imply selective asking. Never blame staff. Two things are stricter than in Run 1: Google added clauses to its rating manipulation policy in April 2026, and the FTC began enforcing its rule with warning letters in December 2025, holding businesses liable for third parties acting on their behalf, which includes Rempo.

| Do not write | Write instead | Why |
|---|---|---|
| "Get more reviews", "X new reviews a month", any guarantee of reviews | "We ask every customer after every job, and follow up." Report the client's own numbers against their baseline | An outcome Rempo does not control; no rate on file |
| "Rank higher on Google", "Better ranking" (the founder's matrix outcome) | "Reviews are one of the things Google weighs in local results. We track your position, and never promise it" | Google: relevance, distance, prominence; proximity and category dominate (research 1c) |
| "Our requests convert better", "personalized requests get more reviews" | "Your customer gets a request with your team's photo and their first name, not a generic text." A number only after Rempo's own A/B test | No study on file (research 1d) |
| Request copy that asks the customer to mention a technician by name, or suggests what to write | Ask for an honest review, with nothing about content | Google policy, April 2026: no soliciting content that identifies a staff member, no supplied wording (research 1e) |
| Technician review quotas, leaderboards, or contests, as a feature or a tip | Recognize staff from reviews that arrive unprompted, if at all | Google policy, April 2026: no staff quotas |
| "Every review gets an instant AI reply" | "Every review gets a reply written for that review." Approval mode or automatic: `{DEFERRED: product}` | 50% of consumers are put off by generic or templated replies (BrightLocal 2026) |
| "Posting weekly boosts your ranking" | "Your profile and social stay current with your real work, without you posting" | Controlled test found no ranking movement from posts (research 2) |
| "Geotagged photos help you rank" | Drop geotagging from all sales assets | Google strips location data on upload; tests found no lasting effect (research 2) |
| "Your FAQ shows up in Google" | "Answers to what your customers ask, on your service pages" | FAQ rich results limited to government and health sites since 2023; Business Profile Q&A removed in 2025 (research 2) |
| "Your reviews will show as stars in Google" (said of the widget) | "Your best recent reviews, on your site where visitors decide" | No star snippets for a business's own reviews on its own site since 2019 |
| "Shows all your reviews", or a widget that hides low ratings while implying it shows everything | "Recent reviews from Google", with nothing implying it is the full set | FTC rule on displaying reviews |
| "No software to learn, no buttons to click" as an absolute | "We connect to the software you already log jobs in. After that, requests go out without anyone at the shop sending them" | True only once job records reach Rempo; the founder's note makes a CRM a requirement |
| "Done for you" with no scope | "We set it up and run it. You give us access once": CRM connection, Google profile access, a team photo, consent wording for texts | The owner always does something; listing it prevents surprises at onboarding |
| "Start Free" with a setup fee | If the trial stays: "15-day free trial of the monthly plan, $299 setup fee charged [at signup / at conversion]". If a paid start replaces it: no "free" anywhere | FTC guide on the word "free" (16 CFR Part 251) |
| A guarantee about reviews, ratings, or rankings | A guarantee about the process: go-live time, requests sent, replies posted. Terms `{TBD}` with counsel | Process is what Rempo controls |
| "24/7 Support" | Support hours as actually staffed, `{TBD}` | One founder with a day job and one assistant |
| "Catch unhappy customers before they post" | "Every customer gets the same request. Alerts tell you when a review posts" | Review gating |
| Referral rewards tied to leaving a review | Rewards, if any, for referrals only | Google and FTC incentive rules |
| "Reputation management" alone | Name what is included, and say Rempo does not remove reviews | Buyers assume removal |

Also banned everywhere: customer counts, uplift figures, testimonials, logos, unsourced statistics, guarantees of outcomes, and the words leverage, unlock, seamless, robust, streamline, cutting-edge, and empower. No em dashes.

# 6. QUESTIONS THE FOUNDER DID NOT ASK

| # | Question | Answered in |
|---|---|---|
| 1 | The founder's note says review requests need an existing CRM. What share of buyers fail that gate, and what happens to them in a self-serve funnel? | Phases 4, 7, 10 |
| 2 | Is a free trial right for a done-for-you service sold online, given the setup labor and the FTC "free" guidance, or does a paid start with a process guarantee convert as well? | Phases 7, 9, 10 |
| 3 | The GBP manager's ranking outcome holds for one-time optimization but not for recurring posting. Should the upsell be split? | Phases 0, 9 |
| 4 | If AI replies read as templated, do they cost more trust than they earn? | Phases 0, 6 |
| 5 | The product layer adds support load the founder wants to avoid. Which add-ons are worth it, and when? | Phases 1, 11 |
| 6 | Footbridge Media bundles a website with review management at $249 a month. How does Rempo's offer read next to it? | Phases 2, 3, 9 |
| 7 | What does each account cost to serve, and what is left after GoHighLevel usage, texting fees, and assistant hours? | Phase 9 |

# 7. PUBLIC FACTS ON FILE

See `research/step-0d-service-outcomes.md` for every figure used in this run, with source and quality. Run 1's facts in `research/` still apply where Step 0D does not supersede them.
