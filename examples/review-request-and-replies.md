# Example, delivery copy: request, reminder, and three replies

Status: DRAFT, written from the brain on 2026-10-19, pending founder approval.
Audience: a client's customers. Stage: delivery. Templates: `../templates/review-request.md`, `../templates/review-reply.md`.
Everything below is a sample for a fictional client, Maple Street Plumbing (sample), and fictional customers.

---

## Request, text (sample)
Image: the Maple Street team in front of their van, with "Thanks, Dana!" on it.

"Hi Dana, thanks for choosing Maple Street Plumbing today. Would you share an honest review of your visit? It helps neighbors choose. [link] Reply STOP to opt out."

## Reminder, text, after 3 days (sample)
"Hi Dana, a quick reminder from Maple Street Plumbing. If you have a minute, we'd appreciate an honest review. [link] Reply STOP to opt out."

## Request, email (sample)
Subject: Thanks from Maple Street Plumbing
[team image with "Thanks, Dana!"]
Thanks for having us out today. If you have a minute, would you share an honest review of your visit? It helps your neighbors choose a plumber.
[Leave a review]
Maple Street Plumbing, [address]. [unsubscribe]

## Reply to a five-star review (sample)
Review: "Showed up on time, fixed the water heater in an hour, and cleaned up after. Great service." (Sam)

Reply: "Thanks, Sam. Getting your hot water back within the hour is exactly what we aim for, and we're glad the cleanup was noticed too. We're here whenever you need us. The Maple Street team"

## Reply to a three-star review (sample)
Review: "Fixed the leak fine but the first appointment window was missed and nobody called." (Priya)

Reply: "Thanks for the honest review, Priya. You're right that a missed window without a call isn't good enough, and we're sorry for the wait. If you'd like to talk it through, call Maria at our office at [number]. The Maple Street team"

## Reply to a one-star review (sample)
Review: "Way too expensive for what they did." (Chris)

Reply: "Chris, thank you for letting us know. We'd like to understand what happened and go over the work with you. Please call Maria at our office at [number] so we can talk directly. The Maple Street team"

---

## Why this works
- The request asks for an honest review only: no star prompt, no wording, no staff name, no reward.
- The same request goes to every customer; nothing screens out unhappy ones.
- Each reply answers what that reviewer actually said, so no two read alike.
- The negative replies stay calm, admit what the reviewer reported, and move the details off the public page.
- Replies name an office contact the client chose, never blame a technician, and share nothing the reviewer did not.

## QA
Checked against `../reference/review-compliance.md` and the delivery section of `../rules/do-not-say.md`: same request for all, no incentive, no staff naming request, no suggested content, opt-out on texts, unsubscribe on email, one reminder only, replies specific and private-detail free. Closest to breaking: the three-star reply's apology could read as admitting liability; it apologizes for the wait the customer described, nothing more. Approval mode for posting replies is `{DEFERRED: product}`.
