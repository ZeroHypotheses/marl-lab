---
title: Stochastic Games
type: topic
status: solid
sources: ["[[ch03-games]]"]
updated: 2026-09-11
---

# Stochastic Games

The core MARL model (Shapley 1953). Adds an environment state that evolves with
the agents' actions [Ch. 3.3, Def. 3]. Also called **Markov games**
(e.g. Littman 1994).

Identical to an [[markov-decision-process|MDP]] except that agents, actions and
rewards are indexed per agent:
- finite agents $I$, finite states $S$ with terminals $\bar{S}$
- per agent $i$: actions $A_i$, reward $R_i : S \times A \times S \to \mathbb{R}$
  with $A = A_1 \times \dots \times A_n$
- transitions $T : S \times A \times S \to [0,1]$, $\sum_{s'} T(s,a,s') = 1$ [Eq. 3.1]
- initial distribution $\mu$ [Eq. 3.2]

At $t$, **every agent observes $s^t$** and picks $a_i^t \sim \pi_i(\cdot \mid h^t)$
where $h^t = (s^0,a^0,\dots,s^t)$. That history "is observed by all agents, which
is a property known as **full observability**" — dropping this gives
[[partial-observability]].

## Markov property

$$\Pr(s^{t+1}, r^t \mid s^t,a^t,\dots,s^0,a^0) = \Pr(s^{t+1}, r^t \mid s^t,a^t)$$
[Eq. 3.3], with $r^t = (r_1^t,\dots,r_n^t)$ the **joint reward**. Note it
conditions on the *joint* action — which is precisely why it stops holding from
any single agent's perspective once the others are learning →
[[non-stationarity]].

## Every state is a normal-form game

With rewards written $R_i(s,a)$, each $s \in S$ is a non-repeated
[[normal-form-games|normal-form game]] with rewards $R_i(s,\cdot)$ [Fig. 3.3].
(On $R_i(s,a,s')$ vs $R_i(s,a)$, see §2.8 → [[ch02-reinforcement-learning]].)

## Special cases

- $|S| = 1$, $\bar{S} = \emptyset$ ⇒ [[repeated-normal-form-games]]
- $|I| = 1$ ⇒ [[markov-decision-process]]

Reward classification carries over unchanged: zero-sum, common-reward or
general-sum → [[reward-structures]]. Continuous state/action variants are
possible; Def. 3 gives the finite case, per Shapley's original.

## Related
[[markov-decision-process]] · [[partial-observability]] · [[normal-form-games]] ·
[[level-based-foraging]] · [[non-stationarity]]
