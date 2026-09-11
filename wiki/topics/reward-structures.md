---
title: Reward Structures
type: topic
status: stub
sources: ["[[ch01-introduction]]"]
updated: 2026-09-11
---

# Reward Structures

How agents' goals relate to one another. Chapter 1 introduces three cases
through application examples rather than defining them formally — formal
treatment is in [[ch03-games]].

| Structure | Meaning | Ch. 1 example |
|---|---|---|
| **Common (shared) reward** | all agents receive identical rewards | multi-robot warehouse: collective reward when any order completes [§1.3.1] |
| **Zero-sum** | one agent's reward is the negative of the other's | two-player board/card games: +1 win, −1 loss [§1.3.2] |
| **General-sum (mixed-motive)** | goals partly align, partly conflict | autonomous driving [§1.3.3]; electronic-market trading [§1.3.4] |

Common reward is called "an important special case in MARL" [§1.3.1]; zero-sum
"another important special case" [§1.3.2]; general-sum is "among the most
challenging tasks in MARL" [§1.3.3].

Fully cooperative and fully competitive are the extremes; in between, goals
"align in some respects while differing in other respects, which can lead to
complex multi-agent interaction problems" [Ch. 1.1].

This taxonomy is a spine of the whole book: it determines which solution
concepts apply ([[ch04-solution-concepts]]) and which algorithm families are
even applicable — e.g. [[value-decomposition]] is defined for *common-reward*
games (§9.5), and self-play results are for *zero-sum* games (§9.8).

> ❓ unverified: whether the book treats "common reward" and "fully cooperative"
> as strictly synonymous. Ch. 1 uses both loosely. Settle from [[ch03-games]].

## Related
[[multi-agent-system]] · [[solution-concepts]] · [[level-based-foraging]]
