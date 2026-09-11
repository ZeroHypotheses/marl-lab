---
title: "Ch. 5 — MARL in Games: First Steps and Challenges"
type: source
status: solid
sources: ["MARL book, Ch. 5, pp. 89–114 (2nd printing)"]
updated: 2026-09-11
---

# Chapter 5 — MARL in Games: First Steps and Challenges

The first chapter that actually *learns* anything. Two naive reductions of MARL
to single-agent RL, used as a vehicle to expose the four challenges properly.
Only 11 numbered equations.

## Contents

- **§5.1** the general learning process → [[general-learning-process]]
- **§5.2** convergence types → [[convergence-types]]
- **§5.3** single-agent reductions → [[central-learning]], [[independent-learning]]
- **§5.4** the four challenges → [[non-stationarity]], [[equilibrium-selection]],
  [[credit-assignment]], [[scaling-in-number-of-agents]]
- **§5.5** self-play and mixed-play → [[self-play]]

## §5.3.3 — CQL vs IQL in level-based foraging

The chapter's empirical centrepiece [Figs. 5.3–5.4]. An 11×11 grid, two level-1
agents, one level-1 item and one level-2 item — so **one item requires
cooperation**. Modelled as a stochastic game, full observability, $\gamma = 0.99$,
$\alpha = 0.01$, $\epsilon$ decayed 1 → 0.05 over 80,000 steps, 50 runs.
Reward $\tfrac13$ per collection; CQL scalarises by summing.

**Result: IQL learns faster, both converge to the optimal joint policy.** IQL's
agents explore 6 actions per state; CQL's central agent explores $6^2 = 36$.
That gap shows up as IQL's early jump — it finds the level-1 item sooner.

The optimal joint policy takes 13 steps: the right-corner agent goes to the
level-2 item and **waits**; the left-corner agent collects the level-1 item first,
then joins it.

> Worth noting how modest this is — two agents, one grid, one task — and that the
> conclusion still favours the *naive* method. §5.3.2 adds that independent
> learning "can often produce results that are competitive with state-of-the-art
> MARL algorithms" (Papoudakis et al. 2021). Keep this as a baseline discipline
> for `experiments/`.

## What this chapter changes about earlier pages

- **[[scaling-in-number-of-agents]]** — §5.4.4 supplies the counter-example
  promised in ch. 1.4. Exponential growth is **not** intrinsic. ✅ resolved
- **[[non-stationarity]]** — given a precise definition via stationary stochastic
  processes, and Eq. 5.10 shows exactly how other agents' policies enter agent
  $i$'s transition function.
- **[[credit-assignment]]** — the common-reward framing from ch. 1 is corrected:
  the problem "exists more generally and does not depend on common rewards."

## Convergence guarantees are thin

> "All known theoretical results in MARL for convergent learning are limited to
> restricted game settings and mostly only work for specific algorithms"
> [§5.4.1].

IGA converges to the average reward of a Nash equilibrium [Eq. 5.8]; WoLF-IGA
to a Nash equilibrium [Eq. 5.3] — **both only for two-agent, two-action
normal-form games**. The stochastic approximation conditions that suffice in
single-agent TD learning [Eq. 2.54] "are usually not sufficient in MARL."

Ongoing work: Zhang, Yang & Basar 2019; Daskalakis, Foster & Golowich 2020;
Wei et al. 2021; Ding et al. 2022; Leonardos et al. 2022.

## Related
[[ch04-solution-concepts]] · [[ch06-foundational-algorithms]] ·
[[independent-learning]] · [[level-based-foraging]]
