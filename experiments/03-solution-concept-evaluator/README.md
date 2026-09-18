# Experiment 03 — Solution-concept evaluator

Turn the written audit of Experiment 02 into executable evaluation. This is a
post-hoc evaluator: it receives a known two-agent payoff matrix and one
deterministic joint action. It does **not** alter or rerun IQL.

## Learning goal

Make the distinction between a learning algorithm and a solution concept
concrete. IQL produces a joint action; this evaluator decides what that action
means under several Chapter 4 specifications →
[`solution-concepts-as-specifications`](../../wiki/notes/solution-concepts-as-specifications.md).

This experiment deliberately demonstrates the **post-training** role only.
Chapter 6 also introduces algorithms in which solution concepts participate in
training itself—for example, joint-action learners can use equilibrium
solutions to select policies and form TD targets [Ch. 6 introduction; §§6.1–6.2].
Those are different algorithms from the plain IQL used in Experiment 02.

## Your task

Implement `evaluate_joint_action()` in `evaluator.py`. Keep the implementation
generic over rectangular, two-agent payoff matrices; do not hard-code the Stag
Hunt payoffs.

For the supplied joint action, return:

1. its two realised returns;
2. each agent's unilateral-deviation gain;
3. whether it is a Nash equilibrium;
4. whether another deterministic joint action Pareto-dominates it;
5. its social welfare (sum of returns);
6. its fairness score (product of returns).

The scope is deliberately narrow: deterministic joint actions in finite,
two-agent normal-form games. Mixed policies, correlated-equilibrium
constraints, and sequential games are out of scope.

## Definitions to translate

- Nash equilibrium: no profitable unilateral deviation [Ch. 4.4, Eq. 4.16].
- Pareto dominance: all agents weakly improve and at least one strictly
  improves [Ch. 4.8, Eq. 4.25].
- Social welfare: sum of expected returns [Ch. 4.9, Eq. 4.26].
- Fairness: product of expected returns [Ch. 4.9, Eq. 4.27].

The deviation gain should include the current action among the alternatives,
so it is never negative. Treat the joint action as Nash when both gains are
zero. The provided games use integer payoffs, so no numerical tolerance is
needed yet.

## Run the checks

```bash
.venv/bin/pytest experiments/03-solution-concept-evaluator/checks.py -q
```

The tests cover all four Stag Hunt outcomes and one Prisoner's Dilemma outcome.
They are intended to fail with `NotImplementedError` until you implement the
evaluator.

## Suggested order

1. Return the realised payoff, welfare, and fairness.
2. Compute unilateral-deviation gains for one agent at a time.
3. Derive `is_nash` from those gains.
4. Enumerate the payoff matrix to determine deterministic Pareto optimality.

## Stretch exercise—after Chapter 6 §6.5

Instrument an episode sequence and compute external regret using Eq. 4.28.
That requires the opponents' realised actions across episodes; it cannot be
recovered from only the final greedy joint action.
