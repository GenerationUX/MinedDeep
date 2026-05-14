---
title: "Emergent Cognitive Maps in Adversarial Environments"
tags:
  - intersection
date: 2026-05-14
---

# Emergent Cognitive Maps in Adversarial Environments

**Type:** intersection (second-order)
**Slug:** intersection--emergent-cognitive-maps-adversarial-environments
**Parents:** intersection--grid-cells-self-play, intersection--fast-slow-RL-alphago-zero-dynamics
**Last updated:** 2026-05-14
**Epistemic status:** Extrapolative

---

## The convergence
Grid cells emerge from navigation tasks. Fast/slow emerges from self-play. Combined: **self-play agents requiring spatial reasoning should develop both grid-like representations and a fast/slow split over them — fine-grained grids for immediate moves, coarse grids for strategic spatial planning.**

## Why this isn't obvious from either parent
The Grid Cells×Self-Play intersection (B) asks whether grid cells emerge under self-play but doesn't connect to the fast/slow dynamics that self-play also produces. The Fast/Slow×AlphaGo intersection (4) identifies emergent dual systems but doesn't ask about their *spatial structure*. Together: the fast/slow split isn't just behavioural — it's spatial, operating over different scales of a grid-like code.

## Generative prediction
Analyse AlphaZero's internal representations at board positions for hexagonal periodicity at multiple spatial scales. If fine-grained grids appear in move-selection layers and coarse grids in value-evaluation layers, this would show the fast/slow split is instantiated as a spatial scale split — the most direct testable prediction from any second-order intersection.

---

**Falsification:** If self-play agents develop grid-like codes but not at multiple scales (only one grid scale), the scale-split fast/slow instantiation is false.
