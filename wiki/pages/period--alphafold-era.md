---
title: "AlphaFold Era (2018–2022)"
tags:
  - period
description: "The era defined by the AlphaFold project's trajectory from early results to atomic-accuracy predictions and the Nobel Prize-cited Nature paper."
date: 2026-05-13
---

# AlphaFold Era (2018–2022)

**Type:** period
**Slug:** period--alphafold-era
**Sources:** a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury--hassabis, a-distributional-code-for-value-in-dopamine-based-reinforcement-learning--hassabis, advancing-mathematics-by-guiding-human-intuition-w--hassabis, applying-and-improving-alphafold-at-casp14--hassabis, big-loop-recurrence-within-the-hippocampal-system-supports-integration-of-information-across-episodes--hassabis, grandmaster-level-in-starcraft-ii-using-multi-agent-rl--hassabis, highly-accurate-protein-structure-prediction-for-the-human-proteome--hassabis, highly-accurate-protein-structure-prediction-with---hassabis, improved-protein-structure-prediction-using-potentials-from-deep-learning--hassabis, mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model--hassabis, protein-complex-prediction-with-alphafold-multimer--hassabis, protein-structure-predictions-to-atomic-accuracy-with-alphafold--hassabis, reinforcement-learning-fast-and-slow--hassabis, vector-based-navigation-using-grid-like-representations-in-artificial-agents--hassabis
**Last updated:** 2026-05-13

---

## Summary
The era defined by the AlphaFold project's trajectory from early results to atomic-accuracy predictions and the Nobel Prize-cited Nature paper. Fourteen publications spanning protein structure prediction, reinforcement learning theory, neuroscience bridge work, clinical AI, game-playing, and mathematics. The period's centrepiece is the AlphaFold2 Nature paper (2021) — the single most impactful publication in the corpus — but the era also contains the final neuroscience publications and the last major game-playing milestone (AlphaStar, MuZero).

## Core content

**The AlphaFold sequence (2019–2021):** Five papers trace the project's evolution. AlphaFold1 (paper--improved-protein-structure-prediction-using-potentials-from-deep-learning, 2019) used deep learning-derived potentials for residue-level distance prediction. AlphaFold2 at CASP14 (paper--applying-and-improving-alphafold-at-casp14, 2021) achieved dramatic accuracy gains. The flagship Nature paper (paper--highly-accurate-protein-structure-prediction-with---hassabis, 2021) described the full AlphaFold2 architecture — attention-based structure module, end-to-end differentiable, trained on PDB structures. The human proteome paper (paper--highly-accurate-protein-structure-prediction-for-the-human-proteome, 2021) applied AlphaFold2 to predict structures for ~98.5% of human proteins. AlphaFold-Multimer (paper--protein-complex-prediction-with-alphafold-multimer, 2021) extended the approach to protein-protein complexes.

**The neuroscience programme's finale (2019–2020):** Three papers represent the last direct neuroscience contributions. Big-loop recurrence (paper--big-loop-recurrence-within-the-hippocampal-system-supports-integration-of-information-across-episodes) extended hippocampal construction to cross-episode integration. The distributional code paper (paper--a-distributional-code-for-value-in-dopamine-based-reinforcement-learning) connected dopamine reward prediction errors to distributional RL. Reinforcement learning fast and slow (paper--reinforcement-learning-fast-and-slow) proposed a dual-system RL framework drawing on Kahneman's System 1/System 2 and complementary learning systems theory.

**Grid cells in artificial agents (2018):** Vector-based navigation (paper--vector-based-navigation-using-grid-like-representations-in-artificial-agents) demonstrated that RL agents spontaneously develop grid-cell-like representations — the most striking neuroscience-AI bridge result in the corpus.

**Game-playing finales (2019–2020):** AlphaStar (paper--grandmaster-level-in-starcraft-ii-using-multi-agent-rl) achieved grandmaster-level play in StarCraft II, a qualitatively harder problem than board games due to partial observability and vast action spaces. MuZero (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model) learned environment dynamics from scratch, planning with a learned model rather than requiring known transition functions — a major step toward model-based RL.

**Clinical AI (2019):** Continuous prediction of acute kidney injury (paper--a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury) applied deep learning to hospital EHR data, DeepMind's second clinical deployment.

**Mathematics AI (2021):** Advancing mathematics by guiding human intuition (paper--advancing-mathematics-by-guiding-human-intuition-with-ai) used RL to guide mathematicians toward conjectures in knot theory and representation theory — the first paper applying AI as a tool for mathematical discovery.

## Connections
- **Themes:** theme--protein-folding, theme--structural-biology, theme--deep-RL, theme--reinforcement-learning, theme--neuroscience-AI-bridge, theme--game-playing-AI, theme--starcraft, theme--AI-for-science, theme--complementary-learning-systems
- **Projects:** project--AlphaFold, project--AlphaFold2, project--AlphaFold-Multimer, project--MuZero, project--AlphaStar, project--hippocampus-research, project--DeepMind-general
- **Collaborators:** John Jumper (4 papers), Richard Evans (4), David Silver (3), Alexander Pritzel (3), Dharshan Kumaran (2), Eleanor A. Maguire (1 — final collaboration), Neil Burgess (1)
- **Venues:** venue--Nature (6), venue--Science (1), venue--Neuron (1), venue--Proteins (1), venue--bioRxiv (1), venue--Nature-Medicine (1), venue--PNAS (1)
- **Succeeds:** period--deepmind-ascent
- **Precedes:** period--post-alphafold — Nobel Prize, public statements, density functionals

## Honest Gaps
- The era boundary is fuzzy — several 2018 papers classified here (vector-based-navigation, neural-scene-representation) may belong to deepmind-ascent.
- The internal decision to pivot from games to protein folding is not documented in any corpus source.
- The AlphaFold2 paper's author list is enormous (~35+); metadata lists only 5 co-authors, making attribution of specific contributions difficult.
- The protein-structure-predictions-to-atomic-accuracy paper's year is wrong in metadata (2020→2021).
- No sources document the CASP14 competition experience or the team's reaction to the results.
- The big-loop-recurrence paper (2019) is the last Maguire collaboration — no source explains why the neuroscience programme wound down.