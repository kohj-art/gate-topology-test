# Test B, the control topology

A throwaway repository that proves the controls behave, using no Accenture content and no
client content. `gate.py` stands in for `harness/check.py`: it takes time, needs no
credentials, and exits zero or non-zero. Nothing else about the real gate matters here.

When the approved host arrives, the configuration transfers and the learning is already
done.

## What this is for

Six things, and each has a test that either passes or does not.

| # | What it proves | How you know |
|---|---|---|
| 1 | A required check blocks a merge | Set `gate-verdict.txt` to `no` in a branch, open a pull request, the merge button stays disabled |
| 2 | Nobody pushes straight to main | `git push origin main` is refused, including by you |
| 3 | An agent can open a pull request | A token scoped to contents and pull requests creates a branch and a pull request |
| 4 | An agent cannot merge | The same token gets 403 on a merge |
| 5 | A deployment needs a person | `deploy` pauses for approval and records who gave it |
| 6 | What a real gate costs | Set `GATE_SECONDS` to 1200 and read the minutes used |

## The controls this repository expects

Branch protection on `main`: pull request required, one approval, the `gate / run` status
check required, force push and deletion refused.

An environment called `instance` with a required reviewer, which `deploy.yml` uses.

## What deliberately is not here

No secrets. The real gate needs none, which is what makes a hosted runner sufficient and
keeps the threat model small. If a secret ever becomes necessary for the gate rather than
for a deployment, that is a design change worth arguing about rather than a configuration
change.

No NCSR content, no authority copies, no declarations. That is the point.
