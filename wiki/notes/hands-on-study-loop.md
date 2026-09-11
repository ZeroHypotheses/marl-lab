---
title: A Hands-On Study Loop for marl-lab
type: note
status: solid
sources: ["[[ch02-reinforcement-learning]]", "[[ch05-marl-in-games]]", "[[iql-tabular]]"]
updated: 2026-09-11
---

# A hands-on study loop for marl-lab

The best first implementation after Chapters 1–5 is the **tabular Independent
Q-Learning exercise** in `upstream/exercises/tabular_marl/iql.py`. It turns the
Q-learning and ε-greedy machinery from [Ch. 2.6] into the independent learners
described in [Ch. 5.3.2], while the one-step, stateless Prisoner's Dilemma keeps
the mechanics visible → [Tabular IQL](../topics/iql-tabular.md).

## The loop

Use a short cycle for each new concept:

1. **Predict before running.** State what each algorithm should learn, what the
   plot should look like, and what observation would falsify that prediction.
2. **Implement the smallest missing mechanism.** For IQL, write `act()` first,
   then `learn()`; translate [Eq. 2.55] and [Eq. 2.58] into the per-agent data
   structures without adding abstractions.
3. **Run the supplied baseline.** Inspect evaluation returns and both Q-tables.
   Explain the result using the payoff matrix before changing anything.
4. **Change one cause at a time.** Start with the ε schedule, then learning
   rate, then random seed. Keep the baseline fixed while varying one factor.
5. **Write the conclusion in the wiki.** Record what the result taught, what
   remains unclear, and whether the evidence supports the prediction. A
   learning curve alone does not establish convergence to a solution
   [Ch. 5.2] → [convergence types](../topics/convergence-types.md).

## Questions to answer during the IQL exercise

- Why does the terminal flag matter to the Q-learning target even though
  `gamma=0.99` is configured?
- Which action is dominant in the exercise's payoff matrix, and which joint
  action is the unique [Nash equilibrium](../topics/nash-equilibrium.md)?
- Why can the agents' learned values move even though the environment's payoff
  matrix never changes? → [non-stationarity](../topics/non-stationarity.md)
- Do evaluation returns and Q-values tell the same story?
- Does the apparent result survive several seeds and a different ε decay?

The final two questions turn the coding exercise into a small experiment.
Prisoner's Dilemma is particularly useful because idealised IQL is not
guaranteed to converge in this game class and may obtain average rewards above
the unique Nash-equilibrium reward [Ch. 5.3.2].

## Cadence

A productive cadence is: read one section, predict, implement or inspect one
mechanism, run it, explain the result aloud, then file the durable insight. Use
[Tabular IQL](../topics/iql-tabular.md) immediately after Chapters 1–5;
continue into Chapter 6 only
after the Q-learning-to-IQL connection is comfortable enough to explain
without looking at the code.

## Related

[Tabular IQL](../topics/iql-tabular.md) ·
[independent learning](../topics/independent-learning.md) ·
[temporal-difference learning](../topics/temporal-difference-learning.md) ·
[learning curves](../topics/learning-curves.md)
