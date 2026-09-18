---
title: Solution Concepts as Specifications
type: note
status: solid
sources: ["[[ch01-introduction]]", "[[ch04-solution-concepts]]", "[[ch05-marl-in-games]]", "[[ch06-foundational-algorithms]]"]
updated: 2026-09-18
---

# Solution concepts as specifications

A solution concept need not appear in every learning update. It can instead be
the **contract that says which learned joint policies count as solutions**. The
learning algorithm is then the search procedure; the solution concept defines
the target set and how the result will be judged. This is the computational
MARL agenda: use learning to compute solutions, potentially without knowing the
complete game in advance [Ch. 1.5].

“Need not” is important: post-training evaluation is only one possible role.
Chapter 6 introduces algorithms that put solution concepts directly inside the
learning process. The useful distinction is therefore not “training versus
solution concepts,” but **where the solution concept enters the pipeline**:

| Role | What the concept does | Chapter 6 example |
|---|---|---|
| Training mechanism | Selects policies and constructs learning targets from current joint-action values | Joint-action learning can use minimax, Nash, or correlated-equilibrium solutions in its TD updates [Ch. 6 introduction; §§6.1–6.2] |
| Training objective | Defines the quantity the dynamics try to improve or drive down | Regret-matching algorithms aim to minimise regret and achieve no-regret outcomes [Ch. 6 introduction; §6.5] |
| Post-training specification | Classifies or scores a learned policy without having shaped its updates | A Nash deviation test applied to the output of plain IQL [Ch. 4.4; Ch. 5.3.2] |

The same solution concept can occupy more than one role: an algorithm may use
an equilibrium operator during training and later be evaluated by its distance
from that equilibrium set. Conversely, plain IQL can accidentally reach a Nash
equilibrium even though Nash appears nowhere in its update.

For Nash equilibrium, the contract is mutual best response. A joint policy
$\pi$ is accepted only if no agent can improve by changing its policy alone
[Ch. 4.4, Eq. 4.16]. In an experiment this can be measured by agent $i$'s
unilateral-deviation gain

$$
\delta_i(\pi) = \max_{\pi_i'} U_i(\pi_i',\pi_{-i}) - U_i(\pi).
$$

$\delta_i=0$ for every agent certifies Nash; bounding every $\delta_i$ gives the
$\epsilon$-Nash relaxation [Ch. 4.4--4.5]. This test is different from merely
reporting the agents' mean returns; see
[[iql-evaluation-vs-solution-concepts]].

## What choosing Nash buys

1. **A definition of success.** It turns “learn something good” into the
   falsifiable claim that the output is stable against unilateral deviations.
2. **An evaluation metric.** Deviation gains let experiments compare policies
   and algorithms even when Nash was not their training objective.
3. **A target for guarantees.** A convergence claim can state whether the
   current policy, its empirical distribution, or its average return approaches
   the Nash solution set [Ch. 5.2, Eqs. 5.3--5.8].
4. **Constraints on algorithm choice and representation.** Some games have only
   mixed Nash equilibria, so an algorithm restricted to deterministic policies
   cannot represent the requested solution [Ch. 4.4]. General-sum Nash
   computation is also PPAD-complete, so the concept warns that the target may
   be computationally difficult [Ch. 4.11].
5. **A design primitive when desired.** Algorithms can explicitly calculate
   [[best-response|best responses]] or solve stage games while learning. In
   those cases Nash shapes the learning mechanism itself; this is not required
   for every algorithm [Ch. 4.2; Ch. 6.3.1--6.3.2].

If Nash affects neither algorithm selection, training, evaluation, theoretical
claims, nor deployment, then merely naming it buys nothing. “Nash is our
solution concept” is useful only when it changes what output will be accepted.

## The Prisoner's Dilemma case

The tabular [[iql-tabular|IQL]] exercise does not optimize a Nash residual or
compute best responses to explicit opponent policies. Defection nevertheless
strictly dominates cooperation, so correctly learned greedy values lead both
agents to defect. The result happens to be the game's unique Nash equilibrium;
Nash is being used **after learning to classify the outcome**, not inside the
Q-learning update.

That coincidence does not generalise. In games with multiple equilibria,
mixed-strategy equilibria, cycles, or inefficient equilibria, plain IQL can
fail to reach Nash or can select an undesirable Nash equilibrium [Ch. 5.3.2;
Ch. 5.4.2]. Moreover, Nash promises stability, not high welfare: mutual
defection in Prisoner's Dilemma is Nash even though mutual cooperation rewards
both agents more [Ch. 4.7].

## Related

[[solution-concepts]] · [[nash-equilibrium]] · [[best-response]] ·
[[convergence-types]] · [[marl-agendas]] · [[equilibrium-selection]]
