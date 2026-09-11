---
title: Evaluation with Learning Curves
type: topic
status: solid
sources: ["[[ch02-reinforcement-learning]]"]
updated: 2026-09-11
---

# Evaluation with Learning Curves

"The standard approach to evaluate the performance of an RL algorithm on a
learning problem" [Ch. 2.7]. Methodologically the most directly useful section of
chapter 2 — it should govern anything written in `experiments/`.
See also §10.6 ([[ch10-marl-in-practice]]).

## The book's own protocol

For Fig. 2.4 (Sarsa vs Q-learning on the Mars Rover, $\gamma = 0.95$):

- **y-axis: *evaluation* returns** — returns of the **greedy** policy extracted
  from the learned values after $T$ steps, not the returns collected while
  exploring. The question answered is: *if I stop now and go greedy, what do I
  get?*
- averaged over **100 independent training runs**, each with a different seed;
- each point runs **100 independent episodes** of that run's greedy policy, then
  averages over runs;
- shaded band = standard deviation **across the per-run averages**.

For policy-gradient algorithms there is usually no "greedy" version, so the
current policy is evaluated unmodified [footnote 8].

## x-axis: cumulative time steps, not episodes

The most transferable point in the section [Ch. 2.7]. Plotting against
**episodes** can silently favour an algorithm: if A explores more per episode
than B, then at equal episode counts A has collected more experience and done
more updates, so its curve rises faster — for reasons that have nothing to do
with the algorithm being better. **Cumulative environment time steps across
episodes removes that confound.**

## Reporting a different metric than you optimised

Undiscounted returns, episode lengths and win rates are often easier to read
than discounted returns — the book shows episode length in Fig. 2.4(b). But:

> "It is important to keep in mind that the evaluated policy was not actually
> trained to maximize these objectives — it was trained to maximize the expected
> discounted return for a specific discount factor" [Ch. 2.7].

And since two problems differing only in $\gamma$ may have different optimal
policies ([[returns-and-discounting]]), an undiscounted curve can rank policies
differently from the objective they were trained on. Report it as a secondary
metric, not as the result.

## Hyperparameters visibly matter

Figs. 2.4(c)/(d) vary $\alpha$ and $\epsilon$ for Q-learning. The "theoretically
sound" $\alpha_k = 1/k$ wins here, but "for more complex MDPs with larger state
and action sets, this choice of learning rate usually leads to much slower
learning compared to appropriately chosen constant learning rates" [Ch. 2.7].

## For this lab

Carry into `workflows/experiment.md`: cumulative steps on the x-axis, evaluation
(greedy) returns on the y, many seeds, report spread, and state which metric is
the objective and which is secondary.

## Related
[[temporal-difference-learning]] · [[returns-and-discounting]] ·
[[ch10-marl-in-practice]]
