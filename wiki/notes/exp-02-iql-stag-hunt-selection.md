---
title: "Experiment 02: IQL equilibrium selection in Stag Hunt"
type: note
status: solid
sources: ["[[equilibrium-selection]]", "[[iql-tabular]]", "[[independent-learning]]"]
updated: 2026-09-17
---

# Experiment 02: IQL equilibrium selection in Stag Hunt

In a one-step, stateless Stag Hunt, the unchanged tabular IQL baseline selected
the risk-dominant hare/hare equilibrium in all 20 preregistered seeds. It never
selected reward-dominant stag/stag or a mismatched final greedy joint action
([experiment record](../../experiments/02-iql-stag-hunt-selection/README.md)).

## Question and prediction

Stag Hunt has two deterministic Nash equilibria: stag/stag pays $(4,4)$ and is
reward-dominant, while hare/hare pays $(2,2)$ and is risk-dominant because Hare
guarantees at least 2 when the other agent's choice is uncertain [Ch. 5.4.2].
The preregistered prediction was that IQL would finish at hare/hare in more than
10 of seeds `0..19`
([preregistration](../../experiments/02-iql-stag-hunt-selection/HYPOTHESIS.md)).

## Setup

- One-step payoff matrix: $(S,S)=(4,4)$, $(S,H)=(0,3)$,
  $(H,S)=(3,0)$, and $(H,H)=(2,2)$ [Ch. 5.4.2, Fig. 5.6(b)].
- Unchanged IQL snapshot from Experiment 01 at commit
  `d379f3b0d296830d29db5fc00d0388cfa7a34126`.
- Seeds `0..19`; 20,000 episodes per seed; learning rate `0.05`;
  `gamma=0.99`; Experiment 01's epsilon schedule
  ([runner](../../experiments/02-iql-stag-hunt-selection/run.py)).
- Evaluation set epsilon to zero and classified the final greedy joint action,
  rather than inferring a solution from mean return
  ([runner](../../experiments/02-iql-stag-hunt-selection/run.py)).

Exact command:

```bash
.venv/bin/python experiments/02-iql-stag-hunt-selection/run.py
```

## Result

| Final greedy joint action | Count |
|---|---:|
| stag/stag | 0 |
| hare/hare | 20 |
| mismatched | 0 |

The prediction was confirmed: the observed hare/hare count was 20, above the
preregistered threshold of 10. Across the 40 final per-agent tables, Hare's
Q-value ranged from `2.000000` to `2.050000`; Stag's ranged from `0.000372` to
`0.127501` ([recorded output](../../experiments/02-iql-stag-hunt-selection/README.md)).

## The same result under different solution concepts

Applying several Chapter 4 concepts to the four deterministic joint actions
changes the verdict without changing the learned policy:

| Criterion | stag/stag $(4,4)$ | hare/hare $(2,2)$ | What it says about Experiment 02 |
|---|---|---|---|
| Nash | passes | passes | The result is stable against unilateral deviation, but Nash does not select between the two equilibria [Ch. 4.4, Eq. 4.16]. |
| Pareto optimality | passes | fails | stag/stag makes both agents strictly better off, so it Pareto-dominates hare/hare [Ch. 4.8, Eq. 4.25]. |
| Social welfare | $8$ | $4$ | stag/stag uniquely maximises the sum of returns among deterministic outcomes [Ch. 4.9, Eq. 4.26]. |
| Fairness product | $16$ | $4$ | stag/stag also wins the book's product-based fairness criterion; symmetry means there is no distributional trade-off here [Ch. 4.9, Eq. 4.27]. |
| Correlated equilibrium | passes | passes | Every Nash equilibrium is a correlated equilibrium, so this broader concept still does not select between them [Ch. 4.6]. |
| No-regret | unknown | unknown | No-regret judges the whole episode sequence, not only the final greedy policy; the runner did not retain the action history needed for Eq. 4.28 [Ch. 4.10]. |

For the mismatched outcomes, the Nash deviation gains are non-zero:
$\delta(S,H)=(2,1)$ and $\delta(H,S)=(1,2)$, whereas both coordinated outcomes
have zero deviation gain. Thus a small checker can distinguish “is Nash?” from
“which Nash equilibrium is desirable?” without changing IQL's update rule.
The corresponding implementation exercise is
[Experiment 03](../../experiments/03-solution-concept-evaluator/README.md).

## Interpretation and limits

The result is consistent with the mechanism in [[equilibrium-selection]]:
early independent exploration often mismatches the agents, giving Stag reward
0 while Hare remains safe, and the learned preferences reinforce hare/hare
[Ch. 5.4.2]. The experiment observes the selected equilibrium; it does not by
itself isolate early mismatches as the cause.

This is not a general convergence result for IQL. It is conditional on this
payoff matrix, zero initial Q-values, constant learning rate, epsilon schedule,
20,000-episode budget, and seed set. The non-zero exploration floor also means
the final Q-values continue to reflect occasional exploratory transitions even
though the reported joint action is extracted greedily
([IQL snapshot](../../experiments/02-iql-stag-hunt-selection/tabular_iql/iql.py)).

## Related

[[equilibrium-selection]] · [[iql-tabular]] · [[independent-learning]] ·
[[convergence-types]] · [[iql-evaluation-vs-solution-concepts]]
