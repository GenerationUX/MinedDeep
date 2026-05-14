# Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model

**Type:** paper
**Slug:** mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model--hassabis
**Sources:** mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model--hassabis
**Last updated:** 2026-05-13

---

## Summary
Schrittwieser, Antonoglou, Hubert, Simonyan, Sifre, Schmitt, Guez, Lockhart, Hassabis, Graepel, Lillicrap, and Silver (2020) introduced MuZero, a reinforcement learning system that achieves superhuman performance in board games (Go, chess, shogi) and Atari games without knowing the rules or state transitions of the environment. MuZero learns a dynamics model of the environment from experience and uses it for planning via Monte Carlo tree search — a major advance toward general-purpose model-based RL.

## Core content

**Core problem addressed:** AlphaZero requires the rules of the game (the transition function) to be provided. MuZero removes this requirement by learning the dynamics model itself (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model §Introduction).

**Three learned functions:**
1. **Representation function:** Maps the observed state (e.g., raw pixels in Atari) to a hidden state (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model §Methods).
2. **Dynamics function:** Predicts the next hidden state and immediate reward given a hidden state and action (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model §Methods).
3. **Prediction function:** Maps the hidden state to policy and value predictions (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model §Methods).

**Planning with learned models:** MCTS operates entirely in the learned latent space — the real environment is only queried to obtain the initial observation and to execute the chosen action (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model §Methods).

**Results:**
- Matched AlphaZero in Go, chess, and shogi despite not knowing the game rules (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model §Results).
- Achieved a new state of the art on 57 Atari games, outperforming both model-free methods (DQN, Rainbow) and prior model-based approaches (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model §Results).
- Demonstrated that learned dynamics models can be accurate enough for effective long-horizon planning (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model §Results).

**Significance:** MuZero demonstrated that model-based planning can scale to complex domains, bridging the gap between model-free RL (which works but doesn't plan) and classical planning (which plans but requires known models).

## Connections- **Theme:** [theme--deep-RL](pages/theme--deep-RL.md), model-based-RL, [theme--game-playing-ai](pages/theme--game-playing-ai.md), chess
- **Project:** MuZero
- **Collaborators:** Julian Schrittwieser (co-first), Ioannis Antonoglou (co-first), Thomas Hubert (co-first), David Silver (co-first), Karen Simonyan, Laurent Sifre, Simon Schmitt, Arthur Guez, Edward Lockhart, Thore Graepel, Timothy Lillicrap
- **Era:** alphafold-era
- **Venue:** venue--Nature
- **Extends:** paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go — MuZero generalizes AlphaZero by removing the need for known rules
- **Notable quote:** "MuZero achieves state-of-the-art performance on Atari, matching the performance of the AlphaZero algorithm on board games without any access to the environment dynamics." (paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model §Abstract)

## Honest Gaps
- Metadata lists 4 co-authors; the actual paper has 12 authors.
- The learned dynamics model can accumulate errors over long planning horizons, though MuZero's re-analysis strategy mitigates this.
- Performance on Atari, while strong, still falls short of the best model-free methods (e.g., Agent57) on some individual games.
- The computational cost of MCTS with learned models is substantial — MuZero requires more compute per decision than model-free methods.
- No code or models were released.
- The PDF extraction has merged text (no spaces between words) in author names and some body text.