# Signal log

Raw market input, captured before judgment. Every signal from a lead, prospect, client, competitor, platform, or channel lands here first, whatever it turns out to mean. Newest at the top.

**Keep the verbatim.** Do not paraphrase a buyer into house vocabulary. The words a real owner used before we taught them ours are the most valuable thing a signal carries.

## How to use this file

**Types:** OBJECTION, LANGUAGE, PROOF, STATUS, COMPETITIVE, SEGMENT, CHANNEL, LOSS, RISK.

**Dispositions:**
- `NOISE`, one instance, no pattern, no action. Logged and closed.
- `WATCH (n/N)`, a plausible pattern awaiting corroboration. Increment as instances arrive.
- `PATCH`, changes copy but not strategy. Route it, edit, done. No decision entry.
- `AMEND`, changes a ledger, a position, or a rule. Follow the amendment procedure in `ops/review-cadence.md` and write a `ops/decisions.md` entry.

**Corroboration thresholds** (agreed 2026-10-19, see `review-cadence.md`):

| Signal class | Threshold to act |
|---|---|
| Opinion, preference, language, objection | 3 independent instances within 60 days |
| Verifiable fact: status, proof, competitive, risk | 1 verified instance, act immediately |
| Loss reason | 2 instances, or 1 if the shop was in the core ICP (HVAC or plumbing, 1 to 2 locations, job software) |
| Channel performance | A full measurement cycle (a funnel gate), never a single week |

Default disposition is NOISE. Triage runs weekly on Monday. A WATCH item that has not incremented in two cycles expires to NOISE, and the expiry is written here.

---

## Entries

The first entries were captured during the build (2026-10-19) from the research and the founder's materials. Each records the event date in its context line.

### 2026-10-19 | STATUS | Production: the Phase 9 live test (abandoned checkout email 1)
**Verbatim:** First draft line: "Most owners ask us the same few questions." Rewritten: "If you stopped on a question, it's probably one of these."
**Context:** One real asset produced using only the brain, then run through `ops/QA-checklist.md`. The brain lacked an abandoned-checkout template and the product requirement for email consent at checkout; the draft's first pass invented a customer history.
**Disposition:** PATCH
**Routed to:** `templates/nurture-email.md` (abandoned-checkout section), `reference/product-requirements.md` (requirement 26), `examples/abandoned-checkout-email-1.md`.

### 2026-10-19 | RISK | Rempo live pricing page (screenshot supplied 2026-10-16)
**Verbatim:** "Includes 15-Day Free Trial." "$299 setup fee" "24/7 Support" "Google Search Boost"
**Context:** The live page offers a free trial beside a setup fee, a support level one founder and one assistant cannot staff, and a feature name that implies a ranking result. Every buyer sees it today.
**Disposition:** AMEND
**Routed to:** `rules/do-not-say.md`, `rules/feature-status.md`, `ops/decisions.md` (downstream debt: the live page, owner founder).

### 2026-10-19 | RISK | Google review policy, rating manipulation clauses added April 2026
**Verbatim:** Google's policy now bars staff review quotas, soliciting review content that identifies a staff member, and supplying review wording.
**Context:** Event April 2026. Applies to every request Rempo writes for a client and to any tip Rempo gives about staff.
**Disposition:** AMEND
**Routed to:** `rules/do-not-say.md` (delivery section), `reference/review-compliance.md`, `ops/QA-checklist.md`.

### 2026-10-19 | RISK | FTC Consumer Review Rule enforcement (16 CFR Part 465)
**Verbatim:** First warning letters under the rule went out on 2025-12-22; the rule reaches third parties acting on a business's behalf.
**Context:** Event 2025-12-22. Rempo writes and sends requests for clients, so it is in scope as a vendor.
**Disposition:** AMEND
**Routed to:** `rules/do-not-say.md`, `reference/review-compliance.md`.

### 2026-10-19 | COMPETITIVE | Google Business Profile Q&A removed; FAQ rich results limited
**Verbatim:** Q&A API closed 2025-11-03, removal confirmed 2025-12-03; FAQ rich results limited to government and health sites since 2023-08-08.
**Context:** The founder's "FAQ website auto-updated" component targeted search features Google no longer shows for this ICP.
**Disposition:** AMEND
**Routed to:** `rules/feature-status.md` (auto-FAQ DROPPED, rebuilt inside the website), `ops/decisions.md`.

### 2026-10-19 | COMPETITIVE | Sterling Sky posting test; geotagging tests
**Verbatim:** Weekly Google Business Profile posts moved no rankings across 441 keywords over 9 weeks; Google strips EXIF location data on upload.
**Context:** The founder's matrix sold autoposting and geotagged images as ranking levers.
**Disposition:** AMEND
**Routed to:** `ops/decisions.md` (split the GBP manager), `rules/do-not-say.md`.

### 2026-10-19 | COMPETITIVE | Footbridge Media offer
**Verbatim:** "$249 a month", website, profile optimization, and review management (Birdeye) included, no contract, 90-day money-back guarantee.
**Context:** A done-for-you alternative sold online to contractors; the sharpest comparison for Rempo's service.
**Disposition:** AMEND
**Routed to:** `reference/competitor-battlecards.md`, `rules/do-not-say.md` (no "only done-for-you" claim).

### 2026-10-19 | SEGMENT | Founder's note on automated review requests
**Verbatim:** "They must have existing CRM where they collect client's data."
**Context:** Internal, from the second briefing. Makes job software part of the ICP and a checkout question.
**Disposition:** AMEND
**Routed to:** `reference/icp-personas.md`, `ops/decisions.md` (one ICP), checkout qualifier.

### 2026-10-19 | LANGUAGE | Founder's note on social posts from reviews
**Verbatim:** "client is not looking for this feature, but they like it when find out during the discovery or after purchase."
**Context:** Internal. Supports keeping social posts as a retention delight, never a lead.
**Disposition:** PATCH
**Routed to:** `reference/feature-matrix.md`.

---

*Real buyer signals start with the first ad. An empty section here a month after launch means the loop is not running.*
