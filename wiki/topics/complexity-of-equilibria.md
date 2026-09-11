---
title: The Complexity of Computing Equilibria
type: topic
status: solid
sources: ["[[ch04-solution-concepts]]"]
updated: 2026-09-11
---

# The Complexity of Computing Equilibria

"How difficult is it to compute an equilibrium solution for a game?" [Ch. 4.11].
Answered for **non-repeated normal-form games** — the building block of the
other models, so results here **lower-bound** the harder ones.

## Why P/NP is the wrong frame

P and NP characterise **decision** problems, which may or may not have
solutions. But games **always have at least one equilibrium**. Computing one is
therefore a **total search problem**, not a decision problem.

Computing an equilibrium with an *extra* property *is* a decision problem, and
these are all **NP-hard** (Gilboa & Zemel 1989; Conitzer & Sandholm 2008):
Pareto-optimal equilibria; equilibria meeting a minimum return per agent;
meeting a minimum social welfare; or assigning zero/positive probability to
given actions.

## What is tractable

| Problem | Complexity |
|---|---|
| [[minimax]] in 2-agent zero-sum normal-form games | polynomial (linear program, §4.3.1) |
| [[correlated-equilibrium]] in general-sum normal-form games | polynomial (linear program, §4.6.1) |
| **NASH** — [[nash-equilibrium]] in general-sum normal-form games | **PPAD-complete** |

Nash resists linear programming precisely **because of the independence
assumption** between policies — the assumption correlated equilibrium drops.

## PPAD

"Polynomial parity argument for directed graphs" [§4.11.1]. Defined via its
complete problem **End-of-Line** [Def. 13]: a directed graph on $2^k$ nodes where
every node has at most one parent and one child, given only `Parent`/`Child`
circuits and a source node — find another source or a sink.

A source always has a corresponding sink (the "parity argument"), so a solution
**must exist**. But with only the circuits, the obvious method is walking the
path — **exponential in the worst case**, since there are $2^k$ nodes.

Whether $P = PPAD$ is open, as $P = NP$ is. PPAD contains problems resisted for
decades — Brouwer fixed-points, Arrow-Debreu market equilibria — and is hard
under cryptographic assumptions (Bitansky, Paneth & Rosen 2015; Garg, Pandey &
Srinivasan 2016; Choudhuri et al. 2019).

## NASH is PPAD-complete

Proved for ≥3 agents (Daskalakis, Goldberg & Papadimitriou 2006, 2009), then for
2 agents (Chen & Deng 2006). Precisely: for **ε-Nash** ([[nash-equilibrium]])
under certain bounds on $\epsilon$, and for exact equilibria with two agents.
The ε formulation matters because equilibria can require irrational
probabilities with ≥3 agents.

> **Why this reaches MARL.** Because the result covers ε-Nash, it covers
> "approximation schemes for computing Nash equilibria, **such as MARL
> algorithms**, which may only learn approximate solutions given a finite number
> of interactions."

## The implication

> "MARL is unlikely to be a magic bullet for solving games... it is unlikely
> that efficient MARL algorithms exist to compute Nash equilibria in polynomial
> time. Much of the research in MARL has focused on identifying and exploiting
> **structures (or assumptions) in certain game types**... without such assumed
> structures, it is likely that any MARL algorithm still requires exponential
> time in the worst case" [Ch. 4.11.2].

This reframes much of the rest of the book: [[value-decomposition]] (common
rewards), [[self-play]] (zero-sum) and the rest are **structure exploitation**,
not general-purpose solvers. See [[reward-structures]] and
[[knowledge-assumptions]].

Harder still: approximating an *actual* Nash equilibrium within a policy-space
distance is **FIXP**-complete for ≥3 agents (Etessami & Yannakakis 2010).

## Related
[[nash-equilibrium]] · [[minimax]] · [[correlated-equilibrium]] ·
[[solution-concepts]] · [[scaling-in-number-of-agents]]
