# The 90-day experiment

Load for: budget questions, weekly reporting, gate reviews at days 30, 60, 90, and any "should we scale or stop" call. Distills: Phase 10, `dashboards/10-90-day-experiment.md`. Allocations are recommendations (OPEN in `ops/decisions.md`); thresholds come from Rempo's own prices, not outside benchmarks.

## What it has to prove

1. Home-service owners buy a done-for-you review service from a VSL page without a call, at $197 a month plus setup.
2. What a paying customer costs, against the $350 working CAC.
3. Which hook leads: done for you, the personalized request, or every review answered.
4. How much the bumpers carry: purchases via a call or the scorecard rather than straight from the page.
5. Whether the CRM gate costs too many sales.
6. Whether personalized requests beat plain ones, and when to send the first ask, inside real accounts.

## The $15,000 allocation

| Line | Month 1 | Month 2 | Month 3 | Total | Share |
|---|---|---|---|---|---|
| Meta ads (VSL, scorecard, retargeting) | $1,500 | $2,000 | $2,500 | $6,000 | 40% |
| Google Search ads | $800 | $800 | $800 | $2,400 | 16% |
| Media buyer plus research strategist | $900 | $900 | $900 | $2,700 | 18% |
| Creative: VSL edit, ad videos | $1,000 | $400 | $400 | $1,800 | 12% |
| Tools: scorecard, geo-grid tracker, call recording | $200 | $200 | $200 | $600 | 4% |
| Reserve: scale the winning hook after day 60, or fund founding-cohort setup credits | $0 | $0 | $1,500 | $1,500 | 10% |
| **Total** | **$4,400** | **$4,300** | **$6,300** | **$15,000** | **100%** |

Not funded: the creative agency ($7,200, 48% of the budget); SEO at $500/month (results arrive after the window); the product layer.

## Week 0, before any spend

The offer goes live (one plan card, add-ons, "book a call" for 3+ locations, paid start and guarantee, "24/7 Support" removed). The funnel core exists. Tracking events from ad click to first request sent, UTM tags on every ad. Proof capture: the permission clause in the terms, the baseline, consent for the request-style comparison. Founder call capacity per week `{TBD}`. Decision floors set before day 1, not after seeing data: month-2 retention `{TBD}`, self-serve share `{TBD}`.

## Tests (one variable each)

| Test | Variants | Measure | Runs |
|---|---|---|---|
| Hook | A done for you / B the personalized request / C every review answered | Cost per purchase; VSL completion to the offer | Meta, weeks 1 to 6 |
| Entry | Ads to the VSL page vs ads to the scorecard first | Cost per purchase within 30 days of first click | Meta, weeks 3 to 10 |
| Request style | Personalized vs plain, alternating by customer in consenting accounts; every customer still asked | Request-to-review rate against the baseline | Inside accounts, 30 days |
| First-ask timing | Same day vs day 3 | Request-to-review rate | After the style test |
| Start | Paid start (default) vs a 15-day trial, only if the gate trips | Checkout conversion; refunds; unpaid setup hours | From day 60, if triggered |

## Bands and gates

| Band | Payback | Front-end CAC |
|---|---|---|
| Green | 3 months or less | $591 or less |
| Yellow | 3 to 6 months | $591 to $1,182 |
| Red | More than 6 months | More than $1,182 |

The $350 working CAC sits inside green; reaching it is the stretch goal. Judge an ad set only after about $700 of spend.

| Gate | Day | Decision rule |
|---|---|---|
| 1 | 30 | Red, or no purchase after $1,500 in a channel: change the hook or the VSL opening first. CRM-question failures above `{TBD}`: name the supported software in every ad |
| 2 | 60 | Red channel: stop it, move its budget. Green and at or below $350: scale with the reserve. High checkout starts, low purchases, price or trial named in abandoned-checkout replies: run the Start test |
| 3 | 90 | Success and stop criteria below |

**Success at day 90 (all four):** blended paid CAC in green; self-serve share at or above its floor; median days from software connection to first request of 7 or fewer; month-2 retention of cohort 1 at or above its floor.
**Stop paid media** if no channel reaches yellow by day 60: put the rest into the founding cohort and the list, rework the VSL and offer.
**Stop selling without a call** if self-serve share is below half its floor at day 60 and call-to-purchase is green: "Book a call" becomes the primary CTA until the page is reworked.

## Capacity rule

When booked onboarding and sales calls reach the founder's weekly cap, stop increasing ad spend and route overflow to assistant-led onboarding (a recorded walkthrough plus a call with the assistant).

## Weekly scorecard

Spend by channel; CTR; cost per VSL visit; VSL completion; clicks per CTA; checkout starts; qualifier failures; purchases; self-serve share; bump and upsell take; calls booked, held, converted; scorecard opt-ins and purchases from the list; paid CAC and band; onboarding booked within 24 hours; days to first request; ask and reply coverage; request-to-review by style and timing; month-2 retention; founder hours on calls. Captured monthly in `snapshots/`.
