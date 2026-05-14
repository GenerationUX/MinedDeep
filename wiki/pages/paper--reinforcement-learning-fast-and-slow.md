---
title: "Reinforcement Learning, Fast and Slow"
tags:
  - peer-reviewed-paper
  - reinforcement-learning
  - neuroscience-ai-bridge
  - complementary-learning-systems
  - alphafold-era
description: "Botvinick, Ritter, Wang, Kurth-Nelson, Blundell, and Hassabis (2020) published a review in Neuron proposing that the brain's RL system comprises parallel…"
date: 2020-01-01
---

# Reinforcement Learning, Fast and Slow

**Type:** paper
**Slug:** reinforcement-learning-fast-and-slow--hassabis
**Sources:** reinforcement-learning-fast-and-slow--hassabis
**Last updated:** 2026-05-13

---

## Summary
Botvinick, Ritter, Wang, Kurth-Nelson, Blundell, and Hassabis (2020) published a review in Neuron proposing that the brain's RL system comprises parallel "fast" and "slow" learning processes, analogous to Kahneman's System 1 and System 2. The fast system (dorsolateral striatum, model-free) learns habits from cached values; the slow system (PFC-hippocampal, model-based) uses cognitive maps for deliberative planning. They argue that deep RL's successes and limitations mirror this dichotomy, and that bridging the two systems is key to more capable AI.

## Core content

**Core analogy:** Just as Kahneman distinguished fast intuitive thinking (System 1) from slow deliberative thinking (System 2), the brain's RL system operates at two timescales (paper--reinforcement-learning-fast-and-slow §Introduction).

**Fast RL (System 1):**
- Implemented in dorsolateral striatum
- Model-free: cached state-action values updated by reward prediction errors
- Fast learning, computationally cheap, but inflexible
- Analogous to DQN and policy gradient methods in deep RL (paper--reinforcement-learning-fast-and-slow §Fast)

**Slow RL (System 2):**
- Implemented in PFC-hippocampal circuit
- Model-based: uses a learned world model to plan via search or simulation
- Slow learning, computationally expensive, but flexible and generalizable
- Analogous to model-based RL, MBPO, and imagination-based methods (paper--reinforcement-learning-fast-and-slow §Slow)

**Key arguments:**
- Current deep RL is overwhelmingly "fast" — most breakthroughs (DQN, AlphaGo, AlphaStar) rely on model-free methods with enormous data (paper--reinforcement-learning-fast-and-slow §Gap).
- The gap between human and AI learning efficiency may be explained by humans' ability to leverage "slow" model-based learning (paper--reinforcement-learning-fast-and-slow §Gap).
- Promising directions: model-based RL, episodic control, meta-learning, and memory-augmented networks as implementations of "slow" RL (paper--reinforcement-learning-fast-and-slow §Bridging).

## Connections- **Theme:** [theme--deep-RL](pages/theme--deep-RL.md), [theme--neuroscience-AI-bridge](pages/theme--neuroscience-AI-bridge.md), complementary-learning-systems
- **Project:** N/A (review article)
- **Collaborators:** Matthew Botvinick (first author), Sam Ritter, Jane X. Wang, Zeb Kurth-Nelson, Charles Blundell
- **Era:** alphafold-era
- **Venue:** venue--Neuron
- **Format:** review-article (maps to paper-- prefix)
- **Synthesizes:** paper--prefrontal-cortex-as-a-meta-[theme--deep-RL](pages/theme--deep-RL.md)-system, paper--a-distributional-code-for-value-in-dopamine-based-[theme--deep-RL](pages/theme--deep-RL.md), paper--human-level-control-through-deep-[theme--deep-RL](pages/theme--deep-RL.md)
- **Related:** paper--what-learning-systems-do-intelligent-agents-need-complementary-learning-systems-theory-updated — both propose multi-system learning architectures

## Honest Gaps
- Metadata lists Kurth-Nelson, Blundell, Botvinick, Dolan as co-authors; actual authors are Botvinick, Ritter, Wang, Kurth-Nelson, Blundell, Hassabis. Raymond Dolan is not an author; Sam Ritter, Jane X. Wang, and Hassabis are missing.
- As a review article, it makes no original empirical claims.
- The fast/slow dichotomy, while heuristically useful, oversimplifies the diversity of learning mechanisms in the brain.
- The analogy between Kahneman's Systems 1/2 and model-free/model-based RL is imperfect — the mapping is not one-to-one.
- Published in 2020, it predates major advances in model-based RL (e.g., Dreamer, MuZero) that partially address the "slow RL" gap.