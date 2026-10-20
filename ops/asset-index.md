# Asset index

Where the source deliverables and live surfaces live. An amendment consults this file to find everything carrying an old claim, so keep it current.

## Source deliverables (the source manifest)
All originals are in `sources/raw/`; machine-readable extracts in `sources/extracted/`. The build repo is `Fit137/rempogtmbuild` (PR 1, branch `claude/affectionate-cerf-ts80in`), which also holds the interactive walkthrough deck.

| Artifact | Type | What it settles | Dated | Location |
|---|---|---|---|---|
| Pricing page | Screenshot and transcription | What is live today: tiers, prices, trial, features | 2026-10-16 | `sources/raw/founder/pricing-page.md`, `.webp` |
| Founder brief | Transcribed DOCX | Business, stack, team, budget, the founder's hypotheses | 2026-10-16 | `sources/raw/founder/founder-brief.md` |
| Service Offer Matrix, Product Features Matrix | CSV and transcription | The founder's assumptions to test | 2026-10-19 | `sources/raw/founder/` |
| GTM brief, Run 2 | MD | Fixed decisions F1 to F7, claim constraints, open decisions | 2026-10-19 | `sources/raw/research/GTM-BRIEF.md` |
| Research Step 0D | MD | What each service produces, prices, compliance facts | 2026-10-19 | `sources/raw/research/step-0d-service-outcomes.md` |
| 00 Service Offer Matrix | XLSX | What to measure; re-rated services; verdicts | 2026-10-19 | `sources/raw/google-folder/` |
| 01 Product Feature Matrix | XLSX | Quadrants; what leads; demand driver | 2026-10-19 | same |
| 02 Competitive Analysis | XLSX | Slate, vectors, wedge | 2026-10-19 | same |
| 03 Positioning Summary, 04 Positioning Statements | DOCX | Category, core claim, statements | 2026-10-19 | same |
| 05 ICP Dashboard, 06 Buying Committee | XLSX | One ICP, two levels, roles, founding cohort | 2026-10-19 | same |
| 07 Value Proposition | DOCX | Promise, pillars, nine copy drills | 2026-10-19 | same |
| 08 Customer Journey | XLSX | The one funnel, stages, bumpers, blockers | 2026-10-19 | same |
| 09 Assets Library | XLSX | Channels, the hire, assets per campaign | 2026-10-19 | same |
| 10 Pricing Dashboard | XLSX | Live vs recommended offer, ROI, funnel economics, ROI calculator | 2026-10-19 | same |
| 11 Lead Magnet Spec, 12 Scorecard Spec | XLSX, DOCX | Scorecard, tiers, email sequence | 2026-10-19 | same |
| 13 90-Day Experiment | XLSX | Budget, tests, gates, success and stop rules | 2026-10-19 | same |
| 14 Offer Architecture | DOCX | The ladder, the release rule | 2026-10-19 | same |
| 15 GTM Requirements for Product | XLSX | The 25 requirements behind every `{DEFERRED: product}` | 2026-10-19 | same |

## Product and brand
- Live site: https://rempo.io (did not resolve from the build environment on 2026-10-16 or 2026-10-19).
- Delivery stack: GoHighLevel, Zapier, NiftyImages, WordPress.
- Brand: the Rempo mark and lockups in `docs/assets/`; design system in the build repo, `brand/DESIGN-SYSTEM.md`.

## Live surfaces (every place a claim is published)
- Rempo pricing page: rempo.io pricing. Carries "24/7 Support", "Start Free" beside a setup fee, "Google Search Boost", and HELD items. Downstream debt in `ops/decisions.md`. Last reviewed 2026-10-19.
- VSL, VSL page, checkout, scorecard, ads, emails: none live yet. Add each here the day it ships.

## Pages
No finished long-form assets yet. When the VSL page, FAQ, or comparison pages ship, file their final copy in `pages/` and list them above.

## Portability
| Adapter | Installed where | Who runs that tool |
|---|---|---|
| `CLAUDE.md` | This repo root | Claude Code |
| `AGENTS.md` | This repo root, with the GTM Brain skill block | Codex and other AGENTS.md tools |
| `adapters/AGENTS.block.md` | Copy into any other repo that writes customer-facing text (the funnel build, the website) | Codex |
| `adapters/portable-control-layer.md` | Pasted into a chat model with no file access | Anyone drafting in ChatGPT, Grok, Gemini |

## Related engagements
- Funnel build (VSL, page, checkout, scorecard): not started; owner founder.
- Product requirements: `reference/product-requirements.md`; owner product.
- Counsel: guarantee terms, text consent wording.
- Pricing decision: `ops/decisions.md`, OPEN.
