# Snapshot, 2026-10-19, pre-launch baseline

The first capture, taken the day the brain was built and before any spend. It records the starting board so the day-30, day-60, and day-90 snapshots have a "before". Most numbers are zero or `{TBD}`, and that is the finding.

## 1. Funnel
No funnel is live. The VSL, page, checkout, scorecard, and nurture sequence are specified (`reference/customer-journey.md`) and not built.

| Step | Count | vs last snapshot |
|---|---|---|
| Ad clicks, VSL page visits, scorecard opt-ins | 0 | first snapshot |
| Checkout starts, purchases, calls booked | 0 | first snapshot |
| Paying clients | `{TBD}` (none on file) | first snapshot |

## 2. Channels
| Channel | Assigned role | Actual | Verdict |
|---|---|---|---|
| Meta ads | Primary demand, to the VSL page or scorecard | Not started | Starts after week 0 |
| Google Search ads | Capture owners already searching | Not started | Starts after week 0 |
| Nurture and retargeting | The middle of the funnel | Not started | Needs the scorecard live |

## 3. Segments
ICP set: owner-led HVAC and plumbing shops, 1 to 2 locations, jobs in job software. No conversion data yet. Watch at day 30: the share of checkout starts failing the job-software question.

## 4. Wins and losses
None yet.

## 5. Competitive
Slate as of 2026-10: NiceJob $75 to $125/month with a 14-day trial without a card; Jobber's review automation on the $199 Grow plan; Podium reported at about $399 to $599/month on annual terms; Footbridge Media $249/month with review management, no contract, 90-day money-back guarantee. Re-check every one at day 30.

## 6. Product and delivery status
Diffed against `rules/feature-status.md`.

| Capability | Ledger says | Reality | Action |
|---|---|---|---|
| Completed-job trigger in job software | PARTIAL | Supported systems unconfirmed | Product confirms Jobber and Housecall Pro before week 0 |
| Run 2 offer and paid start | PLANNED | Live page still shows three tiers and a free trial | Founder decides; page changes in week 0 |
| "24/7 Support" | DROPPED | Still on the live page | Remove in week 0 |
| Baseline at signup | PLANNED | Not yet recorded for any account | Requirement 9, before the first client |
| Time log per account | Not started | Needed for cost to serve | Starts with the first client |

## 7. What this changes
No ledger change this period. This snapshot establishes the baseline, and the open items it found are already in `ops/decisions.md`.

| Change | Type | Files | Owner | Status |
|---|---|---|---|---|
| Decide the Run 2 offer | Decision | `ops/decisions.md`, `rules/feature-status.md` | Founder | Open |
| Confirm job software at launch | STATUS signal when it lands | `rules/feature-status.md` | Product | Open |
| Fix the live pricing page | Downstream debt | Live page | Founder | Open |

**Ledgers reviewed this snapshot:** `rules/feature-status.md`, `rules/do-not-say.md`, `rules/glossary.md`, `rules/writing-rules.md`. `last_reviewed` set to 2026-10-19 on each.
