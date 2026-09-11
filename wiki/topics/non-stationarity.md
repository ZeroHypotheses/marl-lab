---
title: Non-Stationarity
type: topic
status: stub
sources: ["[[ch01-introduction]]"]
updated: 2026-09-11
---

# Non-Stationarity

Caused by the continually changing policies of agents *while they are learning*
[Ch. 1.4]. The first of the four challenges, and the one that most directly
breaks single-agent RL guarantees.

**The moving target problem.** Each agent adapts to the other agents' policies,
which are themselves adapting to it — "thereby potentially causing cyclic and
unstable learning dynamics" [Ch. 1.4].

**Made worse by heterogeneity of rates.** Agents "may learn different behaviors
at different rates as a result of their different rewards and local
observations" [Ch. 1.4] — so it isn't only that the target moves, but that it
moves at a rate you don't control or observe.

Centralisation can alleviate it [Ch. 1.2] → [[training-execution-modes]].

> This page records only what ch. 1 asserts. The substantive treatment is §5.4
> ([[ch05-marl-in-games]]); deep-MARL mitigations are in [[ch09-deep-marl]].
> Ch. 1 gives no formal definition and no equation.

## Related
[[credit-assignment]] · [[scaling-in-number-of-agents]] · [[solution-concepts]] ·
[[centralised-training-decentralised-execution]]
