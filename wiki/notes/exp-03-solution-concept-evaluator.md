---
title: "Experiment 03: Solution-concept evaluator"
type: note
status: solid
sources: ["[[nash-equilibrium]]", "[[pareto-optimality]]", "[[social-welfare-and-fairness]]"]
updated: 2026-09-19
---

# Experiment 03: Solution-concept evaluator

A generic evaluator for deterministic joint actions in finite two-agent matrix
games passed all five acceptance checks
([experiment record](../../experiments/03-solution-concept-evaluator/README.md)).
It computes realised returns, unilateral-deviation gains, Nash status,
deterministic Pareto status, social welfare, and the book's product-based
fairness measure [Ch. 4.4; Ch. 4.8–4.9].

## Result

Both coordinated Stag Hunt outcomes have zero unilateral-deviation gain and
are therefore Nash equilibria. Hare/hare is nevertheless Pareto-dominated by
stag/stag. The mismatched outcomes have positive unilateral-deviation gains and
are not Nash. A Prisoner's Dilemma case passed as a check against hard-coding
the Stag Hunt matrix.

The implementation makes the quantifier difference executable:

- Nash varies one agent's action while holding the opponent fixed.
- Pareto dominance compares the complete return vector of one candidate joint
  action with the current complete return vector.

Thus independent per-agent maxima answer the Nash question, but cannot answer
the Pareto question: the agents' individually preferred alternatives may be
different joint actions and may harm one another [Ch. 4.4, Eq. 4.16; Ch. 4.8,
Eq. 4.25].

## Scope

The evaluator covers deterministic joint actions only. It does not evaluate
mixed policies, correlated equilibria, sequential games, or regret over an
episode history. It is post-hoc evaluation and does not alter IQL training.

## Related

[[exp-02-iql-stag-hunt-selection]] · [[solution-concepts-as-specifications]] ·
[[nash-equilibrium]] · [[pareto-optimality]]
