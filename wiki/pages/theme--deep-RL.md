# Deep Reinforcement Learning

**Type:** theme
**Slug:** theme--deep-RL
**Sources:** human-level-control-through-deep-reinforcement-learning--hassabis, mastering-the-game-of-go-with-deep-neural-networks-and-tree-search--hassabis, mastering-the-game-of-go-without-human-knowledge---hassabis, a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go--hassabis, grandmaster-level-in-starcraft-ii-using-multi-agent-rl--hassabis, human-level-performance-in-3d-multiplayer-games-with-population-based-rl--hassabis, mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model--hassabis, overcoming-catastrophic-forgetting-in-neural-networks--hassabis
**Last updated:** 2026-05-13

---

## Summary
Deep reinforcement learning is the technical foundation of DeepMind's game-playing achievements and a recurring methodological theme across 8 papers (2015–2019). The theme captures the integration of deep neural networks with RL algorithms — DQN's key innovation — and its progressive generalisation from individual games to universal game-playing architectures. The arc runs from value-based RL (DQN) through policy search + self-play (AlphaGo) to learned models (MuZero), with continual learning (EWC) addressing a key limitation.

## Core content

**The DQN paradigm (2015):** Combining CNNs with Q-learning required two stabilisation tricks — experience replay and target networks (paper--human-level-control-through-deep-reinforcement-learning). These became standard in virtually all subsequent deep RL work.

**Self-play and policy gradients (2016–2018):** The Go sequence (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search, paper--mastering-the-game-of-go-without-human-knowledge---hassabis, paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go) moved from value-based to policy gradient methods, with self-play replacing supervised data as the training signal.

**Learned models (2020):** MuZero (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model) learned environment dynamics internally, a significant departure from model-free DQN.

**Multi-agent and population-based (2017, 2019):** Population-based RL (paper--human-level-performance-in-3d-multiplayer-games-with-population-based-rl) and AlphaStar (paper--grandmaster-level-in-starcraft-ii-using-multi-agent-rl) extended deep RL to multi-agent settings with population diversity.

**Continual learning (2017):** Elastic weight consolidation (paper--overcoming-catastrophic-forgetting-in-neural-networks) addressed catastrophic forgetting — a fundamental limitation of deep RL when agents must learn sequentially.

## Connections
- **Theme:** theme--reinforcement-learning, theme--self-play, theme--game-playing-AI
- **Projects:** project--DQN, project--AlphaGo, project--AlphaGo-Zero, project--AlphaZero, project--MuZero, project--AlphaStar
- **Periods:** period--early-deepmind through period--alphafold-era
- **Collaborators:** David Silver, Volodymyr Mnih, Timothy Lillicrap, Koray Kavukcuoglu

## Honest Gaps
- No papers in the corpus evaluate deep RL on real-world robotic or industrial tasks — all results are in game environments.
- Sample efficiency limitations are acknowledged but not substantially addressed in any corpus paper.
- The shift away from deep RL (post-2019, toward protein folding) is not explained.