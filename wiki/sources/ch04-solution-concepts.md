---
title: "Ch. 4 — Solution Concepts for Games"
type: source
status: stub
sources: ["MARL book, Ch. 4, pp. 61–88 (2nd printing)"]
updated: 2026-09-11
---

# Chapter 4 — Solution Concepts for Games

> **Skeleton only — this chapter has not been ingested.** Structure below is
> verified from the book's table of contents; the description is quoted from
> chapter 1's own overview. **Nothing here is a summary of the chapter's
> content**, because the chapter has not been read. Run `/marl-ingest 4` to fill it in.

Introduces "a series of solution concepts that define what it means to solve these game models, that is, what it means for agents to act optimally" [Ch. 1.6], "including equilibrium-type solutions such as minimax, Nash, and correlated equilibrium, as well as other concepts such as Pareto optimality, welfare/fairness, and no-regret", with examples and "important conceptual limitations" [Part I divider].

**pp. 61–88** · **30 numbered equations** · extracted text: `book/text/ch04.md` · slides: `upstream/slides/`

> 📕 errata — entries falling in this chapter (already applied in our 2nd
> printing, see [[errata]]; verify before transcribing):
>
> - p80: added a missing index i in $U(\pi)$
> - p84: removed a clause on exponential time

## Structure

- **4.1** Joint Policy and Expected Return — p62
- **4.2** Best Response — p65
- **4.3** Minimax — p65
  - **4.3.1** Minimax Solution via Linear Programming — p67
- **4.4** Nash Equilibrium — p68
- **4.5** ϵ-Nash Equilibrium — p70
- **4.6** (Coarse) Correlated Equilibrium — p71
  - **4.6.1** Correlated Equilibrium via Linear Programming — p74
- **4.7** Conceptual Limitations of Equilibrium Solutions — p75
- **4.8** Pareto Optimality — p76
- **4.9** Social Welfare and Fairness — p78
- **4.10** No-Regret — p81
- **4.11** The Complexity of Computing Equilibria — p83
  - **4.11.1** PPAD Complexity Class — p84
  - **4.11.2** Computing ϵ-Nash Equilibrium Is PPAD-Complete — p86
- **4.12** Summary — p87

## Notes for ingest

- "Together, a game model and a solution concept define a learning problem in multi-agent reinforcement learning" [Part I divider].
- Fills [[solution-concepts]]. §4.7 on conceptual limitations is flagged as notable.
- §4.3.1 and §4.6.1 hold the linear-programming methods that [[marl-agendas]] contrasts with MARL.

## Related

[[ch01-introduction]] · [[errata]] · [[index|wiki index]]
