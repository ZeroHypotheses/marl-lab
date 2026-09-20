---
title: Nash Q-Learning
type: algorithm
status: solid
sources: ["[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Nash Q-Learning

## One-line

Nash Q-learning bootstraps each agent's joint-action Q-function from a selected
Nash equilibrium of the next state's learned game [Ch. 6.2.2].

## Setting

Finite discounted general-sum stochastic games with observable joint actions
and rewards for all agents [Algorithm 7]. Every state induces a normal-form game
whose payoffs are the agents' Q-values [Eq. 6.10].

## Update rule

Use the [[joint-action-learning]] update, setting
$\operatorname{Value}_i(\Gamma_{s'})$ to agent $i$'s expected payoff under one
Nash equilibrium of $\Gamma_{s'}$ [Ch. 6.2.2]. The chosen equilibrium also
defines the action policy.

## Why it works / when it breaks

The cited convergence result requires every encountered state game to have a
global optimum or saddle point and requires the learners to select equilibria
consistently [Ch. 6.2.2]. Generic general-sum games need not satisfy this.
Multiple equilibria may pay agents differently, so independent learners can
select incompatible equilibria; the target itself can jump when the selected
equilibrium changes [Ch. 6.2.2]. Computing a Nash equilibrium is also generally
harder than solving a zero-sum minimax game [Ch. 4.5.1; Ch. 6.2.2].

## Relation to

[[nash-equilibrium]] · [[joint-action-learning]] · [[minimax-q-learning]] ·
[[equilibrium-selection]]

## In the codebase

No implementation is indexed in `upstream/codebase/`; the book presents it as
an instantiation of Algorithm 7.

## Open questions

- Which equilibrium-selection rule should be shared without assuming a central
  coordinator?
