---
title: Solution Concepts
type: topic
status: solid
sources: ["[[ch04-solution-concepts]]"]
updated: 2026-09-11
---

# Solution Concepts

**A solution to a game is a joint policy $\pi = (\pi_1,\dots,\pi_n)$ satisfying
conditions stated in terms of the expected returns $U_i(\pi)$ and the relations
between them** [Ch. 4].

> A **MARL problem = game model + solution concept** [Fig. 4.1].

This page is the hub. Each concept has its own page.

## Why it isn't obvious

For **common-reward** games the answer is easy to state — maximise the shared
expected return — "but finding such a solution may not be simple at all"
[Ch. 4]. Once rewards differ, there is no single quantity to maximise, and
"optimal" has to be *defined*. → [[reward-structures]]

## The hierarchy

Nearly all of these are **mutual best response** ([[best-response]]) conditions:
no agent can unilaterally deviate and gain.

| Concept | Applies to | Existence |
|---|---|---|
| [[minimax]] | 2-agent zero-sum | always (von Neumann 1928); unique **value** |
| [[nash-equilibrium]] | general-sum, $n$ agents | always in finite normal-form games (Nash 1950) |
| [[correlated-equilibrium]] | general-sum, $n$ agents | contains Nash as a special case |
| coarse correlated equilibrium | general-sum, $n$ agents | contains correlated as a special case |

**minimax ⊂ Nash ⊂ correlated ⊂ coarse correlated.** In two-agent zero-sum
games the minimax solutions and the Nash equilibria coincide (Owen 2013).

### Refinements — used to *narrow* the set
| | |
|---|---|
| [[pareto-optimality]] | no one better off without someone worse off |
| [[social-welfare-and-fairness]] | sum / product of returns |

### Alternative axis
| | |
|---|---|
| [[no-regret]] | judged **across episodes**, i.e. during learning — the only concept here that looks at *how* the policy was reached |

## Three warnings from §4.7

1. **An equilibrium need not be good.** It guarantees mutual best response, not
   high returns. (D,D) in Prisoner's Dilemma is the unique Nash equilibrium and
   is worse for both agents than (C,C).
2. **Equilibria need not be unique**, and different ones pay agents differently —
   the **equilibrium selection problem** (§5.4.2, [[ch05-marl-in-games]]). Folk
   theorems make this dramatic: essentially any feasible, enforceable return
   profile is achievable by *some* equilibrium.
3. **Equilibria are incomplete** for sequential games — silent on off-equilibrium
   paths.

Contrast with the single-agent case, where the optimal value function is unique
and a deterministic optimal policy always exists
([[value-functions-and-bellman]]). Both properties fail here.

## Why this matters for algorithms

- Some equilibria are **only probabilistic** (Rock-Paper-Scissors has no
  deterministic Nash equilibrium). "Some algorithms are unable to represent
  probabilistic policies, and hence cannot learn probabilistic equilibria"
  [Ch. 4.4] — a real constraint in [[ch06-foundational-algorithms]].
- Computing Nash equilibria is **PPAD-complete** →
  [[complexity-of-equilibria]]. MARL is not a way around that.

## Related
[[ch04-solution-concepts]] · [[best-response]] · [[reward-structures]] ·
[[non-stationarity]] · [[marl-agendas]]
