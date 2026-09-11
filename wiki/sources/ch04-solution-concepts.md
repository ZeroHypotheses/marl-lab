---
title: "Ch. 4 — Solution Concepts for Games"
type: source
status: solid
sources: ["MARL book, Ch. 4, pp. 61–88 (2nd printing)"]
updated: 2026-09-11
---

# Chapter 4 — Solution Concepts for Games

What it means for agents to act **optimally**. [[ch03-games]] gave the model;
this gives the objective.

> **A MARL problem = a game model + a solution concept** [Fig. 4.1] — exactly
> parallel to Fig. 2.1 in [[ch02-reinforcement-learning]].

All definitions and existence results **assume finite games** (finite states,
actions, observations, agents). Infinite games admit analogous definitions but
"may have different existence properties" — e.g. every finite two-agent zero-sum
normal-form game has a unique minimax value, yet continuous-action zero-sum
games exist with none (Sion & Wolfe 1957) [footnote 1].

> 📕 errata: two entries here (p80 missing index $i$ in $U(\pi)$; p84 removed
> clause about exponential time on a deterministic Turing machine). Both
> verified applied in our copy. See [[errata]].

## §4.1 — Expected return, universally

To make every solution concept apply to every game model, $U_i(\pi)$ is defined
on the POSG. **Two equivalent definitions:**

- **History-based** [Eqs. 4.1–4.4] — enumerate all full histories, weight each by
  its probability under $\pi$ [Eq. 4.3] and its discounted return [Eq. 4.4].
  Reads as a linear sum; easier to interpret.
- **Recursive** [Eqs. 4.6–4.8] — interlocked $V_i^\pi(\hat{h})$ and
  $Q_i^\pi(\hat{h},a)$, Bellman-style. **Operationalisable** — this is what value
  iteration for games uses (§6.1) → [[ch06-foundational-algorithms]].

Note [Eq. 4.5]: $\pi(a^\tau \mid h^\tau) = \prod_j \pi_j(a_j^\tau \mid h_j^\tau)$
holds **only if agents act independently**. Correlated equilibrium (§4.6) and
central learning (§5.3.1) break that factorisation deliberately.

## The concepts

| Section | Concept | Applies to | Page |
|---|---|---|---|
| 4.2 | Best response | all | [[best-response]] |
| 4.3 | Minimax | 2-agent zero-sum | [[minimax]] |
| 4.4–4.5 | Nash, ε-Nash | general-sum, $n$ agents | [[nash-equilibrium]] |
| 4.6 | (Coarse) correlated equilibrium | general-sum, $n$ agents | [[correlated-equilibrium]] |
| 4.8 | Pareto optimality | refinement | [[pareto-optimality]] |
| 4.9 | Social welfare and fairness | refinement | [[social-welfare-and-fairness]] |
| 4.10 | No-regret | across episodes | [[no-regret]] |
| 4.11 | Complexity | — | [[complexity-of-equilibria]] |

**The containment:** minimax ⊂ Nash ⊂ correlated ⊂ coarse correlated. In
two-agent zero-sum games the minimax solutions *are* the Nash equilibria
(Owen 2013).

## §4.7 — Conceptual limitations (read this one twice)

The section that stops equilibrium from being treated as a synonym for "good":

1. **Sub-optimality.** "Finding equilibrium solutions is not synonymous with
   maximizing expected returns." Prisoner's Dilemma: the unique Nash equilibrium
   (D,D) pays −3 each; (C,C) pays −1 each but isn't an equilibrium. In Chicken,
   the correlated equilibrium pays 5 each while (L,L) pays 6 each and is neither
   Nash nor correlated.
2. **Non-uniqueness.** Multiple, possibly infinitely many equilibria, each paying
   agents differently → the **equilibrium selection problem**, §5.4.2
   ([[ch05-marl-in-games]]). Pareto optimality and welfare/fairness are proposed
   as tie-breakers.
3. **Incompleteness.** For sequential games an equilibrium says nothing about
   **off-equilibrium paths** — histories with $\Pr(\hat{h}\mid\pi) = 0$, reachable
   by a disturbance. Refinements exist: subgame perfect and trembling-hand
   perfect equilibrium (Selten 1988; Owen 2013).

## Folk theorems

For infinite sequential games, **any feasible and enforceable** expected returns
$\hat{U}$ can be realised by an equilibrium, given far-sighted agents
($\gamma \to 1$) [§4.4]. *Feasible* = achievable by some joint policy;
*enforceable* = each $\hat{U}_i$ at least agent $i$'s minmax value $v_i$
[Eq. 4.17]. The construction: play $\pi$; if $i$ deviates, the others punish it
down to $v_i$ forever using their minmax policies.

**Consequence:** the space of equilibria is enormous, which is exactly why the
refinements of §4.8–4.9 are needed.

## Related
[[solution-concepts]] · [[ch03-games]] · [[ch05-marl-in-games]] ·
[[ch06-foundational-algorithms]]
