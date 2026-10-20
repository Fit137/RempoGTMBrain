# Service offer matrix

Load for: any question about what a service produces, how to measure it, or whether a component may be sold. Distills: Phase 0, `dashboards/00-service-offer-matrix.md`, with research Step 0D.

Rempo is service-dominated, so the go-to-market starts from what each service does for the client. The founder's matrix ratings are assumptions; every rating below was checked against research and the founder's rating is kept beside it in the source.

## The 14 vectors every service is scored on

| # | Vector | Question | Scale |
|---|---|---|---|
| 1 | Outcome metric | What number moves for the client? | A named metric |
| 2 | Evidence strength | Does public research show it? | Strong, Moderate, Weak, Not supported |
| 3 | Time to first proof | How soon can the client see something? | Days from purchase |
| 4 | Buyer demand | Does the buyer ask for it by name? | Asked for by name, Recognized when shown, Latent |
| 5 | Differentiation vs software | Can a tool the owner runs do it? | Commodity, Most vendors, A few, Only Rempo |
| 6 | Differentiation vs done-for-you | Can an agency do it? | Same scale |
| 7 | Setup effort | Labor to make it work | Low, Medium, High; hours `{TBD}` |
| 8 | Monthly effort | Labor to keep it working | Low, Medium, High; hours `{TBD}` |
| 9 | Client dependency | What the client hands over | A list |
| 10 | Self-serve fit | Can it be bought from a page? | Page, after a call, after their data shows the need |
| 11 | Market price | What the market charges | A researched range |
| 12 | Funnel role | Where it sits in the one funnel | Free, Front-end, Order bump, One-click upsell, Account upsell, Product add-on, Anchor |
| 13 | Compliance risk | Exposure under Google, FTC, texting rules | Low, Medium, High |
| 14 | Retention role | Does it show value every month? | Every month, Once, Invisible |

## The re-rated matrix (condensed)

| Vector | Review Engine | GBP Tune-Up | GBP Upkeep | Website | Product layer |
|---|---|---|---|---|---|
| Outcome metric | Reviews in last 90 days; profile calls | Completeness; geo-grid rank day 30, 60 | Profile and feed activity | Calls and forms from the site | Answered-call rate |
| Evidence | Strong | Strong | Weak | Moderate | Moderate |
| First proof | About 7 days after the software connection | 1 day; rank 30 to 60 days, if any | First week | 30 to 45 days, `{TBD}` | First week |
| Demand | Asked for by name | Recognized when shown | Latent | Recognized when shown | Recognized when shown |
| Setup / monthly effort | Medium / Low | Low to medium / None | Low / Low | High / Low | Medium / Low to medium plus support |
| Self-serve fit | Page | Page | Page | After a call | After their data shows the need |
| Market price | Software $39 to $125/mo; done-for-you $249 to $600+ | $250 to $750 once | $125 to $500/mo | $1,800 to $4,500 build | $29 to $99/mo |
| Funnel role | Front-end | Order bump | One-click upsell | Account upsell | Product add-on |
| Compliance risk | High | Low | Low | Low | High (AI voice consent) |
| Retention role | Every month | Once | Every month | Once, then invisible | Every month |

## Component verdicts

- **Keep and lead:** automated review request (needs a CRM, so it is a checkout question); review reply (written for each review); custom implementation (the done-for-you promise).
- **Keep, do not claim:** follow-up (test timing); website gallery widget.
- **Keep, show it, test it:** the personalized request. Never claim a lift; never ask customers to name staff.
- **Keep, do not lead:** reviews repurposed to social posts (a retention delight).
- **Keep:** review widget, with no "stars in Google" claim and nothing implying it shows every review.
- **Keep, move to the order bump:** GBP optimization.
- **Keep as an account upsell:** website, home services only, scoped on a call.
- **Reframe:** autoposting to GBP and social (sold as staying current, inside GBP Upkeep); the auto-FAQ (answers on service pages, inside the website).
- **Drop:** geotagging. **Drop as a separate item:** the social scheduler. **Hold:** unified inbox.

## KPI tree

- **Delivery (Rempo controls, may promise):** days to first request; ask coverage (requests ÷ completed jobs with contact details); reply coverage within 48 hours; Tune-Up completeness checklist; Upkeep posts per month.
- **Client outcome (reported against a baseline, never promised):** request-to-review rate split personalized vs plain; reviews in the last 90 days; rating; profile calls, clicks, directions; geo-grid rank (`{DEFERRED: product}`); site calls and forms; answered calls.
- **Business:** retention at months 2, 6, 12; attach rate per add-on; cost to serve per account (time log).

## Baseline at signup (before the first request)

Review count, rating, latest review date, reviews in last 90 days; share of reviews with an owner reply; geo-grid rank for three service keywords; 90 days of profile actions; completed jobs per week; site load time and tracking; consent to compare personalized and plain requests. See [product requirements](product-requirements.md), item 9.

"Better ranking" is the weakest outcome in the founder's matrix. Lead with recency and replies. Status of each service: [`rules/feature-status.md`](../rules/feature-status.md).
