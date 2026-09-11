---
title: Nash Equilibrium (and ε-Nash)
type: topic
status: solid
sources: ["[[ch04-solution-concepts]]"]
updated: 2026-09-11
---

# Nash Equilibrium

Mutual [[best-response]] extended to **general-sum games with $n$ agents**
[Ch. 4.4, Def. 6] (Nash 1950). $\pi$ is a Nash equilibrium if
$$\forall i, \pi_i' : \; U_i(\pi_i', \pi_{-i}) \le U_i(\pi)$$
[Eq. 4.16]

No agent can improve by changing its own policy while the others stay fixed —
i.e. $\pi_i \in BR_i(\pi_{-i})$ for all $i$.

**Existence:** every finite normal-form game has at least one (Nash 1950); also
shown for stochastic games (Fink 1964; Filar & Vrieze 2012). Generalises
[[minimax]] — in two-agent zero-sum games the two sets coincide.

## Examples [Fig. 3.2]

| Game | Nash equilibria |
|---|---|
| Prisoner's Dilemma | unique: (D,D) |
| Coordination | three: (A,A), (B,B), and both agents 50/50 |
| Rock-Paper-Scissors | unique: both uniform (= the minimax solution) |

## Two properties that shape everything downstream

**1. Equilibria may be probabilistic — sometimes necessarily so.**
Prisoner's Dilemma has a deterministic ("pure") equilibrium; Rock-Paper-Scissors
has **only** a probabilistic ("mixed") one.

> "This distinction is important in MARL because some algorithms are unable to
> represent probabilistic policies, and hence cannot learn probabilistic
> equilibria" [Ch. 4.4] → [[ch06-foundational-algorithms]].

(Terminology: pure/mixed = deterministic/probabilistic →
[[rl-game-theory-dictionary]].)

**2. Multiple equilibria may pay agents differently.**
In the coordination game the two deterministic equilibria pay 10 each, the
probabilistic one pays 5 each. Chicken (§4.6) and Stag Hunt (§5.4.2) are further
examples. **Which equilibrium should agents converge to, and how can they
agree?** That is the equilibrium selection problem → §5.4.2,
[[ch05-marl-in-games]].

Contrast [[value-functions-and-bellman]]: in an MDP all optimal policies share
one optimal value. Here they do not.

## Checking whether π is a Nash equilibrium

Reduce $n$-agent to $n$ single-agent problems [Ch. 4.4]: for each $i$, hold
$\pi_{-i}$ fixed and compute an optimal best response $\pi_i'$. If
$U_i(\pi_i',\pi_{-i}) > U_i(\pi)$ for any $i$, it is not an equilibrium. For
normal-form games $\pi_i'$ comes from a linear program (Albrecht & Ramamoorthy
2012); for sequential games, from a single-agent RL algorithm.

# ε-Nash Equilibrium

[Ch. 4.5, Def. 7] Relaxes the strict condition by a slack $\epsilon > 0$:
$$\forall i, \pi_i' : \; U_i(\pi_i',\pi_{-i}) - \epsilon \le U_i(\pi)$$
[Eq. 4.18]

**Why it's needed:** with three or more agents, equilibrium action probabilities
**may be irrational numbers** — Nash (1950) noted this — and finite-precision
floating point cannot represent them. Exact equilibria may also be too costly.

## The trap

Every Nash equilibrium is surrounded by a region of ε-Nash equilibria, and
$\epsilon = 0$ recovers the exact one. **But an ε-Nash equilibrium need not be
anywhere near a real one.**

> "The expected returns under an ϵ-Nash equilibrium may be arbitrarily far away
> from those of any Nash equilibrium, even if the Nash equilibrium is unique"
> [Ch. 4.5].

Fig. 4.2 makes it concrete: a game with unique Nash equilibrium (A,C) paying
(100,100) also has an ε-Nash equilibrium (B,D) at $\epsilon = 1$ paying (1,1).
**The (A,C) rewards can be raised arbitrarily without disturbing (B,D) at all.**
So ε-Nash is a *relaxation*, not an *approximation*.

(Approximating an actual Nash equilibrium within a distance in policy space is
strictly harder — FIXP-complete for ≥3 agents, Etessami & Yannakakis 2010
[footnote 18].)

## Related
[[solution-concepts]] · [[minimax]] · [[correlated-equilibrium]] ·
[[best-response]] · [[complexity-of-equilibria]] · [[pareto-optimality]]
