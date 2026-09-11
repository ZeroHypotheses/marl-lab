---
title: Returns and Discounting
type: topic
status: solid
sources: ["[[ch02-reinforcement-learning]]"]
updated: 2026-09-11
---

# Returns and Discounting

The **return** is the sum of rewards from a point onward. Since outcomes are
stochastic and outside the agent's control, the objective is the **expected**
return [Ch. 2.3, Eq. 2.5], not the return itself.

**Discounted return** [Eq. 2.6]:
$$\mathbb{E}_\pi\left[\sum_{t=0}^{\infty} \gamma^t r^t\right], \quad \gamma \in [0,1]$$

For $\gamma < 1$ and rewards bounded in $[r_{\min}, r_{\max}]$ this is finite,
bounded by $r_{\max}/(1-\gamma)$ [Eq. 2.7] — the closed form of the geometric
series. Without discounting, non-terminating MDPs can give infinite returns,
which cannot distinguish between policies.

## Two equivalent readings of γ

1. **Termination probability.** $(1-\gamma)$ is the chance the process ends after
   each step, so terminating after exactly $T$ steps has probability
   $\gamma^{T-1}(1-\gamma)$. The book's example: $\gamma = 0.95$ models a rover
   battery that fails with probability 0.05 per transition.
2. **Weighting.** The agent gives weight $\gamma^t$ to $r^t$. Near 0 → myopic;
   near 1 → farsighted.

## γ is not a hyperparameter

> "The discount rate is part of the learning objective and not a tunable
> algorithm parameter; $\gamma$ is a fixed parameter specified by the learning
> objective" [Ch. 2.3].

**Two RL problems differing only in γ can have different optimal policies**, and
both are correct — they are different problems. In the Mars Rover MDP,
$\gamma = 0.95$ makes `left` optimal ($V^*(\text{Start}) = 4.1$) while
$\gamma = 0.5$ makes `right` optimal ($V^*(\text{Start}) = 0$) [Ch. 2.7].

Consequence for [[learning-curves]]: tuning γ to improve a curve is changing the
question, not answering it better.

## Absorbing states

Terminal states (or hitting a step cap) are treated as **absorbing**: any action
self-transitions with probability 1 and gives reward 0 [Ch. 2.3]. This lets one
discounted-return definition cover terminating and non-terminating MDPs alike,
and is why $V^\pi(s) = 0$ for $s \in \bar{S}$.

## Related
[[markov-decision-process]] · [[value-functions-and-bellman]] · [[learning-curves]]
