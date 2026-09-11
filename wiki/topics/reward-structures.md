---
title: Reward Structures
type: topic
status: solid
sources: ["[[ch01-introduction]]", "[[ch03-games]]"]
updated: 2026-09-11
---

# Reward Structures

How agents' goals relate to one another. Chapter 1 introduces three cases
through application examples rather than defining them formally — formal
treatment is in [[ch03-games]].

| Structure | Meaning | Ch. 1 example |
|---|---|---|
| **Common (shared) reward** | all agents receive identical rewards ($R_i = R_j$) | multi-robot warehouse: collective reward when any order completes [§1.3.1] |
| **Zero-sum** | one agent's reward is the negative of the other's | two-player board/card games: +1 win, −1 loss [§1.3.2] |
| **General-sum (mixed-motive)** | goals partly align, partly conflict | autonomous driving [§1.3.3]; electronic-market trading [§1.3.4] |

Common reward is called "an important special case in MARL" [§1.3.1]; zero-sum
"another important special case" [§1.3.2]; general-sum is "among the most
challenging tasks in MARL" [§1.3.3].

Fully cooperative and fully competitive are the extremes; in between, goals
"align in some respects while differing in other respects, which can lead to
complex multi-agent interaction problems" [Ch. 1.1].

## Why it decides which algorithms apply

This taxonomy is a spine of the whole book: it determines which solution
concepts apply ([[ch04-solution-concepts]]) and which algorithm families are
even applicable — e.g. [[value-decomposition]] is defined for *common-reward*
games (§9.5), and self-play results are for *zero-sum* games (§9.8).

## Formal definitions [Ch. 3.1] — resolved

Chapter 3 gives these as a classification of **reward functions**, applying
identically to normal-form games, stochastic games and POSGs [§3.1, §3.3, §3.4]:

| | Condition |
|---|---|
| **Zero-sum** | $\sum_{i \in I} R_i(a) = 0$ for all $a \in A$ |
| **Common-reward** | $R_i = R_j$ for all $i, j \in I$ |
| **General-sum** | no restriction |

With two agents, zero-sum gives $R_i = -R_j$. Zero-sum is a **special case of
constant-sum** (rewards sum to a constant) [§3.1, footnote 2].

A POSG with common rewards is a **Dec-POMDP** [§3.4].

> ❓ partially settled: ch. 3 makes **common-reward** the formal term, defined by
> $R_i = R_j$. "Fully cooperative" is ch. 1's informal phrasing and is not given
> a separate formal definition. Treat *common-reward* as the technical condition
> — it is what §9.5 requires for [[value-decomposition]]. Whether the book ever
> uses "fully cooperative" to mean something weaker (aligned but not identical
> rewards) is still unconfirmed; watch for it in [[ch05-marl-in-games]].

## Related
[[multi-agent-system]] · [[solution-concepts]] · [[level-based-foraging]] ·
[[normal-form-games]] · [[knowledge-assumptions]]
