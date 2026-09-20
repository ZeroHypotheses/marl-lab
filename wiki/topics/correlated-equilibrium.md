---
title: (Coarse) Correlated Equilibrium
type: topic
status: solid
sources: ["[[ch04-solution-concepts]]", "[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# (Coarse) Correlated Equilibrium

[[nash-equilibrium|Nash equilibrium]] requires agent policies to be
**probabilistically independent** [Eq. 4.5], "which can limit the expected
returns that can be achieved." Correlated equilibrium (Aumann 1974) drops that
restriction [Ch. 4.6, Def. 8].

Each agent conditions on a private random variable $d_i$, drawn from a joint
distribution known to all. In the common normal-form version, $d_i$ is an
**action recommendation** from a joint policy $\pi_c$ over joint actions.
$\pi_c$ is a correlated equilibrium if for every agent $i$ and every **action
modifier** $\xi_i : A_i \to A_i$,
$$\sum_{a \in A}\pi_c(a) R_i(\langle \xi_i(a_i), a_{-i}\rangle) \le \sum_{a \in A}\pi_c(a) R_i(a)$$
[Eq. 4.19]

Each agent knows $\pi_c$ and **its own** recommendation, not the others'. No
agent gains by deviating from what it was told.

Nash is the special case where $\pi_c$ factorises,
$\pi_c(a) = \prod_i \pi_i(a_i)$ — then knowing your own action tells you nothing
about anyone else's. So **the set of correlated equilibria contains the set of
Nash equilibria** (Osborne & Rubinstein 1994). An ε-version follows by adding
$-\epsilon$ on the left.

## The Chicken example — correlation beats independence

Chicken [Fig. 4.3]: (S,S)→(0,0), (S,L)→(7,2), (L,S)→(2,7), (L,L)→(6,6).

Three Nash equilibria: $(7,2)$, $(2,7)$, and both playing S w.p. $\tfrac13$ giving
$\approx(4.66, 4.66)$.

Correlated: $\pi_c(L,L) = \pi_c(S,L) = \pi_c(L,S) = \tfrac13$, $\pi_c(S,S) = 0$.
**Expected return 5 to each** — better than the symmetric Nash equilibrium's 4.66.

Why no one deviates: told L, agent $i$ infers $j$ plays S or L with probability
0.5 each. Playing L gives $2(\tfrac12) + 6(\tfrac12) = 4$; playing S gives
$0(\tfrac12) + 7(\tfrac12) = 3.5$. So L it is.

> Still not optimal: (L,L) pays 6 each and is **neither** a Nash nor a correlated
> equilibrium [§4.7]. Correlation narrows the gap; it doesn't close it.

## Coarse correlated equilibrium

(Moulin & Vial 1978) Requires Eq. 4.19 only for **unconditional** action
modifiers — constant actions, chosen **before** seeing the recommendation. So
each agent decides up front whether to commit to $\pi_c$ at all. Correlated
equilibria are the special case where the condition holds for *all* modifiers,
so **coarse correlated ⊃ correlated ⊃ Nash**.

## §4.6.1 Via linear programming

Variables $x_a = \pi(a)$ per joint action; the book maximises social welfare
[Eq. 4.20] subject to no-deviation constraints [Eq. 4.21], non-negativity and
normalisation [Eqs. 4.22–4.23]. Coarse correlated: replace Eq. 4.21 with
Eq. 4.24. Polynomial time.

> **But it scales badly.** Variables now range over **joint** actions. For $n$
> agents with $k$ actions each: $k^n$ constraints from Eq. 4.22, $nk^2$ from
> Eq. 4.21, $nk$ from Eq. 4.24. The exponential term is
> [[scaling-in-number-of-agents]] appearing in the *solution* method, not just
> the learning problem (§5.4.4).

## Sequential games

Many definitions exist (Forges 1986; Solan & Vieille 2002; von Stengel & Forges
2008; Farina, Bianchi & Sandholm 2020), varying in whether $d_i$ gives actions
per decision point or a whole policy up front, what it conditions on, whether
outcomes are revealed, and how deviators are treated. "Relatively complex" — the
book does not settle on one.

## As a learning outcome

Chapter 6 reaches this concept in two different ways. [[correlated-q-learning]]
solves for a correlated equilibrium inside every TD target and therefore needs
a shared correlation mechanism [Ch. 6.2.3]. By contrast,
[[regret-matching]] does not solve the equilibrium directly: if all agents drive
internal regret to zero, their empirical joint-action distribution approaches
the set of correlated equilibria; external regret yields the larger coarse set
[Ch. 6.5.2].

## Related
[[nash-equilibrium]] · [[no-regret]] (no internal regret → correlated equilibria) ·
[[solution-concepts]] · [[scaling-in-number-of-agents]] ·
[[correlated-q-learning]] · [[regret-matching]]
