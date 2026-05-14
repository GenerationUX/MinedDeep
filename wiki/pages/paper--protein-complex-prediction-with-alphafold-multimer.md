# Protein Complex Prediction with AlphaFold-Multimer

**Type:** paper
**Slug:** protein-complex-prediction-with-alphafold-multimer--hassabis
**Sources:** protein-complex-prediction-with-alphafold-multimer--hassabis
**Last updated:** 2026-05-13

---

## Summary
Evans, O'Neill, Pritzel, Antropova, Senior, Green, Žídek, Bates, Blackwell, Yim, Ronneberger, Bodenstein, Zielinski, Bridgland, Potapenko, Cowie, Tunyasuvunakool, Jain, Clancy, Kohli, Jumper, and Hassabis (2021) introduced AlphaFold-Multimer, an extension of AlphaFold2 that predicts the structures of protein complexes (multi-chain assemblies). The system modifies the AlphaFold2 architecture to handle multiple protein chains, predicting both intra-chain and inter-chain contacts to produce full complex structures. This addressed a major limitation of the original AlphaFold2.

## Core content

**Problem:** AlphaFold2 predicts single-chain protein structures with high accuracy but cannot natively predict how multiple proteins assemble into complexes. Most biological functions involve protein complexes, not isolated chains (paper--protein-complex-prediction-with-alphafold-multimer §Introduction).

**Key modifications to AlphaFold2:**
- **Input representation:** Extended to handle multiple sequences (one per chain) with explicit chain identifiers in the MSA and pair representations (paper--protein-complex-prediction-with-alphafold-multimer §Methods).
- **Pair representation:** Includes inter-chain residue pairs (not just intra-chain), allowing the model to predict chain-chain interactions (paper--protein-complex-prediction-with-alphafold-multimer §Methods).
- **Training data:** Curated set of experimentally determined protein complex structures from the PDB (paper--protein-complex-prediction-with-alphafold-multimer §Methods).
- **Assembly module:** Predicts stoichiometry and chain ordering for heteromeric complexes (paper--protein-complex-prediction-with-alphafold-multimer §Methods).

**Results:**
- Achieved higher accuracy than dedicated docking methods on heterodimer benchmarks (paper--protein-complex-prediction-with-alphafold-multimer §Results).
- Successfully predicted structures of complexes with up to ~10 chains (paper--protein-complex-prediction-with-alphafold-multimer §Results).
- Performance was strongest for complexes where good MSAs were available; degraded for complexes with few homologs (paper--protein-complex-prediction-with-alphafold-multimer §Results).

## Connections- **Theme:** [theme--protein-folding](pages/theme--protein-folding.md), structural-biology
- **Project:** AlphaFold-Multimer
- **Collaborators:** Richard Evans (co-first), Michael O'Neill (co-first), Alexander Pritzel (co-first), Natasha Antropova (co-first), John Jumper (co-first), Andrew Senior, Tim Green, Pushmeet Kohli
- **Era:** alphafold-era
- **Venue:** venue--bioRxiv (preprint, not peer-reviewed)
- **Extends:** paper--highly-accurate-protein-structure-prediction-with---hassabis — AlphaFold-Multimer builds on AlphaFold2

## Honest Gaps
- Metadata lists only 4 co-authors; the actual paper has ~22 authors.
- This is a bioRxiv preprint — it has not undergone formal peer review.
- Performance on large complexes (>5 chains) and transient interactions is limited.
- The system cannot predict complexes involving nucleic acids, lipids, or small molecules.
- Assembly prediction (which chains form a complex and in what stoichiometry) remains a challenge — the system requires the input chains to be specified.
- Like AlphaFold2, performance depends heavily on MSA depth — complexes with few evolutionary homologs are poorly predicted.