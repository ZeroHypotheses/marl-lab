---
title: "Dictionary: RL ↔ Game Theory"
type: topic
status: solid
sources: ["[[ch03-games]]"]
updated: 2026-09-11
---

# Dictionary: RL ↔ Game Theory

MARL sits at the intersection of two fields that share concepts but not
vocabulary. **This book uses RL terminology** [Ch. 3.7, Fig. 3.5] — worth
knowing when reading the game-theoretic primary sources behind
[[ch04-solution-concepts]] and [[ch06-foundational-algorithms]].

| RL (this book) | Game theory | Meaning |
|---|---|---|
| environment | game | the model of actions, observations, rewards and dynamics |
| agent | player | a decision-making entity |
| reward | payoff, utility | scalar received after acting |
| policy | strategy | assigns probabilities to actions |
| deterministic X | pure X | assigns probability 1 to one option |
| probabilistic X | mixed X | assigns probabilities ≤ 1 across options |
| joint X | X profile | a tuple with one element per agent |

So *mixed Nash equilibrium* = probabilistic Nash equilibrium; *pure strategy
profile* = deterministic joint policy; *payoff profile* = joint reward.

> "Player" can also name a **role** rather than an entity — "row player" in a
> matrix game, "white player" in chess [Fig. 3.5]. Note this sits alongside the
> agent-vs-object distinction in [[multi-agent-system]]: an agent may occupy a
> player role, and control an object.

## Related
[[normal-form-games]] · [[solution-concepts]] · [[multi-agent-system]]
