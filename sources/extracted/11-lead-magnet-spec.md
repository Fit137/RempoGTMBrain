# Source: 11_lead_magnet_spec.xlsx

Original path: `sources/raw/google-folder/11_lead_magnet_spec.xlsx`
Type: xlsx
Size: 13,368 bytes

## Sheet: Overview

| Rempo go-to-market  ·  Lead Magnet Specification |
| Overview.  Skill phase: Lead Magnet.  Source: dashboards/lead-magnet-spec.md (Run 2, 2026-10-19). |
| Scorecard overview |
| Element | Specification |
| Scorecard Name | The Review Engine Scorecard: how fresh are your Google reviews? |
| Target ICP | Owners and office managers of home-service shops, HVAC and plumbing first (Phase 4), at both maturity levels |
| Problem it Reveals | Whether asking for reviews is a habit or an accident: how customers are asked, how recent the latest review is, whether replies go out, how the shop compares with its local top three, and how many customers a week go unasked |
| Immediate Value to User | A score out of 100, the three biggest gaps in plain language, and the free Gap Report by email within one business day |
| Conversion Path to Rempo | Scorecard, results page, then by fit: "See it run for you" (VSL page and checkout); "Book a 15-minute call" (questions, no CRM, 3 or more locations); everyone stays in the nurture sequence until they buy or unsubscribe |

## Sheet: Questions

| Rempo go-to-market  ·  Lead Magnet Specification |
| Questions.  Skill phase: Lead Magnet.  Source: dashboards/lead-magnet-spec.md (Run 2, 2026-10-19). |
| Questions |
| Higher score means a bigger gap. Questions 1 and 7 are unscored and used for routing. The five scored questions total 100. |
| # | Question | Answer Options | Scoring Logic | What It Reveals |
| 1 | Where do you log your jobs? | Jobber / Housecall Pro / ServiceTitan / Another CRM with customer phone or email / Paper or spreadsheets | Unscored. Paper or spreadsheets routes to a call (the upload fallback is {DEFERRED: product}) | Whether "after every job" can run without anyone at the shop |
| 2 | How do you ask customers for reviews today? | We don't really ask / When someone remembers / Our technicians ask in person / Our job software sends a request / A review tool sends requests and follow-ups | 25 / 20 / 15 / 8 / 3 | Whether asking is a system or depends on memory |
| 3 | About how many jobs do you complete in a typical week? | Fewer than 5 / 5 to 15 / 16 to 40 / More than 40 / Not sure | 3 / 8 / 12 / 15 / 8 | How many customers go unasked each week if the habit is weak |
| 4 | When did your most recent Google review arrive? | This week / This month / 1 to 3 months ago / More than 3 months ago / Not sure | 0 / 6 / 14 / 20 / 12 | Recency, the gap buyers see first: 74% look for reviews from the last three months (BrightLocal 2026) |
| 5 | Search your main service and your town. How do your reviews compare with the top three shops? | We're ahead / About even / Behind / Far behind / Haven't checked | 0 / 8 / 18 / 25 / 15 | The local gap, and the invitation to the Gap Report |
| 6 | How often do you reply to your Google reviews? | Every review within two days / Most of them / Some of them / Rarely / Never | 0 / 4 / 8 / 12 / 15 | The reply habit: 80% of consumers prefer a business that replies to all reviews (BrightLocal 2026) |
| 7 | How many locations do you operate? | 1 / 2 / 3 to 9 / 10 or more | Unscored. 3 or more routes to a call | Whether the self-serve checkout fits |

## Sheet: Results_Tiers

| Rempo go-to-market  ·  Lead Magnet Specification |
| Results Tiers.  Skill phase: Lead Magnet.  Source: dashboards/lead-magnet-spec.md (Run 2, 2026-10-19). |
| Results tiers |
| Score Range | Tier Name | Message | CTA |
| 0-39 | Steady engine | You ask consistently, and your answers show it. The next gains are in replying to every review and putting your best ones to work on your site and profile. | Soft: "Get your free Gap Report" |
| 40-69 | Leaky engine | Some customers get asked and some don't. At [answer to question 3] jobs a week, that adds up to a lot of customers who were never asked. | Medium: "See how we run it for you" (VSL page), with the offer line |
| 70-100 | Stalled engine | Right now, asking depends on someone remembering on a busy day. That is the part Rempo runs for you, from the software you already use. | Strong: "Get started" (checkout, with the offer line) plus "Book a 15-minute call" |
| Routing overrides: paper or spreadsheets (question 1), or 3 or more locations (question 7), replace the CTA with "Book a 15-minute call", whatever the score. Every tier also offers the Gap Report. |

## Sheet: Email_Sequence

| Rempo go-to-market  ·  Lead Magnet Specification |
| Email Sequence.  Skill phase: Lead Magnet.  Source: dashboards/lead-magnet-spec.md (Run 2, 2026-10-19). |
| Post-scorecard email sequence |
| Email # | Day | Subject Line | Content Focus | CTA |
| 1 | 0 | Your Review Engine score: [score]/100 | Results delivery and interpretation: the three biggest gaps and what each means; the Gap Report is on its way | Watch how it works (VSL page) |
| 2 | 2 | What customers look for in your reviews | Deeper insight. The skill asks for a case study; none exists, so it is {TBD}. Process substitute: what recency and replies mean to a buyer (BrightLocal 2026, cited), plus the reply guide | Get the reply guide |
| 3 | 5 | We'll run it for you. Here's exactly how. | Solution introduction: what Rempo sets up, what the owner does once, the price, setup fee, and guarantee. Three or more locations: an offer to talk | Get started (offer line); Book a call |
| 4 | 8 | Your first requests, 7 days from now | A real reason to start now, not invented urgency: setup takes about a week from the software connection (texting registration is part of it), and the guarantee covers that week | Get started; Book a call |
| After email 4: one useful email a month (Phase 8, Campaign 3), each with the VSL link and the call link. |

## Sheet: Legend

| Rempo go-to-market  ·  Lead Magnet Specification |
| Legend: what the colors mean, and the dropdown lists |
| •  Colors are conditional-formatting rules, not painted cells: change a value, or pick another option from a dropdown, and the color follows. |
| •  Header rows are royal blue. Rempo's own row or column is tinted brand blue, so it is easy to find in every comparison. |
| •  Orange marks the done-for-you service (the front-end offer and its upsells); violet marks the product layer behind it. |
| Colors used in this workbook |
| Looks like | Means | Where |
| Rempo | Rempo's own row or column | Every comparison table |
| {TBD} | Unknown until Rempo has its own data. Never invented. | Any cell; the color clears when the text is replaced |
| {DEFERRED: product} | Depends on what the product team builds | Any cell; listed in 15_gtm_requirements_for_product |
