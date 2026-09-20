---
title: Temporal-Difference Learning
type: topic
status: solid
sources: ["[[ch02-reinforcement-learning]]", "[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Temporal-Difference Learning (TD)

Learns value functions from **experience** rather than from a known model
[Ch. 2.6]. Like [[dynamic-programming]] it bootstraps off the Bellman equations;
unlike DP it needs no $R$ or $T$.

General update [Eq. 2.50]:
$$Q(s^t,a^t) \leftarrow Q(s^t,a^t) + \alpha\left[X - Q(s^t,a^t)\right]$$
with learning rate $\alpha \in (0,1]$ and **update target** $X$ built from the
experience tuple. The choice of $X$ is what distinguishes the algorithms.

## Sarsa — on-policy

Target from the Bellman equation for $Q^\pi$ [Eq. 2.51], replacing the sums and
$R$ with sampled elements of $(s^t,a^t,r^t,s^{t+1},a^{t+1})$ — hence the name:
$$X = r^t + \gamma Q(s^{t+1}, a^{t+1}), \quad a^{t+1} \sim \pi(\cdot|s^{t+1})$$
[Eq. 2.52, full rule Eq. 2.53, Algorithm 2]

## Q-learning — off-policy

Target from the Bellman **optimality** equation for $Q^*$ [Eq. 2.56]
(Watkins & Dayan 1992):
$$X = r^t + \gamma \max_{a' \in A} Q(s^{t+1}, a')$$
[Eq. 2.57, full rule Eq. 2.58, Algorithm 3]

**The distinction:** Sarsa must gradually push $\pi$ toward $\pi^*$ to reach
$Q^*$. Q-learning "may use any policy to interact with the environment, so long
as the convergence conditions are upheld" [Ch. 2.6]. Hence **off-policy**
(Q-learning) vs **on-policy** (Sarsa) — with implications developed in
[[ch08-deep-rl]].

This is the algorithm the tabular exercise asks you to implement per-agent →
[[iql-tabular]], `upstream/exercises/tabular_marl/iql.py`.

## Convergence conditions

Both converge to $\pi^*$ under two conditions [Ch. 2.6]:

1. every $(s,a) \in S \times A$ is tried **infinitely often**;
2. the **standard stochastic approximation conditions** on the learning rate:
$$\forall s \in S, a \in A: \quad \sum_{k=1}^{\infty} \alpha_k(s,a) \to \infty \quad \text{and} \quad \sum_{k=1}^{\infty} \alpha_k(s,a)^2 < \infty$$
[Eq. 2.54 — 📕 errata-corrected, both sums start at $k=1$; see [[errata]]]

where $\alpha_k(s,a)$ is the rate at the $k$-th selection of $a$ in $s$. The left
sum ensures the rate stays large enough to escape initialisation; the right
ensures convergence at a rate. So $\alpha_k = 1/k$ qualifies and a constant
$\alpha_k = c$ does not — "nonetheless, in practice it is common to use a
constant learning rate since learning rates that meet the above conditions,
while theoretically sound, can lead to slow learning."

> Keep this pair in mind: condition 1 is what forces exploration, and condition
> 1 is also the first thing that breaks in MARL, where the environment an agent
> explores is itself changing → [[non-stationarity]].

## ε-greedy

Reconciles "act greedily" with "try everything infinitely often" [Eq. 2.55]:
$$\pi(a|s) = \begin{cases} 1 - \epsilon + \frac{\epsilon}{|A|} & \text{if } a \in \arg\max_{a'} Q(s,a') \\ \frac{\epsilon}{|A|} & \text{otherwise}\end{cases}$$

Any $\epsilon > 0$ satisfies condition 1; decaying $\epsilon \to 0$ makes $\pi$
converge to $\pi^*$. (Eq. 2.55 assumes a unique greedy action; with ties, split
the $1-\epsilon$ mass among them [footnote 6].)

This is the `act` method and `schedule_hyperparameters` of the tabular exercise.

## Multi-agent continuation values

[[joint-action-learning]] preserves the TD form but replaces the single-agent
$\max$ with a game value computed from the learned joint-action Q-tables:

$$X_i=r_i^t+\gamma\operatorname{Value}_i(\Gamma_{s^{t+1}}).$$

The solution concept defining `Value` creates minimax, Nash, and correlated
Q-learning [Eq. 6.11; Ch. 6.2]. This is exactly where a solution concept becomes
part of training rather than a post-training evaluator. Only the minimax
zero-sum variant inherits a broadly stated contraction-style convergence result;
the general-sum variants face equilibrium-selection problems [Ch. 6.2.1–6.2.3].

## Related
[[dynamic-programming]] · [[value-functions-and-bellman]] · [[learning-curves]] ·
[[iql-tabular]] · [[ch06-foundational-algorithms]] · [[joint-action-learning]]
