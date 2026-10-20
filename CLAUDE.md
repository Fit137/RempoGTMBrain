# Rempo GTM, agent entry point

This repository is the Rempo go-to-market brain. You are an AI agent working inside it. Read this file, then follow its pointers. Do not improvise strategy that is already decided here.

## Read before any customer-facing output
1. `context/Rempo_GTM_Master_Context.md`, the full strategy, ICP, positioning, offer, funnel, and campaigns. Source of truth.
2. `rules/writing-rules.md`, how every word is written, including writing for the ear.
3. `rules/do-not-say.md`, the claims you must never make and their safe replacements.
4. `rules/feature-status.md`, what is LIVE, PARTIAL, PLANNED, HELD, or DROPPED. Check before describing any capability, price, or term.
5. `rules/glossary.md`, the canonical names.

## This GTM is one self-serve funnel, service in front
Rempo is a done-for-you Google review service for home-service shops, sold online. Ads lead to one VSL page; the buyer purchases at checkout, or takes one of two bumpers: book a 15-minute call, or take the Review Engine Scorecard and enter nurture. Product add-ons come later, inside the same funnel, and never lead.

The channels are Meta ads, Google Search ads, the VSL page and checkout, email nurture to opt-ins, retargeting, the sales call, onboarding, and delivery copy written for clients. There is no cold email, LinkedIn outreach, LinkedIn Ads, or cold calling or texting of prospects; refuse those and offer the nearest channel that is in.

For anything in the funnel, load `reference/vsl-funnel-engine.md` first. For delivery copy (requests and replies for a client), load `reference/review-compliance.md`.

## Know the reader first
One ICP and one message, three readers. Never blend them in one asset.
- The owner of an HVAC or plumbing shop, 1 to 2 locations, jobs in job software: ads, the VSL, pages, the sales call.
- The office manager: onboarding, in-account email, the monthly report.
- The client's customers: review requests and replies Rempo writes for the client.

## Non-negotiables (short version, full detail in rules/)
- Claim the process, never a result. No promised reviews, ratings, rankings, calls, or jobs.
- The proof set is empty. No customer counts, results, testimonials, quotes, or logos. Write `[PROOF POINT NEEDED]`.
- The Run 2 offer ($197 per location, the 7-day guarantee, month to month, add-on prices) is PLANNED. Label drafts `[OFFER PENDING]` until `ops/decisions.md` marks it DECIDED.
- Name no job software as supported until the ledger confirms it.
- Same request to every customer: no filtering, no incentives, no staff names, no suggested wording.
- Every statistic carries its source in the same sentence. Samples are labeled.
- No em dashes. None of the banned words in `rules/writing-rules.md`.

## Before you ship
Run `ops/QA-checklist.md` against the draft, item by item, and say which checks you ran. Use `ops/copy-bank.md` lines verbatim where one fits. Ready-made prompts: `prompts/common-tasks.md`.

## When something changes
A new signal from a lead, client, competitor, or platform goes in `ops/signal-log.md` first. If it changes a rule, follow the amendment procedure in `ops/review-cadence.md`: ledger, master context, `ops/decisions.md`, copy, then the portable control layer. Never the other way around. Audit with `python3 scripts/audit.py`.

The GTM Brain skill that built and maintains this repo is installed at `.claude/skills/go-to-market-brain/` (run `/go-to-market-brain`), with `.claude/skills/gtm-slop-filter/` for copy rules.
