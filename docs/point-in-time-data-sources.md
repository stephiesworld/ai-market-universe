# Point-in-time data sources for the first real PEAD experiment

Research date: August 24, 2026

## Decision

Do not purchase or integrate a provider yet.

The recommended next action is a **schema-level evaluation extract** from Intrinio/Zacks for the smallest technical pilot, while requesting equivalent samples and quotes from S&P Global and FactSet. If institutional or university WRDS access already exists, test LSEG I/B/E/S plus CRSP before paying another vendor.

The recommendations are conditional:

1. **Best exact-timestamp fit:** S&P Capital IQ Estimates Snapshot, subject to a successful trial and acceptable license. It snapshots all estimate changes every two hours from August 2016 and exposes effective-from/effective-to timestamps.
2. **Best documented daily PIT consensus:** FactSet Estimates Point-in-Time Consensus, with history from December 2009 and local-midnight snapshots designed to exclude later data. Broker-detail endpoints also expose a source-availability datetime.
3. **Best deep academic/research history:** LSEG I/B/E/S, especially when accessible through WRDS, paired with CRSP for identifiers, returns, and delistings.
4. **Best candidate for a small, low-commitment PEAD plumbing pilot:** Intrinio's Zacks EPS and sales surprise data, because the public schema includes pre-release mean estimates, actuals, report dates, report times, and BTO/DTM/AMC release codes. This recommendation remains conditional because the public documentation does not prove that historical estimate/revision records are immutable vintages.

No source receives `point_in_time_verified=true` merely because its product name contains “historical” or “point in time.” That flag requires a passed sample audit and a written answer about revision/restatement behavior.

## Required information contract

For an observation queried as of timestamp `T`, the source must support or allow conservative derivation of:

| Field | Meaning |
| --- | --- |
| `value` | Numeric or categorical observation; `null` when unavailable. |
| `as_of` | Exact timestamp at which the harness asks what was knowable. |
| `published_at` | Source-native publication or contribution timestamp. |
| `effective_at` | Fiscal period or business date represented by the value. |
| `available_at` | Earliest defensible timestamp when the system could have used it. |
| `ingested_at` | Timestamp when this project captured the record. |
| `source` | Vendor and product identifier. |
| `source_record_id` | Stable vendor record identifier. |
| `point_in_time_verified` | True only after the source passes the vintage audit. |

Immediate rejection conditions:

- Historical queries return today's cleaned or restated value without preserving the original vintage.
- The only “date” is a fiscal-period end date rather than an estimate-publication or availability date.
- A consensus value can change retroactively without a recorded validity interval or revision record.
- Announcement timing cannot distinguish at least before open, during market, and after close.
- The license prohibits internal backtesting, retaining derived features, or keeping reproducibility metadata.
- Delisted securities disappear or identifiers are recycled without permanent mappings, unless the pilot explicitly accepts and discloses that limitation.

## Expectations and earnings-event sources

### Comparison

| Candidate | Historical consensus vintages | Announcement timing | Coverage/history | Access and public pricing | `available_at` assessment | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| **S&P Capital IQ Estimates Snapshot** | Explicit point-in-time history; snapshot every two hours; `spEffectiveDate` and `spToDate`; snapshot history from August 2016. | S&P has broader event data, but the public estimates page does not prove the exact earnings-release timestamp fields. Require an event-schema sample. | S&P states 60,000+ public companies for Capital IQ Estimates and earliest general estimates coverage from 1996; snapshot PIT begins in 2016. | API, cloud, desktop, and feed delivery. Public pages route to sales; trial and research subscriptions are available, but price is not posted. | **Strongest candidate** for intraday validity intervals, pending trial. | Enterprise finalist. |
| **FactSet Estimates PIT + Estimates API** | Daily PIT consensus from December 2009; local-market-midnight snapshots exclude data entered later. Broker-detail endpoints include `inputDateTime`, described as when data became available at the source. | FactSet's Events and Transcripts API includes calendar events and metadata, but the public overview does not establish the exact historical release-time field. Require a sample. | PIT consensus: 10+ years, global, 800+ contributors. General estimates API: 20+ years of broker history and 59,000+ historical companies. | API/feed/desktop; sales contact, no posted package price. | **Verified for daily midnight snapshots** if used exactly as documented. Exact 2:00 PM reconstruction requires broker detail or another source. | Enterprise finalist. |
| **LSEG I/B/E/S + events** | Detail, summary, comparable actuals, and explicit History/PIT products. U.S. estimates history reaches 1976. History feed is distributed monthly; real-time and intraday products are separate entitlements. | LSEG offers event-calendar packages with long-term history, but public documentation reviewed here does not tie each historical earnings actual to a precise release timestamp. | 23,000+ active companies, 90+ countries, 950+ contributors; deep U.S. history. | API, Workspace, Datastream, feeds, FTP, cloud; quote-only through sales. WRDS access may eliminate a new direct purchase for eligible institutions. | **Excellent daily/research candidate**, but exact timestamp semantics must be proven for the selected package. | Best if WRDS/institutional access exists. |
| **Intrinio/Zacks estimates and surprises** | Surprise records expose a pre-release consensus. Separate EPS/sales estimate endpoints expose means and trailing 7/30/60/90-day comparisons, but the public schema does not identify a historical snapshot-availability timestamp for each vintage. | Explicit `actual_reported_time` and BTO/DTM/AMC codes. | Surprise feed: 17,000+ U.S./Canadian listed companies. EPS estimate product: 5,000+ companies. Intrinio advertises 20+ years for enterprise estimate products. | API/CSV/S3/Snowflake; enterprise only for estimates, free trial offered, historical access may require a one-time payment. Price is quote-only. | **Conditional.** Basic surprise fields are promising; revisions and vintage immutability are not publicly proven. | Best technical-pilot candidate if sample passes. |
| **Nasdaq Data Link Zacks products** | Zacks Earnings Estimates and Announcements are premium tables. Public API documentation exposes table snapshot/refresh times, but those describe the delivered table, not necessarily when each historical estimate became knowable. | Product family includes Zacks Earnings Announcements; exact historical release-time fields were not established from public documentation reviewed. | Premium Zacks tables via the Data Link Tables API. | API/CSV/JSON/XML. Product pricing and detailed schema require account access; current docs are scheduled to move after August 31, 2026. | **Unverified.** A table refresh timestamp is not a per-record availability timestamp. | Do not select without a full schema/sample. |

Primary evidence:

- [S&P Capital IQ Estimates](https://www.spglobal.com/market-intelligence/en/solutions/capital-iq-estimates) documents two-hour snapshots, the 2016 start, and effective-date fields. [S&P's broader data page](https://www.spglobal.com/market-intelligence/en/solutions/products/fundamental-data) describes coverage and delivery, while its [Marketplace FAQ](https://www.marketplace.spglobal.com/en/support/faq) confirms trial licenses and discounted research subscriptions.
- [FactSet PIT Consensus](https://insight.factset.com/resources/at-a-glance-factset-estimates-point-in-time-consensus) documents the local-midnight exclusion rule and December 2009 history. The [FactSet Estimates API](https://developer.factset.com/api-catalog/factset-estimates-api) documents broker history and `inputDateTime`; the [Events and Transcripts API](https://developer.factset.com/api-catalog/events-and-transcripts-api) describes calendar-event access.
- [LSEG I/B/E/S](https://www.lseg.com/en/data-analytics/financial-data/company-data/ibes-estimates) documents its coverage, history, delivery products, and update frequencies. WRDS explicitly recognizes I/B/E/S as a widely used empirical-research source and warns that provenance and historical revisions matter in its [I/B/E/S research material](https://wrds-www.wharton.upenn.edu/pages/news/research-webinar-ibes-unpacked/).
- [Intrinio's Zacks EPS surprise schema](https://docs.intrinio.com/documentation/web_api/get_zacks_eps_surprises_v2) documents pre-release mean EPS, actual report time, and BTO/DTM/AMC codes. Its [estimate pricing/product page](https://intrinio.com/pricing) states enterprise access, trials, delivery methods, and 20+ years of history. The [EPS estimate schema](https://docs.intrinio.com/documentation/web_api/get_zacks_eps_estimates_v2) illustrates why a sample audit is still required: its `date` is the period-end date and it does not publicly expose a per-vintage availability timestamp.
- [Nasdaq Data Link's product index](https://docs.data.nasdaq.com/docs/data-organization) lists the Zacks premium tables; its [Tables API documentation](https://docs.data.nasdaq.com/docs/api-and-analysis-tools-for-tables-data) states that most tables update daily with a lag. That is insufficient by itself to prove historical per-record availability.

## Prices, identifiers, delistings, and universe history

Consensus data does not solve survivorship or return-label integrity. A separate price/reference source may be required.

| Candidate | Strengths | Limitations/licensing | Public price as of research date | Recommended role |
| --- | --- | --- | --- | --- |
| **CRSP U.S. Stock Database** | Permanent PERMNO identifiers, return histories, explicit delisting codes, delisting prices and returns, corporate-action handling. | Institutional/academic product; quote/subscription access rather than a lightweight retail API. | Not publicly posted. | Research-grade default when WRDS access exists. |
| **Norgate Data Platinum** | Daily U.S. history from 1990, delisted securities, historical S&P/Russell constituents, and survivorship-aware integrations. | Personal use only; Windows-based updater/Python integration; access ends with subscription; public-repo redistribution is not allowed. Norgate says its delisted set is extensive but does not claim complete early-history coverage. | $346.50 for six months or $630 for 12 months. | Affordable historical-universe audit source if a Windows workflow is acceptable. Not the first Mac/cloud integration. |
| **Tiingo Power** | Raw and adjusted EOD prices, dividends/splits, explicit correction timing, stable `permaTicker` support for delisted/recycled symbols, simple REST API. | Internal-use license; no public claim of complete historical index membership or comprehensive delisting-return treatment. | $30/month or $300/year for individuals. | Good price source for a fixed 10–20 stock technical pilot. |
| **EODHD** | API access to adjusted EOD data, delisted symbols, symbol-change history, and historical S&P constituent records; low entry price. | Personal and commercial licenses differ materially. Historical constituent coverage is described as up to 12 years, and the provider cautions that some market data may be indicative. Validate exchange-close and corporate-action fields. | $19.99/month personal EOD; $99.99/month personal all-in-one; commercial internal-use plan listed at $399/month. | Alternative pilot/reference source; not a research-grade substitute for CRSP without validation. |

Primary evidence:

- [CRSP's research product overview](https://www.crsp.org/research/) explains permanent identifiers and historical continuity. Its [U.S. Stock and Indexes data guide](https://www.crsp.org/wp-content/uploads/guides/CRSP_US_Stock_%26_Indexes_Database_Data_Descriptions_Guide.pdf) documents delisting-return calculation and missing-return codes.
- [Norgate package details and prices](https://norgatedata.com/stockmarketpackages.php) list delisted securities and historical constituents at Platinum/Diamond tiers. Its [subscription terms](https://norgatedata.com/subscribe/subscribe.php) state personal-use-only licensing and Windows/Python limitations.
- [Tiingo EOD documentation](https://www.tiingo.com/documentation/end-of-day) documents raw/adjusted data and correction timing; its [fundamentals documentation](https://www.tiingo.com/documentation/fundamentals) documents stable identifiers for delisted/recycled tickers. [Tiingo pricing](https://www.tiingo.com/about/pricing) states the internal-use license and current prices.
- [EODHD delisted-data documentation](https://eodhd.com/financial-apis/delisted-stock-companies-data-2), [historical constituent documentation](https://eodhd.com/financial-apis-blog/reworked-sp-500-historical-constituents), and [pricing](https://eodhd.com/pricing) support the comparison above. [Commercial pricing](https://eodhd.com/commercial-pricing) is materially higher than personal pricing.

## Smallest real dataset before a major purchase

### Stage A: technical pilot

Purpose: validate the harness, not the PEAD hypothesis.

- **Universe:** 20 U.S. common stocks across at least five sectors, including profitable/unprofitable companies, positive/negative EPS, BTO/AMC releases, ticker changes, and at least one missing-consensus event.
- **Period:** 12 fiscal quarters, preferably 2022–2025.
- **Expected events:** approximately 240 earnings observations before exclusions.
- **Benchmarks:** SPY plus the relevant sector ETFs.
- **Market window:** at least 60 trading days before each event through 100 calendar days after it.
- **Required earnings fields:** permanent company/security IDs, fiscal period, actual EPS, pre-release consensus EPS, estimate count and dispersion, actual revenue, pre-release consensus revenue, announcement date, time, timezone or BTO/DTM/AMC code, vendor record ID, and source update/availability metadata.
- **Required market fields:** raw and adjusted OHLCV, dividends, splits, trading status, exchange, symbol history, and benchmark prices.
- **Nice-to-have, not required:** guidance and estimate revisions.

Acceptance criteria:

1. Repeating the same historical query produces an identical vendor record or an auditable new version.
2. At least 25 sampled events can be reconciled to timestamped company releases or SEC filings.
3. The pre-release consensus is demonstrably the value known before the release.
4. BTO/AMC classification agrees with observed market sessions.
5. Splits and dividends reproduce vendor total returns within a documented tolerance.
6. Missing consensus remains `null`; no zero-filling occurs.
7. Vendor terms permit retaining source record IDs, timestamps, derived features, and reproducibility hashes.

### Stage B: analytical pilot

Purpose: estimate whether basic PEAD survives a recent, out-of-sample test.

- **Universe:** 100–250 historically eligible, liquid U.S. common stocks, including companies that later delisted or left the universe.
- **Period:** at least five years, with a fixed temporal train/validation/test split.
- **Expected events:** roughly 2,000–5,000 observations.
- **Core features only:** EPS surprise, revenue surprise, initial abnormal return, abnormal volume, 20/60-day pre-event momentum, sector, market regime, and days-to-next-event where available.
- **Targets:** 5/20/60/90-day benchmark- and sector-relative returns.
- **Models:** zero, momentum, simple PEAD rule, regularized linear model, then one tree model.

Do not purchase valuation, textual, guidance, or detailed broker-level packages until this core experiment passes data-integrity checks and produces stable evaluation outputs. A null signal is a successful harness validation.

## Conservative event clock

The first experiment can remain defensible even when a vendor supplies only BTO/DTM/AMC rather than an exact minute:

- **BTO:** event-reaction window ends at that trading day's close; prediction begins after that close.
- **AMC:** event-reaction window ends at the next trading day's close; prediction begins after that close.
- **DTM or ambiguous:** conservatively begin after the next trading day's close.

The consensus feature must come from the last snapshot whose availability precedes the announcement. If only daily snapshots exist, use the prior completed snapshot rather than a same-day value whose availability is ambiguous. This may sacrifice freshness, but it does not sacrifice causal validity.

## Vendor evaluation request

Ask every finalist for the same 20-stock/12-quarter extract and written answers to these questions:

1. What exact event creates the estimate timestamp: analyst submission, vendor receipt, quality-control approval, snapshot generation, or API publication?
2. Are original estimate values retained after corrections, exclusions, accounting-basis changes, and restatements?
3. Can the API reconstruct the value known at an arbitrary historical datetime? If not, what snapshot cadence is guaranteed?
4. Does the historical surprise record preserve the consensus that existed immediately before release, or is it recomputed today?
5. Which timezone applies to release timestamps, and how are DST and unknown times represented?
6. Are BTO/DTM/AMC codes historically revised? Are both original and corrected codes retained?
7. Are inactive and delisted securities included? How are ticker reuse, mergers, and share-class changes mapped?
8. May we retain raw samples internally, store source record IDs and hashes, publish derived aggregate metrics, and use features in model training?
9. What happens to stored data and derived artifacts when a trial or subscription ends?
10. What is the price for the technical extract, a five-year 250-stock research license, API access, and later prospective weekly updates?

## Go/no-go recommendation

Proceed only after one expectations/events candidate and one price/reference candidate pass the same technical pilot.

- **If WRDS access exists:** start with I/B/E/S Detail/Point-in-Time plus CRSP. Add a specialist event-time source only if I/B/E/S actuals cannot support the conservative BTO/AMC clock.
- **Without WRDS and before enterprise spend:** request the Intrinio/Zacks trial extract. Pair it with Tiingo for the fixed 20-stock price pilot. Do not use Intrinio revision features until historical vintage semantics are confirmed.
- **For a serious analytical license:** compare the same extract from S&P Estimates Snapshot and FactSet PIT/detail. Prefer S&P when exact two-hour validity intervals are essential; prefer FactSet when daily PIT consensus plus transparent broker detail is sufficient and its commercial terms are better.
- **For survivorship-sensitive scale:** use CRSP where possible. Norgate Platinum is a lower-cost personal research alternative but introduces Windows and license constraints. EODHD can be evaluated as an API-native alternative, but it should not be assumed equivalent to CRSP.

The first purchase should be the smallest extract that proves `available_at`, not the package with the largest feature count.
