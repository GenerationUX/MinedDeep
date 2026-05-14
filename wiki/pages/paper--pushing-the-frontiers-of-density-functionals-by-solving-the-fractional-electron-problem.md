---
title: "Pushing the Frontiers of Density Functionals by Solving the Fractional Electron Problem"
tags:
  - peer-reviewed-paper
  - ai-for-science
  - mathematics-ai
  - post-alphafold
  - DeepMind-general
description: "Kirkpatrick, McMorrow, Turban, Gaunt, and colleagues (2022) used deep learning to develop a neural network density functional that correctly solves the…"
date: 2022-01-01
---

# Pushing the Frontiers of Density Functionals by Solving the Fractional Electron Problem

**Type:** paper
**Slug:** pushing-the-frontiers-of-density-functionals-by-solving-the-fractional-electron-problem--hassabis
**Sources:** pushing-the-frontiers-of-density-functionals-by-solving-the-fractional-electron-problem--hassabis
**Last updated:** 2026-05-13

---

## Summary
Kirkpatrick, McMorrow, Turban, Gaunt, and colleagues (2022) used deep learning to develop a neural network density functional that correctly solves the fractional electron problem — a fundamental failure mode of all existing approximate density functionals in quantum chemistry. The learned functional eliminates delocalization errors that have plagued density functional theory (DFT) for decades, producing accurate energies and electron densities across a range of challenging chemical systems.

## Core content

**The fractional electron problem:** In exact DFT, adding a fractional electron to a system should produce a piecewise-linear energy as a function of electron number. All standard approximate functionals produce curved (convex) energy curves, leading to delocalization errors — electrons are artificially spread out to lower energy (paper--pushing-the-frontiers-of-density-functionals-by-solving-the-fractional-electron-problem §Introduction).

**Approach:** A neural network (multilayer perceptron) learns a density functional by training on exact quantum chemistry data. The functional takes features of the occupied Kohn-Sham orbitals as input and outputs local energies, integrating to produce the total energy (paper--pushing-the-frontiers-of-density-functionals-by-solving-the-fractional-electron-problem §Methods).

**Key innovations:**
- The training procedure explicitly enforces piecewise linearity of the energy with respect to fractional electron number (paper--pushing-the-frontiers-of-density-functionals-by-solving-the-fractional-electron-problem §Methods).
- The functional is described as a local range-separated hybrid, combining local and nonlocal orbital features (paper--pushing-the-frontiers-of-density-functionals-by-solving-the-fractional-electron-problem §Methods).
- Training data generated using high-accuracy quantum chemistry methods (paper--pushing-the-frontiers-of-density-functionals-by-solving-the-fractional-electron-problem §Methods).

**Results:**
- The learned functional produces correct piecewise-linear behavior for fractional electrons (paper--pushing-the-frontiers-of-density-functionals-by-solving-the-fractional-electron-problem §Results).
- Eliminates delocalization errors in stretched bond dissociation, charge transfer complexes, and band gaps (paper--pushing-the-frontiers-of-density-functionals-by-solving-the-fractional-electron-problem §Results).
- Achieves chemical accuracy on standard benchmarks while fixing systematic errors of conventional functionals (paper--pushing-the-frontiers-of-density-functionals-by-solving-the-fractional-electron-problem §Results).

## Connections- **Theme:** [theme--AI-for-science](pages/theme--AI-for-science.md)
- **Project:** DeepMind-general
- **Collaborators:** James Kirkpatrick (co-first), Brendan McMorrow (co-first), David H. P. Turban (co-first), Alexander L. Gaunt (co-first)
- **Era:** post-alphafold
- **Venue:** venue--Science
- **Related:** paper--advancing-mathematics-by-guiding-human-intuition — both apply deep learning to mathematical/scientific domains

## Honest Gaps
- Metadata lists McMorrow as first author and James Spencer as co-author; actual first authors are Kirkpatrick, McMorrow, Turban, Gaunt (all co-first). Spencer does not appear in the author list from the extraction.
- The PDF extraction has scanning artefacts with merged text — difficult to read cleanly.
- The learned functional is not systematically transferable — it was trained on specific molecular systems and may not generalize to arbitrary chemistry.
- Computational cost of evaluating the neural network functional may be higher than standard DFT functionals.
- The approach was demonstrated on relatively small molecular systems; scaling to large systems is unclear.
- The physical interpretability of the learned functional is limited compared to analytical functionals.