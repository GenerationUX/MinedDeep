# Neural Mechanisms of Hierarchical Planning in a Virtual Subway Network

**Type:** paper
**Slug:** neural-mechanisms-of-hierarchical-planning-in-a-virtual-subway-network--hassabis
**Sources:** neural-mechanisms-of-hierarchical-planning-in-a-virtual-subway-network--hassabis
**Last updated:** 2026-05-13

---

## Summary
Balaguer, Spiers, Hassabis, and Summerfield (2016) used fMRI to investigate how humans represent hierarchical plans, using a virtual subway navigation task where participants planned routes with varying numbers of hierarchical levels (e.g., inter-zone vs. intra-zone transitions). They found that plan complexity was encoded in caudal prefrontal cortex, while proximity to goal state was represented in ventromedial prefrontal cortex and hippocampus, providing neural evidence for hierarchical planning in the human brain.

## Core content

**Task:** Participants navigated a virtual subway network with a hierarchical structure (stations grouped into zones). Planning demands varied — some routes required crossing zone boundaries (high-level plan changes), others stayed within zones (low-level adjustments) (paper--neural-mechanisms-of-hierarchical-planning-in-a-virtual-subway-network §Methods).

**Key findings:**
- **Caudal prefrontal cortex** (dorsolateral PFC) encoded the complexity of hierarchical plans — more activation for plans requiring more high-level transitions (paper--neural-mechanisms-of-hierarchical-planning-in-a-virtual-subway-network §Results).
- **Ventromedial prefrontal cortex (vmPFC)** and **hippocampus** encoded proximity to the goal state, consistent with their known roles in goal-directed behavior and episodic simulation (paper--neural-mechanisms-of-hierarchical-planning-in-a-virtual-subway-network §Results).
- Plans were represented hierarchically over both contexts (zones) and states (stations), consistent with formal models of hierarchical planning (paper--neural-mechanisms-of-hierarchical-planning-in-a-virtual-subway-network §Results).
- Behavioral RT patterns confirmed hierarchical decomposition — transitions between zones took longer than within-zone transitions (paper--neural-mechanisms-of-hierarchical-planning-in-a-virtual-subway-network §Results).

**Significance:** Provides neural evidence that humans decompose complex plans into hierarchical sub-plans, with distinct prefrontal subregions encoding different levels of the planning hierarchy.

## Connections- **Theme:** [theme--hippocampal-construction](pages/theme--hippocampal-construction.md), planning, cognitive-neuroscience
- **Project:** hippocampus-research
- **Collaborators:** Jan Balaguer (first author), Hugo Spiers, Christopher Summerfield
- **Era:** deepmind-ascent
- **Venue:** venue--Neuron
- **Related:** paper--the-construction-system-of-the-brain — both examine how hippocampal-prefrontal systems support constructive processes
- **Related:** paper--neuroscience-inspired-artificial-intelligence — hierarchical planning as a neuroscience-AI bridge topic

## Honest Gaps
- Metadata lists completely wrong authors (Kumaran, Dayan, Dolan); actual authors are Balaguer, Spiers, Hassabis, Summerfield. This is a serious metadata error — the paper shares no authors with what was recorded.
- The virtual subway task is highly simplified compared to real-world planning.
- fMRI spatial resolution limits localization claims within prefrontal subregions.
- Sample size was modest (typical for fMRI studies of this era, ~20 participants).
- The hierarchical structure was explicitly imposed by the experimental design — it remains unclear whether the same neural mechanisms apply to self-structured hierarchical plans.