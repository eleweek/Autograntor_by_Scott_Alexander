# Milestones utility weights — Canonical Milestones

**Canonical Milestones.** This file lists the Canonical Milestones: milestones tested and validated by at least one human and multiple AIs. Take them most seriously, both in forecasting and when pricing any new milestone. AIs never edit this file. If you spot a problem with a Canonical Milestone, propose a change in your report, compute your forecast both with and without the change, and let the human user decide.

Two further tiers live in `claude/milestones_added.md`:
- **Approved Milestones** have been approved by the human user. Treat them as weak precedents, like Common Law rulings. Where one seems to conflict with a Canonical Milestone, the Canonical one wins.
- **Proposed Milestones** have been added by an AI and not yet reviewed. Treat them as mild evidence, with no reason to prefer them to your own judgment.

**Order of authority:** the human user's prompt > Common Law > Canonical > Approved > Proposed > your own judgment. All values mean what Common Law CL-1 defines. The overlap and marginal-price notes below apply to every tier. Never sum entries.

**Adding a milestone (milestones_added.md only):**
1. Only add milestones another grant could plausibly use, not outcomes specific to one grant.
2. Check for an existing entry first. If one covers it, add your own estimate to that entry instead of creating a new one.
3. Price it by comparison with at least one named Canonical Milestone.
4. Re-read the file immediately before writing, add at the end of the Proposed section only, and write it back otherwise unchanged. Never edit Approved milestones or other AIs' Proposed ones.
5. Say in your report which milestones you added, and which Approved or Proposed milestones you used.

Entry template: `<milestone> | <value> | priced against: <Canonical comparators and reasoning> | [Proposed <date>, from <grant>, by <model>]`. Additional estimates go underneath as `also: <value>, <one-line reason> [<date>, <grant>, <model>]`.

---

Source: Milestones.xlsx, revised by the human user and uploaded 2026-10-19. This version replaces the 2026-10-16 version (an average of the human user's and several AIs' estimates); the human user has since revised many values, including raising the historical community rows. Utility scale: Plan A-style US–China pause treaty = 1,000,000. All category multipliers are 1 and no per-entry overrides are set in this version. Entries overlap within and across categories; do not sum them. Generic inputs are marginal unit prices at today's margin.

| Category | Entry | Who / status | When | Weight |
|---|---|---|---|---|
| Political | Plan A-style US–China pause treaty (verified halt on new frontier training, declared compute, mutually assured compute destruction) | Proposed | AI Futures Project 'AI 2040: Plan A' | 1,000,000 |
| Political | US–China verification regime without a pause (declared compute, inspections, inference-only checks) | Proposed | Not on any official agenda | 200,000 |
| Political | US federal licensing / pre-deployment approval for frontier models | Proposed | No bill with momentum | 120,000 |
| Political | Federal standby authority to pause frontier training, plus compute tracking to make it enforceable | Proposed | Not introduced | 150,000 |
| Political | International compute registry with hardware-enabled mechanisms on frontier chips | Proposed | Research stage | 120,000 |
| Political | Federal frontier transparency law (public model specs, safety cases, capability disclosure, incident reporting) | Proposed | Preemption drafts would instead weaken state versions | 50,000 |
| Political | Standing US–China government channel on frontier AI risk | Proposed | Only one-off statements so far | 30,000 |
| Political | Mandatory government pre-deployment testing of frontier models (CAISI) | Proposed | Testing is voluntary today | 50,000 |
| Political | Government alignment/control research program over $1B/year | Proposed | Not funded at this scale | 50,000 |
| Political | Legal requirements against AI-enabled power grabs (public model specs, no secret loyalties, limits on government use) | Proposed | Not introduced | 50,000 |
| Political | Restore presumption-of-denial export controls on frontier AI chips to China | Reversed | BIS moved H200-class chips to case-by-case review, effective Jan 2026 | 40,000 |
| Political | Mandatory high security (SL4+) for frontier model weights | Proposed | Voluntary lab frameworks only | 70,000 |
| Political | Federal AI whistleblower protection law | In progress | Introduced 2025 as far as I know; status not verified this session | 20,000 |
| Political | Chip Security Act (location verification on exported AI chips) | In progress | Passed House Foreign Affairs Committee 42–0, March 2026; no floor vote yet | 16,000 |
| Political | Senate strips 10-year moratorium on state AI laws from the reconciliation bill | Happened | July 2025, 99–1 vote | 20,000 |
| Political | EU AI Act obligations for general-purpose models plus the Code of Practice safety chapter | Happened | In force from Aug 2, 2025; unchanged by the 2026 omnibus | 20,000 |
| Political | California SB 53 (Transparency in Frontier AI Act) | Happened | Signed Sept 2025; in force | 25,000 |
| Political | Defeat federal preemption of state AI laws in 2026 (Great American AI Act draft, EO 14365 litigation) | In progress | Discussion draft stalled since June 2026; DOJ task force active | 24,000 |
| Political | New York RAISE Act | Happened | Signed Dec 2025; amended March 2026 to track SB 53; effective Jan 1, 2027 | 8,000 |
| Political | UN Independent International Scientific Panel on AI and Global Dialogue | Happened | Established by UN General Assembly, Aug 2025 (as far as I know) | 5,000 |
| Alignment | Problem framing: orthogonality, instrumental convergence, corrigibility, the sharp left turn | Eliezer Yudkowsky and MIRI | 2001–2023 | 60,000 |
| Alignment | ELK, iterated amplification and related conceptual agendas | Paul Christiano (ARC) | 2016–2024 | 15,000 |
| Alignment | RLHF: deep reinforcement learning from human preferences, scaled up in InstructGPT | Christiano, Leike et al.; OpenAI | 2017–2022 | 10,000 |
| Alignment | Circuits program: reverse-engineering networks, induction heads | Chris Olah and collaborators (Distill, Anthropic) | 2020–2022 | 20,000 |
| Alignment | Superposition and sparse autoencoders (dictionary learning) | Anthropic interpretability team | 2022–2024 | 15,000 |
| Alignment | Constitutional AI, model specs and character training | Anthropic (Bai et al.); OpenAI model spec | 2022–2025 | 15,000 |
| Alignment | AI control: safety even if the model is scheming | Redwood Research (Greenblatt, Shlegeris et al.) | 2023–present | 45,000 |
| Alignment | Model organisms of misalignment: sleeper agents and alignment faking | Anthropic and Redwood (Hubinger, Greenblatt et al.) | 2024 | 25,000 |
| Alignment | Risks from Learned Optimization (mesa-optimization, deceptive alignment) | Hubinger et al. | 2019 | 20,000 |
| Alignment | Chain-of-thought monitorability | OpenAI (Baker et al.) and a multi-lab position paper | 2025 | 18,000 |
| Alignment | Attribution graphs / circuit tracing ('Biology of a Large Language Model') | Anthropic interpretability team | 2025 | 12,000 |
| Alignment | Emergent misalignment | Betley, Evans et al.; OpenAI follow-ups | 2025 | 9,000 |
| Alignment | Representation engineering, steering vectors and persona vectors | Zou et al.; Turner et al.; Chen et al. | 2023–2025 | 7,000 |
| Alignment | J-Lens / global workspace paper | Anthropic | July 2026 | 4,000 |
| Alignment | Persona selection model and inoculation prompting | Anthropic (Marks, Lindsey, Olah) and others | 2025–2026 | 5,000 |
| Alignment | Debate and scalable oversight | Irving, Christiano, Amodei; later empirical work | 2018–2025 | 12,000 |
| Alignment | Alignment auditing: hidden-objective games and auditing agents | Anthropic (Marks et al.) | 2025 | 10,000 |
| Alignment | Natural abstractions and selection theorems | John Wentworth | 2019–present | 2,000 |
| Alignment | Weak-to-strong generalization | OpenAI Superalignment (Burns et al.) | 2023 | 6,000 |
| Alignment | Learning-theoretic agenda / infra-Bayesianism | Vanessa Kosoy | 2019–present | 1,200 |
| Community | LessWrong and the Sequences (with Overcoming Bias) | Eliezer Yudkowsky, Robin Hanson | 2006–2009 | 120,000 |
| Community | Founding of effective altruism (Giving What We Can, CEA, the EA framework) | Toby Ord, Will MacAskill and others | 2009–2012 | 100,000 |
| Community | 80,000 Hours career advice, AI-focused since about 2017 | 80,000 Hours | 2011–present | 40,000 |
| Community | Harry Potter and the Methods of Rationality | Eliezer Yudkowsky | 2010–2015 | 15,000 |
| Community | Slate Star Codex / Astral Codex Ten as a community hub | Scott Alexander | 2013–present | 15,000 |
| Community | MATS (ML Alignment & Theory Scholars) | MATS team | 2021–present | 25,000 |
| Community | LessWrong 2.0 revival and the Alignment Forum | Lightcone Infrastructure (Habryka et al.) | 2017–present | 20,000 |
| Community | CFAR workshops and alumni network | Center for Applied Rationality | 2012–2020 | 5,000 |
| Community | EA Global and EAGx conferences | CEA | 2013–present | 10,000 |
| Community | BlueDot Impact courses (AI Safety Fundamentals) | BlueDot Impact | 2021–present | 10,000 |
| Community | Small-grant ecosystem (Long-Term Future Fund, SFF and similar) | EA Funds, Survival and Flourishing Fund and others | 2017–present | 30,000 |
| Community | Lighthaven | Lightcone Infrastructure | 2023–2025 | 9,000 |
| Community | University AI safety student groups | Harvard AISST, MIT AI Alignment and many others | 2022–present | 8,000 |
| Community | Constellation (Berkeley research center) | Constellation | 2022–present | 12,000 |
| Community | Berkeley rationalist hub and group houses | Community-organized | 2012–present | 15,000 |
| Community | Summer research fellowships (SERI, ERA, CHERI, PIBBSS and similar) | Various | 2021–present | 10,000 |
| Community | LISA (London Initiative for Safe AI) | LISA | 2023–present | 3,000 |
| Community | AI Safety Camp | AI Safety Camp | 2018–present | 4,000 |
| Community | SSC/ACX meetups worldwide | Local organizers | 2016–present | 2,500 |
| Community | Manifest and the Manifold community | Manifold | 2022–present | 1,000 |
| Social shift | Geoffrey Hinton leaves Google and warns publicly about extinction risk | Geoffrey Hinton | May 2023 | 20,000 |
| Social shift | Yoshua Bengio speaks out and reorients his work toward safety | Yoshua Bengio | 2023 | 15,000 |
| Social shift | Frontier safety frameworks adopted across labs (RSPs, Preparedness, Frontier Safety Framework, Seoul commitments) | Anthropic, OpenAI, Google DeepMind, then about 16 companies at Seoul | 2023–2024 | 15,000 |
| Social shift | Governments found AI Safety Institutes | UK, US, then a dozen more | Nov 2023 onward | 27,000 |
| Social shift | AI 2027 scenario goes mainstream | AI Futures Project | Apr 2025 | 18,000 |
| Social shift | Bletchley Declaration | 28 countries including the US and China | Nov 2023 | 8,000 |
| Social shift | If Anyone Builds It, Everyone Dies becomes a bestseller | Yudkowsky and Soares | Sept 2025 | 15,000 |
| Social shift | AI risk concern becomes bipartisan, including on the populist right | Hawley, Bannon and others | 2024–2026 | 30,000 |
| Social shift | CAIS Statement on AI Risk | Center for AI Safety; lab CEOs and hundreds of researchers | May 2023 | 16,000 |
| Social shift | Chinese and Western scientists agree on red lines (IDAIS dialogues) | Andrew Yao, Bengio, Hinton, Zhang Ya-Qin and others | 2023–2024 | 9,000 |
| Social shift | International AI Safety Report | Chaired by Yoshua Bengio, 30+ countries | Jan 2025 | 5,000 |
| Social shift | Statement on Superintelligence (call to prohibit development until there is scientific consensus and public buy-in) | Future of Life Institute; very broad signatories | Oct 2025 | 8,000 |
| Social shift | FLI 'pause giant AI experiments' letter | Future of Life Institute; Musk, Wozniak, many researchers | Mar 2023 | 7,000 |
| Social shift | OpenAI safety departures and the 'right to warn' letter | Jan Leike, Ilya Sutskever, current and former employees | May–June 2024 | 8,000 |
| Social shift | Lab CEOs acknowledge extinction risk in Senate testimony | Sam Altman and others | May 2023 | 8,000 |
| Social shift | Hinton's Nobel Prize amplifies his warnings | Nobel Committee / Geoffrey Hinton | Oct 2024 | 6,000 |
| Social shift | Expert surveys show substantial extinction estimates (AI Impacts) | AI Impacts | 2022–2023 | 8,000 |
| Social shift | White House voluntary commitments | Seven, then fifteen companies | July 2023 | 5,000 |
| Social shift | Pope Leo XIV makes AI a signature issue | Pope Leo XIV | 2025 | 4,000 |
| Social shift | OpenAI board crisis | OpenAI board | Nov 2023 | -7,000 |
| Generic: PERCYs | One million PERCYs | Any persuasion grant | Per million | 1,200 |
| Generic: $1B to grantmaker | $1B given to a grantmaker like CG or SFF, spent in their usual way | Any large donation | One-time | 20,000 |
| Generic: researcher-year | One extra alignment-researcher-year (marginal MATS graduate) | Research and training grants | Per year | 50 |
| Generic: policy-year | One person-year of a skilled, safety-minded professional in a government AI role | Policy pipeline grants | Per year | 100 |
| Generic: lab point | OpenAI or Anthropic becomes 1 point more alignment-pilled (0 = NVIDIA, 100 = Anthropic) | Lab-facing grants | Per point | 3,000 |

## Notes sheet

- **What this is:** All 85 entries on one scale: the four original sheets (political outcomes, alignment discoveries, community building, social shifts) plus five generic inputs. Base values are my estimates under an AI Futures Project-style worldview.
- **How the scaling works:** Each category has an anchor (Plan A = 1,000,000; J-Lens = 4,000; Lighthaven = 10,000; CAIS letter = 5,000; and each of the five generic inputs is its own category, anchored on itself). Changing a category's anchor in the yellow control cells multiplies every entry in that category by the same factor. This changes how categories compare to each other without changing the order inside a category.
- **Per-entry overrides:** Type a number in 'Your base value' to replace my estimate for that entry. It is still multiplied by the category multiplier.
- **Ranked sheet:** Re-sorts automatically. Colors match the categories. Ties keep the order of the main sheet.
- **Colors:** Blue = political, green = alignment, orange = community building, purple = social shifts, teal = generic inputs (each its own category). Yellow cells are for your input; blue numbers are my estimates.
- **Overlap:** Entries overlap within and across categories (e.g. AI 2027 appears as a social shift and drives political outcomes). Don't add them up for totals.
- **Generic inputs are marginal prices:** Each value is for one more unit at today's margin. Don't multiply them up linearly: 5,000 extra researcher-years or $10B extra would each be worth far less than 5,000× or 10× the listed value, because of diminishing returns and limits on how much the field can absorb.
- **Generic inputs:** Provisional guesses, meant as unit prices for grant scoring: a grant's value = how many units it produces × the unit's value here. Values for researcher-year and policy-year are per single year, so they look tiny next to whole programs; that is expected.
- **Sources:** See the four original sheets. Political and alignment statuses were partly checked against sources; community and social-shift facts are from memory.
