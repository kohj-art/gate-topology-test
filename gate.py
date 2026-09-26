# -*- coding: utf-8 -*-
"""A stand-in for `harness/check.py`, with the same shape and none of the content.

WHAT IT IMITATES. The real gate takes fifteen to twenty minutes, needs no credentials,
and exits zero or non-zero. That is everything the control topology depends on. Nothing
here needs to know what the real gate checks.

HOW TO MAKE IT FAIL. Put `no` in `gate-verdict.txt`. That is the whole mechanism, and it
exists so a pull request can deliberately fail the check and you can watch the merge
button stay disabled. A control nobody has seen refuse something is a control nobody has
tested.

HOW LONG IT RUNS. `GATE_SECONDS`, default 60. Run the topology tests at the default so
iteration is quick. Set it to 1200 for one run when you want to measure what a real
twenty minute gate costs in Actions minutes.
"""
import io
import os
import sys
import time

VERDICT = "gate-verdict.txt"


def main():
    seconds = int(os.environ.get("GATE_SECONDS", "60"))
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, VERDICT)

    verdict = "yes"
    if os.path.isfile(path):
        verdict = io.open(path, encoding="utf-8").read().strip().lower()

    print("gate: running for %d second(s)" % seconds)
    print("gate: verdict file says %r" % verdict)
    sys.stdout.flush()

    step = max(1, seconds // 10)
    waited = 0
    while waited < seconds:
        time.sleep(min(step, seconds - waited))
        waited += step
        print("  ... %d of %d seconds" % (min(waited, seconds), seconds))
        sys.stdout.flush()

    if verdict == "no":
        print("")
        print("FAIL  the verdict file says no. This is the deliberate failure.")
        return 2
    print("")
    print("PASS  1 check, proven able to fail.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
