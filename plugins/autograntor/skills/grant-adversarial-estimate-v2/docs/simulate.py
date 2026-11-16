#!/usr/bin/env python3
"""
Autograntor ledger simulator (Common Law CL-16 / CL-55 / CL-74 / CL-18).

Usage
  python simulate.py ledger.csv                      # all sizes in the file
  python simulate.py ledger.csv --size 1M            # one size
  python simulate.py ledger.csv --branches '{"PE_good":0.4,"trust_harm":0.55}' \
                                --corr '{"PE_good|trust_harm":0.5}'
  python simulate.py ledger.csv --exec '{"program":{"mean":0.7,"collapse_p":0.15}}'
  python simulate.py --diff a.csv b.csv --size 1M \
      --branches-a '{...}' --exec-a '{...}' --branches-b '{...}' --exec-b '{...}'
                                                     # headline means and group totals, each ledger under
                                                     # its own branch weights and exec factor; rows >10%
  python simulate.py --template                      # print the example ledger (illustrative rows, one of each kind)

Ledger CSV columns (header required; unknown columns are ignored; blanks are fine)
  size       grant size label this row belongs to ("1M", "3.3M"). Blank = applies to every size.
  row        short name
  kind       event | continuous | charge
             event:      a discrete outcome. Needs weight, p1 (with grant), p0 (without).
                         Contribution = weight × (p1 − p0). Simulated per CL-16: the outcome
                         occurs with prob p1; when it does, credit = weight × (1 − p0/p1).
             continuous: a non-event effect (PERCYs, capacity, probability shifts of post-2030
                         milestones). Needs ev; optional sigma (lognormal spread on magnitude,
                         default 0.5). Per CL-16 these never get dropped from the simulation.
             charge:     a signed line that is not an outcome (money price, people charge,
                         overlap, idling). Needs ev. Treated as fixed unless sigma is given.
  weight     utility weight of the outcome (events only)
  p1, p0     P(outcome | grant), P(outcome | no grant). p1 >= p0 for positive rows; for a
             downside event give a negative weight and p1 >= p0.
  ev         expected contribution (continuous and charge rows)
  sigma      lognormal sigma on the magnitude (continuous/charge rows), default 0.5 / 0
  pivotal    CL-55: share of worlds where the outcome occurs AND the grant was pivotal, in which
             credit = full weight. Remaining occurring worlds get the diffuse credit that keeps
             the mean equal to weight × (p1 − p0). Must be <= (p1 − p0)/p1. Blank = plain CL-16.
  exec       name of a correlated execution factor group (CL-16/CL-37). Rows in a group are
             multiplied by one sampled factor per world. Only program rows; never charges.
  exec_mode  how the execution factor f enters an event row (events only; default "credit"):
             credit: the whole increment scales: credit = f × weight × (1 − p0/p1), so the
                     no-grant probability is scaled too. Right when p0 is the chance the SAME
                     work happens anyway (the no-grant world also has the execution risk).
             p1:     only the with-grant probability scales: the outcome occurs with prob
                     f × p1 and credit = weight × (1 − p0/(f × p1)); mean = weight × (m·p1 − p0).
                     Right when p0 is the base rate from other causes, unaffected by whether
                     this team executes. Cannot be combined with pivotal.
  group      coarse category used by --diff and the agreement test, so that two independent
             ledgers can be compared without matching row names. Mandatory. File by the CAUSAL
             PATH, not by the row's sign or by which branch it sits in: a harm-branch mirror of
             a positive row takes the SAME group as that row (so "harness is net capabilities"
             goes in uptake with "harness is used", not in values or exposure). Definitions:
               research-output  the grant's own outputs existing (a paper, corpus, tool, report,
                                campaign produced), including their direct audience
               uptake           others adopting, citing, building on or being changed by those
                                outputs (labs, teams, funders, follow-on programmes)
               talent           people entering, staying in or upskilling for safety work
               media            PERCYs rows: audiences moved by communication
               policy           laws, regulations, government positions, treaties, champions
               lab              lab-point rows and lab practice changes not via policy
               program          program-year or org-level value rows not split further
               continuation     later years or cohorts the grant makes possible (CL-31, CL-38)
               money            money-price rows: follow-on money, displaced fundraising,
                                freed backstops, banked runway
               charge           people charges, bad hires, management breakdown, idling
               overlap          CL-5 signed overlap rows
               exposure         hostile press, scandal, partisan coding, incident rows
               values           ONLY rows that exist in no causal path above: pure signalling
                                or trust-norm rows (CL-20 iii, CL-76)
               other            anything else; say why in note
             Unknown values are warned about.
  branch     name of a CL-11 values question this row depends on
  branch_val yes | no  — which answer this row belongs to (rows apply only in that branch).
             Rows with branch set but branch_val blank apply in both and are flagged.
  post2030   share of this row's value from activity after 2030 (CL-18 strict), default 0
  note       free text, ignored

--branches is a JSON dict {question: P(answer == "yes")}. Branch questions found in the ledger
but missing from --branches default to 0.5 with a warning.
--corr is a JSON dict {"q1|q2": rho} for correlated values questions (CL-74).
--exec is a JSON dict {group: {"mean": m, "collapse_p": c}}: with prob c the factor is 0; otherwise
  it is drawn from a Beta with mean m/(1−c) (so the overall mean is m) and modest spread.
  The row EVs in the ledger are BEFORE the execution factor; the headline mean = EV × m.

Outputs, per size: mean (analytic and simulated), median, P10/P25/P75/P90, P(negative),
post-2030 share, the fixed-branch-weight spread (outcome risk only, CL-74), every values corner.
"""
import argparse, csv, json, math, sys
import numpy as np

# ----------------------------------------------------------------------------- loading

COLS = ["size", "row", "kind", "weight", "p1", "p0", "ev", "sigma", "pivotal",
        "exec", "exec_mode", "group", "branch", "branch_val", "post2030", "note"]
GROUPS = {"research-output", "uptake", "talent", "media", "policy", "lab", "program", "continuation",
          "money", "charge", "overlap", "exposure", "values", "other"}

def fnum(x, default=None):
    x = (x or "").strip().replace(",", "")
    if x == "":
        return default
    return float(x)

def load(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    out = []
    for i, r in enumerate(rows, 2):
        kind = (r.get("kind") or "").strip().lower()
        if not (r.get("row") or "").strip() and not kind:
            continue
        d = dict(line=i, size=(r.get("size") or "").strip(), row=(r.get("row") or "").strip(),
                 kind=kind, weight=fnum(r.get("weight")), p1=fnum(r.get("p1")), p0=fnum(r.get("p0")),
                 ev=fnum(r.get("ev")), sigma=fnum(r.get("sigma")), pivotal=fnum(r.get("pivotal")),
                 exec=(r.get("exec") or "").strip(), exec_mode=(r.get("exec_mode") or "credit").strip().lower() or "credit",
                 group=(r.get("group") or "").strip().lower(), branch=(r.get("branch") or "").strip(),
                 branch_val=(r.get("branch_val") or "").strip().lower(),
                 post2030=fnum(r.get("post2030"), 0.0))
        if kind == "event":
            if d["weight"] is None or d["p1"] is None or d["p0"] is None:
                sys.exit(f"line {i} ({d['row']}): event rows need weight, p1, p0")
            if not (0 <= d["p0"] <= d["p1"] <= 1):
                sys.exit(f"line {i} ({d['row']}): need 0 <= p0 <= p1 <= 1 (use a negative weight for downside events)")
            d["ev"] = d["weight"] * (d["p1"] - d["p0"])
            if d["pivotal"] is not None:
                cap = (d["p1"] - d["p0"]) / d["p1"] if d["p1"] > 0 else 0
                if d["pivotal"] > cap + 1e-12:
                    sys.exit(f"line {i} ({d['row']}): pivotal {d['pivotal']} exceeds (p1-p0)/p1 = {cap:.3f}")
        elif kind in ("continuous", "charge"):
            if d["ev"] is None:
                sys.exit(f"line {i} ({d['row']}): {kind} rows need ev")
            if d["sigma"] is None:
                d["sigma"] = 0.5 if kind == "continuous" else 0.0
        else:
            sys.exit(f"line {i} ({d['row']}): kind must be event, continuous or charge")
        if d["branch"] and d["branch_val"] not in ("yes", "no", ""):
            sys.exit(f"line {i} ({d['row']}): branch_val must be yes or no")
        if d["branch"] and not d["branch_val"]:
            print(f"warning: line {i} ({d['row']}) has a branch but no branch_val; applied in both branches", file=sys.stderr)
            d["branch"] = ""
        if d["exec"] and kind == "charge":
            print(f"warning: line {i} ({d['row']}) is a charge with an exec factor; CL-37/CL-40 say charges are not multiplied. Ignoring.", file=sys.stderr)
            d["exec"] = ""
        if d["exec_mode"] not in ("credit", "p1"):
            sys.exit(f"line {i} ({d['row']}): exec_mode must be credit or p1")
        if d["exec_mode"] == "p1" and (kind != "event" or not d["exec"]):
            sys.exit(f"line {i} ({d['row']}): exec_mode=p1 only applies to event rows with an exec group")
        if d["exec_mode"] == "p1" and d["pivotal"] is not None:
            sys.exit(f"line {i} ({d['row']}): exec_mode=p1 cannot be combined with pivotal")
        if d["group"] and d["group"] not in GROUPS:
            print(f"warning: line {i} ({d['row']}) has unknown group '{d['group']}'; use one of {sorted(GROUPS)}", file=sys.stderr)
        out.append(d)
    return out

def sizes_in(ledger):
    s = []
    for d in ledger:
        if d["size"] and d["size"] not in s:
            s.append(d["size"])
    return s or ["all"]

def rows_for(ledger, size):
    return [d for d in ledger if d["size"] in ("", size) or size == "all"]

# ----------------------------------------------------------------------------- sampling

def sample_branches(questions, probs, corr, n, rng):
    """Correlated Bernoulli draws via a Gaussian copula."""
    q = list(questions)
    k = len(q)
    if k == 0:
        return {}
    R = np.eye(k)
    for key, rho in corr.items():
        a, b = key.split("|")
        if a in q and b in q:
            R[q.index(a), q.index(b)] = R[q.index(b), q.index(a)] = rho
    try:
        L = np.linalg.cholesky(R)
    except np.linalg.LinAlgError:
        sys.exit("--corr matrix is not positive definite")
    z = rng.standard_normal((n, k)) @ L.T
    from math import erf, sqrt
    u = 0.5 * (1 + np.vectorize(erf)(z / sqrt(2)))
    return {name: (u[:, j] < probs[name]) for j, name in enumerate(q)}

def sample_exec(spec, n, rng):
    m, c = float(spec.get("mean", 1.0)), float(spec.get("collapse_p", 0.0))
    if c >= 1 or m <= 0:
        sys.exit("exec factor needs 0 <= collapse_p < 1 and mean > 0")
    mu = m / (1 - c)
    if mu >= 1:
        base = np.full(n, mu)
    else:
        kappa = 12.0
        base = rng.beta(mu * kappa, (1 - mu) * kappa, n)
    alive = rng.random(n) >= c
    return np.where(alive, base, 0.0)

def simulate(rows, n, rng, branch_probs, corr, exec_specs, fixed_branches=False, force_branch=None):
    questions = sorted({d["branch"] for d in rows if d["branch"]})
    if force_branch is not None:
        bdraw = {q: np.full(n, force_branch[q]) for q in questions}
    elif fixed_branches:
        bdraw = None
    else:
        bdraw = sample_branches(questions, branch_probs, corr, n, rng)
    groups = sorted({d["exec"] for d in rows if d["exec"]})
    edraw = {}
    for g in groups:
        spec = exec_specs.get(g)
        if spec is None:
            print(f"warning: exec group '{g}' not in --exec; using factor 1", file=sys.stderr)
            edraw[g] = np.ones(n)
        else:
            edraw[g] = sample_exec(spec, n, rng)
    total = np.zeros(n)
    post = np.zeros(n)
    for d in rows:
        k = d["kind"]
        if k == "event" and d["exec_mode"] == "p1":
            w, p1, p0 = d["weight"], d["p1"], d["p0"]
            f = edraw[d["exec"]]
            p1f = np.minimum(p1 * f, 1.0)
            occurs = rng.random(n) < p1f
            with np.errstate(divide="ignore", invalid="ignore"):
                credit = np.where(p1f > 0, w * (1 - p0 / p1f), 0.0)
            val = np.where(occurs, credit, 0.0)
            # exec already applied through p1f; skip the generic multiplication below
            d_exec_applied = True
        elif k == "event":
            d_exec_applied = False
            w, p1, p0 = d["weight"], d["p1"], d["p0"]
            occurs = rng.random(n) < p1
            if d["pivotal"] is not None and p1 > 0:
                s = d["pivotal"]
                piv = rng.random(n) < s
                diffuse = w * ((p1 - p0) - p1 * s) / (p1 * (1 - s)) if s < 1 else 0.0
                val = np.where(occurs, np.where(piv, w, diffuse), 0.0)
            else:
                credit = w * (1 - p0 / p1) if p1 > 0 else 0.0
                val = np.where(occurs, credit, 0.0)
        else:
            d_exec_applied = False
            ev, sg = d["ev"], d["sigma"]
            if sg and sg > 0:
                mag = abs(ev) * rng.lognormal(-0.5 * sg * sg, sg, n)   # mean-preserving
                val = np.sign(ev) * mag
            else:
                val = np.full(n, ev)
        if d["exec"] and not d_exec_applied:
            val = val * edraw[d["exec"]]
        if d["branch"]:
            want = d["branch_val"] == "yes"
            if bdraw is None:
                val = val * (branch_probs[d["branch"]] if want else 1 - branch_probs[d["branch"]])
            else:
                val = np.where(bdraw[d["branch"]] == want, val, 0.0)
        total += val
        post += val * d["post2030"]
    return total, post

def row_ev(d, exec_specs):
    """Expected contribution of one row after the execution factor (before branch weights)."""
    m = float(exec_specs[d["exec"]].get("mean", 1.0)) if d["exec"] and d["exec"] in exec_specs else 1.0
    if d["kind"] == "event" and d["exec_mode"] == "p1":
        return d["weight"] * (min(m * d["p1"], 1.0) - d["p0"])
    return d["ev"] * m

def analytic_mean(rows, branch_probs, exec_specs):
    tot = 0.0
    for d in rows:
        v = row_ev(d, exec_specs)
        if d["branch"]:
            p = branch_probs[d["branch"]]
            v *= p if d["branch_val"] == "yes" else 1 - p
        tot += v
    return tot

# ----------------------------------------------------------------------------- reporting

def q(x, p):
    return float(np.percentile(x, p))

def report(ledger, args):
    rng = np.random.default_rng(args.seed)
    branch_probs = json.loads(args.branches) if args.branches else {}
    corr = json.loads(args.corr) if args.corr else {}
    exec_specs = json.loads(args.exec) if args.exec else {}
    questions = sorted({d["branch"] for d in ledger if d["branch"]})
    for qn in questions:
        if qn not in branch_probs:
            print(f"warning: values question '{qn}' not in --branches; using 0.5", file=sys.stderr)
            branch_probs[qn] = 0.5
    sizes = [args.size] if args.size else sizes_in(ledger)
    for size in sizes:
        rows = rows_for(ledger, size)
        if not rows:
            print(f"\n== {size}: no rows ==")
            continue
        total, post = simulate(rows, args.n, rng, branch_probs, corr, exec_specs)
        am = analytic_mean(rows, branch_probs, exec_specs)
        sm = float(total.mean())
        se = float(total.std()) / math.sqrt(args.n)
        print(f"\n== Size {size} ({len(rows)} rows, {args.n:,} worlds) ==")
        print(f"mean (analytic) {am:,.1f}   mean (simulated) {sm:,.1f} ± {se:,.1f}   " +
              ("ok" if abs(am - sm) <= 3 * se + 0.5 else "MISMATCH — check sigma/exec/branch inputs"))
        print("  (rank grants by the analytic mean; quantiles below are descriptive, per CL-16)")
        print(f"median {q(total,50):,.1f}   P10 {q(total,10):,.1f}   P25 {q(total,25):,.1f}   "
              f"P75 {q(total,75):,.1f}   P90 {q(total,90):,.1f}   P(negative) {float((total<0).mean()):.0%}")
        if am != 0:
            print(f"post-2030 share (CL-18 strict): {float(post.mean())/am:.0%}")
        if questions:
            tf, _ = simulate(rows, args.n, rng, branch_probs, corr, exec_specs, fixed_branches=True)
            print(f"spread with branch weights fixed (outcome risk only, CL-74): "
                  f"P10 {q(tf,10):,.1f}   median {q(tf,50):,.1f}   P90 {q(tf,90):,.1f}   P(neg) {float((tf<0).mean()):.0%}")
            print("values corners (analytic mean):")
            import itertools
            for combo in itertools.product([True, False], repeat=len(questions)):
                fb = {qn: (1.0 if v else 0.0) for qn, v in zip(questions, combo)}
                label = ", ".join(f"{qn}={'yes' if v else 'no'}" for qn, v in zip(questions, combo))
                print(f"  {label}: {analytic_mean(rows, fb, exec_specs):,.1f}")
        if args.rows:
            print("rows (EV after branch weights and exec mean):")
            for d in sorted(rows, key=lambda d: -abs(row_ev(d, exec_specs))):
                v = row_ev(d, exec_specs)
                if d["branch"]:
                    p = branch_probs[d["branch"]]
                    v *= p if d["branch_val"] == "yes" else 1 - p
                print(f"  {v:>10,.1f}  {d['row']}" + (f"  [{d['branch']}={d['branch_val']}]" if d["branch"] else ""))

def weighted_ev(d, branch_probs, exec_specs):
    v = row_ev(d, exec_specs)
    if d["branch"]:
        p = branch_probs[d["branch"]]
        v *= p if d["branch_val"] == "yes" else 1 - p
    return v

def settings_for(rows, branches_json, exec_json, label):
    bp = json.loads(branches_json) if branches_json else {}
    ex = json.loads(exec_json) if exec_json else {}
    for qn in sorted({d["branch"] for d in rows if d["branch"]}):
        if qn not in bp:
            print(f"warning: ledger {label}: values question '{qn}' has no weight (pass --branches-{label.lower()}); using 0.5", file=sys.stderr)
            bp[qn] = 0.5
    for g in sorted({d["exec"] for d in rows if d["exec"]}):
        if g not in ex:
            print(f"warning: ledger {label}: exec group '{g}' has no spec (pass --exec-{label.lower()}); using factor 1", file=sys.stderr)
    return bp, ex

def diff(a_path, b_path, args):
    A, B = load(a_path), load(b_path)
    size = args.size or (sizes_in(A) + sizes_in(B))[0]
    ra, rb = rows_for(A, size), rows_for(B, size)
    bpa, exa = settings_for(ra, args.branches_a or args.branches, args.exec_a or args.exec, "A")
    bpb, exb = settings_for(rb, args.branches_b or args.branches, args.exec_b or args.exec, "B")
    ma = sum(weighted_ev(d, bpa, exa) for d in ra)
    mb = sum(weighted_ev(d, bpb, exb) for d in rb)
    ref = max(abs(ma), abs(mb), 1.0)
    print(f"size {size}: A headline mean {ma:,.1f}  B headline mean {mb:,.1f}  (after each ledger's own branch weights and exec factor)")
    print(f"means within 30%: {'yes' if abs(ma - mb) <= 0.3 * ref or (abs(ma) < 50 and abs(mb) < 50) else 'NO'}")
    # --- group totals (the agreement test compares these, since row names never match) ---
    ga = {}; gb = {}
    for d in ra:
        ga[d["group"] or "(no group)"] = ga.get(d["group"] or "(no group)", 0.0) + weighted_ev(d, bpa, exa)
    for d in rb:
        gb[d["group"] or "(no group)"] = gb.get(d["group"] or "(no group)", 0.0) + weighted_ev(d, bpb, exb)
    thr = args.threshold * ref
    print(f"group totals (flagged if they differ by more than {args.threshold:.0%} of the larger mean, {thr:,.1f}):")
    biggest_a = max(ga, key=lambda g: abs(ga[g])) if ga else None
    biggest_b = max(gb, key=lambda g: abs(gb[g])) if gb else None
    flagged = 0
    for g in sorted(set(ga) | set(gb), key=lambda g: -abs(ga.get(g, 0.0) - gb.get(g, 0.0))):
        ea, eb = ga.get(g, 0.0), gb.get(g, 0.0)
        flag = "  <-- differs" if abs(ea - eb) > thr else ""
        flagged += bool(flag)
        print(f"  {g:<18} A {ea:>9,.1f}   B {eb:>9,.1f}   diff {ea-eb:>9,.1f}{flag}")
    if "(no group)" in ga or "(no group)" in gb:
        print("  note: rows without a group are lumped; fill the group column for a meaningful test")
    print(f"largest group: A={biggest_a}  B={biggest_b}  {'same' if biggest_a == biggest_b else 'DIFFERENT'}")
    print(f"groups over the 30% threshold: {sum(1 for g in set(ga)|set(gb) if abs(ga.get(g,0.0)-gb.get(g,0.0)) > 0.3*ref)}")
    print("row-level differences (by name; independent ledgers rarely share names, so read with the group table):")
    def key(d):
        return d["row"].lower().strip()
    da, db = {key(d): d for d in ra}, {key(d): d for d in rb}
    items = []
    for k in sorted(set(da) | set(db)):
        ea = weighted_ev(da[k], bpa, exa) if k in da else 0.0
        eb = weighted_ev(db[k], bpb, exb) if k in db else 0.0
        items.append((abs(ea - eb), k, ea, eb, k in da, k in db))
    items.sort(reverse=True)
    print(f"  rows differing by more than {args.threshold:.0%} of the larger mean ({thr:,.1f}):")
    for dlt, k, ea, eb, ina, inb in items:
        if dlt <= thr:
            break
        tag = "" if ina and inb else ("  (only in A)" if ina else "  (only in B)")
        print(f"  {dlt:>9,.1f}   A {ea:>9,.1f}   B {eb:>9,.1f}   {k}{tag}")
    print("rows only in one ledger (any size):")
    for k in sorted(set(da) ^ set(db)):
        print(f"  {'A' if k in da else 'B'}: {k}")

TEMPLATE = """size,row,kind,weight,p1,p0,ev,sigma,pivotal,exec,exec_mode,group,branch,branch_val,post2030,note
1M,Federal transparency law,event,50000,0.0030,0.0000,,,,program,credit,policy,,,0,"ΔP for the grant at this size (p1−p0 = 0.0030)"
1M,Paper cited or used by a control team,event,125,0.10,0.01,,,,program,p1,uptake,,,0,"p0 is a base rate from other causes, so only p1 scales with execution"
1M,Media PERCYs,continuous,,,,78.1,0.5,,program,,media,,,0.1,"0.065M PERCYs × 1200/M"
1M,Public engagement (good branch),continuous,,,,30,0.6,,program,,values,PE_good,yes,0,"CL-11 branch"
1M,Public engagement (harm branch),continuous,,,,-15,0.6,,program,,values,PE_good,no,0,"CL-11 branch"
1M,Overlap: media vs policy (CL-5),charge,,,,-4,,,,,overlap,,,0,
1M,Bad hires (CL-36),charge,,,,-11.1,0.3,,,,charge,,,0,
1M,Follow-on money (CL-4),charge,,,,-3.75,,,,,money,,,0,"50 per $1M"
"""

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ledger", nargs="?")
    ap.add_argument("--size")
    ap.add_argument("--n", type=int, default=100_000)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--branches", help='JSON {question: P(yes)}')
    ap.add_argument("--corr", help='JSON {"q1|q2": rho}')
    ap.add_argument("--exec", help='JSON {group: {"mean": m, "collapse_p": c}}')
    ap.add_argument("--rows", action="store_true", help="print every row's EV")
    ap.add_argument("--diff", nargs=2, metavar=("A.csv", "B.csv"))
    ap.add_argument("--branches-a", help="diff only: A's branch weights (defaults to --branches)")
    ap.add_argument("--branches-b", help="diff only: B's branch weights (defaults to --branches)")
    ap.add_argument("--exec-a", help="diff only: A's exec spec (defaults to --exec)")
    ap.add_argument("--exec-b", help="diff only: B's exec spec (defaults to --exec)")
    ap.add_argument("--threshold", type=float, default=0.10)
    ap.add_argument("--template", action="store_true")
    args = ap.parse_args()
    if args.template:
        print(TEMPLATE, end="")
        return
    if args.diff:
        diff(args.diff[0], args.diff[1], args)
        return
    if not args.ledger:
        ap.error("ledger.csv required")
    report(load(args.ledger), args)

if __name__ == "__main__":
    main()
