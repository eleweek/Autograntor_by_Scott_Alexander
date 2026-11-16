#!/usr/bin/env python3
"""Checks for the self-contained Autograntor package.

Run:  python3 tests/test_package.py      (needs numpy, as simulate.py does)

Two kinds of check:
  * packaging: the bundled documents are the owner's files byte for byte, and SKILL.md is
    exactly what tools/edit_skill.py makes from the owner's SKILL.md;
  * arithmetic: the owner's simulate.py and mean_range.py give numbers that can be verified
    with a pocket calculator. These tests describe the simulator; they do not change it.
"""
import importlib.util
import os
import subprocess
import sys
import tempfile
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKILL = os.path.join(ROOT, "plugins", "autograntor", "skills", "grant-adversarial-estimate-v2")
DOCS = os.path.join(SKILL, "docs")
PACKAGE = os.path.join(ROOT, "originals", "autograntor_package_2026-11-12_percys-v4.zip")
ORIGINAL_SKILL = os.path.join(ROOT, "originals", "SKILL_v2_package_2026-11-12.md")
TMP = tempfile.mkdtemp()


def load_module(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(DOCS, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sim = load_module("simulate")
mr = load_module("mean_range")
HEADER = ",".join(sim.COLS)


def ledger(name, lines):
    path = os.path.join(TMP, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(HEADER + "\n" + "\n".join(lines) + "\n")
    return path


def mean(path, branches=None, execs=None):
    return sim.analytic_mean(sim.load(path), branches or {}, execs or {})


def simulated(path, branches=None, execs=None, n=400_000):
    import numpy as np
    total, post = sim.simulate(sim.load(path), n, np.random.default_rng(0), branches or {}, {}, execs or {})
    return total, post


def close(a, b, tol=1e-9):
    return abs(a - b) <= tol


def run(args):
    return subprocess.run([sys.executable] + args, capture_output=True, text=True)


# ------------------------------------------------------------------ packaging
def test_docs_are_the_owners_files_byte_for_byte():
    prefix = "autograntor/claude/"
    with zipfile.ZipFile(PACKAGE) as z:
        members = [m for m in z.namelist() if m.startswith(prefix) and not m.endswith("/")]
        assert len(members) == 26, len(members)
        for m in members:
            with open(os.path.join(DOCS, m[len(prefix):]), "rb") as fh:
                assert fh.read() == z.read(m), m
    on_disk = sum(len([f for f in files if not f.endswith(".pyc")]) for _r, _d, files in os.walk(DOCS))
    assert on_disk == 26, on_disk


def test_skill_is_reproducible_from_the_owners_skill():
    with zipfile.ZipFile(PACKAGE) as z:
        packaged = z.read("autograntor/skill/grant-adversarial-estimate-v2/SKILL.md")
    with open(ORIGINAL_SKILL, "rb") as fh:
        assert fh.read() == packaged
    out = os.path.join(TMP, "SKILL.md")
    r = run([os.path.join(ROOT, "tools", "edit_skill.py"), ORIGINAL_SKILL, out])
    assert r.returncode == 0, r.stdout + r.stderr
    with open(out, encoding="utf-8") as a, open(os.path.join(SKILL, "SKILL.md"), encoding="utf-8") as b:
        assert a.read() == b.read()


def test_staging_check_passes_on_a_fresh_copy():
    import shutil
    staged = os.path.join(TMP, "_docs")
    shutil.copytree(DOCS, staged, ignore=shutil.ignore_patterns("__pycache__"))
    r = run([os.path.join(SKILL, "check_staging.py"), DOCS, staged])
    assert r.returncode == 0 and "STAGING OK" in r.stdout, r.stdout + r.stderr
    assert "next free ruling number: CL-95" in r.stdout
    assert "CL-89: 2026-10-21_apart; 2026-10-22_cascade; 2026-10-22_pauseai-local" in r.stdout


def test_staging_check_catches_an_edited_document():
    import shutil
    staged = os.path.join(TMP, "_docs_bad")
    shutil.copytree(DOCS, staged, ignore=shutil.ignore_patterns("__pycache__"))
    with open(os.path.join(staged, "common_law_core.md"), "a", encoding="utf-8") as fh:
        fh.write("\ntidied\n")
    r = run([os.path.join(SKILL, "check_staging.py"), DOCS, staged])
    assert r.returncode == 1 and "STAGING FAILED" in r.stdout


# ------------------------------------------------------------------ simulator arithmetic
def test_event_row_is_weight_times_probability_shift():
    # CL-2's own example: a law worth 8,000 moved from 10% to 12% earns 2% of its weight.
    p = ledger("law.csv", ["1M,Law passes,event,8000,0.12,0.10,,,,,,policy,,,0,"])
    assert close(mean(p), 160.0)


def test_simulated_mean_matches_and_credit_is_paid_only_when_the_event_happens():
    # CL-16: the law happens in 12% of worlds and is then credited 8000 x (1 - 0.10/0.12) = 1333.3.
    p = ledger("law2.csv", ["1M,Law passes,event,8000,0.12,0.10,,,,,,policy,,,0,"])
    total, _ = simulated(p)
    assert abs(float(total.mean()) - 160.0) < 5
    assert abs(float((total > 0).mean()) - 0.12) < 0.005
    assert close(float(total.max()), 8000 * (1 - 0.10 / 0.12), 1e-6)


def test_pivotal_split_changes_the_spread_but_not_the_mean():
    # CL-55: in 5% of the worlds where it happens the grant was pivotal and gets the full 8,000.
    p = ledger("piv.csv", ["1M,Law passes,event,8000,0.12,0.10,,,0.05,,,policy,,,0,"])
    assert close(mean(p), 160.0)
    total, _ = simulated(p)
    assert abs(float(total.mean()) - 160.0) < 8
    assert close(float(total.max()), 8000.0)


def test_charge_is_fixed_and_never_scaled_by_execution():
    # CL-37 / CL-40: a charge with an exec group is not multiplied.
    p = ledger("charge.csv", ["1M,Bad hires,charge,,,,-10,,,team,,charge,,,0,"])
    assert close(mean(p, execs={"team": {"mean": 0.5}}), -10.0)
    total, _ = simulated(p, execs={"team": {"mean": 0.5}}, n=1000)
    assert close(float(total.min()), -10.0) and close(float(total.max()), -10.0)


def test_execution_factor_in_credit_mode_scales_the_whole_increment():
    # 100 of programme value at a 0.7 execution factor is worth 70.
    p = ledger("exec.csv", ["1M,Programme,continuous,,,,100,0.5,,team,,program,,,0,"])
    assert close(mean(p, execs={"team": {"mean": 0.7, "collapse_p": 0.1}}), 70.0)
    total, _ = simulated(p, execs={"team": {"mean": 0.7, "collapse_p": 0.1}})
    assert abs(float(total.mean()) - 70.0) < 1
    assert abs(float((total == 0).mean()) - 0.1) < 0.005     # collapses in 10% of worlds


def test_execution_factor_in_p1_mode_scales_only_the_with_grant_probability():
    # weight 125, P 10% with and 1% without, factor 0.7: 125 x (0.7 x 0.10 - 0.01) = 7.5
    p = ledger("p1.csv", ["1M,Paper used,event,125,0.10,0.01,,,,team,p1,uptake,,,0,"])
    assert close(mean(p, execs={"team": {"mean": 0.7}}), 7.5)
    # the same row in credit mode: 125 x 0.09 x 0.7 = 7.875
    p = ledger("credit.csv", ["1M,Paper used,event,125,0.10,0.01,,,,team,credit,uptake,,,0,"])
    assert close(mean(p, execs={"team": {"mean": 0.7}}), 7.875)


def test_values_branches_are_weighted_by_the_probability_of_yes():
    # +30 if the answer is yes, -15 if no, P(yes) = 0.4: 0.4 x 30 - 0.6 x 15 = 3
    p = ledger("branch.csv", ["1M,Good,continuous,,,,30,0,,,,values,Q,yes,0,",
                              "1M,Harm,continuous,,,,-15,0,,,,values,Q,no,0,"])
    assert close(mean(p, branches={"Q": 0.4}), 3.0)
    assert close(mean(p, branches={"Q": 1.0}), 30.0) and close(mean(p, branches={"Q": 0.0}), -15.0)
    total, _ = simulated(p, branches={"Q": 0.4})
    assert abs(float((total == 30).mean()) - 0.4) < 0.005    # each world takes one answer


def test_post_2030_share():
    # 100 with a 0.5 post-2030 share plus 100 with none: 50 of 200 is post-2030.
    p = ledger("post.csv", ["1M,Late,continuous,,,,100,0,,,,program,,,0.5,",
                            "1M,Early,continuous,,,,100,0,,,,program,,,0,"])
    total, post = simulated(p, n=1000)
    assert close(float(post.mean()) / float(total.mean()), 0.25)


def test_the_bundled_template_ledger():
    # 150 + 11.25 + 78.1 + 0.5 x 30 - 0.5 x 15 - 4 - 11.1 - 3.75 = 228.0 (no exec factor, P(yes) = 0.5)
    assert close(mean(os.path.join(DOCS, "ledger_template.csv"), branches={"PE_good": 0.5}), 228.0, 1e-6)
    r = run([os.path.join(DOCS, "simulate.py"), os.path.join(DOCS, "ledger_template.csv"), "--n", "20000"])
    assert r.returncode == 0 and "mean (analytic) 228.0" in r.stdout, r.stdout + r.stderr
    # corners: the non-branch rows sum to 220.5; plus 30 if yes, minus 15 if no
    assert "PE_good=yes: 250.5" in r.stdout and "PE_good=no: 205.5" in r.stdout


def test_sizes_are_scored_separately():
    p = ledger("sizes.csv", ["250K,Small,continuous,,,,10,0,,,,program,,,0,",
                             "1M,Large,continuous,,,,30,0,,,,program,,,0,",
                             ",Both,charge,,,,-1,,,,,charge,,,0,"])
    rows = sim.load(p)
    assert sim.sizes_in(rows) == ["250K", "1M"]
    assert close(sim.analytic_mean(sim.rows_for(rows, "250K"), {}, {}), 9.0)
    assert close(sim.analytic_mean(sim.rows_for(rows, "1M"), {}, {}), 29.0)


def test_diff_applies_the_agreement_test_on_group_totals():
    a = ledger("A.csv", ["1M,Media A,continuous,,,,100,0,,,,media,,,0,", "1M,Hire A,charge,,,,-10,,,,,charge,,,0,"])
    b = ledger("B.csv", ["1M,Media B,continuous,,,,80,0,,,,media,,,0,", "1M,Hire B,charge,,,,-10,,,,,charge,,,0,"])
    out = run([os.path.join(DOCS, "simulate.py"), "--diff", a, b, "--size", "1M"]).stdout
    assert "A headline mean 90.0  B headline mean 70.0" in out          # 20 apart, limit 0.3 x 90 = 27
    assert "means within 30%: yes" in out and "largest group: A=media  B=media  same" in out
    assert "groups over the 30% threshold: 0" in out
    c = ledger("C.csv", ["1M,Policy C,continuous,,,,30,0,,,,policy,,,0,"])
    out = run([os.path.join(DOCS, "simulate.py"), "--diff", a, c, "--size", "1M"]).stdout
    assert "means within 30%: NO" in out and "DIFFERENT" in out


def test_bad_ledgers_are_rejected():
    p = ledger("bad.csv", ["1M,Backwards,event,100,0.1,0.2,,,,,,policy,,,0,"])
    r = run([os.path.join(DOCS, "simulate.py"), p])
    assert r.returncode != 0 and "p0 <= p1" in r.stderr


# ------------------------------------------------------------------ range on the mean
def test_mean_range_log_combination():
    # ln(100/50)=0.693, ln(100/80)=0.223 -> sqrt(0.530)=0.728 -> 100 x e^-0.728 = 48.3
    # ln(200/100)=0.693, ln(130/100)=0.262 -> sqrt(0.549)=0.741 -> 100 x e^0.741 = 209.8
    low, high, method, shares = mr.mean_range(100, [50, 80], [200, 130])
    assert method == "log" and abs(low - 48.3) < 0.05 and abs(high - 209.8) < 0.05
    assert abs(sum(shares) - 1) < 1e-9 and shares[0] > shares[1]


def test_mean_range_is_additive_when_a_mean_is_not_positive():
    # central 10, lows -5 and 4, highs 20 and 13: down sqrt(15^2+6^2)=16.16, up sqrt(10^2+3^2)=10.44
    low, high, method, _ = mr.mean_range(10, [-5, 4], [20, 13])
    assert method == "additive" and abs(low - (10 - 16.155)) < 0.01 and abs(high - (10 + 10.440)) < 0.01


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    failures = 0
    for name, fn in tests:
        try:
            fn()
            print(f"ok    {name}")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"FAIL  {name}: {type(exc).__name__}: {exc}")
    print(f"\n{len(tests) - failures} of {len(tests)} tests passed")
    sys.exit(1 if failures else 0)
