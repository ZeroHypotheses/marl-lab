---
title: Convergence Types
type: topic
status: solid
sources: ["[[ch05-marl-in-games]]", "[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Convergence Types

How MARL algorithms are evaluated **theoretically** [Ch. 5.2]. Which type a
result uses matters — papers claim different things under the same word.

**The standard criterion** — convergence of the joint policy:
$$\lim_{z\to\infty}\pi^z = \pi^*$$
[Eq. 5.3]

Note "**a** solution $\pi^*$" — games may have many, and the claim is only that
some valid one is reached.

## Weaker types, and why they exist

| | Criterion | |
|---|---|---|
| Expected return | $\lim_z U_i(\pi^z) = U_i(\pi^*)$ | [Eq. 5.4] |
| Empirical distribution | $\lim_z \bar{\pi}^z = \pi^*$ | [Eqs. 5.5–5.6] |
| Empirical distribution → **set** of solutions | $\forall\epsilon\,\exists z_0\,\forall z>z_0\,\exists\pi^*: d(\bar\pi^z,\pi^*)<\epsilon$ | [Eq. 5.7] |
| Average return | $\lim_z \bar{U}_i^z = U_i(\pi^*)$ | [Eq. 5.8] |

$\bar\pi^z$ is the joint policy averaged over episodes; equivalently the
empirical distribution of joint actions [Eq. 5.6] — the two coincide as
$z \to \infty$. Eq. 5.7 differs from Eq. 5.3 in that the distribution reaches the
solution *space* but may then "wander" inside it without settling.

**These are not academic hedges — they exist because specific algorithms cannot
achieve Eq. 5.3:**

- **[[fictitious-play]]** (§6.3.1) learns *deterministic* policies, so it cannot
  represent the uniform Nash equilibrium of Rock-Paper-Scissors — but its
  empirical action distribution converges [Eq. 5.5] (Fudenberg & Levine 1998).
- **IGA** (§6.4.1) learns probabilistic policies yet may still not converge to a
  probabilistic Nash equilibrium — but its *average rewards* do [Eq. 5.8]
  (Singh, Kearns & Mansour 2000).
- **[[regret-matching]]** (§6.5) can change $\pi^z$ abruptly and may converge to no
  single $\pi^*$ — but its empirical distributions converge to the set of
  (coarse) correlated equilibria [Eq. 5.7] (Hart & Mas-Colell 2000)
  → [[no-regret]].

Eq. 5.3 implies all the weaker types.

Chapter 6 supplies the corresponding algorithmic examples. Minimax Q-learning
converges in Q-values under its zero-sum assumptions; WoLF-IGA converges in
policy in its restricted two-agent/two-action setting; IGA may only converge in
average reward; fictitious play, GIGA, and regret matching can instead provide
empirical-distribution guarantees [Ch. 6.2.1, 6.3.1, 6.4.2–6.5.2]. These claims
are not interchangeable.

## What none of them say

> They "make no claims about the performance of any individual joint policy
> $\pi^z$ for a finite $z$" — i.e. **nothing about how agents perform during
> learning**. A stronger criterion would bound $\|\pi^z - \pi^*\|$ at finite $z$.

That gap is precisely the concern of the **prescriptive** agenda
([[marl-agendas]]) and of [[no-regret]].

## The practical substitute, and its limit

In complex games these properties can't be checked, so what's actually done is
plotting $U_i(\pi^z)$ as [[learning-curves]].

> **But:** "even if the expected returns $U_i(\pi^z)$ for all $i$ converge after
> some finite $z$, the joint policy $\pi^z$ might not satisfy **any** of the
> convergence properties of Equations 5.3 to 5.8" [Ch. 5.2].

A flat learning curve is not evidence of convergence to a solution. Worth
remembering before claiming one in `experiments/`.

## Related
[[general-learning-process]] · [[solution-concepts]] · [[learning-curves]] ·
[[no-regret]] · [[non-stationarity]]
