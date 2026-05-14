---
title: "Protein Folding"
tags:
  - theme
description: "The protein folding theme traces the AlphaFold project from its first published results (2019) through atomic-accuracy predictions (2021) to proteome-scale…"
date: 2026-05-13
---

# Protein Folding

**Type:** theme
**Slug:** theme--protein-folding
**Sources:** improved-protein-structure-prediction-using-potentials-from-deep-learning--hassabis, protein-structure-predictions-to-atomic-accuracy-with-alphafold--hassabis, applying-and-improving-alphafold-at-casp14--hassabis, highly-accurate-protein-structure-prediction-with---hassabis, highly-accurate-protein-structure-prediction-for-the-human-proteome--hassabis, protein-complex-prediction-with-alphafold-multimer--hassabis
**Last updated:** 2026-05-13

---

## Summary
The protein folding theme traces the AlphaFold project from its first published results (2019) through atomic-accuracy predictions (2021) to proteome-scale application and protein-complex prediction. Six papers document one of the most celebrated scientific achievements of the 21st century — a deep learning system that solved the 50-year-old protein structure prediction problem. The theme's distinctive feature is its rapid, near-linear progression: each paper is strictly better than the last, with no dead ends or retractions.

## Core content

**The problem:** Proteins fold into 3D structures determined by their amino acid sequences. Predicting these structures from sequence alone (the "protein folding problem") was identified as a grand challenge in biology since Anfinsen's work in the 1970s. CASP (Critical Assessment of protein Structure Prediction) biennial competitions were the standard benchmark.

**AlphaFold1 (2019):** Improved protein structure prediction using potentials from deep learning (paper--improved-protein-structure-prediction-using-potentials-from-deep-learning) used deep learning to predict inter-residue distances and orientations, feeding these as potentials into a conventional structure prediction pipeline. Published in Proteins journal as a CASP13 contribution.

**AlphaFold2 development (2020–2021):** Two papers document the breakthrough. Protein structure predictions to atomic accuracy with AlphaFold (paper--protein-structure-predictions-to-atomic-accuracy-with-alphafold) described the CASP14 results — median GDT-TS score of 92.4, achieving atomic accuracy for the first time. Applying and improving AlphaFold at CASP14 (paper--applying-and-improving-alphafold-at-casp14) provided technical details of the CASP14 entry.

**The AlphaFold2 architecture (2021):** Highly accurate protein structure prediction with AlphaFold (paper--highly-accurate-protein-structure-prediction-with---hassabis) is the flagship Nature paper. Key innovations: Evoformer (jointly processes MSA and pair representations through attention layers), structure module (generates 3D coordinates through iterative refinement), end-to-end training (no separate prediction pipeline). This paper is Nature frontpage, field-defining, top-cited, Science-breakthrough, and Nobel-cited — the most decorated paper in the corpus.

**Proteome-scale application (2021):** Highly accurate protein structure prediction for the human proteome (paper--highly-accurate-protein-structure-prediction-for-the-human-proteome) applied AlphaFold2 to predict structures for ~98.5% of human proteins, releasing 350,000 predictions. This paper is also Nobel-cited, demonstrating the downstream scientific impact.

**Protein complexes (2021):** AlphaFold-Multimer (paper--protein-complex-prediction-with-alphafold-multimer) extended the approach to predict structures of protein-protein complexes, addressing a harder problem where multiple chains must be docked simultaneously.

**Technical philosophy:** The AlphaFold approach is notable for what it does not do — it does not simulate the physical folding process. Instead, it learns statistical patterns from known structures in the PDB. This is a pure pattern-recognition approach, distinct from physics-based molecular dynamics. The success of this approach has broader implications for the learnable nature conjecture (lecture--nobel-prize-lecture-accelerating-scientific-discovery-with-ai).

## Connections
- **Theme:** theme--structural-biology, theme--AI-for-science, theme--learnable-nature-conjecture
- **Projects:** project--AlphaFold, project--AlphaFold2, project--AlphaFold-Multimer
- **Period:** period--alphafold-era
- **Collaborators:** John Jumper (first author on AlphaFold2, key architect), Richard Evans, Alexander Pritzel, David Silver, Koray Kavukcuoglu
- **Venues:** venue--Nature (3), venue--Proteins (1), venue--bioRxiv (1)
- **Precedes:** lecture--nobel-prize-lecture-accelerating-scientific-discovery-with-ai (capstone)

## Honest Gaps
- No corpus source describes the early AlphaFold project history (pre-2019) or the decision to invest heavily in protein structure.
- John Jumper's role as the key architect is clear from authorship but no interview or first-person account documents the division of intellectual labour.
- The CASP14 experience is not documented from the team's perspective.
- No source covers the decision to release the AlphaFold Protein Structure Database publicly.
- AlphaFold3 and subsequent Isomorphic Labs work are not in the corpus.
- The relationship between AlphaFold1's distance-prediction approach and AlphaFold2's end-to-end approach is not explained in any single source.