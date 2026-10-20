# Source: 00_service_offer_matrix.xlsx

Original path: `sources/raw/google-folder/00_service_offer_matrix.xlsx`
Type: xlsx
Size: 31,514 bytes

## Sheet: Column_Audit

| Rempo go-to-market  ·  Service Offer Matrix |
| Column Audit.  Skill phase: Phase 0 (added in Run 2).  Source: dashboards/00-service-offer-matrix.md (Run 2, 2026-10-19). |
| Step 0.1. What the founder's matrix measures, column by column |
| The template behind the matrix was built for professional-services firms: its options include "procurement and legal", "mandate level", and "principal time throughout". Some columns still work for Rempo, some need a new scale, and some are missing. |
| Column | What it captures today | Problem for Rempo | Change |
| Service / Offer | One row per outcome, so services repeat (Reputation management twice, GBP manager twice) | Splits one service's rating across rows | One row per service. Outcomes become measures |
| Client Outcome | A promise in free text ("Better ranking", "online presence") | No metric, no baseline, no time frame, no evidence | Replace with three vectors: outcome metric, evidence strength, time to first proof |
| Client Demand | How many clients want it | For an online funnel, what matters is whether a buyer asks for it by name (it can lead an ad) or only values it once shown | New scale: asked for by name, recognized when shown, latent (valued after purchase) |
| Competitive Differentiation | One scale against "firms" | Rempo competes with two kinds of rival: software the owner runs, and done-for-you providers. A feature can be a commodity in software and rare as a service | Split into two vectors: against software, against done-for-you providers |
| Delivery Effort | Seniority of the work ("senior-led", "principal time") | Rempo's labor is setup hours and monthly hours per account, and how much of it automates | Replace with setup effort and monthly effort, with hours {TBD} until logged |
| Sales Motion | Length and complexity of the buying cycle | Every Rempo service is a 1-decision-maker, under-30-day purchase, so the column carries no information. The question that matters is whether a buyer can purchase it from a page | Replace with self-serve fit: buy from the page, buy after a call, buy after their own data shows the need |
| Ticket Size | Low, Mid, High, relative to nothing | No anchor to the market | Replace with the researched market price and Rempo's price |
| Funnel Role | Entry, core, expansion, anchor | Close, but a self-serve funnel has more specific slots | New scale: free (opt-in), front-end, order bump, one-click upsell, account upsell, product add-on, anchor |
| Missing |  | Nothing records proof, compliance exposure, what the client must hand over, or whether the service shows its value every month | Add: client dependency, compliance risk, retention role |

## Sheet: Service_Vectors

| Rempo go-to-market  ·  Service Offer Matrix |
| Service Vectors.  Skill phase: Phase 0 (added in Run 2).  Source: dashboards/00-service-offer-matrix.md (Run 2, 2026-10-19). |
| Step 0.2. The service vectors: what to score every service on |
| Fourteen vectors. The first three replace "Client Outcome"; the rest replace or extend the template's columns. |
| # | Vector | The question it answers | Scale |
| 1 | Outcome metric | What number moves for the client if this works? | A named metric with a definition |
| 2 | Evidence strength | Does public research show the service moves that metric? | Strong, Moderate, Weak, Not supported (research Step 0D) |
| 3 | Time to first proof | How soon can the client see something happen? | Days, from purchase |
| 4 | Buyer demand | Does the buyer ask for it by name? | Asked for by name, Recognized when shown, Latent |
| 5 | Differentiation against software | Can a tool the owner runs do it? | Commodity, Most vendors, A few, Only Rempo |
| 6 | Differentiation against done-for-you providers | Can an agency or managed service do it? | Commodity, Most providers, A few, Only Rempo |
| 7 | Setup effort | Labor to make it work for one account | Low, Medium, High; hours {TBD} |
| 8 | Monthly effort | Labor to keep it working | Low, Medium, High; hours {TBD} |
| 9 | Client dependency | What the client must hand over | A list |
| 10 | Self-serve fit | Can a buyer purchase it from a page without a call? | Buy from the page, Buy after a call, Buy after their data shows the need |
| 11 | Market price | What the market charges | A researched range |
| 12 | Funnel role | Where it sits in the one funnel | Free, Front-end, Order bump, One-click upsell, Account upsell, Product add-on, Anchor |
| 13 | Compliance risk | Exposure under Google's policies, the FTC rule, or texting rules | Low, Medium, High |
| 14 | Retention role | Does it show its value every month? | Every month, Once, Invisible |

## Sheet: Outcomes_Checked

| Rempo go-to-market  ·  Service Offer Matrix |
| Outcomes Checked.  Skill phase: Phase 0 (added in Run 2).  Source: dashboards/00-service-offer-matrix.md (Run 2, 2026-10-19). |
| Step 0.3. What each service actually produces: the founder's outcomes, checked |
| Service | Founder's outcome | What the research shows | Evidence | What to measure instead |
| Reputation management | More Google reviews without relying on remembering to ask each client | Asking produces reviews: 69% of consumers wrote a local review in the past year and 94% are open to it (BrightLocal 2026). Every published request-to-review rate is vendor data (about 10% to 15% on email; SMS higher), and timing evidence conflicts | Strong | Requests sent per completed job; reviews per 100 requests; reviews in the last 90 days |
| Reputation management | Better ranking | Google says review count and rating feed prominence; Local Services Ads rank on rating and number of reviews (Google); a 2025 study of 8,000+ businesses found rating, volume, and recency among the strongest near-me signals. Proximity and primary category still dominate | Moderate | Geo-grid average rank for three service keywords, before and after; Local Services Ads position if they run them |
| Reputation management | (Added) More calls from people who find the profile | 97% use reviews to choose; 74% look for reviews from the last three months; 31% only use businesses at 4.5 stars or higher; 80% prefer a business that replies to all reviews (BrightLocal 2026); 91% of homeowners rate reviews important when choosing an HVAC contractor (ACHR News 2024) | Strong | Calls, website clicks, and direction requests from the profile; rating; days since the latest review; reply coverage |
| GBP manager | Better visibility and ranking | Holds for one-time optimization: primary category is the top-rated factor, predefined services helped in retests, completeness and hours matter (Google; Whitespark 2026; Sterling Sky). Does not hold for the recurring work: weekly posts moved no rankings in a controlled test; geotagging has no las... | Strong for optimization; Not supported for posting and geotagging | Completeness checklist; categories and services set; geo-grid rank at day 0, 30, 60 |
| GBP manager | Active online without manually doing the work | True as activity. No evidence that posting changes rank; its value is a profile and feed that look current | Weak | Posts and photos published; profile actions trend, never rank |
| Website | Online presence | 17% to 36% of small businesses have no site, but the ICP keeps records in a CRM and most will have one. What moves results is a page for each service (reported as the top local organic factor) and speed (0.1 s faster lifted retail conversion 8.4% and cut lead-generation bounce 8.3%, Deloitte for ... | Moderate | Calls and form fills from the site each month; conversion rate; mobile load time; one page per service |

## Sheet: Rerated_Matrix

| Rempo go-to-market  ·  Service Offer Matrix |
| Rerated Matrix.  Skill phase: Phase 0 (added in Run 2).  Source: dashboards/00-service-offer-matrix.md (Run 2, 2026-10-19). |
| Step 0.4. The re-rated matrix |
| One column per service, as Rempo should sell it. The GBP manager is split in two, because its evidence splits: the one-time optimization has it and the recurring posting does not. |
| Vector | Review Engine | GBP Tune-Up | GBP Upkeep | Website | Product layer |
| What it is | Review requests, follow-ups, personalized requests, replies, social posts and website widget from reviews, set up and run by Rempo | One-time profile optimization: categories, services, description, hours, photos, completeness | Monthly: posts to the profile and social media from real jobs and reviews, photo gallery kept current | Home-service site with a page per service, reviews built in, hosting and updates | Software add-ons: AI voice receptionist first; inbox, booking, chat, and the rest on request |
| Outcome metric | Reviews in the last 90 days; profile calls | Completeness; geo-grid rank at day 30 and 60 | Profile and feed activity | Calls and forms from the site | Answered-call rate (receptionist) |
| Evidence | Strong | Strong | Weak | Moderate | Moderate |
| Time to first proof | About 7 days: first requests out once the CRM is connected | 1 day for the changes; 30 to 60 days for rank, if any | First week | 30 to 45 days to launch, {TBD} | First week |
| Buyer demand | Asked for by name | Recognized when shown | Latent | Recognized when shown | Recognized when shown (missed calls) |
| Differentiation against software | Most vendors can do this | Not offered by review tools | Most vendors can do this | Most vendors can do this | Most vendors can do this |
| Differentiation against done-for-you providers | A few others can do this | Most providers | Most providers | Commodity | A few others can do this |
| Setup effort | Medium: CRM connection, templates, photo, texting registration | Low to medium | Low | High | Medium |
| Monthly effort | Low: automation, reply checks, report | None | Low | Low | Low to medium, plus support |
| Client dependency | A CRM or field-service system with customer phone or email; Google profile access; a team photo | Google profile access | Photos from jobs, or permission to use review content | Content approval, domain access | Phone forwarding, call scripts |
| Self-serve fit | Buy from the page | Buy from the page | Buy from the page | Buy after a call | Buy after their data shows the need |
| Market price | Software $39 to $125 a month; done-for-you $249 to $600+ | $250 to $750 one-time | $125 to $500 a month | $1,800 to $4,500 build, or $249 a month bundled | $29 to $99 a month (AI receptionists) |
| Funnel role | Front-end | Order bump | One-click upsell | Account upsell | Product add-on |
| Compliance risk | High | Low | Low | Low | High (AI voice consent for outbound calls) |
| Retention role | Every month | Once | Every month | Once, then invisible | Every month |

## Sheet: Founder_vs_Research

| Rempo go-to-market  ·  Service Offer Matrix |
| Founder vs Research.  Skill phase: Phase 0 (added in Run 2).  Source: dashboards/00-service-offer-matrix.md (Run 2, 2026-10-19). |
| The founder's rating against research |
| Service | Column | Founder's rating | Research rating | Why |
| Reputation management | Client Outcome | More reviews; better ranking | More reviews (strong); ranking (moderate); more calls from the profile (strong, added) | Section 0.3 |
| Reputation management | Client Demand | Wanted by most | Asked for by name | Reviews are the reason owners shop this category |
| Reputation management | Competitive Differentiation | Fully commoditized | Commodity as software; a few others can do it as a done-for-you service | Flat-priced, self-serve, done-for-you review services are rare; Footbridge bundles a review tool with a site |
| Reputation management | Delivery Effort | Templated but customized | Setup medium, monthly low | Setup is custom (CRM, photo, registration); running it is templated |
| Reputation management | Sales Motion | Fast and simple, under 30 days, 1 decision maker | Buy from the page | Same reading, more useful scale |
| Reputation management | Ticket Size | Low | Mid for a service ($197 a month against $39 to $125 for software and $249 to $600+ for done-for-you) | Research 5 |
| Reputation management | Funnel Role | Core revenue driver | Front-end | Agreed |
| GBP manager | Client Outcome | Better visibility and ranking; active online | Ranking holds for one-time optimization only; activity is real but unproven as value | Section 0.3 |
| GBP manager | Client Demand | Wanted by most | Optimization recognized when shown; posting latent | Owners ask for "Google", not for posts |
| GBP manager | Competitive Differentiation | A few firms can | Most providers can | The founder's own note: "if we consider agencies as a competitor, the answer is most vendors can do this" |
| GBP manager | Delivery Effort | Productized, runs off a template | Optimization low to medium once; upkeep low | Agreed, split in two |
| GBP manager | Ticket Size | Mid | Optimization $250 to $750 once; upkeep $125 to $500 a month (agency guides) | Research 5 |
| GBP manager | Funnel Role | Expansion or upsell | Optimization: order bump. Upkeep: one-click upsell | Split |
| Website | Client Outcome | Online presence | Calls and forms from the site | Presence is not a result a buyer can check |
| Website | Client Demand | Wanted by some (service matrix); Wanted by most (feature matrix) | Recognized when shown | The two matrices disagree; the ICP mostly has a site already |
| Website | Competitive Differentiation | Fully commoditized | Commodity | Agreed |
| Website | Ticket Size | Mid | $1,800 to $4,500 build typical | Research 3 |
| Website | Funnel Role | Expansion or upsell | Account upsell, after a site check on the onboarding call | Needs a call to scope |
| The second block of ratings (headed "Ali" in both files) has no service or feature names, so no row can be matched. It is not used, and it should be refilled with names before the next review. |

## Sheet: Component_Verdicts

| Rempo go-to-market  ·  Service Offer Matrix |
| Component Verdicts.  Skill phase: Phase 0 (added in Run 2).  Source: dashboards/00-service-offer-matrix.md (Run 2, 2026-10-19). |
| Step 0.5. Component verdicts: keep, reframe, or drop |
| # | Component (founder's wording) | Founder: demand | Founder: differentiation | Evidence | Verdict | Note |
| 1 | Automated review request | Wanted by Most | A few others can do this | Strong | Keep and lead | Needs a CRM: make it a checkout question |
| 2 | Automated review request follow up | Wanted by Most | Most vendors can do this | Weak | Keep, do not claim | Test the timing of first ask and reminder |
| 3 | Hyperpersonalized review request | Wanted by Some | A few others can do this | Weak | Keep, show it, test it | Never claim a lift. No asking customers to name staff (Google, April 2026) |
| 4 | Review reply | Wanted by Most | Most vendors can do this | Moderate | Keep and lead | Written for each review: templated replies put off half of consumers |
| 5 | Review repurpose to social media post | Wanted by Most | A few others can do this | Weak | Keep, do not lead | A retention delight, as the founder's note says |
| 6 | Review widget | Wanted by Some | Most vendors can do this | Moderate | Keep | No "stars in Google" claim; never imply it shows every review |
| 7 | Custom Implementation | Wanted by Most | A few others can do this | Moderate | Keep and lead | It is the done-for-you promise |
| 8 | GBP optimization | Wanted by Most | A few others can do this | Strong | Keep, move to the order bump | One-time, low labor, evidence behind it |
| 9 | Autoposting to GBP | Wanted by Most | A few others can do this | Not supported | Reframe | Sold as staying current, never as ranking |
| 10 | Autoposting to major social media | Wanted by Most | A few others can do this | Weak | Reframe | Same, inside GBP Upkeep |
| 11 | Geotagging Images | Wanted by Most | A few others can do this | Not supported | Drop | Remove from every sales asset |
| 12 | FAQ website auto-updated from what customers ask | Wanted by Some | A few others can do this | Weak | Reframe | Rebuild as answers on each service page, inside the Website upsell |
| 13 | Website gallery widget auto-updated | Wanted by Some | A few others can do this | Weak | Keep, do not claim | Conversion content inside GBP Upkeep and the website |
| 14 | Website | Wanted by Most | Most vendors can do this | Moderate | Keep as an account upsell | Home services only, scoped on a call |
| 15 | Unified Inbox | Wanted by Some | Most vendors can do this | Weak | Hold | Product layer, on request after day 60; support load |
| 16 | Social media scheduler | Wanted by Some | Most vendors can do this | Weak | Drop as a separate item | GBP Upkeep covers the need without a tool to run |

## Sheet: KPI_Tree

| Rempo go-to-market  ·  Service Offer Matrix |
| KPI Tree.  Skill phase: Phase 0 (added in Run 2).  Source: dashboards/00-service-offer-matrix.md (Run 2, 2026-10-19). |
| Step 0.6. What to measure: the KPI tree |
| Three layers per service. Delivery is what Rempo controls and can promise. Client outcome is what the client sees, reported against a baseline and never promised. Business is what Rempo earns. Every outcome metric needs a baseline captured at signup (Step 0.7). |
| Service | Layer | Metric | Definition | Data source |
| Review Engine | Delivery | Days to first request | Purchase date to first request sent | Rempo account |
| Review Engine | Delivery | Ask coverage | Requests sent ÷ completed jobs with a phone or email, target every eligible job | CRM job events and request log |
| Review Engine | Delivery | Reply coverage | Share of new reviews answered within 48 hours | Google profile |
| Review Engine | Client outcome | Request-to-review rate | Reviews received per 100 requests, split personalized against plain | Request log matched to new reviews |
| Review Engine | Client outcome | Review recency | Reviews in the last 90 days; days since the latest review | Google profile |
| Review Engine | Client outcome | Rating | Average rating, last 90 days and lifetime | Google profile |
| Review Engine | Client outcome | Profile actions | Calls, website clicks, and direction requests from the profile, month on month | Business Profile Performance |
| Review Engine | Client outcome | Local position | Average rank on a geo-grid for three service keywords, monthly | Geo-grid tracker, {DEFERRED: product} |
| GBP Tune-Up | Delivery | Completeness | Checklist: primary and secondary categories, predefined services, description, hours and special hours, photos, attributes | Google profile |
| GBP Tune-Up | Client outcome | Local position | Geo-grid rank at day 0, 30, and 60 | Geo-grid tracker |
| GBP Upkeep | Delivery | Activity | Posts and photos published per month, to the profile and social | Posting log |
| GBP Upkeep | Client outcome | Profile actions | Same as the Review Engine, read as a trend, never attributed to posts alone | Business Profile Performance |
| Website | Delivery | Service pages and speed | One page per service; mobile load time | Site, PageSpeed |
| Website | Client outcome | Leads from the site | Calls and form fills per month; conversion rate | Call tracking and form events, {DEFERRED: product} |
| Product layer | Client outcome | Answered calls | Share of inbound calls answered by a person or the receptionist; missed calls followed up | Phone system |
| All | Business | Retention | Accounts still paying at month 2, 6, and 12 | Billing |
| All | Business | Attach | Share of front-end buyers who take the bump, the upsell, and each add-on | Checkout and billing |
| All | Business | Cost to serve | Setup and monthly hours by task, platform and texting cost per account | Time log, invoices |

## Sheet: Baseline

| Rempo go-to-market  ·  Service Offer Matrix |
| Baseline.  Skill phase: Phase 0 (added in Run 2).  Source: dashboards/00-service-offer-matrix.md (Run 2, 2026-10-19). |
| Step 0.7. Baseline at signup |
| Captured for every account before the first request, so every later number has a "before". Also a requirement for product (gtm-requirements-for-product.md). |
| 1.  Google review count, average rating, date of the latest review, reviews in the last 90 days |
| 2.  Share of reviews with an owner reply |
| 3.  Geo-grid rank for three service keywords |
| 4.  Profile actions for the last 90 days, where profile access allows |
| 5.  Completed jobs per week, from the CRM |
| 6.  Website: mobile load time; whether calls and forms are tracked |
| 7.  Consent to compare personalized and plain requests inside the account |

## Sheet: Summary

| Rempo go-to-market  ·  Service Offer Matrix |
| Summary.  Skill phase: Phase 0 (added in Run 2).  Source: dashboards/00-service-offer-matrix.md (Run 2, 2026-10-19). |
| What the matrix says |
| 1.  The review engine is the front end, and the evidence agrees. It is the only service with strong evidence for an outcome the buyer feels (calls from people who read reviews) and a process Rempo controls (every job asked, every review answered). |
| 2.  "Better ranking" is the weakest outcome in the founder's matrix. It is moderate for reviews and not supported for posting and geotagging. The message moves from ranking to recency and replies, which buyers read and Rempo can show. |
| 3.  Split the GBP manager. The evidence sits in the one-time optimization, which becomes the checkout order bump. The recurring posting becomes a presence add-on, sold as staying current. |
| 4.  Drop geotagging, rebuild the auto-FAQ. One rests on data Google discards; the other fed a search feature Google removed. |
| 5.  The website sells on a call, after a site check, and is measured by calls and forms. |
| 6.  One product item has a documented problem behind it: the AI voice receptionist, against the calls home-service shops miss. The rest of the product layer waits for a client to ask. |
| 7.  The template's Sales Motion column carries no information for Rempo. Every service is a quick, one-person purchase. Self-serve fit replaces it. |

## Sheet: Legend

| Rempo go-to-market  ·  Service Offer Matrix |
| Legend: what the colors mean, and the dropdown lists |
| •  Colors are conditional-formatting rules, not painted cells: change a value, or pick another option from a dropdown, and the color follows. |  |  |  | Dropdown lists (edit the options here; the dropdowns follow) |
| •  Header rows are royal blue. Rempo's own row or column is tinted brand blue, so it is easy to find in every comparison. |  |  |  | Buyer demand | Competitiveness (who else can do it) | Evidence strength |
| •  Orange marks the done-for-you service (the front-end offer and its upsells); violet marks the product layer behind it. |  |  |  | Wanted by all | Unique to us | Strong |
|  |  |  |  | Wanted by most | A few others can do this | Moderate |
| Colors used in this workbook |  |  |  | Wanted by some | Most vendors can do this | Weak |
| Looks like | Means | Where |  | Wanted by one | Commodity | Not supported |
| Rempo | Rempo's own row or column | Every comparison table |  |  | Commodity, should be free |
| {TBD} | Unknown until Rempo has its own data. Never invented. | Any cell; the color clears when the text is replaced |
| {DEFERRED: product} | Depends on what the product team builds | Any cell; listed in 15_gtm_requirements_for_product |
| Strong | Evidence strength | Component_Verdicts, Outcomes_Checked, Rerated_Matrix |
| Moderate | Evidence strength | Component_Verdicts, Outcomes_Checked, Rerated_Matrix |
| Weak | Evidence strength | Component_Verdicts, Outcomes_Checked, Rerated_Matrix |
| Not supported | Evidence strength | Component_Verdicts, Outcomes_Checked, Rerated_Matrix |
| Keep and lead | Verdict on a component | Component_Verdicts |
| Keep | Verdict on a component | Component_Verdicts |
| Reframe | Verdict on a component | Component_Verdicts |
| Drop | Verdict on a component | Component_Verdicts |
| Hold | Verdict on a component | Component_Verdicts |
| Wanted by most | Buyer demand | Column_Audit, Component_Verdicts, Rerated_Matrix |
| Wanted by some | Buyer demand | Column_Audit, Component_Verdicts, Rerated_Matrix |
| Asked for by name | Buyer demand | Column_Audit, Component_Verdicts, Rerated_Matrix |
| Recognized when shown | Buyer demand | Column_Audit, Component_Verdicts, Rerated_Matrix |
| Latent | Buyer demand | Column_Audit, Component_Verdicts, Rerated_Matrix |
| Not offered by review tools | Competitiveness (who else can do it) | Component_Verdicts, Rerated_Matrix |
| A few others | Competitiveness (who else can do it) | Component_Verdicts, Rerated_Matrix |
| Most vendors | Competitiveness (who else can do it) | Component_Verdicts, Rerated_Matrix |
| Most providers | Competitiveness (who else can do it) | Component_Verdicts, Rerated_Matrix |
| Commodity | Competitiveness (who else can do it) | Component_Verdicts, Rerated_Matrix |
| Front-end | Place in the one funnel | Column_Audit, KPI_Tree, Rerated_Matrix |
| Order bump | Place in the one funnel | Column_Audit, KPI_Tree, Rerated_Matrix |
| One-click upsell | Place in the one funnel | Column_Audit, KPI_Tree, Rerated_Matrix |
| Account upsell | Place in the one funnel | Column_Audit, KPI_Tree, Rerated_Matrix |
| Product add-on | Place in the one funnel | Column_Audit, KPI_Tree, Rerated_Matrix |
| Delivery | Place in the one funnel | Column_Audit, KPI_Tree, Rerated_Matrix |
| Client outcome | Place in the one funnel | Column_Audit, KPI_Tree, Rerated_Matrix |
| Business | Place in the one funnel | Column_Audit, KPI_Tree, Rerated_Matrix |
| None | Effort to deliver (low is good) | Column_Audit, Rerated_Matrix |
| Low to medium | Effort to deliver (low is good) | Column_Audit, Rerated_Matrix |
| Low | Effort to deliver (low is good) | Column_Audit, Rerated_Matrix |
| Medium | Effort to deliver (low is good) | Column_Audit, Rerated_Matrix |
| High | Effort to deliver (low is good) | Column_Audit, Rerated_Matrix |
| High | Compliance risk (low is good) | Rerated_Matrix |
| Low | Compliance risk (low is good) | Rerated_Matrix |
| Buy from the page | Self-serve fit | Rerated_Matrix |
| Buy after a call | Self-serve fit | Rerated_Matrix |
| Buy after their data | Self-serve fit | Rerated_Matrix |
| Every month | Retention role | Rerated_Matrix |
| Once, then invisible | Retention role | Rerated_Matrix |
| Once | Retention role | Rerated_Matrix |
