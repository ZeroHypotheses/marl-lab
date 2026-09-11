---
title: Markov Decision Process (MDP)
type: topic
status: solid
sources: ["[[ch02-reinforcement-learning]]"]
updated: 2026-09-11
---

# Markov Decision Process (MDP)

The standard single-agent model [Ch. 2.2, Def. 1]. A finite MDP consists of:

- finite set of states $S$, with terminal states $\bar{S} \subset S$
- finite set of actions $A$
- reward function $R : S \times A \times S \to \mathbb{R}$
- transition function $T : S \times A \times S \to [0,1]$ with
  $\sum_{s' \in S} T(s,a,s') = 1$ [Eq. 2.1]
- initial state distribution $\mu : S \to [0,1]$ with $\sum_s \mu(s) = 1$ and
  $\mu(s) = 0$ for terminal $s$ [Eq. 2.2]

Loop: $s^0 \sim \mu$; at $t$ the agent observes $s^t$, picks $a^t \sim \pi(\cdot|s^t)$,
the MDP moves to $s^{t+1} \sim T(\cdot|s^t,a^t)$, and the agent gets
$r^t = R(s^t,a^t,s^{t+1})$. One run is an **episode**.

## The Markov property

$$\Pr(s^{t+1}, r^t \mid s^t,a^t,s^{t-1},a^{t-1},\dots,s^0,a^0) = \Pr(s^{t+1}, r^t \mid s^t,a^t)$$
[Eq. 2.3]

"The current state provides sufficient information to choose optimal actions —
past states and actions are not relevant" [Ch. 2.2]. This is what licenses
per-state value functions → [[value-functions-and-bellman]].

## What the agent is assumed to know

"The most common assumption in RL is that the dynamics of the MDP, in
particular the transition and reward functions $T$ and $R$, are a priori unknown
to the agent. Typically, the only parts of the MDP that are assumed to be known
are the action space $A$ and the state space $S$" [Ch. 2.2].

This is the dividing line between [[dynamic-programming]] (needs $T$, $R$) and
[[temporal-difference-learning]] (does not). The multi-agent version of this
question is §3.6, Knowledge Assumptions in Games → [[ch03-games]].

## Special cases and generalisations

- **Multi-armed bandit** — $|S| = 1$, $\bar{S} = \emptyset$, $T = 1$, probabilistic
  unknown $R$. The basic model for studying exploration–exploitation
  (Lattimore & Szepesvári 2020).
- **POMDP** — the agent receives observations $o^t$ rather than seeing $s^t$, so
  it must generally use the history $o^0,\dots,o^t$ to infer the state (Kaelbling,
  Littman & Cassandra 1998). **A POMDP is a POSG with one agent** [Ch. 2.2] —
  see §3.4, [[partial-observability]].
- **An MDP is a [[stochastic-games|stochastic game]] with one agent** [Ch. 3.3].
- States/actions may be continuous or mixed; $R$ may be probabilistic. Def. 1
  gives the finite, deterministic-reward case.

## Related
[[returns-and-discounting]] · [[value-functions-and-bellman]] ·
[[stochastic-games]] (the multi-agent extension) · [[partial-observability]]
