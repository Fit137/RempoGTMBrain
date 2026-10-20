# Product requirements from GTM

Load for: knowing which `{DEFERRED: product}` marker blocks which claim, and what must be true before the experiment spends money. Distills: `dashboards/gtm-requirements-for-product.md`. It states what the go-to-market needs; it does not design the product.

**Priority:** Before = before the 90-day experiment spends money. During = inside the 90 days. After = before the add-on it belongs to is sold. When an item ships, update [`rules/feature-status.md`](../rules/feature-status.md) first, then the copy it unblocks.

## Before

| # | What GTM needs to be true | Copy it unblocks |
|---|---|---|
| 1 | A request fires on a completed job, at launch for Housecall Pro and Jobber at least, with an upload or form fallback | "After every job"; naming supported systems; RTB 1.2 |
| 2 | Checkout asks the three qualifier questions, sells per location, offers the Tune-Up bump and Upkeep upsell, and takes scorecard answers | The offer line; the scorecard-to-checkout path |
| 3 | Timestamps for software connected and first request sent, per account | The 7-day process guarantee |
| 4 | Email requests can start before texting registration clears | "Email requests can start right away" |
| 5 | Every customer gets the same Google request: no filtering, no incentives, no staff naming, no suggested wording | "Every customer asked the same way, under Google's rules" moves from PARTIAL to LIVE |
| 6 | Text consent captured and stored per customer contact | Any texting claim in delivery copy |
| 7 | Replies written for each review, approval or automatic mode set per account | Naming the reply mode ("approved by you" or "posted for you") |
| 8 | A team photo and image template per business; first-name fallback | The personalized request in every ad and the VSL |
| 9 | The baseline recorded at signup and tracked | "Your numbers on day one"; every future result claim |
| 10 | Funnel events tracked from VSL view to first request | Reading the gates |
| 11 | The website display never implies it shows all reviews; no stars-in-Google claim | The widget line in VP 3 |
| 12 | A GBP Tune-Up checklist with a before-and-after record | Selling the order bump |
| 13 | Support hours and response times defined, replacing "24/7 Support" | Any support claim |
| 26 | Checkout captures email consent before payment, so an abandoned checkout can be followed up (added by the 2026-10-19 live test) | The abandoned-checkout emails |

## During

| # | What GTM needs to be true | Copy it unblocks |
|---|---|---|
| 14 | Requests alternate personalized vs plain and same-day vs day-3, tracked by variant | The only route to a number for the personalized request |
| 15 | Monthly report and weekly summary against the baseline | VP 3; the weekly summary email |
| 16 | Profile calls, clicks, directions pulled monthly where access allows | "Calls from your profile" in the report |
| 17 | Geo-grid rank for three service keywords recorded monthly | "We track your position" |
| 18 | Customers who already reviewed are not asked again, even with slightly different names | The double-request answer to "we already have Jobber" |
| 19 | Social posts from reviews need approval and quote reviewers by first name only | RTB 3.2 |
| 20 | GBP Upkeep keeps a posting log and adds no geotags | Selling Upkeep |
| 21 | Setup and monthly hours logged per account, by task | Gross margin; capacity rule; offer revisit triggers |

## After

| # | What GTM needs to be true | Copy it unblocks |
|---|---|---|
| 22 | Website template with a page per service and reviews built in; call tracking and form events | Selling the website on its outcome metric |
| 23 | The receptionist reports answered and missed calls; outbound AI calls have a consent design | Selling the receptionist |
| 24 | Product add-ons log support requests and minutes per account | The support guardrail in [offer architecture](offer-architecture.md) |
| 25 | The Gap Report generated through Google's official APIs within their terms | Automating the demand driver |

Until an item ships, the copy it unblocks stays `{DEFERRED: product}`, PARTIAL, or omitted. Track open items in [`ops/decisions.md`](../ops/decisions.md) under "Open, owned elsewhere".
