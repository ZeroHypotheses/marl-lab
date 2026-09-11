---
title: "Ch. 8 — Deep Reinforcement Learning"
type: source
status: stub
sources: ["MARL book, Ch. 8, pp. 183–218 (2nd printing)"]
updated: 2026-09-11
---

# Chapter 8 — Deep Reinforcement Learning

> **Skeleton only — this chapter has not been ingested.** Structure below is
> verified from the book's table of contents; the description is quoted from
> chapter 1's own overview. **Nothing here is a summary of the chapter's
> content**, because the chapter has not been read. Run `/marl-ingest 8` to fill it in.

The second of the two Part II introductions [Ch. 1.6]: single-agent deep RL, the basis for [[ch09-deep-marl]].

**pp. 183–218** · **43 numbered equations** · extracted text: `book/text/ch08.md` · slides: `upstream/slides/`

> 📕 errata — entries falling in this chapter (already applied in our 2nd
> printing, see [[errata]]; verify before transcribing):
>
> - p198: previously missing equations added after Eq 8.8 (unnumbered)
> - p203 (previously p202): in Eq 8.30 and 8.31, "u(h^...)" → "u^...", ":T" removed

## Structure

- **8.1** Deep Value Function Approximation — p184
  - **8.1.1** Deep Q-Learning—What Can Go Wrong? — p184
  - **8.1.2** Moving Target Problem — p187
  - **8.1.3** Breaking Correlations — p188
  - **8.1.4** Putting It All Together: Deep Q-Networks — p192
  - **8.1.5** Beyond Deep Q-Networks — p193
- **8.2** Policy Gradient Algorithms — p195
  - **8.2.1** Advantages of Learning a Policy — p195
  - **8.2.2** Policy Gradient Theorem — p197
  - **8.2.3** REINFORCE: Monte Carlo Policy Gradient — p200
  - **8.2.4** Actor-Critic Algorithms — p202
  - **8.2.5** A2C: Advantage Actor-Critic — p204
  - **8.2.6** PPO: Proximal Policy Optimization — p207
  - **8.2.7** Policy Gradient Algorithms in Practice — p209
  - **8.2.8** Concurrent Training of Policies — p210
- **8.3** Observations, States, and Histories in Practice — p215
- **8.4** Summary — p217

## Notes for ingest

- Background only — not MARL-specific.
- **Carries two of the three errata that touch equations** — check both before transcribing anything from §8.2.

## Related

[[ch01-introduction]] · [[errata]] · [[index|wiki index]]
