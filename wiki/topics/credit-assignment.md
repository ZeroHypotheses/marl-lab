---
title: Multi-Agent Credit Assignment
type: topic
status: solid
sources: ["[[ch01-introduction]]", "[[ch05-marl-in-games]]"]
updated: 2026-09-11
---

# Multi-Agent Credit Assignment

**Temporal** credit assignment asks *which past actions* produced a reward.
**Multi-agent** credit assignment adds: *whose* actions [Ch. 5.4.3]. The book
keeps the two terms distinct.

## The illustration [Fig. 5.7]

Three agents in [[level-based-foraging]] all choose `collect` and all receive
+1. To us it's obvious the left agent contributed nothing (its level was too
low), and that the reward came from the **combined** action of the two on the
right — not from either individually.

But an agent that sees only the actions, the states before and after, and the
+1 "requires a detailed understanding of the world dynamics, such as the
relationship between agent/item locations and levels, and how the collect action
depends on these."

**Compounded by time:** not only did the left agent's `collect` not contribute,
neither did the move actions that brought it there.

## ⚠️ Correcting a common framing

Chapter 1 introduces this through a common-reward example, which invites the
conclusion that it *is* a common-reward problem. Chapter 5 is explicit that it
isn't:

> It is "especially prominent in common-reward settings... since each reward is
> applied indiscriminately to each agent". **"However, it is important to note
> that the problem of multi-agent credit assignment exists more generally and
> does not depend on common rewards."** [Ch. 5.4.3]

Change the example so only the two right-hand agents get +1 and the left gets 0:
those two **still** have to work out that the left agent contributed nothing to
*their* reward. → [[reward-structures]]

The specific common-reward failure mode is worth naming: an agent's action can
be "repeatedly reinforced when receiving a positive reward to which the agent's
action made no contribution."

## Joint-action values as the lever

The book's Rock-Paper-Scissors example [Ch. 5.4.3]: agent 1 plays R against S
(+1), then R against P (−1). With $Q(s,a_1)$ over its **own** actions only — as
in [[independent-learning]] — the average value of R looks like **0**, because
$Q$ cannot represent agent 2's influence. A **joint-action** value
$Q_1(s,a_1,a_2)$ — as in [[central-learning]] — assigns different values to
$(R,S)$ and $(R,P)$ and gets it right.

This is why joint-action learning (ch. 6) exists.

## Three families of solution

1. **Joint-action values** — [[central-learning]], joint-action learning (§6.2).
2. **Difference rewards** (Wolpert & Tumer 2002; Tumer & Agogino 2007) — the
   counterfactual "what would I have received if agent $j$ had done X instead of
   Y?", with X a default action. **Caveat from the book:** "it is generally
   unclear whether such a default action exists for a given environment and what
   it should be."
3. **Learned value decomposition** into individual contributions (Rashid et al.
   2018; Sunehag et al. 2018; Son et al. 2019; Zhou, Liu, et al. 2020) — i.e.
   [[vdn]], [[qmix]] and relatives → [[value-decomposition]], §9.5.

> This answers the open question logged from ch. 1.4 ("which chapter 9 methods
> implement counterfactual reasoning?"): §9.4.4 Counterfactual Action-Value
> Estimation, and the §9.5 decomposition family. Confirm when ingesting
> [[ch09-deep-marl]].

## Related
[[value-decomposition]] · [[central-learning]] · [[reward-structures]] ·
[[scaling-in-number-of-agents]] · [[non-stationarity]]
