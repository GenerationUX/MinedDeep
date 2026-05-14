---
title: "AlphaFold2"
tags:
  - project
description: "AlphaFold2 is the deep learning system that achieved atomic-accuracy protein structure prediction, published in Nature (2021) and cited in the 2024 Nobel…"
date: 2026-05-13
---

# AlphaFold2

**Type:** project
**Slug:** project--AlphaFold2
**Sources:** highly-accurate-protein-structure-prediction-with---hassabis, protein-structure-predictions-to-atomic-accuracy-with-alphafold--hassabis, applying-and-improving-alphafold-at-casp14--hassabis, highly-accurate-protein-structure-prediction-for-the-human-proteome--hassabis, protein-complex-prediction-with-alphafold-multimer--hassabis
**Last updated:** 2026-05-13

---

## Summary
AlphaFold2 is the deep learning system that achieved atomic-accuracy protein structure prediction, published in Nature (2021) and cited in the 2024 Nobel Prize in Chemistry. It uses an Evoformer architecture to jointly process multiple sequence alignments and pair representations, followed by a structure module that generates 3D coordinates through iterative refinement. The system achieved a median GDT-TS of 92.4 at CASP14, solving what had been a 50-year grand challenge.

## Core content

**Architecture (paper--highly-accurate-protein-structure-prediction-with---hassabis):** The Evoformer processes MSA and pair representations through 48 layers of attention, enabling information flow between sequence and structural domains. The structure module uses invariant point attention and SE(3)-equivariant updates to generate 3D coordinates. End-to-end trained on PDB structures.

**CASP14 result (paper--protein-structure-predictions-to-atomic-accuracy-with-alphafold):** Achieved atomic accuracy (backbone error <1Å) on ~2/3 of targets — the first system to reach this threshold.

**Proteome-scale deployment (paper--highly-accurate-protein-structure-prediction-for-the-human-proteome):** Predicted structures for ~98.5% of human proteins, releasing 350,000 predictions via the AlphaFold Protein Structure Database.

**Complex prediction (paper--protein-complex-prediction-with-alphafold-multimer):** AlphaFold-Multimer extended the approach to protein-protein complexes, docking multiple chains simultaneously.

**Key personnel:** John Jumper (first author, lead architect), Richard Evans, Alexander Pritzel, David Silver, Koray Kavukcuoglu, Demis Hassabis.

## Connections
- **Theme:** theme--protein-folding, theme--AI-for-science, theme--structural-biology
- **Period:** period--alphafold-era
- **Precedes:** lecture--nobel-prize-lecture-accelerating-scientific-discovery-with-ai

## Honest Gaps
- The author list exceeds 35 people — the specific intellectual contributions of Jumper vs. the broader team are not documented from first-person accounts.
- No source covers the training compute requirements or cost.
- AlphaFold3 and subsequent work at Isomorphic Labs are not in the corpus.