---
title: "Ch. 9 — Multi-Agent Deep Reinforcement Learning"
type: source
status: stub
sources: ["MARL book, Ch. 9, pp. 219–304 (2nd printing)"]
updated: 2026-09-11
---

# Chapter 9 — Multi-Agent Deep Reinforcement Learning

> **Skeleton only — this chapter has not been ingested.** Structure below is
> verified from the book's table of contents; the description is quoted from
> chapter 1's own overview. **Nothing here is a summary of the chapter's
> content**, because the chapter has not been read. Run `/marl-ingest 9` to fill it in.

Introduces "several of the most important MARL algorithms developed in recent years, including ideas such as centralized training with decentralized execution, value decomposition, parameter sharing, and population-based training" [Ch. 1.6].

**pp. 219–304** · **98 numbered equations** · extracted text: `book/text/ch09.md` · slides: `upstream/slides/`

> 📕 errata — entries falling in this chapter (already applied in our 2nd
> printing, see [[errata]]; verify before transcribing):
>
> - p233: in Eq 9.10, in y_i, "t" → "t+1" for h and z
> - p285: Figure 9.25a, "InitialiseNode" → "InitializeNode"
> - p294: Figure 9.28 caption, removed "blue bars"

## Structure

- **9.1** Training and Execution Modes — p220
  - **9.1.1** Centralized Training and Execution — p220
  - **9.1.2** Decentralized Training and Execution — p221
  - **9.1.3** Centralized Training with Decentralized Execution — p222
- **9.2** Notation for Multi-Agent Deep Reinforcement Learning — p222
- **9.3** Independent Learning — p223
  - **9.3.1** Independent Value-Based Learning — p224
- **9.4** Multi-Agent Policy Gradient Algorithms — p230
  - **9.4.1** Multi-Agent Policy Gradient Theorem — p231
  - **9.4.2** Centralized Critics — p232
  - **9.4.3** Centralized Action-Value Critics — p236
  - **9.4.4** Counterfactual Action-Value Estimation — p237
  - **9.4.5** Equilibrium Selection with Centralized Action-Value Critics — p239
- **9.5** Value Decomposition in Common-Reward Games — p242
  - **9.5.1** Individual-Global-Max Property — p244
  - **9.5.2** Linear Value Decomposition — p246
  - **9.5.3** Monotonic Value Decomposition — p249
  - **9.5.4** Value Decomposition in Practice — p255
  - **9.5.5** Beyond Monotonic Value Decomposition — p261
- **9.6** Agent Modeling with Neural Networks — p266
  - **9.6.1** Joint-Action Learning with Deep Agent Models — p267
  - **9.6.2** Learning Representations of Agent Policies — p271
- **9.7** Environments with Homogeneous Agents — p274
  - **9.7.1** Parameter Sharing — p276
  - **9.7.2** Experience Sharing — p278
- **9.8** Policy Self-Play in Zero-Sum Games — p281
  - **9.8.1** Monte Carlo Tree Search — p283
  - **9.8.2** Self-Play MCTS — p286
  - **9.8.3** Self-Play MCTS with Deep Neural Networks: AlphaZero — p288
- **9.9** Population-Based Training — p290
  - **9.9.1** Policy Space Response Oracles — p292
  - **9.9.2** Convergence of PSRO — p295
  - **9.9.3** Grandmaster Level in StarCraft II: AlphaStar — p298
- **9.10** Summary — p301

## Notes for ingest

- **The core chapter of the book** — 86 pages, 98 numbered equations, more than double any other.
- Fills [[centralised-training-decentralised-execution]] (§9.1), [[value-decomposition]] (§9.5), [[parameter-sharing]] (§9.7.1), [[self-play]] (§9.8).
- Algorithm pages this chapter should ground: [[idqn]], [[ia2c]], [[ippo]], [[maa2c]], [[mappo]], [[vdn]], [[qmix]].
- §9.5.1 defines the Individual-Global-Max (IGM) property — the condition [[value-decomposition]] rests on.
- Worth splitting across several ingest sessions rather than one.

## Related

[[ch01-introduction]] · [[errata]] · [[index|wiki index]]
