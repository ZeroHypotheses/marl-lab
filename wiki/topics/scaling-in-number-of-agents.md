---
title: Scaling in Number of Agents
type: topic
status: solid
sources: ["[[ch01-introduction]]", "[[ch05-marl-in-games]]"]
updated: 2026-09-11
---

# Scaling in Number of Agents

The joint-action space is the product of the individual ones [Eq. 5.11]:
$$|A| = |A_1| \cdot \ldots \cdot |A_n|$$

In [[level-based-foraging]], going from 3 to 5 agents takes the joint-action
count from **216 to 7,776**. And if agents have their own features in the state
(positions, in LBF), then $|S|$ grows exponentially too [Ch. 5.4.4].

## It bites even without joint-action values

- **Algorithms using $Q(s,a)$ over joint actions** — [[central-learning]],
  joint-action learning (§6.2) — face exponential growth in **both** the space
  to store $Q$ and the number of observations needed to fill it.
- **[[independent-learning]], which avoids joint actions entirely, is still
  hurt**: "a larger number of agents can increase the degree of
  [[non-stationarity]]... since each additional agent adds another moving part
  that the other agents must adapt to."
- **[[credit-assignment]]** gets harder — "each additional agent adds a potential
  cause for an observed reward."

## ✅ The counter-example (resolves ch. 1.4's hedge)

Chapter 1.4 hedged that growth is not always exponential, pointing at §5.4.4.
Here it is.

> Control a power plant with **1,000 control variables**, each taking one of $k$
> values. An action is a length-1,000 vector, so there are $k^{1000}$ actions.
> Factor the vector among $n$ agents, each handling a shorter vector:
> $|A_i| = k^{1000/n}$. But the total is
> $|A| = |A_1|\cdots|A_n| = k^{1000}$ — **independent of $n$.** [Ch. 5.4.4]

**The distinction that matters** [also §5.3.1, footnote 4]:

| | Joint-action space |
|---|---|
| Each added agent brings **new** action variables (LBF: one robot each) | grows exponentially in $n$ |
| A **fixed** set of action variables is **partitioned** among agents | constant, regardless of $n$ |

So the exponential-growth argument for decentralisation ([[training-execution-modes]])
applies to the first case only. In the second, adding agents is pure
decomposition — which is precisely the "decompose a large, intractable decision
problem" motivation of [[ch01-introduction]] §1.2, with no cost in joint-action
count.

## Not unique to MARL

"While exponential growth due to the number of agents is an important challenge
in MARL, it is not unique to MARL." Single-agent reductions like central
learning still face it, and so does model-based multi-agent planning (Oliehoek
& Amato 2016). Part II offers deep learning as one way to improve scalability.

Note it also appears in *solution* methods, not just learning: the correlated
equilibrium linear program has $k^n$ constraints
([[correlated-equilibrium]] §4.6.1).

## Related
[[central-learning]] · [[independent-learning]] · [[non-stationarity]] ·
[[training-execution-modes]] · [[complexity-of-equilibria]]
