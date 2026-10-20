# Feature matrix

Load for: deciding which feature leads a message, which is table stakes, and what the top-of-funnel hook is. Distills: Phase 1, `dashboards/01-product-feature-matrix.md`.

26 features scored on demand (x) and competitiveness (y), each from -20 to +20. The founder's "Wanted by Most" ratings were re-tested with the asked-for test: buyers ask for "Google" and "reviews", not for posts, geotags, or FAQ widgets.

## Quadrants

| Quadrant | Features (demand, competitiveness) | How copy treats them |
|---|---|---|
| **Q1 Hero** | 7 Done-for-you implementation (9.4, 7.1). Borderline: 9 Google Business Profile optimization (6.6, 2.3); 18 AI voice receptionist (5.9, 4.2) | Lead. Done for you is the headline |
| **Q4 Table stakes** | 1 Automated requests from job data (16.8, -5.9); 4 Replies written for each review (7.4, -2.7); 2 Follow-ups (5.2, -6.8); 8 Monitoring, alerts, monthly report (4.1, -8.2) | Must work and be shown. Never the headline on its own |
| **Q2 Differentiators** | 3 Personalized visual request (-3.1, 7.6); 26 Video testimonial requests (-6.9, 4.9, not built); 5 Social posts from reviews (-1.9, 3.8). Weak: 13 auto-FAQ, 24 referrals, 14 gallery widget, 21 reactivation, 25 listings, 10 and 11 autoposting | Show, do not claim. The personalized request is the picture |
| **Q3 Commodities** | 6 Review widget (-4.4, -13.6); 15 Website build; 16 Unified inbox; 17 Social scheduler; 19 Booking; 22 Chat; 12 Geotagging (-12.7, -6.1); 20 Pipeline (-14.8, -7.4); 23 Surveys (-13.2, -4.6) | Never lead. Surveys carry gating risk |

## What this means for messaging

- **Lead with the hero:** "Rempo runs your Google reviews for you." The work gone is what owners want, and only one alternative in the set does setup for the buyer.
- **Prove it with table stakes done well:** every job asked, every review answered with a reply written for that review. Quality, not presence, is the difference.
- **Use the differentiator as the picture:** the request with the team's photo and the customer's first name, on a phone, labeled as a sample.
- **Keep the product layer out of ads.** Only the receptionist has a documented problem behind it (home services missed 14% of calls, CallRail January 2025).

Status of every feature: [`rules/feature-status.md`](../rules/feature-status.md). Tiers and prices: [pricing and packaging](pricing-and-packaging.md).

## Validation applied

- "Wanted by some" excludes "Most vendors": the widget, inbox, and scheduler moved to Commodity (free in GoHighLevel, Podium, and most review tools).
- "Wanted by one" excludes "Commodity": geotagging moved to "Most vendors can do this".

## Demand driver: the top-of-funnel hook

**The Review Engine Scorecard plus the Google Review Gap Report.** Seven questions in about two minutes, an instant score, and the three biggest gaps. The opt-in requests a Gap Report: the business against the three competitors that appear first for its main service in its area.

- **Why it works:** it turns "we should get more reviews" into a number (customers finished each week who were never asked; weeks since the last review). 74% of consumers look for reviews from the last three months (BrightLocal 2026), so recency is a gap the owner can check in a minute.
- **ICP fit:** it asks which job software they use and how many jobs a week, the two facts that decide fit.
- **Routing:** ready buyers to the VSL page; questions or 3+ locations to a call; everyone else to nurture.
- **Delivery:** the Gap Report starts manual (the assistant, within one business day). Automation through Google's official APIs is `{DEFERRED: product}`.

## Variants

| Variant | Perceived value | Ease | Use |
|---|---|---|---|
| Google Review Gap Report | High | Medium | Scorecard results page; nurture |
| Sample request to your phone | High | Medium | VSL page, labeled as a sample |
| Founder video audit (5-minute screen recording) | High | Hard | High-fit scorecard leads who do not buy in 7 days |
| Review Engine Scorecard | Medium | Easy | Meta, Search, VSL page exit |
| Reply guide for home-service owners | Low | Easy | Nurture email 2, retargeting |

Spec: [lead magnet scorecard](lead-magnet-scorecard.md).
