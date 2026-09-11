---
title: "Ch. 2 — Reinforcement Learning"
type: source
status: solid
sources: ["MARL book, Ch. 2, pp. 19–42 (2nd printing)"]
updated: 2026-09-11
---

# Chapter 2 — Reinforcement Learning

Single-agent RL, restricted to exactly what Part I needs. Function
approximation is **deliberately excluded** here and deferred to
[[ch07-deep-learning]] / [[ch08-deep-rl]]. 65 numbered equations, all tabular.

> 📕 errata: p33, Eq 2.54 — sums changed from `k=0` to `k=1`. Verified present
> as `k=1` in our copy. See [[errata]].

## The framing that matters

**An RL problem = a decision process model + a learning objective** [Fig. 2.1].
Not just the MDP. This distinction returns throughout: a game model plus a
[[solution-concepts|solution concept]] defines a *MARL* problem
([[ch04-solution-concepts]]).

Definition given [§2.1]: "Reinforcement learning (RL) algorithms learn solutions
for sequential decision processes via repeated interaction with an environment."

RL is neither supervised nor unsupervised learning: rewards don't say which
action to take (so aren't labels), but do act "as a proxy from which to learn an
optimal policy" [§2.1]. The **exploration–exploitation dilemma** is named here.

## Contents

- **§2.1** general definition → [[markov-decision-process]]
- **§2.2** MDPs (Def. 1), Markov property (Eq. 2.3), bandits, POMDPs
- **§2.3** returns and discounting → [[returns-and-discounting]]
- **§2.4** value functions and Bellman equations → [[value-functions-and-bellman]]
- **§2.5** dynamic programming → [[dynamic-programming]]
- **§2.6** temporal-difference learning → [[temporal-difference-learning]]
- **§2.7** evaluation → [[learning-curves]]
- **§2.8** equivalence of $R(s,a,s')$ and $R(s,a)$
- **§2.9** summary

## Running example

**The Mars Rover MDP** [Fig. 2.3, p23]. From `Start`, `right` goes straight to
`Base` but with probability 0.5 the rover falls off a cliff (−10); `left` takes a
longer route via `Site A` and `Site B` (−1 each, 0.3 chance of becoming
immobilised at −3), reaching base for +10.

With $\gamma = 0.95$: $V^*(\text{Start}) = 4.1$, $V^*(\text{Site A}) = 6.2$,
$V^*(\text{Site B}) = 10$; optimal policy is `left` then `right`, `right`.

**The instructive bit** [§2.7]: with $\gamma = 0.5$ the optimal policy flips to
`right`, with $V^*(\text{Start}) = 0$. Same MDP, different discount factor,
different optimal policy — both valid, because **γ is part of the problem
definition, not a knob**.

## §2.8 — $R(s,a,s')$ vs $R(s,a)$

The two reward-function conventions are **equivalent**: set
$R(s,a) = \sum_{s'} T(s'|s,a) R(s,a,s')$ [Eq. 2.63] to convert. The book uses
$R(s,a,s')$ for two stated pedagogical reasons — it reads better on example
diagrams where one action has several outcomes, and it makes the Bellman
equations visually congruent with TD update targets.

> ⚠️ Worth remembering: "most of the original MARL literature presented in
> Chapter 6 in fact defined reward functions as $R(s,a)$" [§2.8]. Expect the
> mismatch when reading the primary sources behind
> [[ch06-foundational-algorithms]].

## What the next chapters do with this

[[ch03-games]] extends the MDP to multiple agents; [[ch04-solution-concepts]]
uses discounted returns to define solution concepts; [[ch05-marl-in-games]] and
[[ch06-foundational-algorithms]] extend DP and TD to games [§2.9].

## Related
[[markov-decision-process]] · [[returns-and-discounting]] ·
[[value-functions-and-bellman]] · [[dynamic-programming]] ·
[[temporal-difference-learning]] · [[learning-curves]]
