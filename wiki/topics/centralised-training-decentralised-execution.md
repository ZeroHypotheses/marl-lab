---
title: Centralised Training with Decentralised Execution (CTDE)
type: topic
status: stub
sources: ["[[ch01-introduction]]"]
updated: 2026-09-11
---

# Centralised Training with Decentralised Execution (CTDE)

Assume centralisation is available during training — "e.g., in simulation" —
while producing policies executable in a fully decentralised way [Ch. 1.2].
The third of the three [[training-execution-modes]], and the dominant paradigm
in deep MARL.

Motivation: centralisation "can help to improve coordination between agents and
alleviate issues such as [[non-stationarity]]" [Ch. 1.2], but many deployments
cannot centralise at execution time at all.

> Ch. 1 does no more than name it. The real treatment is §9.1
> ([[ch09-deep-marl]]), with concrete algorithms in §9.4–9.5 —
> [[maa2c]], [[mappo]], [[vdn]], [[qmix]].

## Related
[[training-execution-modes]] · [[value-decomposition]] · [[non-stationarity]]
