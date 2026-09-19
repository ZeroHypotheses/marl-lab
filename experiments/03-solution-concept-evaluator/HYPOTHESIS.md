---
experiment: 03-solution-concept-evaluator
date: 2026-09-17
status: confirmed
---

# Question

Can a generic evaluator distinguish equilibrium stability from welfare
desirability for deterministic joint actions in a two-agent matrix game?

# Prediction

For Stag Hunt, the evaluator will classify both stag/stag and hare/hare as Nash
equilibria, but only stag/stag as Pareto-optimal, welfare-optimal, and
fairness-optimal. The two mismatched outcomes will have positive unilateral
deviation gains.

This follows from the Chapter 4 definitions: Nash checks unilateral stability,
whereas Pareto, welfare, and fairness compare the agents' returns [Ch. 4.4;
Ch. 4.8–4.9].

# What would falsify it

The prediction is falsified if a correct implementation of the Chapter 4
definitions produces any different classification for the supplied Stag Hunt
payoff matrix.

# Smallest setup that answers it

- Input: any finite two-agent payoff matrix and one deterministic joint action.
- Output: realised returns, unilateral-deviation gains, Nash status,
  deterministic Pareto status, welfare, and fairness.
- Cases: all four Stag Hunt outcomes plus defect/defect in Prisoner's Dilemma.
- Metric: exact agreement with the acceptance tests.

# What the wiki already says

- [[solution-concepts-as-specifications]]: a solution concept can evaluate an
  output without appearing in the learning update.
- [[nash-equilibrium]]: Nash is mutual best response [Ch. 4.4, Eq. 4.16].
- [[pareto-optimality]]: Pareto dominance compares complete return vectors
  [Ch. 4.8, Eq. 4.25].
- [[social-welfare-and-fairness]]: welfare sums returns and the book's fairness
  measure multiplies them [Ch. 4.9, Eqs. 4.26–4.27].

# Result

Confirmed on 2026-09-19. The evaluator passed all five acceptance checks: both
coordinated Stag Hunt outcomes are Nash, only stag/stag is Pareto-optimal, and
both mismatched outcomes have positive unilateral-deviation gains. The
Prisoner's Dilemma defect/defect case also passed, showing that the evaluator
is not hard-coded to Stag Hunt.

Exact command:

```bash
.venv/bin/pytest experiments/03-solution-concept-evaluator/checks.py -q
```

Observed result: `5 passed in 0.06s`.

# Filed as

[[exp-03-solution-concept-evaluator]]
