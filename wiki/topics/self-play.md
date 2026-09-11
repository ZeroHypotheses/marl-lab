---
title: Self-Play and Mixed-Play
type: topic
status: solid
sources: ["[[ch05-marl-in-games]]"]
updated: 2026-09-11
---

# Self-Play and Mixed-Play

Do all agents use the same learning algorithm? [Ch. 5.5]

**The term "self-play" is used for two distinct things**, and the book
disambiguates them — worth carrying into any paper you read.

## Algorithm self-play

All agents use **the same learning algorithm** (Bowling & Veloso 2002; Banerjee
& Peng 2004; Powers & Shoham 2005; Conitzer & Sandholm 2007; Shoham, Powers &
Grenager 2007; Wunder, Littman & Babes 2010; Chakraborty & Stone 2014).

> "Developing algorithms that converge to some type of equilibrium solution in
> self-play is at the core of much of the literature in MARL. **Essentially all
> of the MARL algorithms introduced in this book operate in this way**"
> [Ch. 5.5.1].

Rooted in game theory's "interactive learning" literature (Fudenberg & Levine
1998; Young 2004). The assumption is a simplification: [[non-stationarity]] "can
be further exacerbated if the agents use different learning approaches."
Practically, one algorithm usable by all agents is convenient.

For [[independent-learning]] it's usually *implicitly* assumed (as in IQL) but
**not required** — independent learners may use different algorithms.

## Policy self-play

Train a policy **directly against itself**, learning to exploit and then remove
its own weaknesses. Developed mainly for zero-sum sequential games.

TD-Gammon (Tesauro 1994) reached champion level at backgammon this way; more
recently Silver et al. 2017, 2018; Berner et al. 2019. **Population-based
training** extends it by training against a distribution of policies including
past versions of itself (Lanctot et al. 2017; Jaderberg et al. 2019; Vinyals et
al. 2019) → §9.8, §9.9, [[ch09-deep-marl]].

## The trade-off between them

**Policy self-play implies algorithm self-play.**

| | Benefit | Restriction |
|---|---|---|
| **Policy** self-play | may learn much faster — all agents' experiences combine to train one policy | requires **symmetrical roles and egocentric observations**, so one policy fits every agent |
| **Algorithm** self-play | no such restriction — agents may have different roles, actions, observations, rewards | no experience pooling |

## Mixed-play

Agents use **different** learning algorithms [Ch. 5.5.2]. Examples: trading
markets, where each organisation builds its own agent; and **ad hoc teamwork**
(Stone et al. 2010; Mirsky et al. 2022), collaborating with previously unknown
agents.

Albrecht & Ramamoorthy (2012) compared Nash-Q, JAL-AM, WoLF-PHC and a regret
matching variant across many normal-form games and metrics. **"There was no
clear winner among the tested algorithms."**

> A gap the book names explicitly: Papoudakis et al. (2021) benchmark deep MARL
> algorithms for *algorithm self-play* in common-reward games, but "there is
> currently no such study for deep learning-based MARL algorithms in mixed-play
> settings" [Ch. 5.5.2]. A live research opening.

## Bridging the two

Extend the self-play equilibrium agenda with: converge to a **best response** if
others are stationary (Bowling & Veloso 2002; Banerjee & Peng 2004; Conitzer &
Sandholm 2007). **Targeted optimality and safety** (Powers & Shoham 2004) assumes
others come from a given class — achieve best-response returns if so, otherwise
guarantee at least maxmin ("security") returns → [[minimax]]. Classes might be
finite state automata, decision trees, or policies conditioned on the last $x$
observations (Powers & Shoham 2005; Vu, Powers & Shoham 2006; Chakraborty &
Stone 2014).

## Related
[[independent-learning]] · [[non-stationarity]] · [[agent-modelling]] ·
[[minimax]] · [[ch09-deep-marl]]
