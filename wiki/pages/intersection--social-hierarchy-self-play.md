---
title: "Social Hierarchy × Self-Play"
tags:
  - intersection
date: 2026-05-14
---

# Social Hierarchy × Self-Play

**Type:** intersection
**Slug:** intersection--social-hierarchy-self-play
**Parents:** paper--computations-underlying-social-hierarchy-learning, claim--self-play-sufficiency
**Last updated:** 2026-05-14
**Epistemic status:** Grounded

---

## The intersection
Social hierarchy learning (2016) shows humans use Bayesian inference to learn rank structures, with amygdala and hippocampus encoding general hierarchy knowledge and mPFC selectively updating self-relevant rank information. Self-play (2017) generates superhuman strategies through competitive interaction with an improving opponent. Combined: **multi-agent self-play should produce internal rank representations of opponents — treating some as "higher status" (play conservatively) and others as "lower status" (play aggressively).**

The social hierarchy paper provides the neuroscience of rank representation. Self-play provides the training regime where rank is constantly renegotiated. In AlphaStar (2019), agents play against many opponents in a league system — but nobody checked whether the agents develop internal representations of opponent strength analogous to the social hierarchy representations found in the human brain.

## What the corpus implies
The social hierarchy paper (Kumaran, Banino, Blundell, Hassabis, Dayan, Neuron 2016) and the self-play papers (2017–2018) share DeepMind authorship and the Hassabis connection, but never connect. The social hierarchy paper frames rank learning as a Bayesian inference problem in a static hierarchy. Self-play creates a *dynamic* hierarchy where ranks change as agents improve. The intersection asks whether the same neural/computational mechanisms that track static social rank can track dynamic competitive rank.

The social hierarchy paper's key neural finding — amygdala/hippocampus for general rank, mPFC for self-relevant rank — maps onto a potential AI architecture: a general opponent model (amygdala/hippocampus analogue) plus a self-relevant strategy adjuster (mPFC analogue). No game-playing AI system uses this decomposition, despite it being how humans handle competitive hierarchies.

## What's missing
- No paper analyses whether self-play agents develop internal rank representations of their opponents.
- No paper applies the Bayesian hierarchy model from the social paper to multi-agent AI systems.
- No paper asks whether the amygdala/hippocampus vs. mPFC dissociation (general rank vs. self-relevant rank) has an analogue in multi-agent AI architectures.
- The social hierarchy paper studies small, static groups (~5 people) — self-play leagues provide large, dynamic groups where hierarchy is constantly renegotiated, a domain the neuroscience hasn't explored.

## Generative potential
**Empirical test:** Train a self-play agent in a league with many opponents. Use representational similarity analysis to check whether the agent's internal representations encode opponent strength in a rank-like structure — a one-dimensional ordering that predicts the agent's strategy against each opponent. If so, the agent has spontaneously discovered a social hierarchy representation.

**Architecture — "Hierarchical self-play":** Explicitly decompose the policy into a general opponent model (encoding rank/strength) and a self-relevant strategy adjuster (conditioned on own rank relative to opponent). This mirrors the amygdala/mPFC dissociation and might improve sample efficiency — instead of learning a separate policy for each opponent, learn a rank parameter and condition on it.

**Neuroscience prediction:** Professional game players (chess, Go, esports) who train extensively through competitive play should show amplified amygdala/hippocampus responses to opponent rank information compared to non-players — the brain's hierarchy system should be sharpened by self-play-like experience.

## Absorbed speculation

*Speculative: social anxiety may be a domain-specific failure of distributional narrowing — the system fails to narrow distributions specifically during social scene construction (weaker priors for mental states than for physical outcomes), while physical scene construction remains normal.*


---

**Falsification:** If multi-agent self-play agents show no internal rank representations (no consistent ordering of opponent strength, no rank-dependent strategy selection), the prediction is false.
