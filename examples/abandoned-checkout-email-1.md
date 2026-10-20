# Example, abandoned checkout email 1 (the live test)

Status: DRAFT, written from the brain on 2026-10-19 as the Phase 9 live test, pending founder approval.
Audience: the owner who started checkout, gave an email with consent, and did not finish. Stage: purchase decision (step 3 in `../reference/customer-journey.md`). Template: the abandoned-checkout section of `../templates/nurture-email.md`. Sent 1 hour after the checkout started.

---

**Subject:** Anything we can answer before you start?
**Preview:** What happens after you buy, and a call link if you'd rather talk.

Hi [first name],

You started setting up Rempo earlier today and didn't finish. No problem. Here's what happens after you buy, so there are no surprises.

You do four things once: connect your job software, give us access to your Google profile, send one team photo, and confirm your texting details. Our team does the rest. We build your request with your team's photo and each customer's first name, send it after every completed job with one reminder, and write a reply for every review.

If you stopped on a question, it's probably one of these: which software we connect to, what the setup fee covers, or whether texts will bother your customers. The answers are here: [FAQ link]

If you'd rather ask a person, book a 15-minute call with [founder name]: [call link]

[Finish getting started]
`[OFFER PENDING]` price, setup fee, and guarantee line, once `../ops/decisions.md` marks the offer DECIDED.

[Founder name], Rempo
[unsubscribe]

---

## Why this works
- It opens with what happened and no pressure: no countdown, no "spots left".
- "What you do once, what we do" answers the doubt most likely to stall a done-for-you purchase: how much work it is.
- "After every completed job" follows "connect your job software", so the condition travels with the claim.
- The three likely questions are framed as possibilities, not as a history of buyers Rempo does not yet have.
- One primary action (finish), with the call as a text line, matching the funnel's buy-then-call order.

## QA
Checked: one reader (the owner), funnel stage, banned words, em dashes, claims (no result, no proof point, no lift), status (no software named as supported, the offer line held as `[OFFER PENDING]`), glossary terms, one primary call to action, unsubscribe present. Closest to breaking: a first draft said "Most owners ask us the same few questions", which invents a customer history; it was rewritten.

## What the live test found (logged in `../ops/signal-log.md`)
1. The brain had no template for abandoned-checkout email; the nurture template covered only the scorecard sequence. Patched: an abandoned-checkout section in `../templates/nurture-email.md`.
2. Email consent at checkout was not in the product requirements, though this email depends on it. Patched: requirement 26 in `../reference/product-requirements.md`.
3. The Phase 8 outline puts the guarantee in this email; the guarantee is PLANNED, so the rule held and the line stays `[OFFER PENDING]`. No change needed.
