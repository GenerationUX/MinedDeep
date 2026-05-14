---
title: "Neuroscience-Inspired Artificial Intelligence"
tags:
  - peer-reviewed-paper
  - neuroscience-ai-bridge
  - deepmind-ascent
description: "Hassabis, Kumaran, Summerfield, and Botvinick (2017) published a landmark review in Neuron arguing that neuroscience can serve as a rich source of inspiration…"
date: 2017-01-01
---

# Neuroscience-Inspired Artificial Intelligence

**Type:** paper
**Slug:** neuroscience-inspired-artificial-intelligence--hassabis
**Sources:** neuroscience-inspired-artificial-intelligence--hassabis
**Last updated:** 2026-05-13

---

## Summary
Hassabis, Kumaran, Summerfield, and Botvinick (2017) published a landmark review in Neuron arguing that neuroscience can serve as a rich source of inspiration for AI, and conversely that AI research can help explain brain function. They identified specific areas where neuroscience has already contributed to AI (reinforcement learning, episodic memory, attention) and proposed promising areas for future cross-pollination (continual learning, imagination, social intelligence).

## Core content

**Core thesis:** The relationship between neuroscience and AI should be a two-way street — not just neuroscience informing AI, but AI frameworks providing new ways to understand the brain (paper--neuroscience-inspired-artificial-intelligence §Introduction).

**Areas where neuroscience informed AI (historical):**
- **Reinforcement learning:** TD learning derived from animal conditioning experiments (Rescorla-Wagner, Schultz dopamine recordings); now the foundation of DQN and policy gradient methods (paper--neuroscience-inspired-artificial-intelligence §RL).
- **Episodic memory:** Complementary learning systems theory (fast hippocampal + slow neocortical learning) inspired experience replay in deep RL (paper--neuroscience-inspired-artificial-intelligence §Memory).
- **Attention:** Biologically inspired attention mechanisms led to neural attention models that prefigured the Transformer architecture (paper--neuroscience-inspired-artificial-intelligence §Attention).

**Promising areas for future cross-pollination:**
- **Continual learning:** EWC and other approaches directly inspired by synaptic consolidation (paper--neuroscience-inspired-artificial-intelligence §Continual).
- **Imagination and planning:** The hippocampus as a simulator for future scenarios, connecting to model-based RL and imagination-based planning (paper--neuroscience-inspired-artificial-intelligence §Imagination).
- **Social intelligence:** Theory of mind, social hierarchy learning as inspiration for multi-agent AI (paper--neuroscience-inspired-artificial-intelligence §Social).
- **Efficient learning:** How the brain learns from few examples vs. millions — connecting to meta-learning and transfer learning (paper--neuroscience-inspired-artificial-intelligence §Efficiency).

**Reverse direction — AI informing neuroscience:**
- Deep RL provides formal frameworks for understanding dopamine signals beyond reward prediction errors (paper--neuroscience-inspired-artificial-intelligence §AI-to-Neuro).
- Neural network representations can be compared to neural recordings to test theories of cortical representation (paper--neuroscience-inspired-artificial-intelligence §AI-to-Neuro).

## Connections- **Theme:** [theme--neuroscience-AI-bridge](pages/theme--neuroscience-AI-bridge.md)
- **Project:** N/A (review article)
- **Collaborators:** Dharshan Kumaran, Christopher Summerfield, Matthew Botvinick
- **Era:** deepmind-ascent
- **Venue:** venue--Neuron
- **Format:** review-article (maps to paper-- prefix)
- **Synthesizes:** paper--overcoming-catastrophic-forgetting-in-neural-networks, paper--the-construction-system-of-the-brain, paper--human-level-control-through-deep-[theme--deep-RL](pages/theme--deep-RL.md), paper--computations-underlying-social-hierarchy-learning
- **Notable quote:** "The most productive approach may be to build on the areas where neuroscience and AI have already successfully intersected, while targeting new areas where the two fields can most fruitfully interact." (paper--neuroscience-inspired-artificial-intelligence §Conclusion)

## Honest Gaps
- Metadata lists Botvinick, Kumaran, Dolan, Dayan as co-authors; actual authors are Hassabis, Kumaran, Summerfield, Botvinick. Neither Dolan nor Dayan are authors, and Christopher Summerfield is missing.
- As a review article, it makes no original empirical claims — its value is in synthesis and framing.
- Some of the "neuroscience inspirations" are post-hoc justifications rather than genuine causal influences (e.g., experience replay was developed independently of CLS theory).
- The review is somewhat DeepMind-centric in its framing, focusing heavily on the lab's own work.
- Published in 2017, it predates Transformers, large language models, and the scaling paradigm — which have dramatically changed the neuroscience-AI relationship.