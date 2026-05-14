---
title: "Decoding Neuronal Ensembles in the Human Hippocampus"
tags:
  - peer-reviewed-paper
  - hippocampal-construction
  - cognitive-neuroscience
  - phd-period
  - hippocampus-research
description: "Hassabis, Chu, Rees, Weiskopf, Molyneux, and Maguire (2009) used multivariate pattern classification (searchlight SVM) with high-resolution fMRI to decode a…"
date: 2009-01-01
---

# Decoding Neuronal Ensembles in the Human Hippocampus

**Type:** paper
**Slug:** decoding-neuronal-ensembles-in-the-human-hippocampus--hassabis
**Sources:** decoding-neuronal-ensembles-in-the-human-hippocampus--hassabis
**Last updated:** 2026-05-13

---

## Summary
Hassabis, Chu, Rees, Weiskopf, Molyneux, and Maguire (2009) used multivariate pattern classification (searchlight SVM) with high-resolution fMRI to decode a person's spatial position within a virtual environment solely from hippocampal activity patterns, even when visual input was held constant. This demonstrated that the hippocampal population code has an anisotropic, functionally organized structure — contradicting the prevailing consensus from invasive animal studies that it is random and uniform. A clean dissociation was found: hippocampus coded position, parahippocampal gyrus coded environment identity.

## Core content

**Research question:** Can spatial position be decoded from patterns of hippocampal fMRI activity, and does this reveal properties of the hippocampal population code?

**Method:** 4 participants navigated between 4 target positions in each of 2 matched VR rooms (blue/green) built with a modified Fable game engine. High-resolution fMRI (1.5mm isotropic voxels) focused on the MTL. At each target, the viewpoint transitioned downward to show only the floor — removing visual input as a confound. Linear SVM classifiers with searchlight feature selection decoded position (pairwise and 4-way) and environment identity from voxel patterns (paper--decoding-neuronal-ensembles-in-the-human-hippocampus §Experimental Procedures).

**Key findings:**
- Pairwise position decoding: large clusters of voxels in body-posterior hippocampus bilaterally discriminated between two positions significantly above chance (paper--decoding-neuronal-ensembles-in-the-human-hippocampus §Results).
- Four-way position decoding: the same hippocampal region simultaneously discriminated among all 4 positions in a room, with findings highly consistent across participants (paper--decoding-neuronal-ensembles-in-the-human-hippocampus §Results).
- Environment classification: voxels in parahippocampal gyrus (not hippocampus) discriminated between blue and green rooms (paper--decoding-neuronal-ensembles-in-the-human-hippocampus §Results).
- Formal dissociation: significantly more hippocampal voxels discriminated position than environment; significantly more parahippocampal voxels discriminated environment than position (all P < 0.05) (paper--decoding-neuronal-ensembles-in-the-human-hippocampus §Results).

**Theoretical significance:** Successful classification requires systematic, consistent patterns across training examples. If the hippocampal population code were truly random and uniform (as per Redish et al. 2001; computational models by Hartley et al. 2000, Samsonovich & McNaughton 1997), voxel-level patterns would be uniform and classification impossible. The results therefore imply hippocampal neuronal ensembles are large, stable, and anisotropically structured (paper--decoding-neuronal-ensembles-in-the-human-hippocampus §Discussion).

**Proposed spatial code:** The spatial code is likely continuous (not limited to discrete positions), with individual position representations aggregating to form the allocentric cognitive map. Parahippocampal gyrus extracts contextual features (object-in-place associations, wall configurations) as input to hippocampal place representations (paper--decoding-neuronal-ensembles-in-the-human-hippocampus §Discussion).

## Connections- **Theme:** [theme--hippocampal-construction](pages/theme--hippocampal-construction.md) — demonstrates the representational structure underlying scene construction
- **Theme:** episodic-memory — spatial representations as scaffold for episodic memory
- **Collaborators:** Eleanor A. Maguire, Geraint Rees, Nikolaus Weiskopf, Carlton Chu, Peter D. Molyneux (Lionhead Studios)
- **Era:** phd-period — published 2009 from UCL
- **Precedes:** paper--decoding-individual-episodic-memory-traces-in-the-human-hippocampus (2010) — extends decoding approach from spatial to episodic memory traces
- **Methodological note:** The VR environment used a modified Fable game engine, connecting to Hassabis's games-industry background

## Honest Gaps
- The metadata co-author list omits Carlton Chu, Geraint Rees, Nikolaus Weiskopf, and Peter D. Molyneux — only Maguire is listed.
- Only 4 participants (all male, right-handed, experienced video-game players) — very small sample, though consistency across participants mitigates this somewhat.
- The spatial code was described as "likely continuous" but only discrete positions were tested — the continuity claim is speculative.