---
title: Correlated Q-Learning
type: algorithm
status: solid
sources: ["[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Correlated Q-Learning

## One-line

Correlated Q-learning uses a selected correlated equilibrium of each learned
state game for behaviour and for the next-state TD value [Ch. 6.2.3].

## Setting

Finite discounted general-sum stochastic games, with joint actions and all
rewards observable to each learner [Algorithm 7]. Execution additionally needs
a mechanism that samples a correlated joint action and privately communicates
recommendations to agents [Ch. 6.2.3].

## Update rule

Use the [[joint-action-learning]] update with

$$
\operatorname{Value}_i(\Gamma_s)
=\sum_a \pi_c(a)Q_i(s,a),
$$

where $\pi_c$ is a selected [[correlated-equilibrium]] of the Q-value game at
$s$ [Ch. 6.2.3]. A linear program can find such a distribution, optionally
using an objective such as social welfare to select among them [Ch. 4.6.1;
Ch. 6.2.3].

## Why it works / when it breaks

Correlated equilibria form a larger set than Nash equilibria and are polynomial
to compute by linear programming, but the larger set worsens equilibrium
selection. Different learners must agree on the same correlated distribution,
and the book gives no general convergence conditions for this Q-learning
variant [Ch. 6.2.3]. Correlated sampling is also an extra execution mechanism,
not something produced automatically by independent action draws.

## Relation to

[[correlated-equilibrium]] · [[joint-action-learning]] · [[nash-q-learning]] ·
[[regret-matching]]

## In the codebase

No implementation is indexed in `upstream/codebase/`; the book presents it as
an instantiation of Algorithm 7.

## Open questions

- Can a decentralised public signal provide the needed correlation without
  becoming a trusted central mediator?
