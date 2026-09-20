---
title: Best Response
type: topic
status: solid
sources: ["[[ch04-solution-concepts]]", "[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Best Response

The primitive from which most [[solution-concepts]] are built [Ch. 4.2].

Given $\pi_{-i} = (\pi_1,\dots,\pi_{i-1},\pi_{i+1},\dots,\pi_n)$, the set of best
responses for agent $i$ is
$$BR_i(\pi_{-i}) = \arg\max_{\pi_i} U_i(\langle \pi_i, \pi_{-i}\rangle)$$
[Eq. 4.9]

Every equilibrium concept in the chapter is then a *mutual* best-response
condition: [[minimax]] is $\pi_i \in BR_i(\pi_j)$ and $\pi_j \in BR_j(\pi_i)$;
[[nash-equilibrium]] is $\pi_i \in BR_i(\pi_{-i})$ for all $i$.

## Best responses are not unique

$BR_i(\pi_{-i})$ may contain many policies — possibly infinitely many. The
book's example [Ch. 4.3]: in Rock-Paper-Scissors, if agent $i$ plays uniformly,
then **every** policy of agent $j$ is a best response, all yielding expected
reward 0.

> The instructive part: even though every $\pi_j$ is a best response to a uniform
> $\pi_i$, the *only* joint policy where both are best responses **to each other**
> is uniform–uniform. Mutuality is what does the work, not optimality alone.

## As an operator

Best-response operators are also used to *compute* solutions iteratively — in
game theory and in MARL. The book points forward to **fictitious play** (§6.3.1)
and **joint-action learning with agent modelling** (§6.3.2)
→ [[ch06-foundational-algorithms]].

Chapter 6 makes the operator concrete: [[fictitious-play]] best-responds to
empirical action frequencies, while [[jal-agent-modelling]] learns
state-conditioned opponent models and evaluates actions through a joint-action
Q-function [Eqs. 6.13–6.17]. Their response is optimal only with respect to the
model; model error and simultaneous adaptation can therefore turn an exact
computed best response into a poor action against the real agent [Ch. 6.3].

Knowing another agent's reward function lets you estimate its best response,
which is one of the things [[knowledge-assumptions]] says MARL usually cannot
assume.

## Related
[[solution-concepts]] · [[minimax]] · [[nash-equilibrium]] · [[agent-modelling]] ·
[[fictitious-play]]
