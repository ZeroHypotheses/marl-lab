---
title: Social Welfare and Fairness
type: topic
status: solid
sources: ["[[ch04-solution-concepts]]"]
updated: 2026-09-11
---

# Social Welfare and Fairness

[[pareto-optimality]] says nothing about **how much** total reward there is or
**how it is distributed** — the Chicken frontier runs from $(7,2)$ through
$(6,6)$ to $(2,7)$ [Ch. 4.9].

*Welfare* concerns the total; *fairness* concerns the distribution.

**Welfare** [Def. 10, Eq. 4.26]: $W(\pi) = \sum_{i \in I} U_i(\pi)$; welfare-optimal
if it maximises $W$.

**Fairness** [Def. 11, Eq. 4.27]: $F(\pi) = \prod_{i \in I} U_i(\pi)$; fairness-optimal
if it maximises $F$. (Also known as **Nash social welfare**, the geometric mean
$(\prod_i U_i)^{1/n}$ — Caragiannis et al. 2019; Fan et al. 2023.)

## Why the product encodes equity

Among joint policies with **equal welfare**, the product is maximised by the one
giving all agents equal return. The book's example: $(1,5)$, $(2,4)$, $(3,3)$ all
have welfare 6, with fairness 5, 8, 9 respectively.

In Chicken this narrows things to a single solution: $(6,6)$ is the only joint
return that is both welfare- and fairness-optimal.

**Battle of the Sexes** [Fig. 4.5]: (A,A)→(10,7), (A,B)→(2,2), (B,A)→(0,0),
(B,B)→(7,10). The deterministic (A,A) and (B,B) are the only joint policies both
Pareto-optimal and fairness-optimal; **the probabilistic Nash equilibrium is
neither.**

## Welfare optimality ⇒ Pareto optimality

Proof [Ch. 4.9]: suppose $\pi$ is welfare-optimal but Pareto-dominated by
$\pi'$. Then $\forall i: U_i(\pi') \ge U_i(\pi)$ with strict inequality for some
$i$, so $\sum_i U_i(\pi') > \sum_i U_i(\pi)$ — contradicting welfare-optimality.

The converse fails, so welfare optimality is **strictly stronger**. Fairness
optimality and Pareto optimality imply each other in neither direction.

## Where they don't help

- **Common-reward games** — welfare and fairness are maximised exactly when each
  agent's return is; they add nothing.
- **Two-agent zero-sum games** — all minimax solutions share the same value, so
  all have equal welfare and fairness (and welfare is always 0).

They are tools for **general-sum** games → [[reward-structures]].

## Known weaknesses of Def. 11

The book flags them itself [footnote 15]: if $U_i(\pi) = 0$ for any agent, the
others' returns stop mattering; and with negative returns permitted,
$(-0.1, 1, 1)$ would count as *less* fair than $(-0.1, -100, 100)$ —
"counter-intuitive". Treat $F$ as a simple illustration, not a settled measure;
the economics literature has many more (Moulin 2004; Fleurbaey & Maniquet 2011;
Sen 2018; Amanatidis et al. 2023).

## Related
[[pareto-optimality]] · [[solution-concepts]] · [[correlated-equilibrium]]
(the §4.6.1 linear program maximises welfare to pick among equilibria)
