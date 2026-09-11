---
title: Knowledge Assumptions in Games
type: topic
status: solid
sources: ["[[ch03-games]]"]
updated: 2026-09-11
---

# Knowledge Assumptions in Games

"What do agents know about the game they are playing?" [Ch. 3.6]. The
multi-agent counterpart to the MDP knowledge assumption in
[[markov-decision-process]], and one of the six dimensions of Fig. 1.4.

## The two ends of the spectrum

**Game theory's default — complete knowledge.** All agents know every component:
all action spaces and reward functions; for stochastic games and POSGs also $S$,
$T$, and every agent's observation function (Owen 2013). This is exploitable:
knowing $R_j$ lets agent $i$ estimate $j$'s [[best-response]]; knowing $T$ allows
planning ahead.

**MARL's default — incomplete information.**

> "In MARL, we usually operate at the other end of the knowledge spectrum:
> agents typically do not know the reward functions of other agents, **nor even
> their own reward function**; and agents have no knowledge of the state
> transition and observation functions" [Ch. 3.6].

Known in game theory as an *incomplete information game* (Harsanyi 1967). Agent
$i$ experiences only the effects of its own actions — its reward $r_i^t$, and
(stochastic game) the joint action and next state, or (POSG) an observation.
From these it may build models of $T$ or of others' policies →
[[agent-modelling]].

## The middle: a simulator

For real applications "it is infeasible to obtain accurate and complete
specifications"; often the best available is a **simulator** $\hat{T}$ producing
samples $(r, s') \sim \hat{T}(s,a)$ with
$$\Pr\{\hat{T}(s,a) = (r,s')\} \approx T(s'\mid s,a)\prod_{i \in I}[R_i(s,a,s') = r_i]_1$$
[Eq. 3.8], where $[x]_1$ is 1 if $x$ holds, else 0.

## Symmetric, asymmetric, common knowledge

Further questions: is knowledge held by all agents or only some? If all know the
reward functions, do all know that all know, and so on — **common knowledge**?

> These have been studied extensively in game theory (Shoham & Leyton-Brown
> 2008; Perea 2012) and agent modelling (Albrecht & Stone 2018), but "in MARL
> they have played a relatively lesser role since the standard assumption is
> that agents have no knowledge of most game components" [Ch. 3.6].
>
> **The exceptions are where reward structure is exploited**: algorithms
> designed specifically for zero-sum or common-reward games, in
> [[ch06-foundational-algorithms]] and [[ch09-deep-marl]]. That is why
> [[reward-structures]] determines which algorithms even apply.

## Fixed agent count

Usually assumed fixed and known to all. **Open** multi-agent environments, where
agents enter and leave, are noted as recent research and **out of scope** (Jiang
et al. 2020; Rahman et al. 2021; Rahman, Carlucho, et al. 2023).

## Related
[[partial-observability]] · [[reward-structures]] · [[agent-modelling]] ·
[[ch06-foundational-algorithms]]
