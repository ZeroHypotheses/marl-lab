---
title: Value Functions and the Bellman Equation
type: topic
status: solid
sources: ["[[ch02-reinforcement-learning]]"]
updated: 2026-09-11
---

# Value Functions and the Bellman Equation

Because of the [[markov-decision-process|Markov property]], expected return can
be defined per state — which is what makes value functions possible [Ch. 2.4].

**State-value function** — expected return starting in $s$ and following $\pi$:
$$V^\pi(s) = \sum_{a \in A} \pi(a|s) \sum_{s' \in S} T(s'|s,a)\left[R(s,a,s') + \gamma V^\pi(s')\right]$$
[Eq. 2.13 — the **Bellman equation**]. $V^\pi(s) = 0$ for absorbing $s \in \bar{S}$.

**Action-value function** — take $a$ in $s$, then follow $\pi$:
$$Q^\pi(s,a) = \sum_{s' \in S} T(s'|s,a)\left[R(s,a,s') + \gamma \sum_{a' \in A} \pi(a'|s')Q^\pi(s',a')\right]$$
[Eq. 2.20]

## Linear system, unique solution

For a finite MDP with $m = |S|$ states, the Bellman equation for $V^\pi$ is a
system of $m$ **linear** equations in $m$ variables [Eqs. 2.14–2.16], with a
unique solution $V^\pi$. If the whole MDP is known it can be solved directly
(e.g. Gauss elimination, $O(m^3)$) — see [[dynamic-programming]] for why that's
usually not how it's done.

## Optimality

$V^*(s) = \max_{\pi'} V^{\pi'}(s)$ and $Q^*(s,a) = \max_{\pi'} Q^{\pi'}(s,a)$
[Eqs. 2.21–2.22]. The **Bellman optimality equations** drop the policy:
$$V^*(s) = \max_{a \in A} \sum_{s'} T(s'|s,a)\left[R(s,a,s') + \gamma V^*(s')\right]$$
$$Q^*(s,a) = \sum_{s'} T(s'|s,a)\left[R(s,a,s') + \gamma \max_{a' \in A} Q^*(s',a')\right]$$
[Eqs. 2.24–2.25]

These are $m$ **non-linear** equations — the non-linearity is the $\max$
operator. Unique solution $V^*/Q^*$.

Given $Q^*$, an optimal policy is just greedy action selection,
$\pi^*(s) = \arg\max_a Q^*(s,a)$ [Eq. 2.26].

## Unique values, non-unique policies

> **The optimal value function is always unique, but there may be many optimal
> policies.** If several actions tie under $Q^*$, any probability assignment
> across them is optimal — in fact infinitely many [Ch. 2.4, footnote 4].
> Crucially, **a deterministic optimal policy always exists** in an MDP.

This is worth holding onto, because it is exactly what **fails** in the
multi-agent case: [[ch04-solution-concepts]] must deal with multiple equilibria
that give *different* returns to different agents, which is the equilibrium
selection problem ([[ch01-introduction]] §1.4). And stochastic policies stop
being merely optional — see minimax/Nash equilibria in
[[ch04-solution-concepts]].

## Related
[[markov-decision-process]] · [[returns-and-discounting]] ·
[[dynamic-programming]] · [[temporal-difference-learning]] · [[solution-concepts]]
