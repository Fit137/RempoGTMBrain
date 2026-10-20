# Prompt library, common Rempo GTM tasks

Ready-to-run prompts for the recurring jobs. Each assumes the agent has loaded the router (`CLAUDE.md` or `AGENTS.md`). Copy, fill the brackets, run. Every prompt ends with the QA instruction, because the checklist is the gate.

There is no cold email, LinkedIn, or cold texting in this GTM, so there are no prompts for them. If asked, say the channel is out of scope and offer a Meta ad, a search ad, or a nurture email instead.

---

## Acquisition and the funnel

### Plan the VSL
"Plan the Rempo VSL using hook [A done for you / B here's what your customer sees / C every review answered]. Load `../reference/vsl-funnel-engine.md`, `../reference/value-proposition-owner.md`, and `../templates/vsl-script.md`. Give me the one-sentence takeaway, the beats with timings, the statistics you will cite with their sources, and the sample assets needed. Check `../ops/decisions.md` for the offer status. Do not write the script yet."

### Write the VSL
"Write the full VSL from this plan: [paste plan]. Follow `../templates/vsl-script.md` and match the voice of `../examples/vsl-opening.md`. Write for the ear. Label every sample. If the offer is not DECIDED in `../ops/decisions.md`, write `[OFFER PENDING]` in the offer beat. Then run `../ops/QA-checklist.md`, including the scripts block, and tell me which rule the draft came closest to breaking."

### Write VSL page sections
"Draft the [hero / what you do once / sample request and reply / pillars / what we don't do / price block / FAQ / calls to action] section of the VSL page for the owner. Follow `../templates/vsl-page.md`, use `../ops/copy-bank.md` lines verbatim where they exist, and match `../examples/vsl-page-hero.md`. Mark every PARTIAL or PLANNED capability per `../rules/feature-status.md`. Run `../ops/QA-checklist.md` before returning."

### Write the FAQ
"Write answers to these FAQ questions: [list, or 'the full set']. Use `../templates/faq.md`, `../reference/objection-handling.md`, and the voice of `../examples/faq-answers.md`. Two to four sentences each. Say 'not yet' where the ledger says not yet. Run `../ops/QA-checklist.md`."

### Write Meta ads
"Write [n] Meta ads for hook [A / B / C] in [9:16 video / static / scorecard lead ad] format, for [cold / VSL viewers / scorecard takers / offer reached, no purchase]. Load `../reference/marketing-campaigns.md` and `../templates/meta-ad.md`; match `../examples/meta-ads.md`. One idea and one call to action each. Ask or describe, never assert a fact about the viewer. Label every sample. Run `../ops/QA-checklist.md`, ads block included."

### Write Google Search ads
"Write a responsive search ad set for the [problem / solution / brand / alternative] term group: [keywords]. Follow `../templates/search-ad.md` and match `../examples/search-ads.md`. 15 headlines of 30 characters or fewer, 4 descriptions of 90 or fewer. No competitor names in the text. No review or ranking promise even when the keyword asks for one. Run `../ops/QA-checklist.md`."

### Write a comparison page
"Write the 'Rempo or [NiceJob / the Jobber review feature / asking by hand]' page. Load `../reference/competitor-battlecards.md` and `../reference/competitive-analysis.md`; follow `../templates/comparison-page.md`. Lead with the other option's real strength. Every competitor fact sourced and dated; flag any fact older than 90 days for re-checking. Run `../ops/QA-checklist.md`."

### Write a nurture email
"Write nurture email [1 / 2 / 3 / 4 / monthly: topic] for people who took the Review Engine Scorecard. Follow `../templates/nurture-email.md`, `../reference/lead-magnet-scorecard.md`, and the voice of `../examples/nurture-email-3.md`. Use merge fields [score], [tier], [jobs per week]. One idea, one call to action, no invented urgency. Run `../ops/QA-checklist.md`."

## Sales

### Prepare a sales call
"I have a 15-minute call with [shop name, trade, town]. They came from [VSL page / scorecard, score [n] / checkout route: no software / 3+ locations]. Using `../templates/sales-call-guide.md`, `../reference/icp-personas.md`, and `../reference/objection-handling.md`, give me the fit check, the three objections they are most likely to raise with honest answers, and what I can say about price today per `../rules/feature-status.md`. Run `../ops/QA-checklist.md` on anything I will say aloud."

### Answer an objection
"A prospect said: '[objection, verbatim]'. Draft the honest answer for the owner, grounded in `../reference/objection-handling.md` and `../rules/do-not-say.md`. If the true answer is 'not yet', say not yet. Then log the objection in `../ops/signal-log.md` with its verbatim. Run `../ops/QA-checklist.md`."

### Competitive positioning
"Write positioning against [competitor] for [Level 1: no review system / Level 2: tried a tool and stalled]. Use `../reference/competitor-battlecards.md` and `../reference/positioning.md`. Lead with the vectors Rempo leads (done for you from the client's job software; personal, not templated). Run every superlative through the scoping section of `../rules/do-not-say.md`. Run `../ops/QA-checklist.md`."

## Onboarding and delivery

### Write onboarding emails
"Write onboarding email [1 to 5] for [shop name]'s office manager. Follow `../templates/onboarding-email.md`. The one message: nothing new for you to run. Name only confirmed job software per `../rules/feature-status.md`. Explain the 7-day clock only if the guarantee is DECIDED. Run `../ops/QA-checklist.md`."

### Write review requests for a client
"Write the review request and one reminder, text and email, for [client shop name, trade]. Sender: [name]. Follow `../templates/review-request.md` and `../reference/review-compliance.md`; match `../examples/review-request-and-replies.md`. Same request for every customer, no staff names, no suggested wording, no reward, opt-out on texts. Run the delivery checks in `../ops/QA-checklist.md`."

### Write review replies for a client
"Write replies for these reviews of [client shop name]: [paste reviews with star ratings and first names]. Follow `../templates/review-reply.md`; shop voice: [notes]. Each reply answers what that reviewer said; no two alike; nothing the reviewer did not share; one and two stars move the conversation to [contact]. Run the delivery checks in `../ops/QA-checklist.md`."

### Write the monthly report narrative
"Write [client shop name]'s monthly report narrative for [month] from these numbers: [paste delivery and profile numbers, with the baseline]. Follow `../templates/monthly-report.md`. Keep 'what we did' and 'what your profile shows' separate. Report changes against the baseline without attributing them to Rempo. Run `../ops/QA-checklist.md`."

## Running the brain

### Log a signal
"Log this in `../ops/signal-log.md`: [paste the call note, review, objection, competitor move, or metric]. Keep the verbatim. Classify the type, assign a disposition using the thresholds in that file, and if it is a PATCH or AMEND, route it and tell me exactly which files change."

### Amend a ledger when something ships
"[Jobber connection confirmed by product / the founder marked the offer DECIDED / the guarantee terms cleared counsel / a HELD item met the release rule]. Run the amendment procedure: update `../rules/feature-status.md` (and `../rules/do-not-say.md` if a ban lifts), then the matching section of `../context/Rempo_GTM_Master_Context.md` with a version bump, then a dated entry in `../ops/decisions.md` with what this does not change, then grep `../ops/copy-bank.md`, `../templates/`, and `../examples/` for the old form and update them, then list every live surface in `../ops/asset-index.md` that needs changing. Finally regenerate `../adapters/portable-control-layer.md`."

### Take a snapshot
"Build this period's snapshot in `../snapshots/` from [paste or point at the data]. Fill every section, diff section 6 against `../rules/feature-status.md`, and finish with what this changes, including 'no ledger change this period' if that is the honest answer. Update `last_reviewed` on every ledger examined."

### Run a gate review (day 30, 60, or 90)
"Run Gate [1 / 2 / 3] of the 90-day experiment using `../reference/experiment-90-day.md` and this data: [paste the weekly scorecard]. Compute paid CAC and the payback band (green $591 or less, yellow $591 to $1,182, red above), the self-serve share, median days to first request, and month-2 retention if available. Apply the gate's decision rule exactly as written; do not move the thresholds. Record the result as a snapshot and log any AMEND in `../ops/decisions.md`."

### Audit the brain
"Run `python3 scripts/audit.py` from the repo root, fix every error, then produce one real asset using only the brain and QA it against `../ops/QA-checklist.md`. Report anything the brain could not supply, and log each gap in `../ops/signal-log.md`."

### Regenerate the portable control layer
"Regenerate `../adapters/portable-control-layer.md` from the current `../rules/` files, `../ops/copy-bank.md`, and the master context: audience, positioning, status summary, the closed proof set, the do-not-say table, channels in and out, and the writing rules. Date it today in its header and note it in `../ops/asset-index.md`."
