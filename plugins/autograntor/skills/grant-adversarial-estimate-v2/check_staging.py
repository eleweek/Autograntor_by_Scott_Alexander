#!/usr/bin/env python3
"""Check that the Autograntor standard documents were staged correctly.

Usage: python3 check_staging.py <skill docs folder> <staged folder, e.g. grant_eval/_docs>

Part of the self-contained packaging, not one of the owner's files. It reads the documents and
runs the bundled scripts; it never changes anything. Exit status is 0 when every check passes.
"""
import filecmp
import os
import re
import subprocess
import sys

if len(sys.argv) != 3:
    sys.exit(__doc__)
src, dst = sys.argv[1], sys.argv[2]
failed = []


def check(label, ok, detail=""):
    print(f"[{'ok' if ok else 'FAIL'}] {label}" + (f": {detail}" if detail else ""))
    if not ok:
        failed.append(label)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def ruling_numbers(path):
    return [int(n) for n in re.findall(r"(?m)^### CL-(\d+)", read(path))]


# ---- 1. every bundled file is present and identical ------------------------------------
missing, changed = [], []
for root, _dirs, files in os.walk(src):
    for name in files:
        if name.endswith(".pyc"):
            continue
        rel = os.path.relpath(os.path.join(root, name), src)
        target = os.path.join(dst, rel)
        if not os.path.exists(target):
            missing.append(rel)
        elif not filecmp.cmp(os.path.join(root, name), target, shallow=False):
            changed.append(rel)
check("every bundled file is staged", not missing, ", ".join(missing))
own_milestones = changed == ["milestones_added.md"]
check("staged copies are byte-identical", not changed or own_milestones,
      "milestones_added.md differs (expected if it is the user's own copy)" if own_milestones
      else ", ".join(changed))

# ---- 2. the frozen Common Law is complete -----------------------------------------------
topics_dir = os.path.join(dst, "common_law_topics")
frozen_files = [os.path.join(dst, "common_law_core.md")]
if os.path.isdir(topics_dir):
    frozen_files += [os.path.join(topics_dir, f) for f in sorted(os.listdir(topics_dir)) if f.endswith(".md")]
counts = {}
for f in frozen_files:
    if os.path.exists(f):
        for n in ruling_numbers(f):
            counts[n] = counts.get(n, 0) + 1
expected = list(range(1, 84)) + [91]
wrong = [n for n in expected if counts.get(n, 0) != 1]
extra = sorted(n for n in counts if n not in expected)
check("CL-1 to CL-83 and CL-91 each have exactly one full text in the core and topic files",
      not wrong and not extra,
      (f"wrong count for {wrong} " if wrong else "") + (f"unexpected {extra}" if extra else ""))
index = os.path.join(dst, "common_law_index.md")
n_index = len(re.findall(r"(?m)^- CL-\d+", read(index))) if os.path.exists(index) else 0
check("the index has 84 ruling lines", n_index == 84, f"found {n_index}")

# ---- 3. the scripts run -----------------------------------------------------------------
def run(args):
    try:
        p = subprocess.run([sys.executable] + args, capture_output=True, text=True, timeout=120)
        return p.returncode, p.stdout, p.stderr
    except Exception as exc:  # noqa: BLE001 - report any failure to start
        return 1, "", str(exc)


try:
    import numpy  # noqa: F401
    check("numpy is installed (simulate.py needs it)", True)
except ImportError:
    check("numpy is installed (simulate.py needs it)", False, "run: pip install numpy")

sim = os.path.join(dst, "simulate.py")
template = os.path.join(dst, "ledger_template.csv")
code, out, err = run([sim, "--template"])
check("simulate.py --template prints the template",
      code == 0 and os.path.exists(template) and out == read(template), err.strip()[-200:])
code, out, err = run([sim, template])
check("simulate.py runs the template ledger and prints a mean",
      code == 0 and "mean (analytic)" in out, err.strip()[-200:])
code, out, err = run([os.path.join(dst, "mean_range.py"), "--central", "100", "--low", "50,80", "--high", "200,130"])
m = re.search(r"range on the mean: ([\d.,]+) to ([\d.,]+)", out)
ok = bool(m) and abs(float(m.group(1)) - 48) < 2 and abs(float(m.group(2).replace(",", "")) - 210) < 5
check("mean_range.py gives about 48 to 210 on the test inputs", code == 0 and ok,
      (m.group(0) if m else err.strip()[-200:]))
code, out, err = run([os.path.join(dst, "fetch_manifund.py"), "--help"])
check("fetch_manifund.py --help runs", code == 0, err.strip()[-200:])

# ---- 4. the proposed folder ---------------------------------------------------------------
prop = os.path.join(dst, "common_law_proposed")
files = sorted(f for f in os.listdir(prop) if f.endswith(".md") and f != "README.md") if os.path.isdir(prop) else []
bundled = set(os.listdir(os.path.join(src, "common_law_proposed"))) if os.path.isdir(os.path.join(src, "common_law_proposed")) else set()
used = {}
for f in files:
    for n in ruling_numbers(os.path.join(prop, f)):
        used.setdefault(n, []).append(f[:-3])
print(f"\ncommon_law_proposed/ holds {len(files)} ruling files (name these in every subagent prompt):")
for f in files:
    nums = ", ".join(f"CL-{n}" for n in ruling_numbers(os.path.join(prop, f)))
    print(f"  {f}  [{nums}]" + ("" if f in bundled else "  (added to the bundled set)"))
dups = {n: fs for n, fs in sorted(used.items()) if len(fs) > 1}
if dups:
    print("ruling numbers used more than once (cite these as number plus file name):")
    for n, fs in dups.items():
        print(f"  CL-{n}: " + "; ".join(fs))
highest = max(list(counts) + list(used) + [83])
print(f"next free ruling number: CL-{highest + 1}")
print(f"newest proposed file: {files[-1] if files else '(none)'}")

print("\nSTAGING " + ("OK" if not failed else "FAILED: " + "; ".join(failed)))
sys.exit(1 if failed else 0)
