# Experiment 02 — IQL equilibrium selection in Stag Hunt

Test whether independent exploration makes tabular IQL select the
risk-dominant hare/hare equilibrium more often than the reward-dominant
stag/stag equilibrium. Read [HYPOTHESIS.md](HYPOTHESIS.md) before writing code.

## Your task

Implement `run.py` without changing the IQL algorithm from experiment 01:

1. Construct the one-step Stag Hunt payoff matrix specified in
   `HYPOTHESIS.md` locally in this experiment.
2. Reuse the tested IQL implementation from experiment 01 and preserve its
   provenance; do not edit `upstream/`.
3. Train once for every preregistered seed `0..19` with the fixed configuration.
4. Disable exploration when extracting each final **greedy** joint action.
5. Classify every seed as stag/stag, hare/hare, or mismatched.
6. Print the per-seed classification and aggregate counts, plus the final
   Q-values as secondary evidence.
7. Fill in `HYPOTHESIS.md` only after all preregistered runs finish.

Do not tune the epsilon schedule, learning rate, budget, or seed set after
seeing the result. Those are possible follow-up experiments, not part of this
one.

## Run it

```bash
.venv/bin/python experiments/02-iql-stag-hunt-selection/run.py
```

The runner prints every seed's final greedy joint action and Q-values, followed
by counts for stag/stag, hare/hare, and mismatched outcomes.

## Reproducing

- Seeds: `0..19`
- Training budget: 20,000 one-step episodes per seed
- Exact command: `.venv/bin/python experiments/02-iql-stag-hunt-selection/run.py`
- Baseline implementation: local `tabular_iql/` snapshot, copied unchanged
  from `experiments/01-tabular-iql/` at commit
  `d379f3b0d296830d29db5fc00d0388cfa7a34126`

## Findings

The preregistered prediction was confirmed: all 20 seeds selected the
risk-dominant hare/hare equilibrium under greedy evaluation.

| Final greedy joint action | Seeds |
|---|---:|
| stag/stag | 0 |
| hare/hare | 20 |
| mismatched | 0 |

Across the 40 final per-agent Q-tables, the learned value of Hare ranged from
`2.000000` to `2.050000`, while Stag ranged from `0.000372` to `0.127501`.
This result is specific to the fixed payoff matrix, epsilon schedule, learning
rate, training budget, and seeds above; it is not a general convergence claim
about IQL.
