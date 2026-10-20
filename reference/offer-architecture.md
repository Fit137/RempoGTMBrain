# Offer architecture

Load for: what is offered when, to whom, in which layer, and when a held product item may be sold. Distills: Phase 11, `dashboards/11-offer-architecture.md`, with prices from Phase 9.

Service in front, product behind, one funnel. Prices below are the Run 2 recommendation: PLANNED until [`ops/decisions.md`](../ops/decisions.md) marks the offer DECIDED. Today's live prices: [pricing and packaging](pricing-and-packaging.md).

## The ladder

| Step | Offer | Layer | When it is offered | Who delivers | Price (PLANNED) |
|---|---|---|---|---|---|
| 0 | Review Engine Scorecard and Gap Report | Free | Ads, VSL page exit, search | Automated; assistant for the report | Free, with opt-in |
| 1 | Review Engine | Service | VSL page, checkout | Rempo's team | $197/location/month plus $299 setup |
| 2 | GBP Tune-Up | Service | Order bump at checkout | Assistant | $197 one-time |
| 3 | GBP Upkeep | Service | One-click upsell after payment | Automated, checked by the assistant | $97/location/month |
| 4 | Website | Service | 30-day review call, after a site check | Assistant (WordPress template) | $1,497 plus $49/month |
| 5 | AI voice receptionist | Product | 30-day review or later, when call data shows missed calls | Set up by Rempo, runs as software | $97/month, setup `{TBD}` |
| 6 | Other product add-ons (inbox, booking, chat, pipeline, reactivation, referrals, listings) | Product | Only under the release rule | Set up by Rempo, run as software | Priced when first released |
| 7 | Annual plan | Terms | Month 3 | Billing | Two months free, setup credited |
| Anchor | Three or more locations, or custom | Service and product | "Book a call" bumper | The founder | Quoted per location |

Every step reaches the same buyer through the same funnel: the same ads, the same VSL, the same onboarding call, the same 30-day review. Nothing in the product layer has its own trial, landing page, or ICP.

## The release rule

The founder prefers not to add software features, to limit support. A held item leaves "Hold" only when all five are true:

1. **Asked for.** At least two paying clients asked for it without being prompted (the number is `{TBD}` for the founder to confirm).
2. **Visible in their data.** The account's own data shows the problem: missed calls for the receptionist, messages lost across apps for the inbox.
3. **Delivered done-for-you.** Rempo sets it up and tunes it; the client never configures software.
4. **A support playbook exists** before the first sale: the five most likely questions answered, and a cap on support time per account per month (`{TBD}`).
5. **Priced as an add-on to the service,** never a standalone software plan, so the buyer stays one customer with one relationship.

When an item is released, update [`rules/feature-status.md`](../rules/feature-status.md) from HELD to PLANNED first, then write the decision entry, then copy.

## What keeps it one company

| Function | Rule |
|---|---|
| ICP | One. Product add-ons are sold only to service clients |
| Marketing | One message; the product layer never leads an ad |
| Funnel | One. Product add-ons appear at the 30-day review and later, never at the front |
| Team | One. The assistant delivers both layers; no product team until the triggers below |
| Numbers | One scorecard, with add-ons as attach rates and support time per account |

## Support load guardrail

From the first add-on sale, measure support requests per account per month, by add-on, and founder and assistant minutes per request. An add-on whose support time exceeds the cap two months running goes back to "Hold" for new sales until its playbook is fixed.

## When to revisit (triggers, not dates)

- **Hours per account fall** far enough that one assistant runs many more accounts: the service starts to scale like software.
- **Clients ask to run it themselves:** a software-only plan may have a buyer.
- **Agencies ask to resell the program:** the implementer route from Run 1 opens.

Each needs the time log by task (requirement 21 in [product requirements](product-requirements.md)), which is why it starts on day one.
