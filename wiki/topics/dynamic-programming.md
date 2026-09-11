---
title: Dynamic Programming (for MDPs)
type: topic
status: solid
sources: ["[[ch02-reinforcement-learning]]"]
updated: 2026-09-11
---

# Dynamic Programming (for MDPs)

Uses the Bellman equations **as operators**, applied iteratively [Ch. 2.5]
(Bellman 1957; Howard 1960). **Requires complete knowledge of the MDP** — both
$R$ and $T$. DP does not "interact" with the environment at all, but it is the
theoretical basis for [[temporal-difference-learning]].

## Policy iteration

Alternates two tasks:
- **Policy evaluation** — compute $V^\pi$ for the current $\pi$
- **Policy improvement** — make $\pi$ greedy w.r.t. $V^\pi$

$$\pi^0 \to V^{\pi^0} \to \pi^1 \to V^{\pi^1} \to \pi^2 \to \dots \to V^* \to \pi^*$$
[Eq. 2.27]

**Iterative policy evaluation** repeatedly sweeps [Eq. 2.28]:
$$V^{k+1}(s) \leftarrow \sum_a \pi(a|s)\sum_{s'} T(s'|s,a)\left[R(s,a,s') + \gamma V^k(s')\right]$$

Updating $V(s)$ using estimates $V(s')$ is **bootstrapping** — "a core property
of many RL algorithms" [Ch. 2.5].

**Policy improvement** [Eqs. 2.38–2.39]:
$\pi'(s) = \arg\max_a Q^\pi(s,a)$. By the policy improvement theorem, $\pi'$ is
at least as good as $\pi$ [Eq. 2.42]. **If $\pi'$ doesn't change, $\pi$ is
optimal** [Eqs. 2.43–2.46] — that's the termination condition.

## Value iteration

Collapses one evaluation sweep and improvement into a single update using the
Bellman *optimality* equation [Eq. 2.47, Algorithm 1]:
$$V^{k+1}(s) \leftarrow \max_{a} \sum_{s'} T(s'|s,a)\left[R(s,a,s') + \gamma V^k(s')\right]$$

Extended to games as the first foundational MARL algorithm — §6.1,
[[ch06-foundational-algorithms]].

## Why it converges

Both operators are **γ-contraction mappings** under the max-norm. A mapping $f$
is a γ-contraction if $\|f(x) - f(y)\| \le \gamma\|x-y\|$ [Eq. 2.29]; by the
**Banach fixed-point theorem** repeated application from any starting vector
converges to a unique fixed point.

The book proves it by writing the Bellman operator in matrix form
$f^\pi(v) = r^\pi + \gamma M^\pi v$ [Eq. 2.32], giving
$\|f^\pi(v) - f^\pi(u)\|_\infty = \gamma\|M^\pi(v-u)\|_\infty \le \gamma\|v-u\|_\infty$
[Eqs. 2.35–2.37], since each row of $M^\pi$ sums to 1.

> This proof structure is worth remembering: contraction ⇒ unique fixed point ⇒
> convergence. Whether the analogous operator in a *game* is still a contraction
> is exactly what's at stake in [[ch06-foundational-algorithms]].

## Related
[[value-functions-and-bellman]] · [[temporal-difference-learning]] ·
[[ch06-foundational-algorithms]]
