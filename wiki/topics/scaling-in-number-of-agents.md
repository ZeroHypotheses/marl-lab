---
title: Scaling in Number of Agents
type: topic
status: stub
sources: ["[[ch01-introduction]]"]
updated: 2026-09-11
---

# Scaling in Number of Agents

"The total number of possible action combinations between agents may grow
exponentially with the number of agents" [Ch. 1.4] — particularly when each
added agent brings its own action variables, as in [[level-based-foraging]],
where each agent controls one robot.

**Concrete instance** [Ch. 1.2]: three robots with 6 actions each give a central
controller $6^3 = 216$ joint actions per step. Decomposing into three
independent agents gives each a 6-action problem — at the cost of needing
coordination.

**How bad in practice:** "In the early days of MARL research, it was common to
use only two agents to avoid issues with scaling. Even with today's deep
learning-based MARL algorithms, it is common to use a number of agents between
2 and 10" [Ch. 1.4]. Worth remembering when reading experimental sections.

> ❓ Ch. 1.4 explicitly hedges: "(But see Section 5.4.4 for a counter-example
> without exponential growth.)" Growth is *not* always exponential. Resolve this
> when ingesting [[ch05-marl-in-games]] — it constrains when the scaling
> argument for decentralisation actually applies.

## Related
[[training-execution-modes]] · [[multi-agent-system]]
