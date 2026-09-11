---
title: Agendas of MARL
type: topic
status: drafted
sources: ["[[ch01-introduction]]", "Shoham, Powers & Grenager 2007"]
updated: 2026-09-11
---

# Agendas of MARL

*Why* you are doing MARL, which determines how success is measured. From
Shoham, Powers & Grenager (2007), "If multi-agent learning is the answer, what
is the question?", via Ch. 1.5.

Ch. 1 is the book's main treatment of this, so this page is fuller than the
other ch. 1 topic pages.

**Computational** — MARL as a way to *compute solutions to game models*. The
output is a set of policies satisfying some property (e.g. Nash equilibrium →
[[solution-concepts]]), either deployed or analysed. Here MARL competes with
direct methods such as linear programming (§4.3.1, §4.6.1), which "can be
significantly more efficient … for certain types of games" but "typically
require full knowledge of the game, including the reward functions of all
agents." MARL's advantage is learning without that knowledge.

**Prescriptive** — concerns agent behaviour and performance *during* learning:
how *should* they learn to meet given criteria? Example criteria: average reward
must not fall below a threshold during learning regardless of how others learn;
learn optimal actions against a specified class of agents (e.g. static
non-learners) while not falling below a threshold otherwise (Powers & Shoham
2004). **Convergence to an equilibrium is not necessarily the goal.**

**Descriptive** — MARL as a *model of how natural agents learn* (humans,
animals) in a population. Proposes an algorithm as an idealised account of
adaptation, tests it against behaviour using social science and behavioural
economics methods (Mullainathan & Thaler 2000; Camerer 2011; Drouvelis 2021),
then analyses population convergence via evolutionary game theory (Bloembergen
et al. 2015).

## Where this book sits

Computational and prescriptive, with computational closest to its perspective —
which is why the book introduces game models and solution concepts *before*
algorithms. **The descriptive agenda is explicitly out of scope** [Ch. 1.5].

Shoham et al.'s point, endorsed by the authors: *be clear about the purpose and
goals when using MARL.* Different agendas make different results meaningful —
useful when reading a paper and wondering why it measures what it measures.

## Related
[[ch01-introduction]] · [[solution-concepts]]
