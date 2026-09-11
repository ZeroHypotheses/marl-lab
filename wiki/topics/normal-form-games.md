---
title: Normal-Form Games
type: topic
status: solid
sources: ["[[ch03-games]]"]
updated: 2026-09-11
---

# Normal-Form Games

A **single** interaction between two or more agents; no environment state
[Ch. 3.1, Def. 2]. Also called strategic-form games. The basic building block of
every model in [[ch03-games]].

A normal-form game consists of:
- finite set of agents $I = \{1,\dots,n\}$
- for each agent $i$: a finite action set $A_i$ and a reward function
  $R_i : A \to \mathbb{R}$, where $A = A_1 \times \dots \times A_n$

Each agent picks a policy $\pi_i : A_i \to [0,1]$, samples $a_i \sim \pi_i$; the
**joint action** is $a = (a_1,\dots,a_n)$; each agent receives $r_i = R_i(a)$.

"What makes these and many other games interesting is that one agent's reward
depends on the choices of the other agents, which are not known in advance"
[Ch. 3.1].

## Matrix games

Two-agent normal-form games, since the reward functions fit in a matrix
[Fig. 3.2]. Agent 1 picks the row, agent 2 the column.

| Game | Structure | Note |
|---|---|---|
| **Rock-Paper-Scissors** | zero-sum | $r_1 = -r_2$; win +1 / lose −1 / draw 0 |
| **Coordination** | common-reward | both pick A or both pick B → 10, else 0 |
| **Prisoner's Dilemma** | general-sum | see below |

**Prisoner's Dilemma** [Fig. 3.2(c)]: rewards $(-1,-1)$ for mutual cooperation,
$(-3,-3)$ for mutual defection, $(0,-5)$ / $(-5,0)$ when one defects. Mutual
cooperation gives each agent its second-highest reward, yet **D is a dominant
action** — it always beats C regardless of what the other agent does. This is
the game the tabular exercise trains in → [[iql-tabular]].

> The book uses "matrix game" for both single- and two-matrix cases; some game
> theory literature reserves "bimatrix game" for the general-sum case
> [footnote 4].

## How many are there?

§11.2 lists **all 78** structurally distinct, strictly ordinal 2×2 normal-form
games [Ch. 3.1] → [[ch11-environments]]. A useful catalogue for small
experiments.

## Related
[[reward-structures]] · [[repeated-normal-form-games]] · [[stochastic-games]] ·
[[solution-concepts]]
