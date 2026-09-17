---
experiment: 02-iql-stag-hunt-selection
date: 2026-09-15
status: complete
---

# Question

With the tabular IQL implementation and hyperparameters held fixed from
`experiments/01-tabular-iql/`, does early independent exploration make the
agents select Stag Hunt's risk-dominant hare/hare equilibrium more often than
its reward-dominant stag/stag equilibrium?

# Prediction

The final greedy joint action will be hare/hare in more than half of the
preregistered seeds. Early random play frequently mismatches the agents: stag
then pays `0`, while hare guarantees at least `2`. IQL absorbs the other
learner's behaviour into its reward samples, so that early safety advantage can
reinforce hare for both agents [Ch. 5.4.2; [[equilibrium-selection]]].

# What would falsify it

The prediction is falsified if hare/hare is the final greedy joint action in at
most 10 of the 20 seeds `0..19`. Stag/stag and mismatched final greedy actions
must be reported separately rather than silently grouped together.

# Smallest setup that answers it

- Environment: one-step stateless Stag Hunt with action `0 = stag`,
  `1 = hare`; payoffs `(S,S)=(4,4)`, `(S,H)=(0,3)`, `(H,S)=(3,0)`,
  `(H,H)=(2,2)` [Ch. 5.4.2, Fig. 5.6(b)].
- Algorithms compared: tabular IQL only, reused unchanged from experiment 01.
- Seeds: the preregistered set `0..19`.
- Training budget: 20,000 one-step episodes per seed.
- Fixed hyperparameters: `gamma=0.99`, learning rate `0.05`, and the existing
  epsilon schedule from experiment 01.
- Primary metric: count of final greedy joint actions classified as stag/stag,
  hare/hare, or mismatched.
- Secondary evidence: final per-agent Q-values for both actions.

# What the wiki already says

- [[equilibrium-selection]]: IQL can be prone to Stag Hunt's risk-dominant
  equilibrium when agents are uncertain about one another [Ch. 5.4.2].
- [[independent-learning]]: each learner treats the changing policies of the
  others as part of its environment [Ch. 5.3.2, Eq. 5.10].
- [[convergence-types]]: stable returns alone do not establish convergence to a
  solution [Ch. 5.2]. This experiment classifies the final greedy policy
  directly rather than relying only on returns.
- [[first-tabular-iql-exercise]]: the reused IQL implementation passed focused
  action-selection and update tests and completed the Prisoner's Dilemma run.

# Result

**Confirmed.** The final greedy joint action was hare/hare for all 20
preregistered seeds. No seed ended at stag/stag or at a mismatched joint action.

| Final greedy joint action | Count |
|---|---:|
| stag/stag | 0 |
| hare/hare | 20 |
| mismatched | 0 |

The primary falsification threshold was hare/hare in at most 10 seeds; the
observed count was 20. Final per-agent Hare Q-values ranged from `2.000000` to
`2.050000`, while Stag Q-values ranged from `0.000372` to `0.127501`.

Exact command:

```bash
.venv/bin/python experiments/02-iql-stag-hunt-selection/run.py
```

This confirms the prediction only for the preregistered configuration. It does
not show that IQL must select hare/hare under different payoff magnitudes,
initialisation, exploration schedules, learning rates, budgets, or seeds.

# Filed as

[[exp-02-iql-stag-hunt-selection]].
