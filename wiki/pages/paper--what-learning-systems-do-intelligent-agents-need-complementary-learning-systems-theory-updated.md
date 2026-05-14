---
title: "What Learning Systems Do Intelligent Agents Need? Complementary Learning Systems Theory Updated"
tags:
  - peer-reviewed-paper
  - neuroscience-ai-bridge
  - complementary-learning-systems
  - deepmind-ascent
description: "Kumaran, Hassabis, and McClelland (2016) published an updated review of Complementary Learning Systems (CLS) theory in Trends in Cognitive Sciences, extending…"
date: 2016-01-01
---

# What Learning Systems Do Intelligent Agents Need? Complementary Learning Systems Theory Updated

**Type:** paper
**Slug:** what-learning-systems-do-intelligent-agents-need-complementary-learning-systems-theory-updated--hassabis
**Sources:** what-learning-systems-do-intelligent-agents-need-complementary-learning-systems-theory-updated--hassabis
**Last updated:** 2026-05-13

---

## Summary
Kumaran, Hassabis, and McClelland (2016) published an updated review of Complementary Learning Systems (CLS) theory in Trends in Cognitive Sciences, extending the original framework beyond episodic memory to address the full range of learning systems an intelligent agent needs. They argue that CLS theory's core insight — the need for complementary fast and slow learning systems — applies not just to memory but to perception, language, motor control, and reinforcement learning, with direct implications for AI system design.

## Core content

**Original CLS theory:** McClelland, McNaughton, and O'Reilly (1995) proposed that the brain has two complementary learning systems: a fast-learning hippocampal system that rapidly acquires specific memories (but is prone to interference), and a slow-learning neocortical system that gradually extracts generalized knowledge (paper--what-learning-systems-do-intelligent-agents-need-complementary-learning-systems-theory-updated §Introduction).

**Key extensions in this update:**
- **Beyond memory:** The fast/slow complementary structure applies to all domains of learning — not just episodic memory but also semantic knowledge, skill acquisition, language, and social learning (paper--what-learning-systems-do-intelligent-agents-need-complementary-learning-systems-theory-updated §Extensions).
- **Generative replay:** The hippocampus can "replay" memories to train the neocortex without catastrophic interference — a mechanism directly implemented in deep RL's experience replay (paper--what-learning-systems-do-intelligent-agents-need-complementary-learning-systems-theory-updated §Replay).
- **Systematicity:** Slow learning enables compositional, systematic generalization that fast learning alone cannot achieve (paper--what-learning-systems-do-intelligent-agents-need-complementary-learning-systems-theory-updated §Systematicity).
- **Meta-learning:** The slow system can learn to configure the fast system, connecting CLS to meta-learning (paper--what-learning-systems-do-intelligent-agents-need-complementary-learning-systems-theory-updated §Meta-learning).

**Implications for AI:** Current deep learning systems lack the fast/slow complementary structure. Adding a fast episodic-like system (e.g., memory-augmented networks) alongside slow gradient descent could improve sample efficiency, continual learning, and systematic generalization (paper--what-learning-systems-do-intelligent-agents-need-complementary-learning-systems-theory-updated §AI).

## Connections- **Theme:** [theme--neuroscience-AI-bridge](pages/theme--neuroscience-AI-bridge.md), complementary-learning-systems
- **Project:** N/A (review article)
- **Collaborators:** Dharshan Kumaran (first author), James L. McClelland (Stanford)
- **Era:** deepmind-ascent
- **Venue:** venue--Trends-in-Cognitive-Sciences
- **Format:** review-article (maps to paper-- prefix)
- **Extends:** McClelland, McNaughton & O'Reilly (1995) — the original CLS paper
- **Related:** paper--overcoming-catastrophic-forgetting-in-neural-networks — EWC as an implementation of CLS-inspired protection
- **Related:** paper--[theme--deep-RL](pages/theme--deep-RL.md)-fast-and-slow — dual-process RL as CLS applied to decision-making

## Honest Gaps
- Metadata lists Botvinick, Kumaran, Dolan, Dayan as co-authors; actual authors are Kumaran, Hassabis, McClelland. Three of the four listed authors are wrong — this is a complete metadata failure.
- As a review/theory article, it makes no original empirical claims.
- The extensions of CLS beyond memory are largely speculative — they frame known phenomena in CLS terms without providing new evidence.
- The AI implications are discussed at a high level without concrete architectural proposals.
- The review is somewhat self-referential, positioning DeepMind's work as the natural continuation of CLS theory.