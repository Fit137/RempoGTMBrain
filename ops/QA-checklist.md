# QA checklist, run before shipping any output

Go through this list against the draft. If any item fails, fix it before shipping, then say which checks you ran. Every item is answerable yes or no by looking at the draft.

## Writing
- [ ] No em dashes or en dashes anywhere.
- [ ] None of the banned words in `rules/writing-rules.md`, or their variants.
- [ ] No banned structures: "It's not just X, it's Y", "In today's fast-paced world", "Whether you're", a rhetorical-question opener.
- [ ] Paragraphs of one to three sentences; specific numbers and named steps over adjectives.
- [ ] Every statistic has its source in the same sentence.
- [ ] Every sample request, reply, report, or screen is labeled as a sample.

## Channel
- [ ] The asset is for a channel this GTM runs: Meta, Google Search, the VSL page and checkout, nurture email to opt-ins, retargeting, the sales call, onboarding, or delivery copy for a client.
- [ ] It is not cold email, LinkedIn outreach, LinkedIn Ads, or a cold call or text to a prospect. If it is, stop and redirect.

## Claims
- [ ] No promise of reviews, ratings, rankings, calls, or jobs.
- [ ] No lift claimed for personalized requests.
- [ ] No customer count, result, testimonial, quote, logo, or case study; `[PROOF POINT NEEDED]` where proof would go.
- [ ] Every capability checked against `rules/feature-status.md`; nothing PARTIAL stated beyond its confirmed part; nothing PLANNED or HELD in the present tense.
- [ ] No Run 2 price, guarantee, or "month to month" unless `ops/decisions.md` marks the offer DECIDED; otherwise the draft is labeled `[OFFER PENDING]`.
- [ ] No job software named as supported unless the ledger confirms it.
- [ ] Any "free" has the setup fee beside it.
- [ ] No "24/7 Support", "Google Search Boost", "geotag", "autopilot", "instant", or "AI employee".
- [ ] Every "only", "first", "best", "never", and "no other" matches a scoped form in `rules/do-not-say.md`.
- [ ] Competitor facts are named, sourced, and dated 2026-10 or later; competitor names appear in search keywords only, never in ad text.

## Naming and strategy
- [ ] Vocabulary matches `rules/glossary.md` (Review Engine, GBP Tune-Up, GBP Upkeep, personalized request, job software, client vs customer).
- [ ] The service leads; no product-layer item appears in an ad, a headline, or the front of the funnel.
- [ ] Nothing contradicts a DECIDED entry in `ops/decisions.md`.

## Audience and stage
- [ ] One reader: the owner (ads, VSL, page), the office manager (onboarding, in-account), or the client's customer (delivery copy).
- [ ] The copy matches its funnel step in `reference/customer-journey.md` and does not jump ahead of it.
- [ ] One primary call to action per section; the same one at the top and bottom of a page.

## Ads (Meta and Google Search)
- [ ] The ad asks or describes; it never asserts a fact about the viewer ("Your reviews are stale").
- [ ] Competitor names appear only as search keywords, never in ad text.
- [ ] The offer line appears only once the offer is DECIDED; otherwise the ad carries no price.
- [ ] Any statistic in the ad or lead form names its source in the same sentence.
- [ ] Problem-term search ads offer the free scorecard, not the product.
- [ ] One idea and one call to action per ad.

## Delivery checks (requests and replies written for a client)
- [ ] Every customer gets the same request; nothing routes only happy customers to Google.
- [ ] No staff name requested, no suggested wording, no star prompt, no incentive.
- [ ] Texts carry an opt-out line and go only to customers with consent on file.
- [ ] Replies answer what the reviewer said, use a first name at most, and never argue or reveal job details.

## Scripts and video
- [ ] Written for the ear and read aloud without stumbling.
- [ ] The hook lands in the first 5 seconds of an ad or 15 seconds of the VSL.
- [ ] Every spoken statistic is on screen with its source.
- [ ] Nothing PARTIAL, PLANNED, or HELD is shown working; "once your software is connected" is said, not dropped.

## Voice
- [ ] Reads like the matching file in `examples/`.

## After shipping
- [ ] Asset filed in `pages/` or listed in `ops/asset-index.md` under live surfaces.
- [ ] Anything the work taught you is logged in `ops/signal-log.md`.
