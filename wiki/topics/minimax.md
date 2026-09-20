---
title: Minimax
type: topic
status: solid
sources: ["[[ch04-solution-concepts]]"]
updated: 2026-09-20
---

# Minimax

For **two-agent zero-sum** games only [Ch. 4.3, Def. 5] (von Neumann 1928; von
Neumann & Morgenstern 1944). A joint policy $\pi = (\pi_i,\pi_j)$ is a minimax
solution if
$$U_i(\pi) = \max_{\pi_i'}\min_{\pi_j'} U_i(\pi_i',\pi_j') = \min_{\pi_j'}\max_{\pi_i'} U_i(\pi_i',\pi_j') = -U_j(\pi)$$
[Eqs. 4.10–4.11]

Each agent plays optimally **against a worst-case opponent**.

- Eq. 4.10 — the return $i$ can *guarantee*: $\pi_i$ is $i$'s **maxmin** policy.
- Eq. 4.11 — the return $j$ can *force on* $i$: $\pi_j$ is the **minmax** policy.
- In a minimax solution these coincide.

> **Interpretation:** the order of the min/max operators doesn't matter — $i$
> announcing its policy first is equivalent to $j$ announcing first. **Neither
> agent gains from announcing.**

## Existence and uniqueness

Exists in every two-agent zero-sum normal-form game; also in two-agent zero-sum
stochastic games, finite-horizon and infinite-horizon-discounted (Shapley 1953).
Several minimax solutions may exist, but **all yield the same unique value**
$U_i(\pi)$ — the **value of the game**.

(Finite games only; continuous-action zero-sum games exist with no minimax
value, Sion & Wolfe 1957.)

## Example

Rock-Paper-Scissors has a **unique** minimax solution: both agents uniform, value
0 to each [Ch. 4.3] — and no deterministic solution exists, which matters for
algorithms that can only represent deterministic policies.

## §4.3.1 Via linear programming

For non-repeated zero-sum normal-form games, solve two linear programs (one per
agent). Variables $x_{a_i} = \pi_i(a_i)$ and $U_j^*$:

$$\min U_j^* \quad \text{s.t.} \quad \sum_{a_i} R_j(a_i,a_j)x_{a_i} \le U_j^* \;\; \forall a_j;\quad x_{a_i}\ge 0;\quad \textstyle\sum x_{a_i}=1$$
[Eqs. 4.12–4.15]

Eq. 4.13 says no single action of $j$ beats $U_j^*$ — which implies no
*distribution* over $j$'s actions does either. In a minimax solution
$U_i^* = -U_j^*$.

Solvable in **polynomial time** (interior-point; simplex is exponential in the
worst case but fast in practice). This is one of the "direct methods" that
[[marl-agendas]] notes can beat MARL when the game is fully known — and it makes
minimax one of the few tractable cases in [[complexity-of-equilibria]].

### What an LP solver receives

$U_j^*$ is an optimization variable, not an input. For $m$ actions of agent
$i$, collect all variables into

$$z=(x_1,\ldots,x_m,U_j^*).$$

Then “minimize $U_j^*$” is the linear objective $c^Tz$ with
$c=(0,\ldots,0,1)$. Each opponent action $a_j$ contributes one inequality

$$\sum_{a_i}R_j(a_i,a_j)x_{a_i}-U_j^*\le 0,$$

which becomes one row of $A_{ub}z\le b_{ub}$. The probability constraint is
one row of $A_{eq}z=b_{eq}$, and the bounds enforce $x_{a_i}\ge0$ while leaving
$U_j^*$ unrestricted. For any fixed policy $x$, the inequalities force
$U_j^*$ to be at least the opponent's return for every pure response; minimizing
it therefore minimizes the opponent's best achievable response [Ch. 4.3.1,
Eqs. 4.12–4.15].

Geometrically, the constraints form a convex polytope and the linear objective
is lowered until it touches the feasible region. Simplex moves between its
vertices; interior-point methods approach the optimum through its interior.

## Related
[[nash-equilibrium]] · [[best-response]] · [[reward-structures]] ·
[[complexity-of-equilibria]] · [[solution-concepts]]
