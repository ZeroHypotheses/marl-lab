---
title: Equilibrium Selection
type: topic
status: solid
sources: ["[[ch05-marl-in-games]]"]
updated: 2026-09-11
---

# Equilibrium Selection

"Which equilibrium the agents should agree on and how they can achieve
agreement" [Ch. 5.4.2] (Harsanyi & Selten 1988). Arises whenever a game has
multiple equilibria paying agents differently — see §4.7,
[[solution-concepts]].

Chicken has three, paying $(7,2)$, $(2,7)$ and $\approx(4.66,4.66)$.

> The hard part in MARL: agents "typically do not have prior knowledge about the
> game" ([[knowledge-assumptions]]), so they cannot simply agree in advance.

## Stag Hunt — why agents drift to the *worse* equilibrium

[Fig. 5.6(b)] (S,S)→(4,4), (S,H)→(0,3), (H,S)→(3,0), (H,H)→(2,2). Hunting a stag
needs cooperation and pays more; a hare can be taken alone for less.

Two deterministic Nash equilibria (plus a probabilistic one):
- **(S,S)** — **reward-dominant**: pays more, and is Pareto-optimal.
- **(H,H)** — **risk-dominant**: choosing H guarantees at least 2 regardless.

> "Algorithms such as independent Q-learning can be prone to converging to a
> risk-dominant equilibrium if they are uncertain about the actions of other
> agents" [Ch. 5.4.2].

The mechanism is a feedback loop worth internalising: early in learning actions
are near-random, so S is often punished (0) while H reliably pays 2 or more.
Agents shift probability toward H — **which makes deviating from H worse for
everyone**, reinforcing it. Exploration noise, not the payoff structure, picks
the equilibrium.

## Four approaches

1. **Refine the solution space** — require [[pareto-optimality]] or
   [[social-welfare-and-fairness]]. Sometimes reduces infinitely many solutions
   to one (§4.9).
2. **Exploit game structure** — minimax Q-learning (§6.2.1) benefits from
   zero-sum games having a **unique equilibrium value**, so selection doesn't
   arise. In no-conflict games like Stag Hunt, Pareto actor-critic (ch. 9) uses
   the fact that all agents know the reward-dominant equilibrium is preferred by
   all. → [[reward-structures]]
3. **[[agent-modelling]]** (§6.3) — predict others' actions. If agent 1 expects
   agent 2 to play S after agent 1 played S, it may reinforce (S,S). "However,
   whether such an outcome occurs depends on several factors, such as the
   details of the agents' exploration strategies and learning rates."
4. **Communication** → [[communication-in-games]]. But agents may not be "bound
   to the information they communicate", others cannot verify it, and **where
   equilibria pay differently there is a genuine conflict of preference** — so
   talking does not dissolve the problem.

## Related
[[solution-concepts]] · [[nash-equilibrium]] · [[independent-learning]] ·
[[non-stationarity]] · [[agent-modelling]]
