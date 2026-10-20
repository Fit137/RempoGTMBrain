# Step 0D. What each service actually produces

Run 2026-10-19 for the second GTM run (service-dominated hybrid). The founder's Service Offer Matrix and Product Features Matrix rate each service and component from experience. This step checks every outcome they claim against public evidence, so the ratings in `dashboards/00-service-offer-matrix.md` rest on research rather than on the dropdown choices.

**Method and evidence quality.** Direct page fetches were blocked by this environment's network policy on 2026-10-19 (the same DNS and proxy limits as the first run), so every finding below comes from web search summaries of the named source. Primary sources (Google, the FTC, peer-reviewed or survey research with a stated sample) are marked **Primary**. Industry surveys with a stated sample are **Survey**. Vendor data, agency guides, and single case studies are **Vendor** and count as directional only. Expert-opinion surveys (Whitespark) are **Expert survey**: they rank what practitioners believe, not what was measured.

**Evidence strength scale used in the dashboards:**

| Strength | Meaning |
|---|---|
| Strong | A primary source says it, or two or more independent studies with stated samples agree |
| Moderate | One study with a stated sample, or an expert survey plus consistent vendor data |
| Weak | Vendor claims or single case studies only, or studies that disagree |
| Not supported | Controlled tests found no effect, or the platform feature it depended on is gone |

---

## 1. Reputation management: the review engine

### 1a. Does asking produce reviews?

| Finding | Figure | Source | Quality |
|---|---|---|---|
| Consumers who wrote a review of a local business in the past 12 months | 69%; 94% open to doing so | BrightLocal Local Consumer Review Survey 2026 (1,002 US adults, February 2026), via SocialPilot roundup | Survey, secondary |
| Reviews per request, automated email only | About 15 reviews per 100 requests | GatherUp, own customer data | Vendor |
| Typical response for service businesses on automated email requests | 10% to 15% | Focus Digital | Vendor, no method stated |
| SMS against email | SMS: 33% higher feedback rate, 20% higher click to review sites (GatherUp); 1.3x to 1.5x review rate (Postscript, e-commerce); 66% higher (Yotpo, 2020) | Vendor A/B data | Vendor. Direction consistent, size not |
| Reminder sequences | One tree service: +690% reviews after a four-step SMS and email sequence (NiceJob case study); Birdeye 2025: businesses sent 25% more requests | Vendor | Vendor, single case |
| Timing | A controlled study reported in secondary write-ups: next-day prompts produced half as many reviews as no prompt, delayed prompts (day 5 to 14) raised the rate, ratings unchanged. Vendors claim the opposite (within 24 hours, 3x) without a method | nearmedia.co, powerreviews.com, focus-digital.co | Conflicting. Test it |

**Verdict: Strong** that a consistent ask produces reviews. **Weak** on any specific rate: every rate is vendor data, and timing evidence conflicts. Rempo measures its own request-to-review rate per account from a baseline; it never quotes one.

### 1b. Do reviews change who gets the call?

| Finding | Figure | Source | Quality |
|---|---|---|---|
| Consumers who use reviews to choose a local business | 97% | BrightLocal LCRS 2026 | Survey |
| Always read reviews | 41%, up from 29% in 2025 | BrightLocal LCRS 2026 | Survey |
| Only use businesses rated 4.5 stars or higher | 31%, up from 17% | BrightLocal LCRS 2026 | Survey |
| Look for reviews from the last three months / last two weeks | 74% / 32% | BrightLocal LCRS 2026 | Survey |
| More likely to use a business that replies to all its reviews | 80% | BrightLocal LCRS 2026 | Survey |
| Put off by generic or templated replies | 50% | BrightLocal LCRS 2026 | Survey |
| Homeowners who rate online reviews important when choosing an HVAC contractor | 91% (400 homeowners) | Clear Seas Research for ACHR News, September 2024 | Survey |
| Purchase likelihood with five reviews against none | +270%; +380% for higher-priced items; diminishing after the first few | Spiegel Research Center, Northwestern, 2017 (retailer e-commerce data) | Primary research, e-commerce context |
| Consumers who have used AI to find or get a recommendation for a local business | 58% | BrightLocal LCRS 2026 | Survey |

**Verdict: Strong.** Recency, rating, and replies shape whether a searcher calls. This is the outcome the founder's "better ranking" column under-describes: the larger, better-evidenced effect is on conversion from the profile, not only on rank. Two design consequences: recency is a measurable target (reviews in the last 90 days), and AI replies must read as written for that review, because templated replies put off half of consumers.

### 1c. Do reviews change ranking?

| Finding | Figure | Source | Quality |
|---|---|---|---|
| Google's own statement | Local results rest mainly on relevance, distance, and prominence; review count and rating feed prominence; there is no way to pay for a better local ranking | support.google.com/business/answer/7091 | Primary |
| Local Services Ads ranking | Ranking weighs relevance and profile quality, including rating, number of reviews, response time, images, and verification; higher-quality profiles may rank higher and pay less per lead; up to 5 reviews may be needed to go live | support.google.com/localservices/answer/7527305 and /7496631 | Primary |
| Expert weighting of review signals in the local pack | About 15% to 20% of local pack weight (secondary summaries disagree); top single factors are primary category (227 points) and proximity (225) | Whitespark Local Search Ranking Factors 2026 (Darren Shaw, published 2025-11-06; 47 experts, 187 factors), via harmo.me, blckalpaca.at, gmbapi.com | Expert survey, secondary |
| Near-me ranking study, 2025 | 8,000+ businesses in 200 cities: review rating, volume, and recency were among the strongest signals; steady fresh reviews beat older or fewer reviews even at a lower average rating | Sterling Sky (Joy Hawkins), via soci.ai and nicejob.com | Study, secondary |
| What the 3-pack holds | Median ranking business about 47 reviews; ratings cluster at 4.5 to 4.9; urban markets 3 to 5 times more competitive than rural (50.4 million US results, Q4 2025) | Local Falcon whitepaper, 2026-01-14 | Vendor study, own summary |
| Owner replies and rank | No controlled study found that replies move rankings; the case for replies is trust and conversion | localsearchforum.com, digitalshiftmedia.com | Weak |

**Verdict: Moderate.** Reviews feed ranking (Google says so; studies agree on recency and volume), but proximity and category dominate, and nothing guarantees a position. For home services there is a second, primary-sourced channel: Google Local Services Ads rank on rating and review count. Rempo measures ranking with a geo-grid before and after, and never promises it.

### 1d. Components of the review engine

| Component (founder's wording) | What it is supposed to do | Evidence | Strength |
|---|---|---|---|
| Automated review request (needs an existing CRM) | Ask every customer after every job | 1a. Housecall Pro exposes a "new completed job" trigger through Zapier and webhooks, used by NiceJob, ReviewNudger, ReviewBuzz and others; Jobber triggers natively on job close, visit complete, or invoice paid | Strong |
| Automated review request follow-up | Catch the customers who missed the first ask | Vendor case studies only; timing evidence conflicts | Weak to moderate |
| Hyper-personalized review request (owner or team photo, customer's name in the image) | Raise request-to-review conversion | No study of personalized images in review requests or texts. Survey research: personalization (name plus handwritten signature) raised postal response, odds ratio 1.45 (95% CI 1.27 to 1.66) in a pooled analysis; Dillman's review of 9 studies found about +6%; a Dutch experiment with 39,518 people found no consistent effect; NiftyImages claims +30% email clicks (vendor, 2015) | Weak. A plausible lift to test, not to claim |
| Review reply | Show every reviewer they were heard | BrightLocal 2026: 80% more likely to use a business that replies to all; 50% put off by templated replies. No ranking effect shown | Moderate (conversion); not supported (ranking) |
| Review repurposed to social media posts | Put good reviews in front of followers | No study of local services found. General trust data favors peer opinions (Nielsen, via secondary); eMarketer: 62% more likely to buy after seeing customer photos and videos (retail) | Weak |
| Review widget on the website | Show reviews where visitors decide | Spiegel: reviews on the page raise purchase likelihood (e-commerce). Since September 2019 Google shows no star snippets for a business's own reviews on its own site, including through widgets | Moderate (on-page conversion); not supported (search stars) |
| Custom implementation | Connect the CRM and set everything up, so it runs | Setup effort and onboarding support are complaint themes for NiceJob, Podium, and Birdeye (first run, Step 2.7) | Moderate as a buying reason |

### 1e. Compliance that now shapes the product

| Rule | What changed | Source | Quality |
|---|---|---|---|
| Google Maps rating manipulation policy | On 2026-04-17 Google added two clauses: merchants may not ask staff to solicit a certain number of reviews, or to solicit reviews with specific content, "including content that identifies a staff member". Gating (asking only happy customers) and incentives were already banned. Google also announced it can pause reviews on unusual activity (2026-04-16, Trust and Safety report) | ppc.land; digitalshiftmedia.com; nicejob.com | Secondary reports of a Google policy change. Check the live policy page |
| FTC Consumer Review Rule, 16 CFR Part 465 | Effective 2024-10-21. First public enforcement: warning letters to 10 companies on 2025-12-22, civil penalties up to $53,088 per violation; the FTC's position is that a business can be liable for third parties acting on its behalf | lexblog.com (2026-01-02), beneschlaw.com, kjk.com (2026-08-06) | Law-firm summaries |

**What this means for the personalized request.** Showing the owner's or the team's photo is allowed. Asking the customer to mention the technician by name, suggesting wording, or giving technicians review quotas or contests is not. Rempo is a vendor acting on the business's behalf, so the FTC position on third parties applies to it directly.

---

## 2. Google Business Profile manager

| Component (founder's wording) | Founder's claimed outcome | Evidence | Strength |
|---|---|---|---|
| GBP optimization (one-time) | Better visibility and ranking | Primary category is the top-rated local pack factor (Whitespark 2026); selecting Google's predefined services had a positive ranking effect in Sterling Sky retests (2022, 2024; no effect in 2019); Google: a complete profile makes customers 2.7 times more likely to consider the business reputable, 70% more likely to visit, 50% more likely to consider buying (support.google.com/business/answer/10515606); being open at the time of search affects rank through the day (Whitespark Local Insider) | Strong |
| Autoposting to GBP | Better visibility and ranking; active online without doing the work | Sterling Sky controlled test: three listings, weekly posts for nine weeks, 441 keywords each, no measurable ranking movement (year reported as 2021 or 2025; secondary). Posts are read as a conversion and engagement tool | Not supported (ranking); weak (conversion) |
| Autoposting to major social media | Active online without doing the work | No evidence found that social posting affects local rankings; value is presence | Weak |
| Geotagging images | Better ranking | Google strips EXIF data on upload; Sterling Sky tests found no lasting effect; one 10-week Salt Lake City test found a small effect on "near me" queries near the coordinates and a decline on city-name queries (Search Engine Land). Separately, a Sterling Sky case study found adding photos to a profile had no measurable local pack effect | Not supported |
| FAQ on the website, auto-updated from what customers ask | Local SEO value the client does not know they need | Google limited FAQ rich results to authoritative government and health sites on 2023-08-08; Google removed public Q&A from Business Profiles (API closed 2025-11-03, removal confirmed 2025-12-03), replaced by an AI "Ask" feature. What remains: dedicated service pages are reported as the top local organic factor (Whitespark 2026, secondary), and local and AI search signals are converging | Weak (as a FAQ widget); moderate if rebuilt as service-page content |
| Website gallery widget, auto-updated | Local SEO value | Sterling Sky: website images and alt text had a minor ranking effect; photo count correlates with profile actions (BrightLocal 2019, correlational: listings with 100+ photos got 520% more calls than average) | Weak |

**Verdict on the service as a whole.** The founder's outcome for GBP manager, "better visibility and ranking", holds for the one-time optimization and not for the recurring autoposting. The recurring part can honestly promise activity ("your profile and social stay current without you"), measured as activity and profile actions, never as rank. Geotagging should be dropped from every sales asset.

---

## 3. Website (home services)

| Finding | Figure | Source | Quality |
|---|---|---|---|
| Small businesses without a website | 17% (Clutch 2025, 406 owners; Webtonic 2026 census of 91,904 local businesses) to 27% to 36% (Zippia 2023, WebFX, Moneyzine) | Various | Survey and census, definitions differ |
| HVAC companies with a website | 68,523 of 169,827 active US HVAC companies (about 40%) | Orbital, May 2026 | Vendor dataset |
| Top local organic factor | A dedicated page for each service (Whitespark 2026, via Loganix and others); doorway location pages carry risk (one HVAC company lost rankings after the March 2024 core update) | Secondary | Expert survey, secondary |
| Speed | 0.1 s faster on mobile: +8.4% retail conversions, +10.1% travel, lead-generation pages' bounce rate improved 8.3% (37 brands, 30 million sessions) | Deloitte Digital and fifty-five for Google, "Milliseconds Make Millions", 2020, web.dev case study | Primary research |
| Landing pages | Home improvement median conversion 2.6% (older Unbounce edition); pages with a mix of calls, forms, and clicks 4% | Unbounce Conversion Benchmark | Vendor dataset |
| What consumers do after a positive review | 54% visited the website (2016); 17% fewer in 2017 as more called or visited directly | BrightLocal LCRS 2016, 2017 | Survey, old |
| Market price, one-time build | Typical trade site $1,800 to $4,500; HVAC median about $6,150 (freelancer $2,900 to $9,450; agency $7,250 to $23,200); custom $8,000 to $25,000 | projectcostestimator.com, nopio.com | Vendor estimates |
| Market price, monthly | DIY builders about $9 to $29 a month; ServiceTitan's bundled site often $300+ a month; Footbridge Media $249 a month including site, hosting, SEO, citations, and review management, no build fee | mightysites.com, footbridgemedia.com | Vendor |

**Verdict: Moderate** for "online presence" as the founder states it, and the stronger, measurable outcome is calls and form fills from the site. For the ICP (established shops already running a CRM), most will have a site; the upsell is a faster site with a page per service and the reviews built in.

---

## 4. The product layer (software)

| Component | Problem it addresses | Evidence | Strength |
|---|---|---|---|
| AI voice receptionist (Pro on the pricing page) | Calls that go unanswered | Home services missed 14% of calls (CallRail, January 2025); a person answered 52% of inbound home-services calls (Invoca, July 2026; 65% excluding calls of 15 s or less); owners estimated they answered 97%, measured 66% (Service Direct). Speed matters: contacting a lead within an hour made a qualifying conversation nearly 7 times more likely than an hour later (HBR, "The Short Life of Online Sales Leads", 2011) | Moderate (problem); outcome unmeasured for Rempo |
| Unified inbox (FB, IG, GBP, SMS, email) | Messages spread across apps | Podium's ratings rest largely on its inbox (first run); demand depends on the account; the founder prefers not to add it, to limit support | Weak to moderate |
| Social media scheduler | Posting without logging in to each app | Commodity in GoHighLevel and every social tool | Weak |
| Market prices | AI receptionists about $29 to $99 a month (Dialzara, Rosie $49, Goodcall $59 to $79, Smith.ai AI-only about $95); human answering about $235 to $293 a month | dupple.com, lowcode.agency, beside.com | Vendor and affiliate guides |

---

## 5. Prices and terms in the market (for Phases 2 and 9)

| Offer | Price and terms | Source | Quality |
|---|---|---|---|
| NiceJob (software) | Reviews $75 a month, Pro $125 a month (referrals, AI replies, rebooking); volume tiers up to $290 a month reported; 14-day trial, no card; no contract | Capterra, nicejob.com LLM info, dupple.com | Vendor and directory |
| Podium (software, sold by demo) | Core about $399 a month, Pro about $599, Signature custom; annual contracts; about $50 a month per extra location | CostBench, Capterra | Third-party |
| Jobber (field-service software) | Core $39, Connect $119, Grow $199 a month for one user; marketing automation on Grow | tofu.com comparison | Third-party |
| Housecall Pro | Review requests after job completion; marketing suite an add-on, included in MAX; plan prices conflict ($49 to $79 Basic, $129 to $189 Essentials, $199 to $329 MAX) | schedulingkit.com, softwareadvice.com | Third-party |
| Footbridge Media (done-for-you contractor marketing) | $249 a month; no contract, build fee, or setup fee; website, hosting, SEO, citations, GBP optimization, automated review management (Birdeye); 90-day money-back guarantee; price fixed for three years | footbridgemedia.com | Vendor's own pages |
| Done-for-you review or GBP services | GBP management $300 to $1,200 a month per location, setup $250 to $750; ongoing optimization $125 to $500; done-for-you review services $500 to $2,500 a month; one contractor-focused service at a flat $600 a month | Agency pricing guides | Vendor guides |
| Scorpion (home-services agency) | Custom quote plus ad spend; 12+ month contracts; proprietary CMS, the site stays when the client leaves (law-firm review) | growlaw.co | Third-party, indirect |
| Lead cost benchmark | Google Local Services Ads: $53 a lead on average (HVAC $51, plumbing $57), against $149 (HVAC) and $183 (plumbing) for non-branded search leads | SearchLight Digital, February and Q1 2026, 888 contractors | Vendor dataset |
| Average job value | Plumbing $338; HVAC repair $350 | Angi cost guides (first run) | Third-party |

## 6. Cost to serve inputs (for Phase 9)

| Input | Figure | Source | Quality |
|---|---|---|---|
| GoHighLevel platform | Starter $97, Unlimited $297, Agency Pro (SaaS mode) $497 a month; usage credits for SMS, email, voice, and AI add about $30 to $300 a month per account depending on volume | ecosire.com (third-party guide) | Third-party |
| Business texting registration (A2P 10DLC) | Brand: about $4.50 (low volume) to $46 to $48.51 (standard, with vetting), one-time; campaign vetting about $15 to $16.54 one-time; campaign fee about $1.50 to $10 a month; carrier surcharges about $0.003 to $0.005 per segment (unverified) | calilio.com, bandwidth.com, Twilio support | Third-party; check current rates |
| Agency retainer churn | About 1.6% a month for retainer agencies (56-month average life); SEO services about 3.2% a month, 38% a year | agiled.app, quickseo.ai | Vendor reports |

## 7. Buyers and self-serve

| Finding | Figure | Source | Quality |
|---|---|---|---|
| B2B buyers who prefer a rep-free buying experience | 75% (2021, 725 buyers); 61% (2024, 632); 67% (2025, 646), with 45% using AI tools in a recent purchase | Gartner, via a Gartner deck, digitalcommerce360.com and distributionstrategy.com (2026-03) | Survey, secondary |
| Order bumps at checkout | Typically 15% to 40% take rate | SamCart; systeme.io calculator citing ClickFunnels public funnels (2023) | Vendor |
| One-click upsell after purchase | Typically 10% to 25%; about 20% as a planning benchmark | SamCart; systeme.io | Vendor |
| Video on a landing page | Lifts reported from +69% to +100% in vendor case studies; no benchmark for service VSLs | Unbounce and Vidyard via foundrycro.com | Vendor |
| Market size | HVAC: about 120,000 businesses (IBISWorld, NAICS 23822a, 2026) or 169,827 active companies (Orbital, May 2026); plumbing about 127,300 (IBISWorld 2025) | IBISWorld, Orbital | Paid-data publishers, public summaries |

## Not found, and left open

- Any study of personalized images in review requests or texts. Rempo's own A/B test is the only route to a number.
- Any independent data on how many reviews a done-for-you service produces against a self-run tool.
- Adoption of field-service software among small US home-service shops. The founder's own note ("they must have existing CRM") makes this a gate in the funnel; the share of buyers who fail it is measured in Phase 10.
- Google's statement on social signals and local ranking. "No evidence found" is used instead of "Google says".

## Sources

- BrightLocal Local Consumer Review Survey 2026: https://www.brightlocal.com/research/local-consumer-review-survey/ ; coverage: https://www.pinmeto.com/news/brightlocal-local-consumer-review-survey-2026/ ; https://www.socialpilot.co/reviews/online-review-statistics
- Whitespark Local Search Ranking Factors 2026: https://whitespark.ca/local-search-ranking-factors/ ; summaries: https://harmo.me/en/blog/local-seo-ranking-factors-2026-whitespark , https://blckalpaca.at/en/knowledge-base/seo-geo/local-seo/local-ranking-factors-2026-the-complete-overview , https://loganix.com/google-local-search-ranking-factors/ , https://gmbapi.com/news/local-ranking-factors-comparison-2026-2023/
- Google: https://support.google.com/business/answer/7091 ; https://support.google.com/business/answer/10515606 ; https://support.google.com/localservices/answer/7527305 ; https://support.google.com/localservices/answer/7496631 ; https://developers.google.com/search/blog/2023/08/howto-faq-changes
- Google Q&A removal: https://ppc.land/google-discontinues-business-profile-q-a-api-effective-november-3/ ; https://www.footbridgemedia.com/marketing-tips/google-shutting-down-gbp-q-a ; https://www.brightlocal.com/learn/google-business-profile-qa
- Google review policy, April 2026: https://ppc.land/google-tightens-maps-review-policy-staff-names-and-quotas-now-banned/ ; https://digitalshiftmedia.com/google-review-policy-changes-2026-home-services/ ; https://get.nicejob.com/resources/how-to-recognize-your-best-team-members-without-breaking-googles-review-rules
- FTC enforcement: https://www.lexblog.com/2026/01/02/ftc-issues-warning-letters-for-violations-of-consumer-reviews-rule/ ; https://www.beneschlaw.com/insight/five-stars-zero-tolerance-ftc-turns-up-enforcement-under-consumer-review-rule/ ; https://kjk.com/2026/08/06/ftc-consumer-review-rule-enforcement-what-businesses-need-to-know/
- Sterling Sky: https://www.sterlingsky.ca/photos-ranking-google-my-business/ ; https://www.sterlingsky.ca/services-in-google-business-profile-impact-ranking/ ; posts test via https://cubecreative.design/blog/small-business-marketing/google-business-profile-posts ; near-me study via https://get.nicejob.com/resources/do-google-reviews-help-seo-what-the-data-actually-shows
- Predefined services: https://whitespark.ca/blog/increase-local-seo-rankings-with-predefined-services/ ; https://searchengineland.com/google-business-profile-pre-defined-services-local-seo-427538
- Geotagging: https://searchengineland.com/geotagging-photos-google-business-profile-rank-453525 ; https://localmarketinginstitute.com/geotag-photos/
- Opening hours: https://insider.whitespark.ca/p/opening-hours-affecting-rankings
- Review snippets: https://whitespark.ca/blog/local-businesses-say-goodbye-to-review-snippets-in-google/
- Photos and actions: https://www.brightlocal.com/research/google-my-business-insights-study/
- Local Falcon: https://www.localfalcon.com/research/whitepaper-google-reviews-ratings--location-what-50-million-search-results-reveal-about-ranking-in-the-local-3pack
- Spiegel Research Center: https://www.xait.com/hubfs/Spiegel_Online-Review_eBook_Jun2017_FINAL.pdf
- HVAC homeowners: https://www.achrnews.com/articles/155206-91-of-homeowners-rely-on-online-reviews-before-picking-contractors
- Request rates and timing: https://gatherup.com/blog/sms-vs-email-review-requests/ ; https://focus-digital.co/average-review-response-rate/ ; https://get.nicejob.com/resources/case-study-millers-tree ; https://birdeye.com/blog/review-request-trends-2025 ; https://www.nearmedia.co/when-is-the-right-time-to-ask-for-customer-reviews/
- Personalization research: https://pmc.ncbi.nlm.nih.gov/articles/PMC1574304 ; https://link.springer.com/article/10.1186/s13104-015-1570-5 ; https://www.ssoar.info/ssoar/handle/document/44208 ; https://blog.niftyimages.com/2015/11/09/how-to-dramatically-improve-your-email-marketing-in-less-than-2-minutes/
- Integrations: https://zapier.com/apps/reviewnudger/integrations/housecall-pro ; https://help.getjobber.com/hc/en-us/articles/20621046897559-Automated-Google-Reviews
- Website: https://web.dev/case-studies/milliseconds-make-millions ; https://unbounce.com/industry/home-improvement/ ; https://projectcostestimator.com/blog/plumber-website-cost-2026 ; https://www.nopio.com/blog/hvac-website-cost/ ; https://mightysites.com/articles/website-builders-hvac-contractors-2026 ; https://withorbital.com/data/tam-reports/hvac/ ; https://www.webfx.com/blog/web-design/website-statistics
- Missed calls and speed to lead: https://stealthagents.com/research/home-services-missed-call-revenue-statistics-2026 ; https://www.mightycall.com/blog/research-businesses-arent-answering-the-phone-as-much-as-they-think/ ; https://crankwheel.com/how-to-massively-increase-the-chance-of-qualifying-sales-leads/
- AI receptionist prices: https://dupple.com/learn/best-ai-receptionists ; https://www.lowcode.agency/blog/best-ai-receptionist-for-small-business
- Competitor prices: https://www.capterra.com/p/142037/NiceJob/pricing/ ; https://get.nicejob.com/nicejob-llm-info ; https://costbench.com/software/review-management/podium/ ; https://tofu.com/blog/jobber-vs-housecall-pro ; https://schedulingkit.com/reviews/housecall-pro-review ; https://footbridgemedia.com/keith ; https://www.footbridgemedia.com/quoteiq ; https://growlaw.co/blog/scorpion-legal-marketing-review
- GBP and review service prices: https://coloradowebimpressions.com/answers/how-much-does-google-business-profile-management-cost ; https://slashpost.ai/blogs/google-business-profile/google-business-profile-optimization-cost ; https://insights.lookhin4.com/google-review-management-pricing/ ; https://builtrightdigital.com/best-remodeler-google-business-profile-agencies-compared/ ; https://www.webfx.com/digital-marketing/pricing/reputation-management/
- Lead costs: https://thevalleymarketinggroup.com/blog/google-lsa-vs-google-search-ads-service-businesses/ ; https://themediacaptain.com/google-local-service-ad-statistics/
- Cost to serve: https://ecosire.com/blog/gohighlevel-pricing-worth-it-2026 ; https://calilio.com/blogs/10dlc-pricing ; https://www.bandwidth.com/blog/how-to-register-with-10dlc-to-avoid-unnecessary-costs-in-2022/
- Churn: https://agiled.app/statistics/client-retention-statistics ; https://quickseo.ai/blog/the-state-of-the-seo-agency-industry-in-2026-50-stats
- Gartner: https://www.digitalcommerce360.com/2026/03/17/gartner-b2b-buyers-rep-free-purchasing-ai-reshapes-sales/amp/ ; https://distributionstrategy.com/2026/03/most-b2b-buyers-prefer-rep-free-purchasing-as-ai-reshapes-sales/
- Funnel benchmarks: https://www.samcart.com/blog/order-bumps-vs-upsells ; https://systeme.io/free-tools/funnel-stack-pricing-calculator/ ; https://foundrycro.com/blog/landing-page-video-benchmarks-2026/
- Market size: https://www.ibisworld.com/united-states/industry/heating-air-conditioning-contractors/1945/ ; https://www.ibisworld.com/united-states/number-of-businesses/plumbers/1946/
