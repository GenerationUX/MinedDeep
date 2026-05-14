---
title: "Game-Playing AI"
tags:
  - theme
description: "Eight publications trace DeepMind's game-playing programme from Atari (2015) through Go, chess, shogi, Quake III, and StarCraft II (2019)."
date: 2026-05-13
---

# Game-Playing AI

**Type:** theme
**Slug:** theme--game-playing-ai
**Sources:** mastering-the-game-of-go-with-deep-neural-networks-and-tree-search--hassabis, mastering-the-game-of-go-without-human-knowledge---hassabis, a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go--hassabis, grandmaster-level-in-starcraft-ii-using-multi-agent-rl--hassabis, human-level-performance-in-3d-multiplayer-games-with-population-based-rl--hassabis, mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model--hassabis, human-level-control-through-deep-reinforcement-learning--hassabis, artificial-intelligence-chess-match-of-the-century--hassabis
**Last updated:** 2026-05-13

---

## Summary
Eight publications trace DeepMind's game-playing programme from Atari (2015) through Go, chess, shogi, Quake III, and StarCraft II (2019). The intellectual arc moves from learning to play individual games (DQN) to general game-playing architectures (AlphaZero, MuZero) that master multiple games with a single algorithm. The Go sequence — AlphaGo → AlphaGo Zero → AlphaZero — is the most clearly documented progression in the corpus, showing the elimination of human knowledge as a training signal.

## Core content

**DQN (2015):** The starting point — a single CNN trained with Q-learning plays 29 Atari games from raw pixels (paper--human-level-control-through-deep-reinforcement-learning). The key insight: a general architecture can learn diverse game strategies without game-specific engineering.

**The Go sequence (2016–2018):**
- AlphaGo (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search): Supervised learning from human games + self-play reinforcement learning + Monte Carlo tree search. Defeated Lee Sedol 4-1.
- AlphaGo Zero (paper--mastering-the-game-of-go-without-human-knowledge): Removed supervised learning entirely. Pure self-play from random initialisation. Surpassed AlphaGo in 40 days. The "without human knowledge" title is programmatic — it argues that self-play is sufficient.
- AlphaZero (paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go): Single architecture, single algorithm, no human data, superhuman in Go, chess, and shogi. The generalisation claim is the key contribution.

**MuZero (2020):** Learned a model of game dynamics from scratch, planning without knowing the rules (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model). This is architecturally significant — it separates the planning algorithm from the environment model, a step toward model-based RL that doesn't require known transition functions.

**Real-time games (2017, 2019):** Population-based RL in Quake III capture-the-flag (paper--human-level-performance-in-3d-multiplayer-games-with-population-based-rl) demonstrated multi-agent coordination. AlphaStar (paper--grandmaster-level-in-starcraft-ii-using-multi-agent-rl) tackled StarCraft II's partial observability, vast action spaces, and strategic depth — the hardest game in the corpus.

**Public framing (2016):** The Nature book review (paper--artificial-intelligence-chess-match-of-the-century) framed the Lee Sedol match as a test of human creativity, not just machine intelligence.

## Connections
- **Theme:** theme--deep-RL, theme--self-play, theme--go, theme--chess, theme--starcraft
- **Projects:** project--DQN, project--AlphaGo, project--AlphaGo-Zero, project--AlphaZero, project--MuZero, project--AlphaStar
- **Periods:** period--early-deepmind (DQN), period--deepmind-ascent (Go sequence, Quake III), period--alphafold-era (AlphaStar, MuZero)
- **Collaborators:** David Silver (7 papers), Timothy Lillicrap (5), Koray Kavukcuoglu (4)

## Honest Gaps
- No source explains why games were chosen as the primary testbed — whether this was strategic (public attention) or principled (games as well-defined RL environments).
- The Lee Sedol match itself has no primary account from Hassabis — only a book review.
- The decision to stop pursuing game-playing milestones after MuZero/AlphaStar is not documented.
- No comparison papers evaluate DeepMind's game-playing approaches against alternatives from other labs.
- The public discourse around "AI beating humans at games" and its societal impact is not in the corpus.