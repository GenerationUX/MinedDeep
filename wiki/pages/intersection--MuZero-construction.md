---
title: "MuZero × Construction"
tags:
  - intersection
date: 2026-05-14
---

# MuZero × Construction

**Type:** intersection
**Slug:** intersection--MuZero-construction
**Parents:** paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model, paper--the-construction-system-of-the-brain
**Last updated:** 2026-05-14
**Epistemic status:** Extrapolative

---

## The intersection
MuZero (2020) learns environment models without being given the rules — given state and action, it predicts the next state and reward. Hippocampal construction builds scene models without being given scene grammars — given elements, it predicts coherent scenes. Both learn internal models from experience alone. But MuZero's model is *predictive* (forward simulation: what happens next?) while construction's model is *generative* (scene assembly: what could exist?). The intersection asks: **can a MuZero-like system learn a generative model of scenes, not just a predictive model of transitions?**

A "MuZero for imagination" would learn: given partial elements + a "mental action" (recombination operation), what constructed scene results? MuZero predicts state transitions; a construction-MuZero would predict *scene completions* — filling in the missing details of a partially specified imagined scene.

## What the corpus implies
MuZero (Schrittwieser et al., Nature 2020) and the construction papers (2007–2014) share DeepMind authorship through Hassabis but never connect. MuZero's learned model is its most celebrated feature — it achieves superhuman play without knowing the game rules. The construction hypothesis's most celebrated claim is that the hippocampus builds scenes without knowing scene rules. These are the same claim in different domains, but the parallel is never drawn.

MuZero's model has three outputs: next state, reward, and value. A construction model would need different outputs: completed scene, plausibility score, and scene utility. The reward/value outputs in MuZero correspond to the evaluation component that construction lacks — construction papers describe how scenes are built but not how they're evaluated.

## What's missing
- No paper proposes applying MuZero's model-learning approach to scene construction.
- No paper asks whether the hippocampus implements something analogous to MuZero's learned model — predicting scene completions rather than just storing/retrieving scenes.
- MuZero's model is learned end-to-end from game outcomes; construction's "model" (if it exists) would need to be learned from perceptual experience — the training signal is less obvious.
- No paper connects MuZero's planning capability (search through learned model) to the hippocampus's role in episodic future thinking (search through constructed scenes).

## Generative potential
**Architecture — "Constructive MuZero":** Replace MuZero's dynamics function (state, action → next state) with a construction function (partial scene, recombination operation → completed scene). Train on egocentric video where the "reward" is how well the completed scene matches what was actually perceived. The system would learn to construct plausible scenes from partial information, using the same model-learning machinery as MuZero but in a generative rather than predictive mode.

**Episodic future thinking as planning:** MuZero uses its learned model for planning (tree search over future states). The hippocampus uses constructed scenes for future thinking (imagining future events). If Constructive MuZero works, it would model episodic future thinking as planning through a learned generative model — unifying two literatures (planning in RL, future thinking in neuroscience) that currently proceed independently.

**Key difference to explain:** MuZero's model is deterministic (single predicted next state). Construction must be stochastic (many possible scene completions from the same elements). This suggests the brain's "MuZero" uses a distributional generative model — predicting a distribution over possible scenes, not a single scene. This connects back to the distributional RL intersection.

---

**Falsification:** If MuZero's learned dynamics model cannot be repurposed for generative scene construction (even with architectural modification), the shared internal model claim is false.
