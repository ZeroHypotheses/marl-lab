---
title: Lessons from the First Tabular IQL Exercise
type: note
status: solid
sources: ["[[iql-tabular]]", "[[independent-learning]]", "[[temporal-difference-learning]]"]
updated: 2026-09-15
---

# Lessons from the first tabular IQL exercise

Completed in `experiments/01-tabular-iql/`, copied from the read-only upstream
exercise. The implementation was checked with focused tests for greedy action
selection, exploration over heterogeneous action spaces, and terminal updates;
a separate probe verified the non-terminal bootstrap. The full 20,000-episode
training run completed and learned the expected defect/defect behaviour.

## What became concrete

- The one-step Prisoner's Dilemma is stateless: both agents always observe `0`.
  The joint action affects rewards but is not part of either agent's observation
  [`matrix_game.py:24`](../../experiments/01-tabular-iql/matrix_game.py#L24).
- Each independent learner therefore stores $Q_i(0,a_i)$, not a value over the
  joint action. The other learner's changing behaviour appears only through the
  reward samples → [[independent-learning]] [Ch. 5.3.2].
- The two actions are encoded indirectly as `Discrete(2)`, inferred from the
  first two dimensions of the payoff matrix
  [`matrix_game.py:16`](../../experiments/01-tabular-iql/matrix_game.py#L16).
- `learn()` mutates `self.q_tables` in place. Its return value is not consumed by
  the training loop
  [`train_iql.py:100`](../../experiments/01-tabular-iql/train_iql.py#L100).
- A terminal transition must still learn from its reward; `done` removes only
  the bootstrap term. Thus the target is $r_i$ when terminal and
  $r_i+\gamma\max_{a_i'}Q_i(o_i',a_i')$ otherwise [Eq. 2.58].
- The supplied schedule linearly reduces $\epsilon$ from $1$ to $0.01$ over the
  first 80% of training, then holds it at $0.01$. Using a strict comparison
  `random_draw < epsilon` makes the boundary meanings exact: zero always
  exploits and one always explores [Eq. 2.55].

## Evaluation lesson

The learned greedy behaviour reaches the unique Nash equilibrium $(D,D)$, while
evaluation returns sit slightly above its payoff $(1,1)$ because evaluation
retains $\epsilon=0.05$. Mean returns measure performance, not whether a
solution concept is satisfied → [[iql-evaluation-vs-solution-concepts]].

## Related

[[iql-tabular]] · [[independent-learning]] · [[nash-equilibrium]] ·
[[iql-evaluation-vs-solution-concepts]]
