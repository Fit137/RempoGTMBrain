# Review cadence

Who reviews what, how often, and when a file is considered stale. Agreed 2026-10-19 as the build default; the founder confirms or changes it at the first ledger sweep. Rempo is early-stage, so the cadence is monthly, and the 90-day experiment gates double as snapshot dates.

## Rituals

| Ritual | Frequency | Owner | Work |
|---|---|---|---|
| Signal triage | Weekly, Monday | Founder (assistant logs) | Disposition every new signal, increment WATCH counters, execute PATCHes |
| Weekly scorecard read | Weekly, Monday | Founder, media buyer | Read the experiment scorecard in `reference/experiment-90-day.md`; log anything odd as a CHANNEL signal |
| Ledger sweep | Monthly | Founder | Read all four `rules/` files against reality, update `last_reviewed`, expire stale WATCH items |
| Snapshot | Monthly, and at each gate (day 30, 60, 90) | Founder | The full capture in `snapshots/`, ending in what it changed |
| Master context version | On any AMEND, and quarterly | Founder | Bump version, refresh `status_notes`, verify sections against the ledgers |
| Portable control layer | On any AMEND | Whoever makes the AMEND | Regenerate `adapters/portable-control-layer.md`, date it |
| Brain audit | Quarterly | Founder or assistant | `python3 scripts/audit.py`, then produce one live asset using only the brain |

## Ledger ownership and staleness

| File | Owner | Stale after |
|---|---|---|
| `rules/feature-status.md` | Founder, with the assistant for delivery facts | 30 days |
| `rules/do-not-say.md` | Founder; counsel for the guarantee and consent wording | 90 days |
| `rules/glossary.md` | Founder | 90 days |
| `rules/writing-rules.md` | Founder | 180 days |
| `context/Rempo_GTM_Master_Context.md` | Founder | 90 days |
| `adapters/portable-control-layer.md` | Founder | Regenerated on every AMEND; 90 days at most |

`feature-status.md` goes stale fastest and does the most damage, because it stands between a plan and a promise. The first two changes it is waiting for: product confirming which job software connects at launch, and the founder deciding the Run 2 offer.

## The amendment procedure (all steps or none)

1. Update the ledger in `rules/` and its `last_reviewed` date.
2. Update the matching section of the master context; bump `version` and `last_updated`; revise `status_notes`.
3. Write the dated entry in `ops/decisions.md`, with "What this does not change" and the downstream list.
4. Propagate to copy: grep `ops/copy-bank.md`, `templates/`, `examples/`, and `reference/` for the old phrasing.
5. List affected live surfaces from `ops/asset-index.md` as downstream items with owners.
6. Regenerate `adapters/portable-control-layer.md`.

## Authority
- A PATCH can be made by anyone producing work (founder, assistant, media buyer, research strategist, an agent).
- An AMEND to any `rules/` file requires the founder.
- A change to positioning, the ICP, the offer, or the channel mix requires the founder and a dated entry in `ops/decisions.md`.
- Guarantee terms and consent wording require counsel before they ship.
