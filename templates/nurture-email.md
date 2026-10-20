# Template, nurture email

Audience: an owner or office manager who opted in through the scorecard (email consent on the form). Opt-in only. This GTM sends no cold email.
Funnel stage: discovery and evaluation (the side loop in `../reference/customer-journey.md`).
Load first: `../reference/lead-magnet-scorecard.md`. Voice reference: `../examples/nurture-email-3.md`.

## The sequence
| # | Day | Subject | Focus | Call to action |
|---|---|---|---|---|
| 1 | 0 | Your Review Engine score: [score]/100 | The three biggest gaps and what each means; the Gap Report is on its way | Watch how it works |
| 2 | 2 | What customers look for in your reviews | Recency and replies, cited (BrightLocal 2026); the reply guide. No case study exists: use the process substitute | Get the reply guide |
| 3 | 5 | We'll run it for you. Here's exactly how. | What Rempo sets up, what you do once, price and guarantee only as allowed; 3+ locations, an offer to talk | Get started, or book a call |
| 4 | 8 | Your first requests, 7 days from now | A real reason to start: setup takes about a week from the connection. Guarantee only if DECIDED | Get started, or book a call |
| Monthly | | [one useful thing] | The reply guide, the setup week, an FAQ answer | Watch how it works |

Email 4's subject depends on the guarantee. If it is not DECIDED, use: "What your first week with us looks like".

## Each email
- Subject: specific, not clever. What the reader gets.
- Preview text: extends the subject, does not repeat it.
- Opening: one paragraph of value. No "hope you're well".
- Body: one idea. Use their scorecard answers by merge field: [score], [tier], [jobs per week].
- Takeaway: what they can do differently after reading.
- One call to action, plus the call link as a text line in emails 3 and 4.
- Sign-off: the founder's name.

## Abandoned checkout (two emails: 1 hour, 1 day)
Only to buyers who gave an email with consent at checkout (requirement 26). Email 1: "Anything we can answer before you start?", what you do once and what we do, the likely questions with the FAQ link, the call link. Email 2: the same offer, the guarantee only if DECIDED, the call link. No pressure. Example: `../examples/abandoned-checkout-email-1.md`.

## Merge rules
- [jobs per week] comes from scorecard question 3. Fallback: "every week".
- Paper or spreadsheets (question 1), or 3 or more locations (question 7): the CTA becomes "Book a 15-minute call".

## Guardrails
No invented urgency, no countdowns, no "spots left". No result promised. No proof points; `[PROOF POINT NEEDED]` where a case study would go. Every statistic sourced. Unsubscribe in every email. Check `../rules/do-not-say.md`, `../rules/feature-status.md`, `../rules/glossary.md`, `../rules/writing-rules.md`, then `../ops/QA-checklist.md`.
