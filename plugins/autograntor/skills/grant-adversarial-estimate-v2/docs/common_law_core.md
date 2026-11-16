# Autograntor Common Law — Core (Part I and Adopted rulings)

Version: 2026-11-10.2 · Owner: the human user · Status legend: **Adopted** (approved by the human user; binding) · **Proposed** (added by an AI; provisional until the human user adopts or strikes it)

This file is a verbatim copy of Part I and Part II of `claude/common_law.md` (the frozen archival original, which remains the source of truth), except for changes the human user made on 2026-11-10: CL-4's money price, a reworded CL-8, and the new CL-91 on funging. Where the two differ, this file governs. Where a Proposed ruling (CL-14, 21, 28, 34, 35, 43, 66, 75, 87 and others) speaks of "the money price" or requires an outside funder's probability to be the same in both worlds, CL-91 governs: use the funder's price from its table and model the funder's real response. Every agent reads this file in full. Proposed rulings CL-14 to CL-83 are summarised one line each in `claude/common_law_index.md` and given in full, grouped by topic, in `claude/common_law_topics/`. Rulings added after the freeze are in `claude/common_law_proposed/`.

Every grant report must state the Common Law version it used.

This document is kept free of grant names, applicant details and past forecast results, so that it can be given to independent forecasters without revealing earlier answers (see "Keeping this document clean" in Part I).

---

## Part I: How to use this document

**Order of authority.** When sources conflict, follow the higher one and say so in your report:
1. The human user's instructions in the current prompt
2. Adopted rulings in this document
3. Proposed rulings in this document
4. Your own judgment

**Procedure for any judgment call about how to use the system:**
1. **Look for a precedent.** Search this document for a ruling that covers the situation. If one exists and you agree with it, apply it and cite it by number (e.g. "per CL-4").
2. **If there's no precedent:** make your own call, then add it to Part III as a **Proposed** ruling using the template below. Say in your report that you did this.
3. **If a precedent exists but you disagree:** apply it anyway for your headline numbers. Then recompute *only the rows it affects* under your alternative, and report both results and the difference, with your reasoning. Don't edit the ruling; the human user decides.
4. **If you applied a Proposed ruling,** say so in your report.

**Editing rules for AIs.** You may only append new rulings to Part III. Never change or delete Adopted rulings, Part I, or other AIs' Proposed rulings. To append: re-read the document immediately before writing (another run may have added rulings since), add yours at the end of Part III with the next free number, and write back the full document unchanged except for your addition.
*(Since 2026-10-21 "Part III" for new rulings means a new file in `claude/common_law_proposed/`; see its README. AIs never write to the frozen original or to this core file.)*

**Keeping this document clean.** State every ruling generally. Never name a real grant, applicant, organisation being evaluated, person, funder or evaluator, and never record a forecast result, a parameter value taken from a specific forecast, or how a ruling changed a specific forecast's numbers. Those belong in the grant report, not here. An example is optional; if you give one, make it hypothetical, with invented round numbers.

**Ruling template (for Part III):**
```
### CL-<next number>: <short title> [Proposed <YYYY-MM-DD>, by <model>]
**Rule:** <one or two sentences, stated generally>
**Why:** <one or two sentences, without naming any grant or result>
**Example (optional):** <a hypothetical illustration with invented numbers>
```

---

## Part II: Adopted rulings

### CL-1: What a value means
**Rule:** Every entry and every grant is valued the same way, whether it is a law, a research result, a community or a shift in opinion: the counterfactual value of the thing existing, judged from 2030, including everything downstream it caused. Formally, value(X) = Σ over consequences of [weight × (P(consequence | X) − P(consequence | not X))], plus any value X has in itself. Consequences can be negative, and are signed.
**Why:** One definition across categories is what makes the scale comparable.

### CL-2: Computing credit for an outcome
**Rule:** When **forecasting** (a grant, a new project), credit for an outcome = P(outcome | cause) − P(outcome | no cause). When **judging something that has already happened** (a historical entry), credit = 1 − P(outcome | cause absent), because P(outcome | cause) = 1.
**Why:** Using the retrospective formula for a forecast hugely overstates small effects.
**Example:** A grant that raises the odds of a law from 10% to 12% gets 2% of the law's weight, not 90%.

### CL-3: No credit pie
**Rule:** Compute counterfactual credit independently for each cause. Credit does not have to sum to 100% across causes; if an outcome needed both A and B, each gets full counterfactual credit. Don't divide credit among actors (no Shapley values, no shares that must add to one). What shrinks a cause's claim is the chance the outcome would have happened anyway (CL-2), so long causal chains lose credit at each link with no separate discount.
**Why:** For a funding decision, the question is what changes if this grant is or isn't made. If full credit fails the scale-up check, the fix is CL-4, not a fractional share.

### CL-4: Charge for the resources a grant pulls in [Adopted; money price set by funder under CL-91 by the human user 2026-11-10]
**Rule:** If a grant's value depends on later resources it causes to be spent (follow-on donations or loans, purchase capital, the time of scarce leaders or staff), subtract what those resources would have produced elsewhere. Money: charge it at the supplying funder's price in the CL-91 table (50 utility per $1M where the funder is the platform itself or a best AI safety funder; the human user may override). These prices are set directly in CL-91 and are not derived from the "$1B to grantmaker" entry on the weights list, which prices one very large gift and must not be scaled down linearly (CL-13). People: use the policy-year or researcher-year prices, or a stated multiple for unusually scarce people. Count only the resources that would not have been spent anyway, weighted by the probability they are spent.
**Why:** Without this, "no credit pie" overvalues seed and leverage grants, which get credit for outcomes paid for mostly by other people's money.
**Example (hypothetical):** A grant that raises the chance of a $10M follow-on raise by 30 points pulls in about $3M of expected follow-on money; if it comes from a top-tier funder, subtract about 150 utility, and if from a 10-per-$1M funder, about 30.

### CL-5: Count each consequence once [Adopted; row-type clause added by the human user 2026-10-20, drafted by Claude]
**Rule:** Within one grant's accounting, never credit the same consequence twice. If a grant builds a node (a movement, program or institution), credit either the node or the downstream outcomes it produces, not both, since the node's value already includes them. Credit through the most proximate node whose probability you can actually forecast. Separate consequences can each be credited: a grant that funds an organization and also directly produces an unrelated outcome gets both. Entries in the weights table overlap and must never be summed.

**Row types.** Label every positive row in a grant ledger with one of three types:
- **Output:** something the grant produces (a report, a campaign, a channel's audience, a scenario, a body of research), valued *including* everything it causes downstream. Once a row is an Output, no other row may credit the outcomes it causes.
- **Outcome:** a final event on or priced from the weights list (a law, a treaty, a lab commitment), credited at weight × ΔP. Its ΔP covers only the routes to that event that do *not* run through an Output row in the same ledger.
- **Upgrade:** the move from one outcome state to a better one (e.g. from a transparency-level law to a licensing regime), valued at the difference between the two states' weights and credited only on top of the lower state, never alongside the higher state's full weight.

For every pair of rows that could describe the same causal path (an Output and an Outcome it may cause; two Outputs whose audiences or effects overlap, such as a flagship publication and the ongoing communication it feeds), either state in one line why they are separate or add one signed overlap row. Never leave an overlap implicit. Mutually exclusive success levels of one portfolio count as a single row for this purpose.
**Why:** The only place double-counting can enter is inside one grant's ledger. Most double counts come from an output and the outcomes it causes both being credited in full, or from two outputs that reach the same people; declaring each row's type makes those overlaps visible before they reach the total.
**Example (hypothetical):** A grant funds a policy report (Output, 300, including its effect on a bill) and is also credited with a federal law (Outcome). The law row may count only influence that doesn't pass through the report, e.g. separate briefings, or the two rows get a signed overlap line. Upgrading that law from transparency (50,000) to licensing (120,000) at +0.1 point is an Upgrade row worth 70 (70,000 × 0.001), not 120.

### CL-6: Old rows price old things
**Rule:** Historical entries value the thing at the date it existed. A new institution started now is worth what it will plausibly produce by 2030, plus later effects discounted per CL-7, using the historical entry as a comparable for scale and quality and as an upper bound. It is an upper bound partly because the field is more crowded now: a new venue or program today is partly redundant with existing ones in a way its predecessor wasn't.
**Example:** A new venue modelled on a historical one listed on the weights table is worth less than that entry, because part of its function is already served by existing venues.

### CL-7: Time horizon
**Rule:** Value a grant as it would look from 2030. Count milestones reached by 2030, plus changes in the probability of later milestones that are already evident by 2030. Discount effects expected after 2030 for the chance that transformative AI has made them moot (use the human user's stated discount if the prompt gives one). Always report the share of value that comes from post-2030 effects.

### CL-8: The no-grant world [Adopted; reworded by the human user 2026-11-10, drafted by Claude]
**Rule:** If the grant is declined, the platform's money is not replaced by the platform: other evaluators and later rounds of the same platform do not step in (CL-62). The organization keeps its existing funds, pledges and earned revenue, and its team can keep working with those. Funders outside the platform behave as they really would toward the organization in each world; how their giving differs between the two worlds is handled under CL-91. Don't model an organization forbidden from ever raising money again.

### CL-9: Scale-up check
**Rule:** An extra dollar is not worth more than the organization's average dollar. Multiply every grant estimate up to the organization's full annual budget and list the implied probability shifts for the largest rows. If any is implausible (e.g. one year of the organization adding tens of points to the odds of a federal law), revise the estimate. Also compare with the organization's track record: past utility credited ÷ past spending.
*(How strictly to apply the first sentence, and what "average dollar" means: see CL-15.)*

### CL-10: Outcomes not on the weights list
**Rule:**
- A new state AI law that mostly copies SB 53: at most the NY RAISE Act weight, scaled down for smaller or less influential states. A law with substantial new provisions (e.g. mandatory third-party audits) may go higher, justified relative to SB 53.
- "Implementation" or "preservation" of existing laws counts only when tied to a specific, checkable event, valued as a stated fraction of that law's weight.
- Influence on AI labs: use the lab-point price (per point at OpenAI or Anthropic on a 0–100 scale, 0 = NVIDIA, 100 = Anthropic); other labs at a stated fraction.
- Anything else: name it, price it by comparison with the closest listed items, and say which ones.

### CL-11: Contested values questions go back to the human user
**Rule:** If a large share of a grant's value or downside depends on a values judgment rather than a factual one (e.g. whether hosting accelerationists at a neutral convening helps or hurts), don't silently pick an answer. Price the grant under each reasonable answer and report both as a question for the human user.

### CL-12: Other evaluators' opinions
**Rule:** Treat other evaluators' written opinions as evidence, not answers. Weigh them by the evaluator's track record and access, discount them for conflicts of interest (e.g. a board seat), and say when a large part of your estimate rests on one person's view.

### CL-13: Generic prices
**Rule:** The generic entries (PERCYs, $1B to grantmaker, researcher-year, policy-year, lab point) are marginal prices for one more unit today. Use them to price a grant's outputs and as cross-checks, never as a starting point or a ceiling for a specific organization, and never multiply them up linearly to large quantities.

### CL-15: CL-9 is a soft sanity check, measured against the organization not existing [Adopted by the human user 2026-10-16; drafted by Claude]
**Rule:** The "organization's average dollar" in CL-9 is the value of the organization's full annual program compared with the organization not existing, divided by its annual budget, on the same CL-11 mixture as the grant. It is not the grant's increment over the no-grant world divided by the budget. CL-9 is a sanity check, not a cap, and not a strong one: a grant may be valued above the organization's average dollar when the estimator says why. Legitimate reasons include: the grant buys the program's strongest lines and the average is pulled down by weaker lines it doesn't fund (tiered budgets); or the grantor judges the funded program unusually valuable compared with the rest of the organization's spending (the organization may be mistaken in not redirecting its other money to it, or may have fixed costs it can't redirect). Always report the organization's average dollar next to the grant's figure; the bigger the excess, the more specific and checkable the reason should be.
**Why:** Dividing the grant's increment by the budget mixes bases and, as a cap, forbids diminishing returns within a grant. A hard cap at the organization's average penalizes tiered budgets and wrongly assumes an organization's own spending is efficient.

### CL-33: Grants that may never be disbursed [Adopted by the human user 2026-10-17; drafted by Claude]
**Rule:** If some branches of a grant end with the money cleanly returned to the funder before it is spent (e.g. the lead decides not to proceed, a condition isn't met), drop those branches and value the grant conditional on the money leaving the pot: the headline mean, median, percentiles and per-$1M figures are all conditional on disbursement, with per-$1M computed on the dollars actually disbursed. This applies only to clean refunds. Keep, at whatever value they produce, branches where the money leaves and the program then fails, and score partial refunds per dollar actually kept. If a refund would come back too late to be re-granted at the usual bar, or would have held up other grants, charge that delay as a signed row. If the grant offer itself changes whether the gate opens (e.g. a larger offer makes the lead likelier to commit), or the worlds where the money is kept differ systematically from the others, reflect that in the conditional estimate.
**Why:** Returned money goes back to the pot and funds the next-best grant, so valuing it at zero makes an uncertain grant look like a bad one; whether to fund depends on value per dollar disbursed against the bar, which doesn't depend on the probability of disbursement.

### CL-62: Other evaluators' allocations in the same round are ignored [Adopted by the human user 2026-10-18; drafted by Claude]
**Rule:** When scoring a grant for a funding platform on which several evaluators allocate money in the same round, ignore the other evaluators' allocations to the same organisation in that round: they are absent from both the grant and the no-grant worlds. Score the grant as if this ruling directs all of the platform's money to the organisation in that round, so the question answered is whether the platform as a whole should fund it at this size. Money from outside the platform (other funders, pledges, the organisation's own fundraising) still stays in both worlds, per CL-8 and CL-43. Later rounds of the same platform are likewise left out of both worlds when the organisation survives without the grant; CL-31's grant-world continuation for a program that dies without the grant is unchanged. This supersedes CL-43's original same-round clause, CL-58 (struck) and CL-59, and limits CL-60's second clause.
**Why:** The forecast is meant as a naive estimate of whether the platform should fund the organisation at all, not of what one evaluator's slot adds on top of the others.

### CL-91: Funging and the funder price table [Adopted by the human user 2026-11-10; drafted by Claude]
**Rule:** Every forecast reports two values. The **base** value assumes every grant dollar is net new to the organisation: outside funders give what they would have given anyway and do not react to the grant. The **with-funging** value is the headline and is used for ranking. It models how each outside funder would really respond to the grant (a smaller ask, a smaller or skipped award, a rescue if the grant is declined), with no requirement that a funder's probability be the same in both worlds.

For the with-funging value: (a) state, per outside funder, the expected dollars displaced by the grant, meaning money that funder would have given the organisation without the grant and does not give with it; (b) total displacement may never exceed 75% of the grant; (c) subtract the programme value the organisation loses because those dollars are not net new; (d) credit each displaced dollar at its funder's price below, multiplied by 0.8. Banked money that lowers the organisation's later fundraising is displacement from its usual funders, at their tier, and falls under the same cap and factor.

| Funder tier | Utility per $1M |
|---|---|
| The platform's own money; best AI safety funders (EAIF, AISTOF, AIRM, Macroscopic) | 50 |
| Irregular AI safety funders (SFF, Manifund); AI welfare and s-risk funders; known AI-safety-motivated individual donors | 33 |
| Peripheral AI safety funders (Longview, Astralis, FLI, CSET, Astera); Coefficient Giving; an unknown or mixed donor base | 10 |
| Smart and competent but not focused on AI (e.g. the Gates Foundation); general-public small donors | 4 |
| Neither smart nor competent | 0 |

Assign an unlisted funder to the nearest tier and say so in the report. Money a grant pulls in from others (CL-4) is charged at the supplying funder's full price, without the 0.8 factor. The funder names in this table are the human user's stated policy and are a deliberate exception to the keep-clean rule in Part I.
**Why:** A displaced dollar is not lost; it stays with a funder who spends it on something else, and how much that is worth depends on who the funder is. The 75% cap guards against assuming others will pay. The 0.8 factor is a deliberate bias against leaving other funders to do the platform's work.
**Example (hypothetical):** A $1M grant leads the organisation to ask a 10-per-$1M funder for $600K less. $400K is net new to the organisation and is valued as programme. The $600K displaced earns 0.6 × 10 × 0.8 = 4.8. Had the grant displaced $900K, displacement would be capped at $750K.
