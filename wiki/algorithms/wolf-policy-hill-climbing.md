---
title: Win or Learn Fast Policy Hill Climbing (WoLF-PHC)
type: algorithm
status: solid
sources: ["[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Win or Learn Fast Policy Hill Climbing (WoLF-PHC)

## One-line

WoLF-PHC combines Q-learning and policy hill climbing, moving cautiously when
winning and rapidly when losing [Ch. 6.4.4].

## Setting

Finite general-sum stochastic games with any finite number of agents and
actions. Each agent learns independently from its own state, action, and reward;
it does not require other policies or reward functions [Algorithm 9].

## Update rule

For every state, the agent keeps Q-values, its current stochastic policy
$\pi_i$, an incremental average policy $\bar\pi_i$, and a visit count. Q-values
receive the ordinary off-policy Q-learning update [Eq. 6.40]. The average
policy is updated toward the current policy [Eqs. 6.41–6.42]. Policy hill
climbing shifts probability toward a greedy action [Eqs. 6.43–6.46], using a
small step $\delta_w$ when the current policy's estimated value exceeds the
average policy's and a larger step $\delta_l$ otherwise, with
$\delta_l>\delta_w$ [Algorithm 9].

## Why it works / when it breaks

The asymmetric rates damp movement near a successful strategy while permitting
fast correction when the opponent gains an advantage [Ch. 6.4.3–6.4.4]. The
book demonstrates stronger policy convergence than ordinary PHC in
Rock-Paper-Scissors, but does not give WoLF-PHC a general stochastic-game
convergence theorem [Ch. 6.4.4]. Its winning test depends on learned Q-values
and a historical average, both of which can lag a changing game.

## Relation to

[[generalized-infinitesimal-gradient-ascent]] · [[independent-learning]] ·
[[convergence-types]]

## In the codebase

No implementation is indexed in `upstream/codebase/`; the book gives Algorithm
9.

## Open questions

- How sensitive is the behaviour to the ratio $\delta_l/\delta_w$?
