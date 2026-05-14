---
title: "Self-Play"
tags:
  - theme
description: "Self-play is the training paradigm in which an agent improves by playing against itself rather than learning from human data."
date: 2026-05-13
---

# Self-Play

**Type:** theme
**Slug:** theme--self-play
**Sources:** mastering-the-game-of-go-without-human-knowledge---hassabis, a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go--hassabis, grandmaster-level-in-starcraft-ii-using-multi-agent-rl--hassabis, mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model--hassabis
**Last updated:** 2026-05-13

---

## Summary
Self-play is the training paradigm in which an agent improves by playing against itself rather than learning from human data. Four corpus papers (2017–2020) demonstrate its transformative power: AlphaGo Zero learned Go from scratch in 40 days, AlphaZero generalised this to chess and shogi, MuZero added learned environment models, and AlphaStar extended it to StarCraft II. The intellectual significance is that self-play eliminates the need for human expertise as a training signal — the environment itself provides the curriculum.

## Core content

**The founding result (2017):** AlphaGo Zero (paper--mastering-the-game-of-go-without-human-knowledge) is the canonical self-play paper. Starting from random play, a single RL agent trained entirely through self-play surpassed the supervised-learning-based AlphaGo (which had trained on human expert games) in 40 days. The title is programmatic: "without human knowledge."

**Generalisation (2018):** AlphaZero (paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go) demonstrated that the same self-play algorithm, with no game-specific tuning, achieves superhuman play in Go, chess, and shogi — evidence that self-play discovers strategies beyond human knowledge.

**Learned models (2020):** MuZero (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model) combined self-play with learned environment dynamics, planning without knowing the game rules.

**Multi-agent (2019):** AlphaStar (paper--grandmaster-level-in-starcraft-ii-using-multi-agent-rl) used league-based self-play with a population of diverse agents, extending self-play to asymmetric multi-agent settings.

## Connections
- **Theme:** theme--game-playing-AI, theme--deep-RL
- **Projects:** project--AlphaGo-Zero, project--AlphaZero, project--MuZero, project--AlphaStar
- **Periods:** period--deepmind-ascent, period--alphafold-era
- **Collaborators:** David Silver (all 4), Timothy Lillicrap (3)

## Honest Gaps
- No corpus paper analyses why self-play works so well — whether it's related to optimal curriculum learning, exploration efficiency, or something else.
- Self-play has not been applied to non-game domains in this corpus — the transfer potential is undiscussed.
- AlphaGo (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search) used supervised pre-training + self-play, not pure self-play — it's excluded from this theme's core sources.