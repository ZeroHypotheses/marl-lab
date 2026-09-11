---
title: Modelling Communication in Games
type: topic
status: solid
sources: ["[[ch03-games]]"]
updated: 2026-09-11
---

# Modelling Communication in Games

Communication needs no new model — it is "a type of action that can be observed
by other agents but does not affect the state of the environment" [Ch. 3.5].

Split each agent's action space [Eq. 3.6]:
$$A_i = X_i \times M_i$$
with $X_i$ environment actions and $M_i$ messages (discrete symbols, continuous
values, vectors, or $\emptyset$). Each action $(x_i, m_i)$ does both at once.

**The formal condition** that messages don't move the state [Eq. 3.7]: for all
$s, s'$, all $a \in A$ and all $m \in M$,
$$T(s'\mid s,a) = T(s'\mid s,\langle(a_1^x,m_1),\dots,(a_n^x,m_n)\rangle)$$
i.e. transitions are independent of the communication components.

## Where the messages land

- In a **[[stochastic-games|stochastic game]]**, everyone observes $a^{t-1}$, so
  every message is received by all.
- In a **[[partial-observability|POSG]]**, the observation function does the
  work: $o_i^t = [\bar{s}^t, w_1^{t-1},\dots,w_n^{t-1}]$ with $w_j^{t-1} = f(m_j^{t-1})$.
  Noise: $f(m) = m + \eta$, $\eta$ Gaussian. Message loss: set $w_j$ to
  $\emptyset$ with some probability. Limited range: set $w_j = \emptyset$ when
  out of range.

**Messages are ephemeral** — one time step only. But since agents see the
history, they can in principle remember past messages.

## The learning difficulty

> "In reinforcement learning, the standard assumption is that agents do not know
> the meaning of the actions in $A_i$, including the communication actions"
> [Ch. 3.5] → [[knowledge-assumptions]].

So a message is just another abstract action, and agents must learn both **what
to send** and **how to interpret what they receive**. That opens the possibility
of agents evolving a shared language (Foerster et al. 2016; Sukhbaatar, Szlam &
Fergus 2016; Wang, He, et al. 2020; Guo et al. 2022) — the "shared language"
gestured at in [[ch01-introduction]]'s opening paragraph.

> The book gives communication **no special treatment** after this section:
> algorithms "learn policies over any given action sets $A_i$, which may or may
> not include communication actions" [Ch. 3.5].

## Related
[[partial-observability]] · [[stochastic-games]] · [[knowledge-assumptions]]
