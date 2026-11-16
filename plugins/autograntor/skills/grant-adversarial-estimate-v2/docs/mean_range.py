#!/usr/bin/env python3
"""
Range on the mean for an Autograntor forecast (input uncertainty, not outcome risk).

simulate.py's P10-P90 says how the world might turn out if the ledger's inputs are right.
This script answers the other question: how far the MEAN could move if the inputs are wrong.

The judge picks the three to five inputs whose uncertainty matters most (for example the
no-grant run-rate, the marginal factor, an elite headcount, a career-entry rate). For each
it states a plausible low and high value, roughly a 10th and 90th percentile, and recomputes
the mean with only that input changed. Give those means here:

  python3 mean_range.py --central 360 --low 300,270,290 --high 480,400,410 \
                        --names "entry rate,run-rate,absorptive share"

--low and --high are MEANS (in utility), one per input, in the same order. If an input's
"low" value happens to raise the mean, that is fine: the script sorts each pair itself.

Method. The inputs are treated as independent. When the central mean and every low/high
mean are positive, deviations are combined in log space (right for inputs that multiply):
  up = sqrt(sum ln(high_i/central)^2), down = sqrt(sum ln(central/low_i)^2),
  range = central*exp(-down) .. central*exp(up).
Otherwise (a mean at or below zero somewhere) they are combined additively:
  range = central - sqrt(sum (central-low_i)^2) .. central + sqrt(sum (high_i-central)^2).
Combining 10th/90th-percentile deviations this way gives about an 80% range.
"""
import argparse, math, sys


def parse(s):
    try:
        return [float(x.strip()) for x in s.split(",") if x.strip()]
    except ValueError:
        sys.exit(f"could not read numbers from '{s}' (use comma-separated means, no thousands separators)")


def mean_range(central, lows, highs):
    pairs = [(min(a, b, central), max(a, b, central)) for a, b in zip(lows, highs)]
    use_log = central > 0 and all(lo > 0 for lo, _ in pairs)
    if use_log:
        downs = [math.log(central / lo) for lo, _ in pairs]
        ups = [math.log(hi / central) for _, hi in pairs]
        low = central * math.exp(-math.sqrt(sum(d * d for d in downs)))
        high = central * math.exp(math.sqrt(sum(u * u for u in ups)))
    else:
        downs = [central - lo for lo, _ in pairs]
        ups = [hi - central for _, hi in pairs]
        low = central - math.sqrt(sum(d * d for d in downs))
        high = central + math.sqrt(sum(u * u for u in ups))
    weight = [d * d + u * u for d, u in zip(downs, ups)]
    total = sum(weight) or 1.0
    shares = [w / total for w in weight]
    return low, high, ("log" if use_log else "additive"), shares


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--central", type=float, required=True, help="the headline mean")
    ap.add_argument("--low", required=True, help="comma-separated means, one per input at its low value")
    ap.add_argument("--high", required=True, help="comma-separated means, one per input at its high value")
    ap.add_argument("--names", help="optional comma-separated input names, same order")
    # Join "--low -9,-10.6" into "--low=-9,-10.6" so that negative means are not read as options.
    argv, i = [], 1
    while i < len(sys.argv):
        if sys.argv[i] in ("--central", "--low", "--high", "--names") and i + 1 < len(sys.argv):
            argv.append(sys.argv[i] + "=" + sys.argv[i + 1])
            i += 2
        else:
            argv.append(sys.argv[i])
            i += 1
    args = ap.parse_args(argv)
    lows, highs = parse(args.low), parse(args.high)
    if not lows or len(lows) != len(highs):
        sys.exit(f"--low has {len(lows)} values and --high has {len(highs)}; they must match, one pair per input")
    names = [n.strip() for n in args.names.split(",")] if args.names else [f"input {i + 1}" for i in range(len(lows))]
    if len(names) != len(lows):
        sys.exit(f"--names has {len(names)} entries for {len(lows)} inputs")
    low, high, method, shares = mean_range(args.central, lows, highs)
    print(f"80% range on the mean: {low:,.1f} to {high:,.1f}  (central {args.central:,.1f}; "
          f"{len(lows)} inputs; {method} combination; inputs assumed independent)")
    if args.central > 0 and low > 0:
        print(f"as multiples of the central mean: x{low / args.central:.2f} to x{high / args.central:.2f}")
    print("share of the spread from each input:")
    for n, lo, hi, s in sorted(zip(names, lows, highs, shares), key=lambda r: -r[3]):
        print(f"  {s:>4.0%}  {n}  (mean {min(lo, hi):,.1f} to {max(lo, hi):,.1f})")
    if len(lows) < 3:
        print("note: fewer than three inputs; the range is probably too narrow")


if __name__ == "__main__":
    main()
