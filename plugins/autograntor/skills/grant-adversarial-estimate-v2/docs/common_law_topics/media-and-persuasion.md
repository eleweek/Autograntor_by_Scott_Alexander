# Common Law topic file — media and persuasion

Verbatim copies of Proposed rulings from Part III of `claude/common_law.md` (frozen original, version 2026-10-20.1), grouped by topic. The original remains the source of truth. Rulings in this file: CL-24, 25, 26, 30, 71, 77, 78, 80. Read it together with `claude/PERCYs_v4.md` for any grant with media, audience, creator, game or campaign rows.

### CL-24: Games as an exposure class, and their borrowed streaming reach [Proposed 2026-10-17, by Claude]
**Rule:** For a video game, split owners by playtime: heavy players (>20h) as Sustained (Y=3) with Δ cut by a message-fidelity factor (≈0.4–0.6 when the argument is carried by mechanics rather than text); 1–20h as Long-form; <1h and free-demo players as Glance; never-launched owners at zero. Stream audiences are borrowed reach counted in unique viewers: full let's-play viewers ≈0.3 per copy sold (Engaged, Long-form), clip/feed viewers ≈2.5 per copy (General, Glance). Apply the fidelity cut once, to Δ; don't also lower Y or add a separate blanket backfire haircut.
**Why:** The PERCYs exposure classes don't describe deep interactive play; without a rule, estimators either treated all players as a year-long returning audience or double-discounted them.

### CL-25: Cultural-hit lump for mass media [Proposed 2026-10-17, by Claude]
**Rule:** For a game, film or similar product, add at most one step row for a cultural breakout, only at clear thresholds (e.g. ≥300k and ≥1M owners for a game; nothing at 100k), priced at no more than about 1/8 of the smallest comparable listed social-shift entry, counted once; the audience below those thresholds stays in the per-person PERCYs rows.
**Why:** CL-6 makes listed entries (IABIED bestseller, AI 2027) upper bounds and CL-5 forbids re-counting the same audience; the nearest precedent (Universal Paperclips) produced no listed milestone.

### CL-26: Talent redirected by entertainment media [Proposed 2026-10-17, by Claude]
**Rule:** Price people a piece of media moves into safety work as discrete (Poisson) events. Anchor the rate on HPMOR (~1 per 5k readers) scaled down by how explicitly the work points at the field (≈1/20–1/30 for a work that never names it), with "would have entered anyway" inside the rate. Value each at pre-2030 researcher-years (with a ramp) plus post-2030 years at the TAI discount, at the researcher-year price.
**Why:** The PERCYs pipeline rule prices communicator output, not research careers, and this row is often the largest one in a media grant, so it needs a common anchor.

### CL-30: Applicant-defined reach metrics need an audit before conversion [Proposed 2026-10-17, by Claude]
**Rule:** Before converting an applicant's topical reach figure (e.g. "topic-relevant views") to PERCYs, check any single item over ~25% of the total and look for an independent audit. Convert only strictly on-topic units at the full PERCYs rate and the applicant's broader category at about one-third of it; adjacent content that does not move the AI-risk scale counts at ≤0.25. If no audit exists, assume the applicant's figure is about 3× the strict one. Apply any salience-saturation factor after major warning-shot events to general-audience Δ only, and state it.
**Why:** A single viral adjacent item can dominate an applicant's reported total, and independent audits can find the strictly on-topic figure is a small fraction of the headline; Δ per glance-view also falls once most of the audience has a handle on the issue.

### CL-71: Geographic leverage for non-US general audiences in PERCYs [Proposed 2026-10-20, by Claude]
**Rule:** PERCYs field rows are calibrated on US adults. For media whose audience is partly outside the US, count the US-resident share at full value and price the rest at a stated leverage factor: for general publics, about 0.1 for countries without frontier labs or a seat at frontier-AI negotiations, and up to the CL-51 executive factor for countries that have one. Apply it once, to N, and state the US-resident share and its source.
**Why:** Without a factor, foreign-language channels with mostly non-US audiences are priced as if every viewer were a US voter, which can triple the media rows.

### CL-77: Comparator audits count on-topic partner content as on-topic [Proposed 2026-10-20, by Claude]
**Rule:** When an audit of a comparable program is used to set the CL-30 inflation factor, the ratio is the program's headline figure ÷ all strictly on-topic views the program reported, including on-topic pieces by mentors or partners that the program counted; only off-topic or adjacent items count as inflation. Report the stricter "program participants only" ratio as a sensitivity.
**Why:** Counting a partner's genuinely on-topic content as inflation roughly triples the implied discount and, transferred to another applicant, removes most of its attention rows on a definitional choice rather than evidence.

### CL-78: Unpaid creator pledge coalitions [Proposed 2026-10-20, by Claude]
**Rule:** A coalition of creators who sign an unpaid public pledge is an Output row for its moment value, priced below the nearest listed statement or letter (CL-6), plus a Relay row (PERCYs §4) only for the extra on-topic pieces it demonstrably causes. Never convert the signatories' combined subscriber counts to PERCYs, and treat headline audience totals of overlapping channels as an upper bound on unique reach.
**Why:** Combined follower counts overlap heavily and measure the creators' existing audiences, not what the pledge changed; converting them directly overstates such campaigns by an order of magnitude.

### CL-80: Salience versus opinion change in mass-attention campaigns [Proposed 2026-10-20, by Claude]
**Rule:** Price a campaign whose stated goal is attention or salience through PERCYs rows with CL-30 saturation on general-audience Δ, plus small-ΔP Outcome rows on listed or Proposed entries for "activation" (champions, bills, sponsors), plus at most one Output row for the chance the campaign becomes a listed-scale moment, with one signed overlap line between the activation rows and the Output rows. Do not invent a bespoke salience milestone or unit.
**Why:** Salience matters mainly through the political actions it enables, which the weights list already prices; a large invented salience milestone lets one row dominate the ledger with no comparable on the list.
