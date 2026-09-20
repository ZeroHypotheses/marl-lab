---
title: "Ch. 6 — Multi-Agent Reinforcement Learning: Foundational Algorithms"
type: source
status: solid
sources: ["MARL book, Ch. 6, pp. 115–160 (2nd printing)"]
updated: 2026-09-20
---

# Chapter 6 — Multi-Agent Reinforcement Learning: Foundational Algorithms

Chapter 6 turns the solution concepts of Chapter 4 into learning operators. Its
central question is not merely whether a learned policy is an equilibrium, but
**where game-theoretic reasoning enters the update itself**. The chapter moves
from model-based value iteration, through value-based and model-based learning,
to direct policy and regret dynamics [Ch. 6].

## Map of the chapter

| Section | Family | Main idea |
|---|---|---|
| §6.1 | Dynamic programming | Apply a game-value operator to the continuation-payoff game at every state. |
| §6.2 | [[joint-action-learning]] | Learn joint-action values and solve the induced state game inside the TD target. |
| §6.3 | [[agent-modelling]] | Predict the other agents, then best-respond to those predictions. |
| §6.4 | Policy-based learning | Move policies directly along reward gradients; alter the learning dynamics to improve convergence. |
| §6.5 | [[regret-matching]] | Choose actions in proportion to positive counterfactual regret. |

These are genuinely different uses of solution concepts. Minimax Q-learning
puts minimax in the bootstrap target; fictitious play learns an opponent model
and repeatedly best-responds; WoLF changes the update speed depending on whether
the agent is winning; regret matching targets vanishing regret rather than a
single pointwise policy [Ch. 6.2–6.5].

## §6.1 — Shapley value iteration

For a finite discounted stochastic game with known transition function $T$ and
rewards $R_i$, construct at each state $s$ a normal-form continuation game:

$$
M_{s,i}(a)=\sum_{s'}T(s'\mid s,a)
\left[R_i(s,a,s')+\gamma V_i(s')\right].
$$

Here $a$ is a joint action, $M_{s,i}$ is agent $i$'s payoff matrix at $s$, and
$V_i$ is its current state-value estimate [Eq. 6.3]. The update is

$$V_i(s)\leftarrow \operatorname{Value}_i(M_{s,1},\ldots,M_{s,n}),$$

where `Value` is supplied by a solution concept [Eq. 6.4]. In a two-agent
zero-sum game it is the [[minimax]] value. Transition averaging and the minimax
value operator are non-expansive, while discounting multiplies differences by
$\gamma<1$; therefore the complete update is a $\gamma$-contraction and has a
unique fixed-point value [Eq. 6.8; Ch. 6.1]. See [[dynamic-programming]].

The guarantee is narrow but clean: two agents, zero-sum rewards, finite state
and action spaces, known model, and discounting [Ch. 6.1].

## §6.2 — Joint-action learning

[[joint-action-learning]] replaces the known model with sampled experience. It
learns $Q_i(s,a)$ for joint actions and treats each state as a normal-form game
$\Gamma_s$ whose payoffs are those Q-values [Eqs. 6.9–6.10]. A solution concept
then provides both behaviour in $s$ and the value used in the next-state TD
target [Eq. 6.11].

- [[minimax-q-learning]] has a zero-sum convergence result under infinite
  sampling and standard learning-rate conditions, but its worst-case policy may
  fail to exploit a weak opponent [Ch. 6.2.1].
- [[nash-q-learning]] targets Nash equilibria in general-sum games, but its
  guarantee requires restrictive structure in every encountered state game and
  consistent equilibrium selection [Ch. 6.2.2].
- [[correlated-q-learning]] uses correlated equilibria, which can be computed
  by linear programming, but requires a correlation mechanism and still faces
  selection among multiple equilibria [Ch. 6.2.3].

All three versions make strong information assumptions: each learner observes
the joint action and all agents' rewards so it can maintain all agents' Q-tables
[Algorithm 7]. More fundamentally, a table of $Q_i(s,a)$ need not contain enough
information to identify a unique stationary probabilistic equilibrium. The
book's turn-taking example requires mixing, while a deterministic selection
from identical state games cannot coordinate which mixed equilibrium to use
[Ch. 6.2.4].

## §6.3 — Agent modelling

Instead of imposing a normative equilibrium response, an agent can estimate
the other agents' policies and choose a [[best-response]] to the estimates
[Eq. 6.13].

- [[fictitious-play]] models each opponent by its empirical action frequencies
  and best-responds to those frequencies [Eqs. 6.14–6.15].
- [[jal-agent-modelling]] makes those frequency models state-dependent and
  combines them with a learned personal joint-action Q-function
  [Eqs. 6.16–6.17; Algorithm 8]. It needs joint-action observations, but unlike
  Algorithm 7 it does not require the other agents' rewards.
- Bayesian modelling maintains a posterior over possible opponent models.
  Value-of-information planning accounts for both physical state change and
  the way observations update that posterior [Eqs. 6.18–6.20]. Its conclusions
  depend on the true opponent being represented in, or suitably covered by,
  the model space [Ch. 6.3.3].

The repeated Prisoner's Dilemma example shows why information itself has value:
an agent may cooperate temporarily to distinguish a cooperative opponent from
an always-defecting one. With a finite horizon, the incentive changes near the
end because information can no longer pay off later [Ch. 6.3.3].

## §6.4 — Policy-based learning

Directly parameterised stochastic policies can represent mixed equilibria that
deterministic best-response actions cannot [Ch. 6.4].

- Infinitesimal gradient ascent (IGA) follows the expected-reward gradient in
  two-agent, two-action normal-form games [Eqs. 6.29–6.32]. Its policies may
  cycle, although convergent policies are Nash equilibria and average rewards
  converge to Nash-equilibrium rewards [Ch. 6.4.1–6.4.2].
- Win or Learn Fast (WoLF) changes the step size: learn slowly while winning and
  quickly while losing. WoLF-IGA converges in the restricted two-agent,
  two-action setting under infinitesimal analysis [Ch. 6.4.3].
- [[wolf-policy-hill-climbing]] combines that idea with Q-learning, an average
  policy, and policy hill climbing in stochastic games [Algorithm 9].
- [[generalized-infinitesimal-gradient-ascent]] extends projected gradient
  updates to more agents and actions. With a diminishing step size it has
  sublinear regret, so the empirical joint-action distribution approaches the
  set of coarse correlated equilibria [Ch. 6.4.5].

## §6.5 — No-regret learning

[[regret-matching]] turns positive counterfactual regret into action
probabilities. Unconditional regret asks whether one fixed replacement action
would have done better; conditional regret asks whether occurrences of one
action should have been replaced by another [Eqs. 6.53–6.58].

The distinction determines the limiting solution set: vanishing unconditional
(external) regret yields coarse correlated equilibrium, while vanishing
conditional (internal) regret yields correlated equilibrium [Ch. 6.5.2]. This
is convergence of the **empirical joint-action distribution**, not necessarily
of the policies used on each round. In Rock-Paper-Scissors, those policies may
continue moving while the empirical frequencies converge [Ch. 6.5.2]. See
[[convergence-types]] and [[no-regret]].

## What the chapter establishes

1. A solution concept can be an internal learning operator, not just a
   post-training test [Ch. 6.1–6.5].
2. Stronger game-solving machinery generally demands stronger observability or
   structural assumptions [Algorithms 6–9].
3. “Convergence” must name its object: values, policies, average rewards, regret,
   or empirical distributions [Ch. 6.2–6.5].
4. General-sum games add an equilibrium-selection problem that does not occur
   for the unique minimax value of a zero-sum game [Ch. 6.2.1–6.2.3].
5. Foundational algorithms isolate the ideas later reused in deep MARL; neural
   networks change representation and scale, not these underlying strategic
   questions [Ch. 6.6].

## Assumptions to keep visible

- Algorithm 6 assumes a known model; Algorithms 7–9 learn from samples
  [Algorithms 6–9].
- JAL-GT and JAL-AM observe joint actions; JAL-GT additionally observes all
  rewards [Algorithms 7–8].
- The strongest convergence results apply to restricted game classes, often
  two-agent zero-sum or two-agent/two-action normal-form games [Ch. 6.1,
  6.2.1, 6.4.2–6.4.3].
- No-regret guarantees do not require assumptions about how the other agents
  choose actions, but they guarantee empirical-distribution convergence rather
  than pointwise policy convergence [Ch. 6.4.5, 6.5.2].

## Related

[[ch05-marl-in-games]] · [[ch09-deep-marl]] · [[solution-concepts]] ·
[[stochastic-games]] · [[temporal-difference-learning]] · [[convergence-types]] ·
[[bcn-summer-school]]
