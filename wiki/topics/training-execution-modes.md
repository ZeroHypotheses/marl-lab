---
title: Training and Execution Modes
type: topic
status: stub
sources: ["[[ch01-introduction]]"]
updated: 2026-09-11
---

# Training and Execution Modes

What information is centrally available during **training** versus during
**execution**. Introduced in Ch. 1.2; the substantive treatment is §9.1
([[ch09-deep-marl]]).

| Mode | Training | Execution |
|---|---|---|
| **Centralised training and execution** | shared mechanism/information | shared mechanism/information |
| **Decentralised training and execution** | local information only | local information only |
| **Centralised training, decentralised execution (CTDE)** | centralised (e.g. in simulation) | fully decentralised |

Centralisation "can help to improve coordination between agents and alleviate
issues such as non-stationarity" [Ch. 1.2]. CTDE "aims to combine the benefits
of the two aforementioned approaches" — centralise while you can, deploy
policies that don't need it. → [[centralised-training-decentralised-execution]]

## Why this is not just an optimisation

Ch. 1.2 gives two distinct justifications for decentralisation, worth keeping
apart:

1. **Tractability** — a central controller over n agents faces a joint action
   space that grows exponentially. → [[scaling-in-number-of-agents]]
2. **Feasibility** — some applications *cannot* centralise at execution time:
   urban autonomous driving, search-and-rescue robots that "may not be possible
   to communicate with a central coordinator." Here decentralised execution is a
   hard constraint on the deployed system, not a choice about efficiency.

## Related
[[non-stationarity]] · [[scaling-in-number-of-agents]] · [[ch09-deep-marl]]
