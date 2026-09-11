---
title: "Ch. 6 — Multi-Agent Reinforcement Learning: Foundational Algorithms"
type: source
status: stub
sources: ["MARL book, Ch. 6, pp. 115–160 (2nd printing)"]
updated: 2026-09-11
---

# Chapter 6 — Multi-Agent Reinforcement Learning: Foundational Algorithms

> **Skeleton only — this chapter has not been ingested.** Structure below is
> verified from the book's table of contents; the description is quoted from
> chapter 1's own overview. **Nothing here is a summary of the chapter's
> content**, because the chapter has not been read. Run `/marl-ingest 6` to fill it in.

Introduces "different classes of foundational algorithms developed in MARL research and discusses their learning properties" [Ch. 1.6], going "beyond the basic approaches introduced in the prior chapter", with "their convergence properties" [Part I divider].

**pp. 115–160** · **64 numbered equations** · extracted text: `book/text/ch06.md` · slides: `upstream/slides/`

## Structure

- **6.1** Dynamic Programming for Games: Value Iteration — p116
- **6.2** Temporal-Difference Learning for Games: Joint-Action Learning — p118
  - **6.2.1** Minimax Q-Learning — p121
  - **6.2.2** Nash Q-Learning — p123
  - **6.2.3** Correlated Q-Learning — p124
  - **6.2.4** Limitations of Joint-Action Learning — p125
- **6.3** Agent Modeling — p127
  - **6.3.1** Fictitious Play — p128
  - **6.3.2** Joint-Action Learning with Agent Modeling — p131
  - **6.3.3** Bayesian Learning and Value of Information — p134
- **6.4** Policy-Based Learning — p140
  - **6.4.1** Gradient Ascent in Expected Reward — p141
  - **6.4.2** Learning Dynamics of Infinitesimal Gradient Ascent — p142
  - **6.4.3** Win or Learn Fast — p145
  - **6.4.4** Win or Learn Fast with Policy Hill Climbing — p147
  - **6.4.5** Generalized Infinitesimal Gradient Ascent — p149
- **6.5** No-Regret Learning — p151
  - **6.5.1** Unconditional and Conditional Regret Matching — p151
  - **6.5.2** Convergence of Regret Matching — p153
- **6.6** Summary — p156

## Notes for ingest

- The tabular/foundational counterpart to the deep algorithms of [[ch09-deep-marl]].
- Named algorithms per the TOC: Minimax Q-Learning, Nash Q-Learning, Correlated Q-Learning, Fictitious Play, JAL-AM, WoLF, WoLF-PHC, GIGA, Regret Matching.
- Related to the tabular exercise: `upstream/exercises/tabular_marl/iql.py` → [[iql-tabular]].

## Related

[[ch01-introduction]] · [[errata]] · [[index|wiki index]]
