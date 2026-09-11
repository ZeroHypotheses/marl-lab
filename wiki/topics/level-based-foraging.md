---
title: Level-Based Foraging (LBF)
type: topic
status: drafted
sources: ["[[ch01-introduction]]", "[[ch03-games]]"]
updated: 2026-09-11
---

# Level-Based Foraging (LBF)

The book's running example, introduced in Ch. 1.1 (Fig. 1.2) and used
throughout. Open-source implementation:
<https://github.com/uoe-agents/lb-foraging>. Full description in §11.3.1
([[ch11-environments]]).

**Setup.** Robots collect items distributed in a grid world. Each robot and item
has a skill **level**. A group of one or more robots can collect an item if they
are adjacent to it and **the sum of their levels ≥ the item's level** — so some
items require cooperation.

## As a stochastic game [Ch. 3.3]

State is a vector of x/y positions of all agents and items plus a binary
collected-flag per item; joint actions move agents and flip flags via $T$;
terminates on a step cap or when all items are collected.

**State** — x/y positions of robots and items, plus a binary existence variable
per item. Levels are *not* in the state, being assumed constant; if levels vary
across episodes they would have to be [Ch. 1.1, footnote 2].

**Actions** — `{up, down, left, right, collect, noop}` (6). Movement is blocked
at grid edges (no effect). `collect` attempts an adjacent item.

**Episode** ends when all items are collected or a step limit is reached.

## Reward structure — both variants are intended [resolved by Ch. 3.3]

The apparent contradiction in ch. 1 is not one. **LBF is a template with two
reward variants**, and §3.3 states both explicitly when modelling LBF as a
[[stochastic-games|stochastic game]]:

> "In a **common-reward version** of the game, every agent will receive a reward
> of +1 whenever any of the items has been collected by any agents. A
> **general-sum version** may specify individual rewards for agents, such as +1
> reward for agents which were actually involved in the collection of an item
> and 0 reward for all other agents." [Ch. 3.3]

So ch. 1.1–1.2 illustrate the common-reward variant, while the note about "the
actual implementation we use in this book" describes the general-sum one.
Both are legitimate; **which one is in play must be stated** whenever LBF
results are compared. → [[reward-structures]]

> ❓ still open: which variant §11.3.1 specifies as the book's default, and
> whether the `_coop` suffix in `lbf_8x8-2p-3f_coop` marks the common-reward
> version. Settle at [[ch11-environments]].

Used in `upstream/exercises/deep_marl_data/lbf_8x8-2p-3f_coop` (the `_coop`
suffix suggests the cooperative variant) and runnable via
`upstream/codebase` — see [[ch10-marl-in-practice]].

## Related
[[reward-structures]] · [[credit-assignment]] · [[scaling-in-number-of-agents]] ·
[[stochastic-games]] · [[partial-observability]] (Fig. 3.4 shows the partially observable variant)
