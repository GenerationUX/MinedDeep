---
title: "Highly Accurate Protein Structure Prediction for the Human Proteome"
tags:
  - peer-reviewed-paper
  - protein-folding
  - structural-biology
  - protein-structure
  - alphafold-era
  - AlphaFold2
description: "Tunyasuvunakool, Adler, Wu, Green, Zielinski, Žídek, Bridgland, Cowie, Meyer, Laydon, Velankar, Kleywegt, Bateman, Evans, Pritzel, Figurnov, Ronneberger,…"
date: 2021-01-01
---

# Highly Accurate Protein Structure Prediction for the Human Proteome

**Type:** paper
**Slug:** highly-accurate-protein-structure-prediction-for-the-human-proteome--hassabis
**Sources:** highly-accurate-protein-structure-prediction-for-the-human-proteome--hassabis
**Last updated:** 2026-05-13

---

## Summary
Tunyasuvunakool, Adler, Wu, Green, Zielinski, Žídek, Bridgland, Cowie, Meyer, Laydon, Velankar, Kleywegt, Bateman, Evans, Pritzel, Figurnov, Ronneberger, Bates, Kohl, Potapenko, Ballard, Romera-Paredes, Nikolov, Jain, Clancy, Berghammer, Bodenstein, Senior, Kavukcuoglu, Kohli, and Hassabis (2021) applied AlphaFold2 to predict structures for the entire human proteome (~20,000 proteins), producing confident predictions for ~98.5% of human proteins. This companion paper to the AlphaFold2 method paper demonstrated the immediate practical impact of the system on biology and medicine.

## Core content

**Scope:** Predicted structures for all proteins in the UniProt human reference proteome, using the AlphaFold2 system without modification (paper--highly-accurate-protein-structure-prediction-for-the-human-proteome §Methods).

**Key results:**
- Confident predictions (pLDDT > 70) for 98.5% of human protein residues (paper--highly-accurate-protein-structure-prediction-for-the-human-proteome §Results).
- High-confidence predictions (pLDDT > 90) for 58% of residues — comparable to experimental accuracy (paper--highly-accurate-protein-structure-prediction-for-the-human-proteome §Results).
- Only ~1.5% of residues were predicted as disordered (pLDDT < 50), consistent with known disorder fractions (paper--highly-accurate-protein-structure-prediction-for-the-human-proteome §Results).
- Predictions were validated against known experimental structures not in the training set (paper--highly-accurate-protein-structure-prediction-for-the-human-proteome §Results).

**Impact:** All predictions were released via the AlphaFold Protein Structure Database in collaboration with EMBL-EBI, providing open access to the entire human proteome for the first time (paper--highly-accurate-protein-structure-prediction-for-the-human-proteome §Discussion).

## Connections- **Theme:** [theme--protein-folding](pages/theme--protein-folding.md), structural-biology
- **Project:** AlphaFold2
- **Collaborators:** Kathryn Tunyasuvunakool (first), Jonas Adler, Zachary Wu, Tim Green, Michal Zielinski, Augustin Žídek, Alex Bridgland, Andrew Cowie, Clemens Meyer, Agata Laydon, Sameer Velankar, Gerard J. Kleywegt, Alex Bateman, Richard Evans, Alexander Pritzel, Michael Figurnov, Olaf Ronneberger, Russ Bates, Simon A. A. Kohl, Anna Potapenko, Andrew J. Ballard, Bernardino Romera-Paredes, Stanislav Nikolov, Rishub Jain, Ellen Clancy, Tamas Berghammer, Sebastian Bodenstein, Andrew W. Senior, Koray Kavukcuoglu, Pushmeet Kohli
- **Era:** alphafold-era
- **Venue:** venue--Nature
- **Companion to:** paper--highly-accurate-protein-structure-prediction-with---hassabis

## Honest Gaps
- Metadata lists only 4 co-authors; the actual paper has ~30 authors.
- Some predictions, especially for disordered regions and proteins with few homologs, should not be treated as reliable structures.
- The paper does not systematically validate predictions against experimental data beyond comparison statistics.
- Membrane proteins, which constitute ~30% of drug targets, were not separately analyzed for quality.
- Predictions are static structures — no information about dynamics, flexibility, or conformational changes.