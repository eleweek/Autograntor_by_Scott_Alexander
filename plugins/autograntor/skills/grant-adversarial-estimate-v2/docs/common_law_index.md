# Autograntor Common Law — Index (one line per ruling, CL-1 to CL-83)

Covers the frozen original `claude/common_law.md`, version 2026-10-20.1, with later changes by the human user on 2026-11-10 (core file version 2026-11-10.2): CL-4's money price now comes from the funder table in CL-91, CL-8 is reworded, and CL-91 is new. Where a Proposed line below mentions "the money price" or equal probabilities in both worlds, CL-91 governs. Adopted rulings are in full in `claude/common_law_core.md` (always read). Proposed rulings are in full in `claude/common_law_topics/<file>.md`; read the topic files the coordinator names for this grant, and fetch any other ruling's full text from its topic file before citing it. Rulings added after the freeze live in `claude/common_law_proposed/` and are not indexed here.

Format: `CL-n | status | topic file | one-line summary`. Status: A = Adopted, P = Proposed, S = struck or superseded (do not apply).

## Adopted (full text in common_law_core.md)
- CL-1 | A | core | A value is the counterfactual value of the thing existing, judged from 2030, including everything downstream; consequences are signed.
- CL-2 | A | core | Forecast credit = P(outcome|cause) − P(outcome|no cause); historical credit = 1 − P(outcome|cause absent).
- CL-3 | A | core | No credit pie: each cause gets full counterfactual credit; no Shapley shares; chains lose credit only through "would have happened anyway".
- CL-4 | A | core | Charge for follow-on resources a grant pulls in: money at the supplying funder's CL-91 price (50/$1M at the top tier), people at researcher-year or policy-year prices, weighted by P(spent).
- CL-5 | A | core | Count each consequence once; label rows Output / Outcome / Upgrade; every overlapping pair gets a one-line reason or a signed overlap row.
- CL-6 | A | core | Historical entries price old things; a new institution is worth less than its historical comparable, which is an upper bound.
- CL-7 | A | core | Value as seen from 2030; discount post-2030 effects for TAI; always report the post-2030 share.
- CL-8 | A | core | No-grant world: the platform's money is not replaced by the platform; existing funds, pledges and revenue stay; outside funders behave as they really would in each world (CL-91).
- CL-9 | A | core | Scale-up check: multiply up to the full budget, check implied probability shifts and track record (softened by CL-15).
- CL-10 | A | core | Pricing outcomes not on the list: SB 53 copies ≤ RAISE; implementation only as a checkable event; lab influence at the lab-point price; else price by named comparables.
- CL-11 | A | core | Contested values questions: price both ways and report both to the human user.
- CL-12 | A | core | Other evaluators' opinions are evidence: weight by track record and access, discount conflicts, flag reliance on one view.
- CL-13 | A | core | Generic prices are marginal unit prices: cross-checks, never a start point, ceiling or linear multiplier.
- CL-15 | A | core | CL-9 is a soft check against the org not existing; grants may exceed the org's average dollar for stated, checkable reasons; always report the average dollar.
- CL-33 | A | core | Clean-refund branches are dropped; headline figures are conditional on disbursement.
- CL-62 | A | core | Other evaluators' same-round platform allocations are left out of both worlds; outside money stays per CL-8/CL-43.
- CL-91 | A | core | Funging: report a base value (every dollar net new) and a with-funging headline; displacement capped at 75% of the grant; displaced dollars credited at the funder-tier price (50/33/10/4/0 per $1M) × 0.8.

## Proposed — money, funders and the no-grant world (topic file: money-and-funders.md)
- CL-14 | P | money-and-funders | A pending application elsewhere is an event at a stated probability in both worlds; differs between worlds only for a stated, small reason.
- CL-21 | P | money-and-funders | Freed backstop: credit dollars a grant releases at the CL-4 money price × P(backstop drawn).
- CL-23 | P | money-and-funders | Reported-but-unlisted grants are pledges at a stated probability; use per-year operating-at-scale probabilities with partial-loss states, not binary survival.
- CL-28 | P | money-and-funders | Earned revenue is CL-8 revenue, not a CL-4 charge; follow-on grants are charged at the money price, scaled by traction; don't charge continuation twice.
- CL-34 | P | money-and-funders | Intended but unsubmitted application to a repeat funder: same probability in both worlds; expected award falls convexly with grant size; freed money credited at the money price.
- CL-35 | P | money-and-funders | Grant above absorptive capacity even within the ask: cap plan-year spend from the applicant's hiring statements; bank the rest as a money-price / next-year-program mixture plus an idling charge.
- CL-41 | P | money-and-funders | When the applicant says funding sets plan ambition, raise the CL-35 cap by ≈0.3 of the grant (hiring-rate cap still applies to FTE spend).
- CL-43 | P | money-and-funders | Funders outside the platform keep their independent money in the no-grant world; same-round platform allocations are not outside money (CL-62).
- CL-44 | P | money-and-funders | Unfilled donor-adviser recommendations are pending money; blend funding states with a marginal factor per state.
- CL-53 | P | money-and-funders | Applicant minimum-size statements: the no-grant world runs the project only if independent pending money reaches the minimum; the grant's increment is the top-up.
- CL-63 | P | money-and-funders | Option-value grants to well-funded orgs with no stated plan: CL-35 mixture plus at most one bounded ambition row; never credit the flagship's existence.
- CL-64 | P | money-and-funders | Distraction row for money above absorptive capacity: leaders pulled into weaker projects, probability rising with the excess, cost ≈ a tenth of a senior-team year.
- CL-65 | P | money-and-funders | Debts to the platform operator or an evaluator's org: reduce runway in both worlds, never credited as value; conflict discounted under CL-12 and priced as a small exposure row.
- CL-66 | P | money-and-funders | When the ordinary funder is a routine patron, set the displaced share from the applicant's likely change in its own ask, not runway arithmetic.
- CL-72 | P | money-and-funders | Merged funding targets or cash above the scored ask: value the grant as unrestricted money allocated by the org's own statements; report the restricted value as a sensitivity.
- CL-75 | P | money-and-funders | Matching pledges small relative to ordinary fundraising: P(grant pivotal) ≈0.1 or less; unlocked money at the grant's marginal rate net of the money price.
- CL-83 | P | money-and-funders | Under CL-72, when the restricted value is below the unrestricted value, say so; unrestrictability is then not a cost.

## Proposed — expansion, hiring and the marginal factor (topic file: expansion-and-hiring.md)
- CL-22 | P | expansion-and-hiring | Grants above the ask: price the excess as runway plus the applicant's weakest initiatives with an idling charge; assume diminishing returns except at named thresholds.
- CL-36 | P | expansion-and-hiring | Scaling risk as signed rows: Poisson bad hires (≈1 per 3 beyond identified candidates) and a management-breakdown episode rising ≈cubically with expansion; no separate drag term.
- CL-37 | P | expansion-and-hiring | Marginal factor for new staff is bounded by the non-founder average dollar; correlated execution factor only on program rows, not charges.
- CL-38 | P | expansion-and-hiring | Persistence of grant-funded hires at a surviving org counts only as a timing gain (≈0.1–0.2 of the plan-year increment) net of a money charge.
- CL-39 | P | expansion-and-hiring | When the marginal dollar buys contractors: CL-36 on FTE hires only, no CL-4 people charge on contractors, CL-38 at the bottom of its range, exposure rows scale with campaigns.
- CL-40 | P | expansion-and-hiring | Substantive downside rows scale with share × marginal factor; exposure rows scale with activity share; neither is multiplied by the execution factor.
- CL-54 | P | expansion-and-hiring | Mostly-volunteer orgs: report the average dollar on cash and on cash plus imputed volunteer labour; blend the CL-37 comparator by how much the paid role substitutes for volunteers.
- CL-56 | P | expansion-and-hiring | The CL-37 org value must be checked against track record (≤ ~1.5× without a specific reason); CL-15's strongest-line exception needs a hire-specific, checkable reason.
- CL-57 | P | expansion-and-hiring | Report the grant figure with and without funder-specific and hire-specific rows when comparing with the org average (optional).
- CL-60 | P | expansion-and-hiring | No CL-36 breakdown charge in worlds already scored as a collapse; identified candidates already paid by outside money are not grant-funded.
- CL-61 | P | expansion-and-hiring | Founder-gated sensitive work: scale incident and exposure rows with activity^0.7; report the linear version as a sensitivity.
- CL-67 | P | expansion-and-hiring | People charge for a role the losing org will refill: unit price × (1 − P(refilled within a quarter)), default 0.5; apply once.
- CL-70 | P | expansion-and-hiring | No-grant baseline for a founder with a day job: ≈0.1–0.2 FTE on lines needing no money, no pipeline or continuation rows beyond what part-time work already produced.

## Proposed — media and persuasion (topic file: media-and-persuasion.md)
- CL-24 | P | media-and-persuasion | Games: split owners by playtime into exposure classes with a message-fidelity cut on Δ; stream audiences are borrowed reach at stated ratios per copy.
- CL-25 | P | media-and-persuasion | Cultural-hit lump for mass media: at most one step row at clear thresholds, ≤ ~1/8 of the smallest comparable social-shift entry.
- CL-26 | P | media-and-persuasion | Talent redirected by entertainment media: Poisson events anchored on HPMOR (~1 per 5k readers) scaled down by how explicitly the work points at the field.
- CL-30 | P | media-and-persuasion | Audit applicant reach metrics before converting to PERCYs: strict on-topic at full rate, broader category at ~1/3, adjacent ≤0.25; no audit → assume ~3× inflation; salience saturation on general-audience Δ only.
- CL-71 | P | media-and-persuasion | Non-US general audiences in PERCYs: US-resident share at full value, the rest at ≈0.1 (no frontier labs) up to the CL-51 executive factor; apply once to N.
- CL-77 | P | media-and-persuasion | Comparator audits: a partner's on-topic content counts as on-topic, not inflation; report the participants-only ratio as a sensitivity.
- CL-78 | P | media-and-persuasion | Unpaid creator pledge coalitions: an Output row below the nearest listed statement plus a Relay row for pieces demonstrably caused; never convert combined subscriber counts.
- CL-80 | P | media-and-persuasion | Salience campaigns: PERCYs rows with CL-30 saturation, small-ΔP activation rows, at most one listed-scale-moment row with an overlap line; no bespoke salience milestone.

## Proposed — policy, laws and non-US actors (topic file: policy-and-laws.md)
- CL-45 | P | policy-and-laws | Ladder rows for successive upgrades of one jurisdiction's law; each rung an increment with its own P(reached by 2030); fold authority use into the rung that creates it.
- CL-46 | P | policy-and-laws | Attribute a multi-year outcome to one funded year by the share of critical-path effort in that year, summing to ≤1 across years; never pro-rata by budget.
- CL-47 | P | policy-and-laws | Candidate fundraising: value only through the laws it makes likelier; partisan-coding risk as a signed exposure row; integrity harm in a CL-11 branch; price any restricted no-elections account.
- CL-48 | P | policy-and-laws | c4 dollars are valued by what they buy at the tranche's marginal factor; never multiply by the c3:c4 indifference ratio or raise the money price.
- CL-49 | P | policy-and-laws | State-law rows: enactment probability × P(still in force in 2030) with a preemption loss factor that bites hardest on stronger rungs; anti-preemption work in its own row.
- CL-50 | P | policy-and-laws | Paired c3/c4 orgs: one ledger, one joint program budget built on a realistic hiring ramp.
- CL-51 | P | policy-and-laws | Leverage factors for non-US national actors: executives (France/Germany ≈0.2–0.3, UK ≈0.25, EU ≈0.4–0.5, other G7 ≈0.1–0.15); individual legislators ≈0.10 where treaty policy is executive-reserved; apply once.
- CL-52 | P | policy-and-laws | Recruit-on-funding lags (default 2–3 months), dated-window rows priced on post-lag critical-path share, part-time roles at ≈0.4–0.5 of full-time.
- CL-68 | P | policy-and-laws | "Actor newly becomes X" milestones that may already have happened: re-scope as "an additional actor", price at ≈0.4–0.6 of the original, raise the base rate.
- CL-69 | P | policy-and-laws | External base rates with looser resolution than the row: build a two-rung ladder (loose event at the forecast rate, strict event as an increment).

## Proposed — reputation, conflicts and values questions (topic file: reputation-and-values.md)
- CL-17 | P | reputation-and-values | A CL-11 branch changes only the rows whose sign or size depends on the answer (plus strongly correlated ones); never a general pessimism multiplier.
- CL-20 | P | reputation-and-values | Projects of a troubled parent or fiscal sponsor: price liability exposure, an incident row and a CL-11 trust-norm row separately, sublinear in size.
- CL-27 | P | reputation-and-values | Deliberately edgy products: "hostile piece names the funder" at ≈3% base plus ~1 point per $1M above the ask, ×3 with traction, cost ≈ −50.
- CL-32 | P | reputation-and-values | Already-run hostile stories aren't charged but raise sequel probability; founder-profile risk ≈8–12%/yr at ≈ −100 (×2 in the harm branch); serious-incident row for residential programs.
- CL-42 | P | reputation-and-values | Bound a sequel story's cost by the realised bite of stories that already ran; ≤ ~ −600 per story for an advocacy org in a live fight.
- CL-73 | P | reputation-and-values | A leader's conflict of interest at an evaluation org: separate rows for credibility haircut, public story, actual bias and conflicted-role adoption; trust-norm harm in a CL-11 branch.
- CL-74 | P | reputation-and-values | When CL-11 branches flip the sign, report the fixed-weight spread and every corner; correlate overlapping values questions at a stated coefficient.
- CL-76 | P | reputation-and-values | Under CL-62, endorsement and trust-norm rows grow with grant size at ≈G^0.7; report the flat version as a sensitivity.
- CL-79 | P | reputation-and-values | Applications that withhold plans: CL-30 no-audit default, wider execution dispersion, a signed fungibility row; no separate secrecy haircut.
- CL-81 | P | reputation-and-values | Unverified integrity allegations in evaluator notes: carry at a stated probability in exposure rows only; late self-disclosure counts as disclosed for CL-73 but is evidence for the trust weight.
- CL-82 | P | reputation-and-values | Values objections to attention-maximising persuasion: a CL-11 question; in the harm branch reverse a stated fraction of glance and long-form Output rows only.

## Proposed — method, venues and programs (topic file: method-and-programs.md)
- CL-16 | P | method-and-programs | P10/median/P90 are quantiles of realised 2030 value: simulate whether outcomes happen; continuous effects stay in at full EV; rank by mean.
- CL-18 | P | method-and-programs | "Post-2030" means value from activity after 2030, discounted for TAI; unit prices are already 2030 values, so don't split and discount their downstream again.
- CL-19 | P | method-and-programs | Hosted programs at a venue get a venue/ops share (≈20%); self-run programs get full credit × P(runs) × a first-run quality factor (≈0.7).
- CL-29 | S | method-and-programs | Leader-commitment-gated refundable grants (superseded in part by Adopted CL-33; headline is now conditional on disbursement).
- CL-31 | P | method-and-programs | Continuation of a program that dies without the grant: per-year probabilities on the same per-cohort ledger with crowding decay and money charges; report the funded-year share.
- CL-55 | P | method-and-programs | CL-16 amendment: for traceable rows simulate pivotal (large, rare) and diffuse (small) credit separately; untraceable rows keep the plain CL-16 credit.
- CL-58 | S | method-and-programs | Struck by the human user 2026-10-18; do not apply; number not reused.
- CL-59 | S | method-and-programs | Superseded by Adopted CL-62; do not apply (later platform rounds are out of both worlds when the org survives).
