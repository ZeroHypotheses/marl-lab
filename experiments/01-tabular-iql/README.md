# Exercise 01 — Tabular IQL

Implement and understand independent Q-learning in the one-step Prisoner's
Dilemma. The `act()` and `learn()` implementation is complete, the focused
tests cover action selection and the terminal update, and the full training run
learned the expected defect/defect greedy behaviour.

## Run the current tests

```bash
uv run pytest experiments/01-tabular-iql/test_iql.py
```

## What this established

- Each agent performs epsilon-greedy selection from its own action space.
- Each agent applies the Q-learning update to its own table.
- Terminal transitions learn their immediate reward without bootstrapping.
- The one-step Prisoner's Dilemma exposes a constant observation and uses
  `0 = cooperate`, `1 = defect`.
- Greedy evaluation after training selects the game's unique Nash equilibrium,
  defect/defect.

The durable write-up is
[`wiki/notes/first-tabular-iql-exercise.md`](../../wiki/notes/first-tabular-iql-exercise.md).

## Follow-up

[`../02-iql-stag-hunt-selection/`](../02-iql-stag-hunt-selection/). That
experiment reused a frozen snapshot of this implementation and found that all
20 preregistered seeds selected Stag Hunt's risk-dominant hare/hare equilibrium.
