---
title: "Vector-Based Navigation Using Grid-Like Representations in Artificial Agents"
tags:
  - peer-reviewed-paper
  - neuroscience-ai-bridge
  - alphafold-era
description: "Banino, Barry, Uria, Blundell, Lillicrap, Mirowski, Pritzel, Chadwick, Degris, Modayil, Wayne, Soyer, Viola, Zhang, Goroshin, Rabinowitz, Pascanu, Beattie,…"
date: 2018-01-01
---

# Vector-Based Navigation Using Grid-Like Representations in Artificial Agents

**Type:** paper
**Slug:** vector-based-navigation-using-grid-like-representations-in-artificial-agents--hassabis
**Sources:** vector-based-navigation-using-grid-like-representations-in-artificial-agents--hassabis
**Last updated:** 2026-05-13

---

## Summary
Banino, Barry, Uria, Blundell, Lillicrap, Mirowski, Pritzel, Chadwick, Degris, Modayil, Wayne, Soyer, Viola, Zhang, Goroshin, Rabinowitz, Pascanu, Beattie, Petersen, Sadik, Gaffney, King, Kavukcuoglu, Hassabis, Hadsell, and Kumaran (2018) demonstrated that deep reinforcement learning agents trained to navigate in environments spontaneously develop grid-cell-like representations — hexagonal firing patterns resembling those found in the mammalian entorhinal cortex. This was a landmark result in the neuroscience-AI bridge, showing that biological navigational algorithms can emerge from general-purpose RL.

## Core content

**Biological background:** Grid cells in the entorhinal cortex fire in hexagonal patterns as animals navigate, forming a vector-based code for spatial position discovered by the 2014 Nobel Prize winners O'Keefe, Moser, and Moser (paper--vector-based-navigation-using-grid-like-representations-in-artificial-agents §Introduction).

**Agent architecture:** A deep RL agent with a recurrent network navigating a rodent-like arena, trained to reach goal locations from random starting positions (paper--vector-based-navigation-using-grid-like-representations-in-artificial-agents §Methods).

**Key finding:** When analyzing the agent's recurrent activations, the researchers discovered hexagonal periodic firing patterns that closely matched biological grid cells — despite never being explicitly trained to produce such representations (paper--vector-based-navigation-using-grid-like-representations-in-artificial-agents §Results).

**Mechanistic analysis:**
- Grid-like representations emerged only when agents had to perform vector-based navigation (path integration), not in simpler control tasks (paper--vector-based-navigation-using-grid-like-representations-in-artificial-agents §Results).
- Ablation studies showed that disrupting grid-like activity impaired navigation performance (paper--vector-based-navigation-using-grid-like-representations-in-artificial-agents §Results).
- The representations shared key properties with biological grid cells: hexagonal symmetry, multiple spatial scales, and orientation (paper--vector-based-navigation-using-grid-like-representations-in-artificial-agents §Results).

**Significance:** Provided strong evidence that grid cells implement a general-purpose computation for vector navigation that biological evolution and artificial RL training converge upon independently.

## Connections- **Theme:** [theme--neuroscience-AI-bridge](pages/theme--neuroscience-AI-bridge.md)
- **Project:** (none — neuroscience-AI bridge research)
- **Collaborators:** Andrea Banino (co-first), Caswell Barry (co-first), Dharshan Kumaran (co-first/corresponding), Raia Hadsell, Benigno Uria, Charles Blundell, Timothy Lillicrap, Piotr Mirowski, Alexander Pritzel, Martin J. Chadwick, Thomas Degris, Joseph Modayil, Greg Wayne, Hubert Soyer, Fabio Viola, Brian Zhang, Ross Goroshin, Neil Rabinowitz, Razvan Pascanu, Charlie Beattie, Stig Petersen, Amir Sadik, Stephen Gaffney, Helen King, Koray Kavukcuoglu
- **Era:** alphafold-era (note: metadata era seems late for a 2018 paper; would fit deepmind-ascent better)
- **Venue:** venue--Nature
- **Related:** paper--neuroscience-inspired-artificial-intelligence — both bridge neuroscience and AI

## Honest Gaps
- Metadata lists only 4 co-authors; the actual paper has ~25 authors.
- The grid-like representations, while visually striking, may not implement exactly the same computation as biological grid cells — similarity in firing patterns does not guarantee mechanistic identity.
- The emergence of grid cells depended heavily on architectural choices and training conditions — it is not a universal feature of all RL agents.
- Some critics argued the hexagonal patterns could be an artifact of the analysis method rather than a genuine computational feature.
- The environments were simple 2D arenas — it is unclear whether similar representations would emerge in more complex 3D or naturalistic environments.