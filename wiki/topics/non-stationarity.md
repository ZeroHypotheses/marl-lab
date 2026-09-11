---
title: Non-Stationarity
type: topic
status: solid
sources: ["[[ch01-introduction]]", "[[ch05-marl-in-games]]"]
updated: 2026-09-11
---

# Non-Stationarity

"The non-stationarity resulting from the continual co-adaptation of multiple
agents as they learn from interactions with one another" [Ch. 5.4.1]. The
defining challenge of MARL.

## The definition, precisely

A stochastic process $\{X^t\}$ is **stationary** if the distribution of
$X^{t+\tau}$ does not depend on $\tau$ — the dynamics don't change over time.

**In an MDP with a fixed policy, the process is stationary:** $s^t$ depends only
on $s^{t-1}, a^{t-1}$ (Markov property), and $a^{t-1}$ only on $s^{t-1}$ via
$\pi$. No dependence on $t$.

## Non-stationarity already exists in single-agent RL

Once learning starts, $\pi^{z+1} = L(D^z,\pi^z)$ makes the policy depend on $t$,
so the process is non-stationary. This breaks **value learning**: the TD target
$r^t + \gamma Q(s^{t+1},a^{t+1})$ ([[temporal-difference-learning]]) uses value
estimates that are themselves changing — the **moving target problem**.

## What MARL adds

Not just the value estimates but **the environment itself** appears
non-stationary from each agent's view. In [[independent-learning]], the other
agents' policies enter agent $i$'s transition function [Eq. 5.10]:
$$T_i(s^{t+1}\mid s^t,a_i^t) \propto \sum_{a_{-i}} T(s^{t+1}\mid s^t,\langle a_i^t,a_{-i}\rangle)\prod_{j\ne i}\pi_j(a_j\mid s^t)$$

As each $\pi_j$ is updated, $T_i$ changes.

> **The consequence that matters most:** the dynamics become **non-Markovian**,
> "since they now also depend on the history of the interaction" (Laurent,
> Matignon & Le Fort-Piat 2011). The Markov property that licensed per-state
> value functions ([[value-functions-and-bellman]]) no longer holds from a
> single agent's perspective.

**Cyclic dynamics** follow: each agent adapts to the others, who adapt back.
Fig. 5.5 visualises two WoLF-PHC agents in Rock-Paper-Scissors spiralling
through policy space before settling on the uniform Nash equilibrium.

## Why the single-agent guarantees don't carry over

> "Because of these non-stationarity issues, the usual stochastic approximation
> conditions required for temporal-difference learning in single-agent RL
> (Equation 2.54) are usually **not sufficient** in MARL to ensure convergence"
> [Ch. 5.4.1].

And what exists instead is narrow: "all known theoretical results in MARL for
convergent learning are limited to restricted game settings and mostly only work
for specific algorithms." IGA converges to the average reward of a Nash
equilibrium; WoLF-IGA to a Nash equilibrium — **both only for two-agent,
two-action normal-form games** → [[convergence-types]],
[[ch06-foundational-algorithms]].

Ongoing: Zhang, Yang & Basar 2019; Daskalakis, Foster & Golowich 2020; Wei et
al. 2021; Ding et al. 2022; Leonardos et al. 2022.

## Mitigations

- **Centralisation** — [[central-learning]] "circumvents" it by having one
  learner; CTDE alleviates it during training
  → [[centralised-training-decentralised-execution]].
- **More agents makes it worse** → [[scaling-in-number-of-agents]].

## Related
[[independent-learning]] · [[convergence-types]] · [[equilibrium-selection]] ·
[[credit-assignment]] · [[markov-decision-process]]
