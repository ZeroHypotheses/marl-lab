---
title: Multi-Agent Credit Assignment
type: topic
status: stub
sources: ["[[ch01-introduction]]"]
updated: 2026-09-11
---

# Multi-Agent Credit Assignment

Temporal credit assignment in single-agent RL asks **which past actions**
produced a reward. MARL adds a second axis: **whose action** produced it
[Ch. 1.4].

**The book's illustration** [Ch. 1.4]: in [[level-based-foraging]], all agents
choose `collect` and receive a collective reward of +1. From the
state/action/reward data alone it is "highly non-trivial to disentangle the
contribution of each agent" — in particular that the agent on the left
contributed nothing, because its action had no effect (its level was too low to
matter).

Note this bites hardest under **common reward** ([[reward-structures]]), where
the signal is identical for everyone regardless of contribution.

**Status per ch. 1:** counterfactual reasoning "can address this problem in
principle," but it "is still an open problem how to resolve multi-agent credit
assignment in an efficient and scalable way."

> Ch. 1 only names the problem. [[value-decomposition]] (§9.5) is one family of
> answers; check whether the book frames it as such.

## Related
[[value-decomposition]] · [[reward-structures]] · [[non-stationarity]]
