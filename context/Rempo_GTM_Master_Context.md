---
title: Rempo Go-To-Market Master Context
project: Rempo
type: gtm_context_file
purpose: Single source of truth for any AI agent executing Rempo go-to-market work.
version: 1.0
last_updated: 2026-10-19
status_notes: Pre-launch for proof. No customers, results, testimonials, or logos are on file, so the proof set is empty. The live pricing page (Starter $197 plus $299 setup, Growth $297 plus $499 setup, Pro call for price, 15-Day Free Trial) is what a buyer sees today. The Run 2 offer (Review Engine at $197 per location plus $299 setup, paid start with a 7-day process guarantee, GBP Tune-Up, GBP Upkeep, website, AI voice receptionist) is RECOMMENDED and awaits the founder's decision; never present it as live. Which job software connects at launch is unconfirmed. The funnel (VSL, page, checkout, scorecard) is specified, not built.
canonical_vocabulary: Rempo, Review Engine, GBP Tune-Up, GBP Upkeep, Review Engine Scorecard, Google Review Gap Report, personalized request, job software, setup fee, process guarantee, offer line, location, owner, office manager, client, customer, done for you, home-service
---

# Rempo Go-To-Market Master Context

This file is the complete, distilled go-to-market for Rempo. It exists so that any AI agent can absorb the strategy, ICP, positioning, messaging, competitive frame, funnel, offer, and campaign plan in one read, then execute go-to-market work precisely and on-brand without re-deriving anything.

If you are an AI agent, read the next section first. It tells you how to use everything below.

---

## 0. Agent operating instructions

**What this file is.** The consolidated output of the gtm-builder Run 2 (2026-10-19): a Service Offer Matrix, nine skill dashboards, a 90-day experiment, an offer architecture, a lead magnet, and a product handoff, built on the founder's two briefings and dated research. The originals are in `sources/`. Every section is authoritative unless a status flag says otherwise.

**How to use it.**

1. Before writing any customer-facing copy, load the canonical vocabulary (Section 2), the status ledger (Section 3), and the claim hygiene ledger (Section 4). The standalone versions in `rules/` are what you check on every task.
2. Know who you are writing for. There is one ICP and one message (Section 8). Paid acquisition speaks to the owner. Onboarding and in-account copy speak to the office manager. Delivery copy (review requests and replies written for a client) speaks to that client's customers, under the rules in `reference/review-compliance.md`.
3. Respect the funnel stage. Section 13 gives the mindset, questions, and assets at each step. Write to the stage, not past it.
4. Obey the strategic verdicts in Section 9. They are decided. Do not contradict them, and do not describe a recommended or planned change as live.
5. Honor the house writing rules in Section 1.

**Hard guardrails, never violate:**

1. **Claim the process, never a result.** Rempo controls asking every customer, following up, and replying to every review. It does not control how many reviews arrive, the rating, or Google rankings. Never promise reviews, ratings, rankings, calls, or jobs.
2. **The proof set is empty and closed.** No customer counts, results, uplift figures, testimonials, quotes, or logos exist. Write `[PROOF POINT NEEDED]` where proof would go. Market facts from third parties may be used only with the source named in the asset.
3. **Status flags travel with capabilities.** Anything PLANNED or HELD is never described in the present tense. The Run 2 offer is PLANNED until `ops/decisions.md` marks it DECIDED.
4. **Google review policy and the FTC Consumer Review Rule govern every word about reviews.** Same request to every customer, no filtering of unhappy customers, no incentives, no asking a customer to name a staff member, no suggested wording, no staff quotas.
5. **One ICP, one funnel, one message.** The product layer never leads an ad, a page, or an email. There is no separate sales-led lane.
6. **Channel discipline.** This GTM runs Meta ads, Google Search ads, the VSL page and checkout, email nurture to people who opted in, and retargeting. It does not produce cold email, LinkedIn outreach, LinkedIn Ads, or cold calls or texts to prospects.

---

## 1. House writing rules

- No em dashes. Use commas, or restructure.
- Banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower, elevate, revolutionize, game-changing, best-in-class, world-class, supercharge, turbocharge, harness, delve, tapestry, realm, testament, foster, facilitate, utilize, myriad, plethora, pivotal.
- Short paragraphs, one to three sentences. Specific numbers and named steps over adjectives.
- Tone: plain, direct, and respectful of a busy tradesperson. The buyer runs crews and phones all day and has heard every marketing promise. Talk like someone who does the work: say what happens, who does it, and what the owner does once.
- Every statistic carries its source in the same sentence, for example "(BrightLocal 2026)".
- Every sample (a request, a reply, a report) is labeled as a sample.
- For anything spoken (the VSL, video ads, the sales call), write for the ear. See `rules/writing-rules.md`.

---

## 2. Canonical vocabulary

| Term | Rule |
|---|---|
| Rempo | One word, capital R. The company and the brand. |
| Review Engine | The done-for-you review program, the front-end service. The live page calls this plan Starter; use Review Engine in copy for the new funnel. |
| GBP Tune-Up | The one-time Google Business Profile optimization. Replaces "Google Search Boost". |
| GBP Upkeep | The monthly profile and social posting service, sold as staying current, never as ranking. |
| Review Engine Scorecard | The seven-question self-assessment, the middle-of-funnel opt-in. |
| Google Review Gap Report | The free one-page comparison against the local top three, sent after the scorecard. |
| Personalized request | A review request showing the shop's team photo with the customer's first name. Never "hyperpersonalized". |
| Job software | Buyer-facing name for the CRM or field-service software (Jobber, Housecall Pro, ServiceTitan). |
| Client and customer | Client: the shop that pays Rempo. Customer: the client's customer, who is asked for a review. Never blur them. |
| Offer line | "$197 a month per location, $299 setup. First requests out within 7 days of your software connection, or your setup fee back. Month to month." PLANNED. |

Full list and banned near-synonyms: `rules/glossary.md`.

---

## 3. Status ledger

Legend: LIVE = offered on the live pricing page or in delivery today, claimable in the present tense. PARTIAL = live, but part of how it works is unconfirmed; say only the confirmed part. PLANNED = recommended or decided, not live; mark "coming soon" or omit. HELD = product layer under the release rule; do not sell or advertise. DROPPED = removed from every sales asset.

### Review Engine (core service)
- Review requests by text and email: LIVE.
- Requests triggered by a completed job in the client's job software: PARTIAL. Which systems connect at launch is unconfirmed (`{DEFERRED: product}`); Housecall Pro and Jobber expose a completed-job trigger.
- Follow-up reminder after the first request: LIVE (founder's brief).
- Personalized request with team photo and customer's first name: LIVE (founder's brief). First-name fallback: unconfirmed.
- Reply written for each review: LIVE ("AI Review Reply Assistant" on the page). Approval mode or automatic posting: unconfirmed, so never say "instant" or "automatic".
- Negative review alerts: LIVE. A reply drafted inside the alert: PARTIAL.
- Review dashboard and monthly performance report: LIVE. Report against a day-one baseline: PLANNED.
- Recent reviews displayed on the client's website: LIVE. Never imply it shows every review.
- Social posts made from five-star reviews: LIVE (Growth plan). Approval before posting: unconfirmed.
- Done-for-you setup (software connection, Google access, messages, team photo, texting registration): LIVE, paid by the setup fee.

### Offer and terms
- Live page: Starter $197/month plus $299 setup; Growth $297/month plus $499 setup; Pro "Call for price"; 15-Day Free Trial; "Start Free" and "Book a Demo" buttons: LIVE.
- Run 2 offer ladder, per-location pricing, one plan card, add-on prices, annual plan: PLANNED.
- Paid start with the 7-day process guarantee, replacing the free trial: PLANNED. Terms with counsel.
- Month to month, no contract: PLANNED as part of the offer line. Omit until confirmed.
- "24/7 Support": DROPPED. Still on the live page; removal is a downstream item.

### Profile, website, and product add-ons
- GBP Tune-Up as a $197 order bump: PLANNED. The optimization exists today inside Growth as "Google Search Boost", a name that is DROPPED.
- GBP Upkeep as a $97/month upsell: PLANNED. Social Media Manager exists in Growth today.
- Geotagged images: DROPPED. Posting sold as ranking: DROPPED. Auto-updated FAQ for Google: DROPPED, rebuilt as answers on service pages inside the website.
- Website build ($1,497 plus $49/month): PLANNED, sold on a call after a site check.
- AI voice receptionist ($97/month): PLANNED as the first product add-on, offered when call data shows missed calls. Listed under Pro today.
- Unified inbox, booking calendars, pipeline and workflow automation, reactivation, website and AI chat, surveys, referral and testimonial requests, listings sync, social scheduler: HELD (Section 11 release rule). Still listed on the live page under Growth and Pro.
- Video testimonial requests: HELD, a candidate, not built.

### Funnel assets
- VSL, VSL page, FAQ, checkout with qualifier and order bump, one-click upsell, thank-you and booking, call page, Review Engine Scorecard, Gap Report, sample request to your phone, nurture sequence: PLANNED. Specified, not built.

### Proof
- Customers, results, testimonials, logos: none on file.

Standalone, with notes: `rules/feature-status.md`.

---

## 4. Claim hygiene ledger

| Do not say | Say instead |
|---|---|
| "Get more reviews", "X new reviews a month", any review guarantee | "We ask every customer after every job, and follow up." Report the client's own numbers against their baseline. |
| "Rank higher on Google" | "Reviews are one of the things Google weighs in local results. We track your position, and never promise it." |
| "Personalized requests get more reviews" | "Your customer gets a request with your team's photo and their first name, not a generic text." |
| Request copy that asks the customer to name a technician, or suggests what to write | Ask for an honest review, with nothing about content. |
| Staff quotas, leaderboards, contests | Recognize staff from reviews that arrive unprompted, if at all. |
| "Every review gets an instant AI reply" | "Every review gets a reply written for that review." |
| "Posting weekly boosts your ranking" | "Your profile and social stay current with your real work." |
| "Geotagged photos help you rank" | Nothing. Geotagging is dropped. |
| "Your FAQ shows up in Google" | "Answers to what your customers ask, on your service pages." |
| "Shows all your reviews" | "Recent reviews from Google." |
| "No software to learn, no buttons to click" as an absolute | "We connect to the software you already log jobs in. After that, requests go out without anyone at the shop sending them." |
| "Catch unhappy customers before they post" | "Every customer gets the same request. Alerts tell you when a review posts." |
| "Start Free" next to a setup fee, with the fee hidden | The fee stated beside the word "free", or no "free" at all. |
| "24/7 Support" | Support hours as actually staffed, `{TBD}`. |
| "Reputation management" alone | Name what is included, and say Rempo does not remove reviews. |
| Run 2 prices or the guarantee as if live | Omit, or label the draft `[OFFER PENDING]` until the decision log marks the offer DECIDED. |

Superlative scoping, competitor facts, and channel-specific bans: `rules/do-not-say.md`.

---

## 5. What Rempo is

A **hybrid of service and product, service-dominated.** Rempo is a done-for-you Google review program for local service businesses, sold online as a monthly subscription with a one-time setup fee, and delivered by Rempo's team on GoHighLevel (with Zapier, NiftyImages, and WordPress). The service is the front-end offer. Software capabilities from the same platform are sold later, as add-ons to existing clients, inside the same funnel.

**What the Review Engine does.** Rempo connects to the software the shop logs jobs in. After each completed job the customer gets a review request by text or email, with the team's photo and their first name, then one reminder. Every new review gets a reply written for that review. Negative reviews trigger an alert. Recent reviews show on the shop's website and five-star reviews become social posts. Every month the owner sees requests sent, reviews in, replies posted, and calls from the Google profile.

**What the owner does once:** connect the job software, give Google profile access, send a team photo, and approve the texting registration details.

**What Rempo does not do:** remove reviews, filter unhappy customers, offer incentives for reviews, write reviews, or guarantee counts, ratings, or rankings.

**Team and capacity.** The founder works full-time elsewhere, runs onboarding, the 30-day review, and sales calls. One technical assistant does setup and monthly checks. Support hours are `{TBD}`.

**Budget.** $15,000 for a 90-day experiment, including external help and advertising.

---

## 6. Service and feature matrix

**What each service actually produces (Phase 0, research Step 0D).**

| Service | Outcome metric | Evidence | Funnel role | Verdict |
|---|---|---|---|---|
| Review Engine | Reviews in the last 90 days; calls from the profile | Strong | Front-end | Lead with it |
| GBP Tune-Up | Profile completeness; geo-grid rank at day 30 and 60 | Strong for one-time optimization | Order bump | Sell as a one-time fix |
| GBP Upkeep | Profile and feed activity | Weak (no ranking evidence for posting) | One-click upsell | Sell as staying current |
| Website | Calls and forms from the site | Moderate | Account upsell, on a call | Home services only |
| Product layer | Answered-call rate (receptionist) | Moderate for the receptionist | Product add-on | Receptionist first; the rest held |

"Better ranking", the founder's headline outcome, is the weakest claim in the founder's matrix: moderate for reviews, not supported for posting or geotagging. The message moved from ranking to recency and replies, which buyers read and Rempo can show.

**Feature quadrants (Phase 1, demand and competitiveness scored from -20 to +20).**

- **Q1 Hero:** done-for-you implementation (demand 9.4, competitiveness 7.1). Borderline: Google Business Profile optimization, AI voice receptionist.
- **Q4 Table stakes:** automated requests from job data (demand 16.8, competitiveness -5.9), follow-ups, replies, monitoring and the monthly report. Must work; never the headline.
- **Q2 Differentiators:** the personalized request (competitiveness 7.6), social posts from reviews, autoposting, the website widgets, referrals, reactivation, listings, video testimonials.
- **Q3 Commodities:** the review widget, website build, inbox, scheduler, booking, chat, geotagging, pipeline, surveys.

**Demand driver (top-of-funnel hook):** the Review Engine Scorecard plus the Google Review Gap Report. Variant: a sample request sent to the visitor's own phone.

**What to measure on every account (KPI tree).** Delivery, which Rempo controls and can promise: days to first request, ask coverage (requests sent ÷ completed jobs with contact details), reply coverage within 48 hours. Client outcome, reported against a baseline and never promised: request-to-review rate, reviews in the last 90 days, rating, profile actions, geo-grid position. Business: retention at months 2, 6, 12; attach rate per add-on; cost to serve per account.

---

## 7. Competitive market analysis

**The slate.** A competitor earns a slot only if this buyer weighs it.

| Rival | What it is | Real strength | Real gap |
|---|---|---|---|
| NiceJob | Review software, $75 to $125/month, bought without a call | Easy setup, integrations, 14-day trial without a card | The owner runs it; restrictive timing and wording; slow onboarding help |
| Jobber Reviews | The review feature inside field-service software (Housecall Pro has one too) | Already inside the software where the job closes | Jobber users only; marketing tools on the $199 Grow plan; fixed follow-up; nobody runs it |
| Podium | The category name owners know; an "AI employee" platform sold by demo | Breadth; G2 rating about 4.6 from 2,000+ reviews | Reported annual terms at about $399 to $599/month; difficult cancellation; unpublished pricing |
| Footbridge Media | Contractor marketing, $249/month: website, SEO, profile optimization, Birdeye review tool | One price, no contract, 90-day money-back guarantee | Reviews are a bundled third-party tool, not a program run from the client's job data |
| Google by hand | The free review link and QR code | Free, native | Depends on someone remembering; no follow-up |

**Positioning vectors (0 to 10; Rempo scored as designed, proven `{TBD}`).**

| Vector | Rempo | NiceJob | Podium | Jobber | Footbridge | By hand |
|---|---|---|---|---|---|---|
| Easy, hands-off automation (they lead) | 8.4 | 9.1 | 6.8 | 8.4 | 7.6 | 2.3 |
| Platform breadth (they lead) | 6.2 | 5.2 | 9.3 | 7.1 | 8.1 | 3.8 |
| Done for you, from your CRM (we lead) | 9.2 | 3.7 | 3.1 | 2.6 | 7.3 | 0.4 |
| Personal, not templated (we lead) | 8.6 | 4.6 | 4.2 | 3.3 | 3.9 | 5.6 |

**The wedge.** Compete on effort, not features. The tools leave someone at the shop running the program; the one service in the set runs the website and treats reviews as a bundled tool. Rempo runs the review program itself, from the jobs the shop already logs, and sells it the way the tools sell: a published price, bought online.

**Defensibility** is not in the features (any agency on GoHighLevel can buy them). It is in the operating playbook (connections, timing, reply quality, compliance with Google's April 2026 rules), a home-service focus that makes every result transfer, and the proof base the first cohort builds. Until customers exist, all of it is designed, not proven.

---

## 8. Ideal customer profile and buying committee

**One ICP.** Owner-led home-service businesses in repair and maintenance trades, starting with residential HVAC and plumbing, with one or two locations, that already run jobs in field-service software or a CRM holding customer phone numbers or emails. United States, English (default; open decision).

**Why this ICP.** Jobs close every day, so there is someone to ask every day. About 120,000 to 170,000 HVAC businesses (IBISWorld; Orbital) and about 127,000 plumbing businesses (IBISWorld). Average jobs of $338 (plumbing) and $350 (HVAC repair) (Angi) make breakeven arithmetic easy. 91% of homeowners rate reviews important when choosing an HVAC contractor (ACHR News 2024). The owner decides alone and pays by card.

**Two maturity stages, one funnel.**

| | Level 1: no review system | Level 2: tried a tool and stalled |
|---|---|---|
| Pain | Asking depends on whoever remembers; the newest review is old; replies unwritten | The review switch was turned on once and nobody owns it; generic texts; templated replies; a contract |
| What wins | Done for them, from software they already use; bought online | Someone runs the program instead of a switch nobody watches; it reads like the shop |
| Extra answer needed | None | "We already have reviews in Jobber"; how double requests are avoided (`{DEFERRED: product}`) |

**Roles.** The **owner** buys: holds the card, decides alone. Blocks on price against NiceJob or the job-software switch, the setup fee before seeing anything, "we tried this before", and not wanting a call. The **office manager** is the user and the champion: runs the job software, decides in month two whether Rempo stays, and worries about one more system and texting customers too much. The VSL speaks to the owner; onboarding is built for the office manager.

**Checkout qualifier.** Three questions protect the done-for-you promise: where do you log your jobs (no software routes to a call or the upload fallback, `{DEFERRED: product}`), how many jobs a week (fewer than 5 continues with a note), how many locations (3 or more routes to "Book a call").

**Triggers.** A bad review; a slow week; a new competitor nearby; a new office manager; starting Local Services Ads; a tool contract ending.

**Founding cohort.** The first 5 to 10 paying shops: HVAC or plumbing, owner reachable, Jobber or Housecall Pro, willing to compare personalized and plain requests. They give a baseline and feedback calls. They are never asked for a testimonial or a review of Rempo as a condition of their terms.

---

## 9. Strategic verdicts (decided)

1. **Service in front, product behind, one funnel.** The founder fixed it; the evidence agrees (Section 6). Product add-ons are sold only to service clients, never lead an ad, and leave "Hold" only under the release rule (Section 11).
2. **One ICP, one funnel, one message.** No second go-to-market for the product, no sales-led lane.
3. **Self-serve purchase with two bumpers:** "Book a 15-minute call" and "Take the scorecard". Three or more locations go to a call inside the same funnel.
4. **Lead with done for you.** Core claim: "Rempo runs your Google reviews for you. Every job asked, every review answered."
5. **The personalized request is the picture, not the claim.** Shown in the VSL and ads as what the customer receives. No lift claimed until Rempo measures one.
6. **Claim the process, never a result.** Ranking is reported as a tracked number, never promised.
7. **Split the GBP manager; drop geotagging; reframe autoposting and the auto-FAQ.** The evidence sits in the one-time optimization only.
8. **First 90 days of channels:** Meta ads, Google Search ads, nurture and retargeting. LinkedIn and cold email are out because they do not reach this buyer.

Open and recommended (prices, the paid start, the guarantee, the hire, the budget split): `ops/decisions.md`.

---

## 10. Value proposition: the owner

**Brand promise:** Every customer asked, every review answered, and you never have to run it.

**Positioning:** A done-for-you Google review program for home-service shops, run from the job software they already use.

| Pillar | Description | Reasons to believe |
|---|---|---|
| VP 1. Done for you | We set it up from the software you already use, and we run it | Our team does the setup. A request goes out after every completed job once your software is connected (`{DEFERRED: product}`: which systems). First requests within 7 days of the connection, or the setup fee back (PLANNED, terms `{TBD}`). |
| VP 2. Personal, not templated | Requests and replies that read like your shop | Each request shows your team's photo with the customer's first name. Every review gets a reply written for that review. Every customer is asked the same way, under Google's rules. |
| VP 3. Proof you can see | The work and the numbers every month, against where you started | A baseline on day one and a monthly report (baseline PLANNED). Your best recent reviews keep working on your site and as social posts. An alert the day a negative review posts. |

Every "social proof" headline and supporting proof point is `{TBD}`. Each copy drill names a process substitute instead, something true that can be shown today. Copy drills: `reference/value-proposition-owner.md`. Approved lines: `ops/copy-bank.md`.

**The office manager** hears one thing: nothing new for you to do. That line belongs in onboarding, the "what you do, what we do" section, and the sample report, not in the ads.

---

## 11. Offer architecture and pricing

**Today (LIVE):** Starter $197/month plus $299 setup; Growth $297/month plus $499 setup; Pro "Call for price"; 15-Day Free Trial.

**Recommended (PLANNED, awaiting the founder):** one plan card, priced per location, with add-ons offered in funnel order.

| Step | Offer | Layer | When it is offered | Price |
|---|---|---|---|---|
| 0 | Review Engine Scorecard and Gap Report | Free | Ads, VSL page exit, search | Free, with opt-in |
| 1 | Review Engine | Service | VSL page, checkout | $197/location/month plus $299 setup |
| 2 | GBP Tune-Up | Service | Order bump at checkout | $197 one-time |
| 3 | GBP Upkeep | Service | One-click upsell after payment | $97/location/month |
| 4 | Website | Service | 30-day review, after a site check | $1,497 plus $49/month |
| 5 | AI voice receptionist | Product | When call data shows missed calls | $97/month, setup `{TBD}` |
| 6 | Other product add-ons | Product | Only under the release rule | Priced when released |
| 7 | Annual plan | Terms | Month 3 | $1,970/location/year, setup credited |
| Anchor | Three or more locations | Service | "Book a call" bumper | Quoted per location |

**Why per location:** each location is its own profile, photo, setup, and request stream, and it grows with the customer (value metric score 8.9 of 10). **Why not $97 to $149:** at a $350 CAC, payback is 3.6 months at $97 against 1.8 at $197, and setup labor costs the same at any price.

**Release rule for a held product item,** all five true: asked for by at least two paying clients unprompted; visible in their own data; delivered done-for-you; a support playbook exists with a time cap; priced as an add-on to the service.

**ROI anchors (arithmetic for the buyer, never a promise).** Year-one cost of the Review Engine: $2,663. One average plumbing job ($338) covers 1.7 months; one HVAC repair ($350) covers 1.8 months. Breakeven: about 7.9 plumbing jobs a year. Funnel planning numbers: $574 cash per buyer at purchase, $216 monthly recurring per buyer, CAC payback 1.8 months front-end only.

---

## 12. Positioning statement

**Category:** Done-for-you Google review management for local service businesses.
**Niche:** Owner-led home-service shops that already keep customer records in job software.

Rempo can lead the review category for busy home-service owners by competing on effort, not features. Every tool, from the free Google link to Podium, leaves someone at the shop running the program. Rempo runs it, from the jobs the shop already logs, and sells it the way the tools sell: a published price, bought online.

**Against review software:** Not another review tool you have to run. Rempo connects to the software you already log jobs in and runs your review program for you.
**Against agencies and bundles:** Not a marketing package with a review tool inside. Rempo runs one thing, your Google reviews, and shows you the numbers every month.
**Against asking by hand:** Not one more thing to remember after every job.

**The two objections that matter most:**
- "We already have reviews in Jobber." The switch sends requests; nobody owns it. Rempo runs the program: every job asked, a reminder, a reply written for each review, and a monthly report.
- "Why pay $197 when NiceJob is $75?" NiceJob is a tool you run. Rempo is a service that runs. If you want to run it yourself, a tool is cheaper, and we say so.

---

## 13. Customer journey: the one funnel

Self-serve first: a buyer can go from an ad to a paid account without speaking to anyone. Bumpers catch the buyers who need a person or are not ready.

| Step | What the buyer meets | Calls to action | Bumper |
|---|---|---|---|
| 1. Entry | Meta or Google ad, retargeting, nurture email | "Watch how it works"; "Take the scorecard" | |
| 2. VSL page | Video; what you do once and what we do; sample request and reply; price, setup, guarantee on one screen; FAQ | Primary "Get started"; "Book a 15-minute call"; "Not ready? Take the scorecard" | Exit intent offers the scorecard |
| 3. Checkout | Three qualifier questions, payment, GBP Tune-Up order bump | "Complete purchase" | No software or 3+ locations: to a call. Abandoned: emails at 1 hour and 1 day |
| 4. Upsell | GBP Upkeep, one click | "Add it" or "No thanks" | |
| 5. Thank-you | Onboarding booking and the access checklist | "Book my onboarding call" | Not booked in 24 hours: reminder, then a call |
| 6. Setup | Software connected; email requests start; texts once registration clears | | Client-side stall: reminder at day 3 |
| 7. First 30 days | Requests, replies, first monthly report | "Book your 30-day review" | No jobs coming through in 14 days: check the connection |
| 8. Account upsells | 30-day review with profile, site, and call data | Website; receptionist if missed calls show | |
| Side loop | Scorecard, Gap Report, four-email nurture, monthly email | "See it run for you"; "Book a call" | |

**Why a paid start instead of the free trial (PLANNED).** The trial means setup labor before payment, a "free" claim that needs the fee beside it (FTC, 16 CFR Part 251), and texting registration that can use half the trial. The trial returns only if checkout conversion is the measured bottleneck.

**Critical success factors:** days to first request; the software connection; the office manager's first week (nothing new to do); a monthly report that makes invisible work visible.

**Activation blockers between payment and the first request:** the software connection, Google profile access, the team photo, texting registration (A2P 10DLC, about a week, vendor estimate; email starts first), and consent wording for texts (counsel).

---

## 14. Campaign and asset plan

**Three campaigns into one funnel core.**

1. **Meta ads (primary).** Creates demand; sends it to the VSL page or the scorecard. Hooks under test: A "We run your Google reviews from your job software." B "Here's what your customer sees." C "Every review answered, every job asked." Plus the scorecard lead ad: "Most customers look for reviews from the last three months. How do yours look?" (BrightLocal 2026).
2. **Google Search ads (secondary).** Problem terms go to the scorecard; solution terms to the VSL page; comparison pages ("Rempo or NiceJob") with dated, sourced facts. Competitor names as keywords only, never in ad text.
3. **Nurture and retargeting (the middle of the funnel).** Scorecard opt-ins and VSL visitors get four emails, then one useful email a month, and retargeting until they buy, book a call, or leave.

**Funnel core:** VSL (5 to 8 minutes, recorded by the founder); VSL page; FAQ; sample request to your phone; checkout with qualifier and bump; one-click upsell page; thank-you and booking; call booking page; sales call guide. All PLANNED.

**The hire:** media buyer plus research strategist at $900/month, not the $2,400/month creative agency. The strongest creative is the product itself: a phone receiving a personalized request.

**The 90-day experiment ($15,000, recommended):** Meta $6,000; Google Search $2,400; media buyer and strategist $2,700; creative $1,800; tools $600; reserve $1,500. Gates at days 30, 60, 90. Front-end CAC bands: green $591 or less, yellow $591 to $1,182, red above $1,182; the founder's $350 working CAC is the stretch goal. Success at day 90: blended paid CAC in green, self-serve share at or above its floor, median days to first request of 7 or fewer, month-2 retention at or above its floor. Detail: `reference/experiment-90-day.md`.

**Later, not in the 90 days:** field-service app marketplaces, SEO comparison pages ranked, partnerships with trade groups and web designers.

---

## 15. Quick-reference execution cheatsheet

- **One-line positioning:** Rempo runs your Google reviews for you. Every job asked, every review answered.
- **Supporting line:** Connected to the job software you already use, live within a week, month to month (the last two PLANNED).
- **Brand promise:** Every customer asked, every review answered, and you never have to run it.
- **Flagship differentiator:** done for you, from the client's own job data.
- **The picture:** the personalized request on a phone. Never a claimed lift.
- **Table stakes:** automated requests, follow-ups, replies, monitoring, the monthly report.
- **Top-of-funnel hook:** the Review Engine Scorecard and the Google Review Gap Report.
- **Audience:** one ICP; the owner buys, the office manager uses.
- **ICP:** owner-led HVAC and plumbing shops, 1 to 2 locations, jobs in Jobber, Housecall Pro, or similar.
- **Proof points on file:** none. Market facts only with the source named.
- **Primary rivals:** NiceJob (price), the Jobber review switch (default), Footbridge Media (bundle).
- **Channels in:** Meta, Google Search, the VSL page and checkout, nurture email to opt-ins, retargeting.
- **Channels out:** cold email, LinkedIn outreach, LinkedIn Ads, cold calls or texts to prospects.
- **Prices you may state today:** the live page only, with the setup fee beside any "free". The Run 2 offer is PLANNED.
- **Never:** promise reviews, ratings, rankings, calls, or jobs; claim a lift for personalized requests; name staff in request copy; say "24/7 Support", "geotag", or "Google Search Boost".
- **Always:** cite the source of a statistic in the same sentence; label samples; one call to action per asset section; no em dashes.

---

*End of the Rempo GTM master context. This file is the single source of truth. When status changes, update the relevant ledger in `rules/` first, then this file, then `ops/decisions.md`, then downstream copy.*
