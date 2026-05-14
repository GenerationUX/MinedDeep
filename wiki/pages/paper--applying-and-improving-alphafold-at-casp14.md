# Applying and Improving AlphaFold at CASP14

**Type:** paper
**Slug:** applying-and-improving-alphafold-at-casp14--hassabis
**Sources:** applying-and-improving-alphafold-at-casp14--hassabis
**Last updated:** 2026-05-13

---

## Summary
Jumper, Evans, Pritzel, Green, Figurnov, Ronneberger, Tunyasuvunakool, and colleagues (2021) provided a detailed account of AlphaFold2's participation in CASP14, describing the practical improvements made to the system during the competition and analyzing its performance across all target domains. Published in *Proteins: Structure, Function, and Bioinformatics*, this companion to the main Nature paper offers implementation details and lessons from the CASP14 experience.

## Core content

**CASP14 participation details:** AlphaFold2 was entered as "Group 427" and submitted predictions for all regular CASP14 targets across all categories (free-modeling, template-based, refinement) (paper--applying-and-improving-alphafold-at-casp14 §Methods).

**Improvements made during CASP14:**
- Iterative refinement of the model architecture and training procedure during the competition window (paper--applying-and-improving-alphafold-at-casp14 §Methods).
- Adjustments to the MSA generation pipeline and template search parameters (paper--applying-and-improving-alphafold-at-casp14 §Methods).
- Ensemble strategies combining multiple predictions (paper--applying-and-improving-alphafold-at-casp14 §Methods).

**Performance analysis:**
- Detailed breakdown of performance by target difficulty, domain type, and MSA depth (paper--applying-and-improving-alphafold-at-casp14 §Results).
- Analysis of failure modes — where AlphaFold2 underperformed and why (paper--applying-and-improving-alphafold-at-casp14 §Results).
- Comparison with other CASP14 methods showing the magnitude of AlphaFold2's advantage (paper--applying-and-improving-alphafold-at-casp14 §Results).

**Distinguishing from the Nature paper:** This paper focuses on the practical aspects of running AlphaFold2 in a competitive setting, while the Nature paper presents the method and overall results. The two papers share authors but serve complementary purposes.

## Connections- **Theme:** [theme--protein-folding](pages/theme--protein-folding.md), structural-biology
- **Project:** AlphaFold2
- **Collaborators:** John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko, Alex Bridgland, Clemens Meyer, Simon A. A. Kohl, Andrew J. Ballard, Andrew Cowie, Bernardino Romera-Paredes, Stanislav Nikolov, Rishub Jain, Jonas Adler, Trevor Back, Stig Petersen
- **Era:** alphafold-era
- **Venue:** venue--Proteins (note: metadata incorrectly lists "Nature"; actual venue is *Proteins*)
- **Companion to:** paper--highly-accurate-protein-structure-prediction-with---hassabis

## Honest Gaps
- Metadata incorrectly lists venue as "Nature"; the paper was published in *Proteins: Structure, Function, and Bioinformatics*.
- Metadata lists only 4 co-authors; the actual paper has ~20+ authors.
- This is a companion/detailed analysis paper rather than a primary contribution — most key results are in the Nature paper.
- The iterative improvements during CASP14 mean the "final" AlphaFold2 system evolved over the competition period.
- Limited independent validation beyond CASP targets.