---
title: "Computations Underlying Social Hierarchy Learning: Distinct Neural Mechanisms for Updating and Representing Self-Relevant Information"
tags:
  - peer-reviewed-paper
  - hippocampal-construction
  - cognitive-neuroscience
  - deepmind-ascent
  - hippocampus-research
description: "Kumaran, Banino, Blundell, Hassabis, and Dayan (2016) investigated how humans learn social hierarchies, finding that social hierarchy learning is…"
date: 2016-01-01
---

# Computations Underlying Social Hierarchy Learning: Distinct Neural Mechanisms for Updating and Representing Self-Relevant Information

**Type:** paper
**Slug:** computations-underlying-social-hierarchy-learning--hassabis
**Sources:** computations-underlying-social-hierarchy-learning--hassabis
**Last updated:** 2026-05-13

---

## Summary
Kumaran, Banino, Blundell, Hassabis, and Dayan (2016) investigated how humans learn social hierarchies, finding that social hierarchy learning is well-described by Bayesian inference. fMRI revealed that amygdala and hippocampus support domain-general social hierarchy learning, while medial prefrontal cortex selectively updates knowledge about one's own position in the hierarchy — dissociating mechanisms for representing vs. updating self-relevant social information.

## Core content

**Task:** Participants learned social hierarchies in two contexts — one where they were a member of the hierarchy (self-relevant) and one where they observed a hierarchy of others (other-relevant) (paper--computations-underlying-social-hierarchy-learning §Methods).

**Computational model:** A Bayesian inference scheme where participants maintain beliefs about each individual's rank, updated based on observed comparison outcomes. The model captured participant judgments better than alternative models (simple heuristics, associative learning) (paper--computations-underlying-social-hierarchy-learning §Results).

**Key neural findings:**
- **Amygdala and hippocampus** encoded domain-general social hierarchy knowledge — representations of rank that were present regardless of whether the hierarchy was self-relevant (paper--computations-underlying-social-hierarchy-learning §Results).
- **Medial prefrontal cortex (mPFC)** selectively represented and updated self-relevant hierarchy information — activation scaled with prediction errors about one's own rank position (paper--computations-underlying-social-hierarchy-learning §Results).
- This dissociation between representation (amygdala/hippocampus) and self-relevant updating (mPFC) parallels the architecture of complementary learning systems theory (paper--computations-underlying-social-hierarchy-learning §Discussion).

**Significance:** First formal computational account of social hierarchy learning in the brain, identifying distinct neural mechanisms for general social knowledge vs. self-relevant social updating.

## Connections- **Theme:** [theme--hippocampal-construction](pages/theme--hippocampal-construction.md), social-cognition, computational-neuroscience
- **Project:** hippocampus-research
- **Collaborators:** Dharshan Kumaran (first author), Andrea Banino, Charles Blundell, Peter Dayan
- **Era:** deepmind-ascent
- **Venue:** venue--Neuron
- **Related:** paper--deconstructing-episodic-memory-with-construction — both use computational modeling to understand hippocampal-prefrontal interactions
- **Related:** paper--the-construction-system-of-the-brain — hippocampus as a general construction system

## Honest Gaps
- Metadata lists Kumaran, Dayan, Dolan as co-authors; actual authors are Kumaran, Banino, Blundell, Hassabis, Dayan. Raymond Dolan is not an author.
- Metadata theme "hippocampal-construction" is only partially appropriate — the paper focuses on social cognition and amygdala/mPFC as much as hippocampus.
- The Bayesian model, while effective, is computationally optimal — humans may use approximations that differ from the ideal observer.
- The experimental hierarchy was simple (linear, small groups of ~5 individuals) compared to the complexity of real social hierarchies.
- Sample size was modest (typical for fMRI of this era).