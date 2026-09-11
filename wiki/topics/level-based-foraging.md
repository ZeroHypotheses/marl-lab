---
title: Level-Based Foraging (LBF)
type: topic
status: stub
sources: ["[[ch01-introduction]]"]
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

**State** — x/y positions of robots and items, plus a binary existence variable
per item. Levels are *not* in the state, being assumed constant; if levels vary
across episodes they would have to be [Ch. 1.1, footnote 2].

**Actions** — `{up, down, left, right, collect, noop}` (6). Movement is blocked
at grid edges (no effect). `collect` attempts an adjacent item.

**Episode** ends when all items are collected or a step limit is reached.

> ⚠️ conflict (apparent, within ch. 1): §1.1–1.2 illustrate LBF as **fully
> cooperative** — "+1 if any of the items has been collected." But §1.1 also
> states that in "the actual implementation of level-based foraging we use in
> this book (described in Section 11.3.1), only those agents that were involved
> in the collection of an item (rather than all agents) will receive a positive
> normalized reward." So the real environment is **mixed-motive**: agents race
> for items they can take alone, yet must cooperate on items they cannot.
> Resolve against §11.3.1 when ingesting [[ch11-environments]].

Used in `upstream/exercises/deep_marl_data/lbf_8x8-2p-3f_coop` (the `_coop`
suffix suggests the cooperative variant) and runnable via
`upstream/codebase` — see [[ch10-marl-in-practice]].

## Related
[[reward-structures]] · [[credit-assignment]] · [[scaling-in-number-of-agents]]
