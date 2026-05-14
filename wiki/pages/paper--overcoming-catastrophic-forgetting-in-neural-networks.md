---
title: "Overcoming Catastrophic Forgetting in Neural Networks"
tags:
  - peer-reviewed-paper
  - reinforcement-learning
  - deep-rl
  - deepmind-ascent
  - DeepMind-general
description: "Kirkpatrick, Pascanu, Rabinowitz, Veness, Desjardins, Rusu, Milan, Quan, Ramalho, Grabska-Barwińska, Hassabis, Clopath, Kumaran, and Hadsell (2017) introduced…"
date: 2017-01-01
---

# Overcoming Catastrophic Forgetting in Neural Networks

**Type:** paper
**Slug:** overcoming-catastrophic-forgetting-in-neural-networks--hassabis
**Sources:** overcoming-catastrophic-forgetting-in-neural-networks--hassabis
**Last updated:** 2026-05-13

---

## Summary
Kirkpatrick, Pascanu, Rabinowitz, Veness, Desjardins, Rusu, Milan, Quan, Ramalho, Grabska-Barwińska, Hassabis, Clopath, Kumaran, and Hadsell (2017) introduced Elastic Weight Consolidation (EWC), an algorithm that allows neural networks to learn sequentially without catastrophic forgetting. Inspired by synaptic consolidation in the mammalian brain, EWC constrains important weights for previously learned tasks from changing excessively, achieving near-sequential performance on Permuted MNIST, Atari games, and a reinforcement learning maze task.

## Core content

**Problem:** Standard neural networks catastrophically forget previously learned tasks when trained on new ones — weights are overwritten with no mechanism to protect old knowledge (paper--overcoming-catastrophic-forgetting-in-neural-networks §Introduction).

**Biological inspiration:** When mice learn new skills, only a subset of dendritic spines are modified; previously strengthened spines are protected (paper--overcoming-catastrophic-forgetting-in-neural-networks §Introduction). EWC formalizes this as a Bayesian approach: after learning task A, the posterior over weights serves as a prior for task B (paper--overcoming-catastrophic-forgetting-in-neural-networks §Results).

**Algorithm:** Compute the Fisher information matrix F (diagonal approximation) for each parameter after learning a task — F measures how important each weight is for that task's performance. When learning a new task, add a regularization term Σ F_i (θ_i − θ*_i)² to the loss, penalizing changes to important weights (paper--overcoming-catastrophic-forgetting-in-neural-networks §Results).

**Key results:**
- **Permuted MNIST:** EWC achieved ~92% accuracy on task 1 after learning 10 sequential permutations, compared to ~62% for standard SGD and ~90% for a joint training upper bound (paper--overcoming-catastrophic-forgetting-in-neural-networks §Results).
- **Atari:** EWC trained on two games sequentially retained ~50–90% of original performance on the first game (depending on game pair), while SGD retained ~0–20% (paper--overcoming-catastrophic-forgetting-in-neural-networks §Results).
- **RL maze task:** EWC learned multiple goals in the same maze sequentially without forgetting previous goals; SGD forgot almost completely (paper--overcoming-catastrophic-forgetting-in-neural-networks §Results).
- Performance degraded gracefully as more tasks were added, but EWC consistently outperformed SGD and L2 regularization baselines (paper--overcoming-catastrophic-forgetting-in-neural-networks §Results).

**Limitations acknowledged:** EWC's diagonal Fisher approximation cannot capture parameter correlations; extending to full Fisher is computationally prohibitive. Performance degrades with many sequential tasks as the constraint terms accumulate (paper--overcoming-catastrophic-forgetting-in-neural-networks §Discussion).

## Connections- **Theme:** reinforcement-learning, [theme--deep-RL](pages/theme--deep-RL.md), continual-learning
- **Project:** DeepMind-general
- **Collaborators:** James Kirkpatrick (first author), Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A. Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwińska, Claudia Clopath (Imperial College), Dharshan Kumaran, Raia Hadsell (joint senior)
- **Era:** deepmind-ascent
- **Venue:** venue--PNAS
- **Influences:** McClelland et al. (1995) complementary learning systems; Losonczy & Magee (2006) dendritic spine consolidation

## Honest Gaps
- Metadata lists only 4 co-authors; the actual paper has 14 authors.
- Metadata theme lacks "continual-learning" — the paper's primary contribution is to continual/sequential learning, not RL per se.
- The diagonal Fisher approximation is a significant simplification; later work (Online EWC, SI, MAS) addressed this limitation.
- Permuted MNIST is a weak benchmark — tasks are too similar for meaningful transfer, and later benchmarks (Split CIFAR, Split Tiny ImageNet) revealed more substantial limitations.
- EWC cannot add new output neurons; task identity must be provided at test time (an "aware" continual learning setting).
- The biological analogy, while inspiring, is loose — the Fisher information matrix has no direct neural correlate.