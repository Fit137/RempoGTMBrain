# Rempo GTM, agent entry point

Cross-tool entry file. Codex, Cursor, Zed, opencode, and most newer agents read `AGENTS.md`, so this is the widest door into this brain. Kept identical in intent to `CLAUDE.md`. If the two differ, `CLAUDE.md` wins.

Working in a tool that reads neither, or in a chat window with no file access? See `adapters/`.

## Start here
1. `context/Rempo_GTM_Master_Context.md`, the full go-to-market. Source of truth.
2. `rules/writing-rules.md`, house writing rules.
3. `rules/do-not-say.md`, claim hygiene and safe replacements.
4. `rules/feature-status.md`, LIVE, PARTIAL, PLANNED, HELD, DROPPED.
5. `rules/glossary.md`, canonical names.
6. `reference/vsl-funnel-engine.md` for any funnel asset; `reference/review-compliance.md` for delivery copy.

## Channel discipline
In: Meta ads, Google Search ads, the VSL page and checkout, nurture email to opt-ins, retargeting, the sales call, onboarding, delivery copy for clients. Out: cold email, LinkedIn outreach, LinkedIn Ads, cold calls or texts to prospects.

## One ICP, three readers, never blended
The owner (ads, VSL, pages, calls); the office manager (onboarding, monthly report); the client's customers (review requests and replies).

## Non-negotiables
Claim the process, never a result. The proof set is empty. The Run 2 offer is PLANNED: label drafts `[OFFER PENDING]`. Name no job software as supported until the ledger confirms it. Same request to every customer, no incentives, no staff names, no suggested wording. Statistics carry their source. No em dashes.

## Before shipping
Run `ops/QA-checklist.md`. Prompts: `prompts/common-tasks.md`.

## Compounding
New market input goes to `ops/signal-log.md`. Rule changes follow the amendment procedure in `ops/review-cadence.md`: ledger, master context, decision log, copy, portable control layer. Audit: `python3 scripts/audit.py`.

<!-- gtm-brain:begin -->
## Go-to-Market Brain

For any go-to-market work in this project, read `.claude/skills/go-to-market-brain/SKILL.md` first and follow
its procedure instead of improvising a method it already defines.

It routes to three modes:

- **BUILD**, turn source material (dashboards, decks, positioning docs) into a governed context repository.
- **UPDATE**, take a signal from a lead, customer, or competitor, or a periodic snapshot, triage it, and route it to the right ledger.
- **OPERATE**, produce, check, and ship an asset against a brain that already exists.

Open the reference file `SKILL.md` names for the mode you are in at the point you need it,
rather than reading the whole skill up front.

If this project already contains a built brain, load its entry file and its `rules/` layer
before writing anything customer-facing. Never describe an unshipped capability as live,
never invent a number or a customer, and run the brain's `ops/QA-checklist.md` against a
draft before returning it.

For copy rules alone, with no brain in play, read `.claude/skills/gtm-slop-filter/SKILL.md`.
<!-- gtm-brain:end -->
