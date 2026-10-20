# Lead magnet: the Review Engine Scorecard

Load for: the scorecard build (ScoreApp), its results copy, the Gap Report, and the four-email nurture. Distills: `dashboards/lead-magnet-spec.md` and Step 1.6. Status: PLANNED.

The middle-of-funnel asset the founder asked for: something a buyer who is not ready can consume, with an opt-in that puts them on the email list.

## Overview

| Element | Specification |
|---|---|
| Name | The Review Engine Scorecard: how fresh are your Google reviews? |
| For | Owners and office managers of home-service shops, HVAC and plumbing first, both maturity levels |
| Reveals | Whether asking is a habit or an accident: how customers are asked, the latest review date, the reply habit, the gap to the local top three, customers a week who go unasked |
| Immediate value | A score out of 100, the three biggest gaps in plain words, and the free Gap Report by email within one business day |
| Path | Results page routes by fit: ready to the VSL page; questions, no software, or 3+ locations to a call; everyone to nurture until they buy or unsubscribe |

## Questions (higher score means a bigger gap; Q1 and Q7 unscored, for routing)

| # | Question | Options | Points |
|---|---|---|---|
| 1 | Where do you log your jobs? | Jobber / Housecall Pro / ServiceTitan / Another CRM with phone or email / Paper or spreadsheets | Unscored. Paper routes to a call |
| 2 | How do you ask customers for reviews today? | Don't really ask / When someone remembers / Technicians ask in person / Job software sends a request / A review tool sends requests and follow-ups | 25 / 20 / 15 / 8 / 3 |
| 3 | About how many jobs do you complete in a typical week? | Fewer than 5 / 5 to 15 / 16 to 40 / More than 40 / Not sure | 3 / 8 / 12 / 15 / 8 |
| 4 | When did your most recent Google review arrive? | This week / This month / 1 to 3 months ago / More than 3 months ago / Not sure | 0 / 6 / 14 / 20 / 12 |
| 5 | Search your main service and your town. How do your reviews compare with the top three shops? | Ahead / About even / Behind / Far behind / Haven't checked | 0 / 8 / 18 / 25 / 15 |
| 6 | How often do you reply to your Google reviews? | Every review within two days / Most / Some / Rarely / Never | 0 / 4 / 8 / 12 / 15 |
| 7 | How many locations do you operate? | 1 / 2 / 3 to 9 / 10 or more | Unscored. 3+ routes to a call |

Why Q4 and Q6 matter: 74% of consumers look for reviews from the last three months; 80% prefer a business that replies to all reviews (BrightLocal 2026).

## Results tiers

| Score | Tier | Message (approved, in `ops/copy-bank.md`) | CTA |
|---|---|---|---|
| 0-39 | Steady engine | You ask consistently. The next gains are replying to every review and putting your best ones to work | Soft: "Get your free Gap Report" |
| 40-69 | Leaky engine | Some customers get asked and some don't. At [Q3 answer] jobs a week, that adds up | Medium: "See how we run it for you" |
| 70-100 | Stalled engine | Asking depends on someone remembering on a busy day. That is the part Rempo runs for you | Strong: "Get started" plus "Book a 15-minute call" |

**Routing overrides:** paper or spreadsheets (Q1) or 3+ locations (Q7) replace the CTA with "Book a 15-minute call", whatever the score. Every tier also offers the Gap Report.

## Google Review Gap Report

The business against its local top three for its main service: reviews in the last 90 days, latest review date, rating, reply coverage, and the arithmetic of asking every customer at their job count. Public data only; no promise. Built by the assistant within one business day; automation through Google's official APIs is `{DEFERRED: product}`.

## Post-scorecard emails

| # | Day | Subject | Focus | CTA |
|---|---|---|---|---|
| 1 | 0 | Your Review Engine score: [score]/100 | The three biggest gaps and what each means; the Gap Report is on its way | Watch how it works |
| 2 | 2 | What customers look for in your reviews | Case study `{TBD}`; process substitute: what recency and replies mean to a buyer (BrightLocal 2026), plus the reply guide | Get the reply guide |
| 3 | 5 | We'll run it for you. Here's exactly how. | What Rempo sets up, what the owner does once, the price, setup fee, and guarantee; 3+ locations: an offer to talk | Get started; Book a call |
| 4 | 8 | Your first requests, 7 days from now | A real reason to start now: setup takes about a week from the software connection, and the guarantee covers it (PLANNED) | Get started; Book a call |

After email 4: one useful email a month (the reply guide, the 7-day setup, an FAQ answer), each with the VSL link and the call link.

## Build notes

Email consent on the form, and a plain statement of what is done with the answers. No incentive linked to reviews, anywhere. Answers to Q1, Q3, and Q7 pass into checkout so a buyer is not asked twice (requirement 2 in [product requirements](product-requirements.md)). Email 3 and 4 carry the offer only once DECIDED.
