---
title: The General Learning Process in MARL
type: topic
status: solid
sources: ["[[ch05-marl-in-games]]"]
updated: 2026-09-11
---

# The General Learning Process in MARL

Four elements [Ch. 5.1, Fig. 5.1]:

- **Game model** — from [[ch03-games]].
- **Data** — $D^z = \{h^{t_e} \mid e = 1,\dots,z\}$ [Eq. 5.1], histories from
  episodes, possibly incomplete and of differing lengths.
- **Learning algorithm** — $\pi^{z+1} = L(D^z, \pi^z)$ [Eq. 5.2]; $\pi^0$
  typically random.
- **Learning goal** — a joint policy $\pi^*$ satisfying a chosen
  [[solution-concepts|solution concept]].

## Three nuances worth keeping

**1. The game model fixes what policies condition on.**

| Model | Policy conditions on |
|---|---|
| non-repeated normal-form | nothing — just a distribution over actions |
| repeated normal-form | action history $(a^0,\dots,a^{t-1})$ |
| stochastic game | state-action history $(s^0,a^0,\dots,s^t)$ |
| POSG | own observation history $(o_i^0,\dots,o_i^t)$ |

These are the *general* forms and may be constrained — condition only on the
current state, or the last $k$ observations.

**2. The data may hold more than the policies can see.** $D^z$ may contain full
histories while policies condition on less. **This gap is exactly what CTDE
exploits** — the algorithm sees everyone's observations during training, the
policies see only local ones [§5.1, pointing to §9.1] →
[[centralised-training-decentralised-execution]].

**3. $L$ may be many algorithms.** One $L_i$ per agent, each possibly on its own
data $D_i^z$ — which is [[independent-learning]].

> And: "an important characteristic of RL is that the learning algorithm is
> actively involved in the generation of the data by exploring actions, rather
> than just passively consuming the data" [§5.1]. The policy randomises partly
> to produce data worth learning from.

## Related
[[convergence-types]] · [[independent-learning]] · [[central-learning]] ·
[[solution-concepts]]
