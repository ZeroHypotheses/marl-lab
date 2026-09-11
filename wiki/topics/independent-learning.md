---
title: Independent Learning
type: topic
status: solid
sources: ["[[ch05-marl-in-games]]"]
updated: 2026-09-11
---

# Independent Learning (IL)

Each agent learns $\pi_i$ from **its own** observations, actions and rewards,
**ignoring that other agents exist** [Ch. 5.3.2] (Tan 1993; Claus & Boutilier
1998). Other agents' effects are simply absorbed into the environment dynamics.

**Independent Q-learning (IQL)** [Algorithm 5]: each agent runs its own copy of
Q-learning on $Q_i(s,a_i)$, ε-greedy over **its own** action set, updating from
its own reward $r_i^t$. This is the algorithm the tabular exercise implements
→ [[iql-tabular]].

## What it fixes and what it costs

**Fixes:** no exponential joint-action space; works when local policies are
required by the system's structure; **no reward scalarisation needed** — each
agent just uses its own reward. All three are [[central-learning]]'s limitations.

**Costs:** non-stationarity. From agent $i$'s view the other agents' policies are
folded into the transition function [Eq. 5.10]:
$$T_i(s^{t+1}\mid s^t, a_i^t) \propto \sum_{a_{-i} \in A_{-i}} T(s^{t+1}\mid s^t, \langle a_i^t, a_{-i}\rangle)\prod_{j \ne i}\pi_j(a_j \mid s^t)$$

As each $\pi_j$ changes, $T_i$ changes. "Independent learning approaches may
produce unstable learning and may not converge to any solution of the game."
→ [[non-stationarity]]

## What the idealised analysis predicts

Wunder, Littman & Babes (2010) study IQL with ε-greedy exploration under
**infinitesimal** learning steps $\alpha \to 0$, which permits linear dynamical
systems analysis. Fig. 5.2 classifies two-agent two-action general-sum games by
their numbers of deterministic/probabilistic Nash equilibria, whether an agent
has a dominant action, and whether some joint action beats the equilibrium:

| Subclass | 1a | 1b | 2a | 2b | 3a | 3b |
|---|---|---|---|---|---|---|
| # deterministic NE | 0 | 0 | 2 | 2 | 1 | 1 |
| # probabilistic NE | 1 | 1 | 1 | 1 | 0 | 0 |
| Dominant action? | No | No | No | No | Yes | Yes |
| Det. joint act. > NE? | No | Yes | No | Yes | No | Yes |
| **IQL converges?** | Yes | **No** | Yes | Y/N | Yes | **Y/N** |

Battle of the Sexes is 2a; Chicken 2b; **Prisoner's Dilemma 3b**.

> The striking finding: in class 3b (Prisoner's Dilemma) IQL "can have a chaotic
> non-convergent behavior that results in rewards that **average above** the
> expected reward under the unique Nash equilibrium of the game" [Ch. 5.3.2].
> Failing to converge outperforms converging. A sharp reminder that equilibrium
> ≠ good ([[solution-concepts]] §4.7).

## Don't dismiss it

> "Despite their relative simplicity, independent learning algorithms still
> serve as important baselines in MARL research. In fact, they can often produce
> results that are competitive with state-of-the-art MARL algorithms"
> (Papoudakis et al. 2021) [Ch. 5.3.2].

And in the chapter's own LBF experiment, **IQL beat CQL** ([[ch05-marl-in-games]]
§5.3.3). The deep descendants are [[idqn]], [[ia2c]], [[ippo]] in
[[ch09-deep-marl]].

## Related
[[central-learning]] · [[non-stationarity]] · [[iql-tabular]] ·
[[equilibrium-selection]] · [[self-play]]
