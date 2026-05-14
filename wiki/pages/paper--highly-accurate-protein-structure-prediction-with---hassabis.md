---
title: "Highly Accurate Protein Structure Prediction with AlphaFold"
tags:
  - paper--highly-accurate-protein-structure-prediction-with-
description: "Jumper, Evans, Pritzel, Green, Figurnov, Ronneberger, Tunyasuvunakool, and 26 colleagues, with Silver, Senior, Kavukcuoglu, Kohli, and Hassabis (2021)…"
date: 2026-05-13
---

# Highly Accurate Protein Structure Prediction with AlphaFold

**Type:** paper
**Slug:** highly-accurate-protein-structure-prediction-with---hassabis
**Sources:** highly-accurate-protein-structure-prediction-with---hassabis
**Last updated:** 2026-05-13

---

## Summary
Jumper, Evans, Pritzel, Green, Figurnov, Ronneberger, Tunyasuvunakool, and 26 colleagues, with Silver, Senior, Kavukcuoglu, Kohli, and Hassabis (2021) introduced AlphaFold2, which achieved atomic-level accuracy in protein structure prediction at CASP14 — a result widely described as solving the 50-year-old protein folding problem. AlphaFold2's key innovations were the Evoformer architecture (which jointly evolves MSA and pair representations through attention) and a structure module that builds 3D coordinates via invariant point attention. The system achieved a median GDT-TS of 92.4 across all CASP14 targets.

## Core content

**Architecture — two main components:**
1. **Evoformer:** A novel attention-based architecture that processes multiple sequence alignment (MSA) representations and pairwise residue representations simultaneously. MSA-to-pair and pair-to-MSA attention layers allow information to flow between these representations, capturing both evolutionary constraints and spatial relationships (paper--highly-accurate-protein-structure-prediction-with---hassabis §Methods).
2. **Structure module:** Takes the evolved pair representation and produces 3D atom coordinates using invariant point attention (IPA), which respects SE(3) equivariance — rotations and translations of the input produce corresponding transformations of the output (paper--highly-accurate-protein-structure-prediction-with---hassabis §Methods).

**Training:** End-to-end training on known experimental structures from the PDB, with a custom loss function combining frame-aligned point error (FAPE), auxiliary distogram losses, and other structural terms (paper--highly-accurate-protein-structure-prediction-with---hassabis §Methods).

**CASP14 results:**
- Median GDT-TS of 92.4 across all targets (paper--highly-accurate-protein-structure-prediction-with---hassabis §Results).
- On the hardest free-modeling targets, AlphaFold2 achieved accuracies comparable to experimental methods (median backbone accuracy ~1.0 Å) (paper--highly-accurate-protein-structure-prediction-with---hassabis §Results).
- Outperformed the next-best method by a large margin on nearly every target (paper--highly-accurate-protein-structure-prediction-with---hassabis §Results).
- pLDDT confidence scores reliably predicted per-residue accuracy (paper--highly-accurate-protein-structure-prediction-with---hassabis §Results).

**Significance:** Described as solving the protein folding problem. Led directly to the AlphaFold Protein Structure Database (200M+ structures), the 2024 Nobel Prize in Chemistry for Hassabis and Jumper, and has transformed structural biology.

## Connections- **Theme:** [theme--protein-folding](pages/theme--protein-folding.md), structural-biology
- **Project:** AlphaFold2
- **Collaborators:** John Jumper (first/corresponding), Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko, Alex Bridgland, Clemens Meyer, Simon A. A. Kohl, Andrew J. Ballard, Andrew Cowie, Bernardino Romera-Paredes, Stanislav Nikolov, Rishub Jain, Jonas Adler, Trevor Back, Stig Petersen, David Reiman, Ellen Clancy, Michal Zielinski, Martin Steinegger, Michalina Pacholska, Tamas Berghammer, Sebastian Bodenstein, David Silver, Oriol Vinyals, Andrew W. Senior, Koray Kavukcuoglu, Pushmeet Kohli
- **Era:** alphafold-era
- **Venue:** venue--Nature (front page)
- **Supersedes:** paper--improved-protein-structure-prediction-using-potentials-from-deep-learning
- **Precedes:** paper--protein-structure-predictions-to-atomic-accuracy-with-alphafold — further improvements
- **Notable quote:** "We assess the accuracy of the method on CASP14 targets and find that it achieves a median backbone accuracy of 0.96 Å." (paper--highly-accurate-protein-structure-prediction-with---hassabis §Abstract)

## Honest Gaps
- Metadata lists only 5 co-authors; the actual paper has 34 authors.
- Struggles with protein complexes and multi-chain assemblies — addressed by AlphaFold-Multimer (paper--protein-complex-prediction-with-alphafold-multimer).
- Performance depends heavily on MSA depth — proteins with few homologs are predicted with lower confidence.
- Does not predict dynamics, conformational ensembles, or protein-ligand interactions.
- Training required massive compute (multiple TPU v3 pods over weeks).
- The end-to-end differentiable structure module is complex and difficult to interpret.