# Improved Protein Structure Prediction Using Potentials from Deep Learning

**Type:** paper
**Slug:** improved-protein-structure-prediction-using-potentials-from-deep-learning--hassabis
**Sources:** improved-protein-structure-prediction-using-potentials-from-deep-learning--hassabis
**Last updated:** 2026-05-13

---

## Summary
Senior, Evans, Jumper, Kirkpatrick, Sifre, Green, Qin, Žídek, Nelson, Bridgland, Penedones, Petersen, Simonyan, Crossan, Kohli, Jones, Silver, Kavukcuoglu, and Hassabis (2020) introduced AlphaFold, DeepMind's first entry in the CASP13 protein structure prediction competition. AlphaFold used deep learning to predict inter-residue distance distributions and angles, then used these as potentials to guide structure assembly via gradient descent. It achieved the highest accuracy in the free-modeling category at CASP13, marking a step-change in the field.

## Core content

**Problem:** Protein structure prediction from amino acid sequence is a long-standing grand challenge in biology. Traditional methods relied on fragment assembly and physics-based energy functions with limited accuracy (paper--improved-protein-structure-prediction-using-potentials-from-deep-learning §Introduction).

**Approach:** Train a deep residual network to predict distributions of inter-residue distances and dihedral angles from the amino acid sequence and multiple sequence alignment (MSA) features. These predicted distributions are converted into a smooth potential energy function, and gradient descent optimizes 3D coordinates to minimize this potential (paper--improved-protein-structure-prediction-using-potentials-from-deep-learning §Methods).

**Key innovations:**
- Distance distribution prediction rather than single distance values — captures structural uncertainty (paper--improved-protein-structure-prediction-using-potentials-from-deep-learning §Methods).
- End-to-end differentiable pipeline from sequence to 3D structure (paper--improved-protein-structure-prediction-using-potentials-from-deep-learning §Methods).
- Iterative refinement: predicted structure is fed back to improve predictions (paper--improved-protein-structure-prediction-using-potentials-from-deep-learning §Methods).

**CASP13 results:**
- Won the free-modeling category with median GDT-TS of ~68.5 (paper--improved-protein-structure-prediction-using-potentials-from-deep-learning §Results).
- Outperformed all template-based and template-free methods, the first time a purely learning-based method dominated (paper--improved-protein-structure-prediction-using-potentials-from-deep-learning §Results).
- Still far from experimental accuracy on the hardest targets — motivating AlphaFold2 (paper--improved-protein-structure-prediction-using-potentials-from-deep-learning §Discussion).

## Connections- **Theme:** [theme--protein-folding](pages/theme--protein-folding.md), structural-biology
- **Project:** AlphaFold
- **Collaborators:** Andrew W. Senior (co-first), Richard Evans (co-first), John Jumper (co-first), James Kirkpatrick, Laurent Sifre, Tim Green, Chongli Qin, Augustin Žídek, Alexander W. R. Nelson, Alex Bridgland, Hugo Penedones, Stig Petersen, Karen Simonyan, Steve Crossan, Pushmeet Kohli, David T. Jones, David Silver, Koray Kavukcuoglu
- **Era:** alphafold-era
- **Venue:** venue--Nature (note: metadata says "Proteins" but actual venue is Nature, published alongside CASP13 special issue)
- **Precedes:** paper--highly-accurate-protein-structure-prediction-with---hassabis — AlphaFold2 dramatically improved on these results

## Honest Gaps
- Metadata lists only 3 co-authors; the actual paper has 18 authors.
- Metadata incorrectly lists venue as "Proteins"; the paper was published in Nature.
- AlphaFold1 was impressive at CASP13 but still far from experimental accuracy — median GDT-TS ~68 vs. ~90+ for AlphaFold2.
- The approach produced some physically unrealistic structures (clashes, bond geometry violations) on difficult targets.
- The gradient descent optimization could get trapped in local minima, limiting accuracy on large proteins.