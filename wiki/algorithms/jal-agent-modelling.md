---
title: Joint-Action Learning with Agent Modelling (JAL-AM)
type: algorithm
status: solid
sources: ["[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Joint-Action Learning with Agent Modelling (JAL-AM)

## One-line

JAL-AM learns its own value for each joint action and predicts the others with
state-conditioned empirical action models [Ch. 6.3.2].

## Setting

A finite stochastic game with observable state and joint action. Agent $i$
observes only its own reward, unlike JAL-GT, and stores $Q_i(s,a)$ plus a policy
model $\hat\pi_j(a_j\mid s)$ for each other agent [Algorithm 8].

## Update rule

The empirical model counts how often $j$ selected $a_j$ in $s$ [Eq. 6.16]. For
candidate action $a_i$, agent $i$ computes

$$
\widehat Q_i(s,a_i)=
\sum_{a_{-i}}Q_i(s,\langle a_i,a_{-i}\rangle)
\prod_{j\ne i}\hat\pi_j(a_j\mid s),
$$

where the product treats the modelled policies as independent [Eq. 6.17]. It
acts greedily or explores from these expected values, while its joint-action
Q-table receives an off-policy Q-learning update [Algorithm 8].

## Why it works / when it breaks

If the other policies become fixed and stationary and each relevant state is
observed infinitely often, the empirical models converge to those policies
[Ch. 6.3.2]. During simultaneous learning those assumptions need not hold. The
factorised model cannot express correlated opponent actions, and table size
still grows with the joint action space. In the chapter's level-based-foraging
experiment JAL-AM reduced variance and reached the optimum sooner than IQL for
that particular setup; this is evidence, not a general dominance result
[Ch. 6.3.2, Fig. 6.4].

## Relation to

[[agent-modelling]] · [[fictitious-play]] · [[joint-action-learning]] ·
[[independent-learning]]

## In the codebase

No implementation is indexed in `upstream/codebase/`; the book gives Algorithm
8 and compares it experimentally with IQL.

## Open questions

- Does modelling correlation improve the result enough to justify its larger
  representation in small cooperative games?
