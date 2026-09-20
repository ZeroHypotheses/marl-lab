---
title: No-Regret
type: topic
status: solid
sources: ["[[ch04-solution-concepts]]", "[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# No-Regret

The odd one out among [[solution-concepts]]. Every other concept in
[[ch04-solution-concepts]] judges **a single joint policy**; no-regret judges
**a sequence of episodes** [Ch. 4.10].

> "No-regret considers the performance of learning agents across multiple
> episodes... In this sense, no-regret can be viewed as an example of the
> **prescriptive agenda**" → [[marl-agendas]].

**Regret** for normal-form games over episodes $e = 1,\dots,z$ [Eq. 4.28]:
$$\text{Regret}_i^z = \max_{a_i \in A_i}\sum_{e=1}^{z}\left[R_i(\langle a_i, a_{-i}^e\rangle) - R_i(a^e)\right]$$

i.e. how much better $i$ would have done by playing one fixed action throughout,
against the others' **observed** actions.

**No-regret** [Def. 12, Eq. 4.29]: $\forall i : \lim_{z\to\infty}\tfrac{1}{z}\text{Regret}_i^z \le 0$.
Replacing $\le 0$ with $\le \epsilon$ gives ε-no-regret.

For sequential games, redefine over **policies** from a finite set $\Pi_i$
[Eq. 4.30]; this subsumes Eq. 4.28 when each $\Pi_i$ is the deterministic
policies.

## Worked example [Fig. 4.6]

Ten episodes of Prisoner's Dilemma. Agent 1 scored −21. Always-C would have
given −30; always-D would have given −15. So D was best,
$\text{Regret}_1^{10} = -15 + 21 = 6$, average 0.6.

## Two limitations, and they compound

1. **It assumes the others' actions would have been unchanged.** Sensible if
   they use fixed policies; false if they adapt. "Therefore, regret does not
   actually quantify what would have happened under counterfactual situations."
   In MARL, where everyone learns, this is exactly the [[non-stationarity]]
   assumption failing.
2. **Minimising regret ≠ maximising returns** (Crandall 2014) — a consequence of
   the first. In non-repeated and finitely repeated Prisoner's Dilemma, the only
   no-regret joint policy is both agents always defecting. Same shape of problem
   as §4.7's sub-optimality of equilibria.

## Internal vs external regret, and the equilibrium connection

- **External (unconditional)** regret — Eq. 4.28, replace *all* past actions.
- **Internal (conditional)** regret — replace only the occurrences of one
  specific action $a_i'$ with $a_i$.

The payoff of the distinction [Ch. 4.10] (Hart & Mas-Colell 2000; Young 2004):

| If all agents have… | the empirical distribution of joint actions converges to… |
|---|---|
| no **external** regret, 2-agent zero-sum | the set of [[minimax]] solutions |
| no **external** regret, general-sum | the set of **coarse** correlated equilibria |
| no **internal** regret, general-sum | the set of [[correlated-equilibrium|correlated equilibria]] |

## Algorithms that realise the guarantee

[[regret-matching]] assigns probability in proportion to positive average
regret [Eqs. 6.53–6.58]. Its regret decreases at rate $O(1/\sqrt z)$ without
assuming anything about how the other agents choose actions [Ch. 6.5.2].
[[generalized-infinitesimal-gradient-ascent]] reaches the same external-regret
order through projected policy-gradient updates [Ch. 6.4.5].

The convergence object matters: neither result says the current policy
$\pi^z$ settles. If every agent has vanishing external regret, the **empirical
joint-action distribution** approaches the set of coarse correlated equilibria;
vanishing internal regret strengthens that limiting set to correlated
equilibria [Ch. 6.4.5, 6.5.2]. Rock-Paper-Scissors illustrates the distinction:
the policies can keep moving while empirical play approaches the uniform
distribution [Ch. 6.5.2; [[convergence-types]]].

Other regret definitions: de Farias & Megiddo 2003; Lehrer 2003; Chang 2007;
Zinkevich et al. 2007; Arora, Dekel & Tewari 2012; Crandall 2014.

## Related
[[solution-concepts]] · [[correlated-equilibrium]] · [[marl-agendas]] ·
[[non-stationarity]] · [[regret-matching]] ·
[[generalized-infinitesimal-gradient-ascent]]
