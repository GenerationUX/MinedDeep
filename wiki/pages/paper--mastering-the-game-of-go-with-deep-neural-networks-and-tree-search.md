# Mastering the Game of Go with Deep Neural Networks and Tree Search

**Type:** paper
**Slug:** mastering-the-game-of-go-with-deep-neural-networks-and-tree-search--hassabis
**Sources:** mastering-the-game-of-go-with-deep-neural-networks-and-tree-search--hassabis
**Last updated:** 2026-05-13

---

## Summary
Silver, Huang, Maddison, Guez, Sifre, van den Driessche, Schrittwieser, Antonoglou, Panneershelvam, Lanctot, Dieleman, Grewe, Nham, Kalchbrenner, Sutskever, Lillicrap, Leach, Kavukcuoglu, Graepel, and Hassabis (2016) introduced AlphaGo, the first computer program to defeat a human professional Go player (Fan Hui, 2p European champion, 5–0) in the full-sized game. AlphaGo combined deep neural networks (policy network for move selection, value network for position evaluation) with Monte Carlo tree search, trained on human expert games and self-play reinforcement learning.

## Core content

**Why Go is hard:** The game tree has ~10^170 possible positions (more than atoms in the universe), and heuristic position evaluation was previously considered impossible due to the subtle, global nature of Go strategy (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search §Introduction).

**Training pipeline (three stages):**
1. **Supervised learning policy network (SL policy):** A 13-layer CNN trained on 30 million positions from the KGS Go server to predict human expert moves. Achieved 57% prediction accuracy on held-out data (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search §Methods).
2. **Reinforcement learning policy network (RL policy):** The SL network was further trained by self-play, optimizing for game outcomes rather than imitating humans. The RL policy won 80% of games against the SL policy (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search §Methods).
3. **Value network:** A CNN trained to predict the game winner from a board position, using 30 million self-play game positions (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search §Methods).

**Search algorithm:** MCTS modified to use the policy network to bias the search tree (reducing effective branching factor from ~250 to ~4) and the value network to evaluate leaf nodes (replacing random rollouts) (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search §Methods).

**Key results:**
- AlphaGo vs. Fan Hui: 5–0 in formal matches; estimated ~3 dan strength above Fan Hui (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search §Results).
- AlphaGo vs. other Go programs: 99.8% win rate in 500 games (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search §Results).
- Ablation: Each component contributed — removing the value network (pure MCTS rollouts) reduced Elo by ~600; removing the RL policy reduced it by ~200 (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search §Results).
- Distributed version used 1,202 CPUs and 176 GPUs (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search §Methods).

**Significance:** Go was the last classical board game where humans outperformed computers. This result, published on the Nature cover, was a landmark in AI that captured global public attention and set the stage for the Lee Sedol match (paper--mastering-the-game-of-go-without-human-knowledge).

## Connections- **Theme:** [theme--game-playing-ai](pages/theme--game-playing-ai.md), go, [theme--deep-RL](pages/theme--deep-RL.md)
- **Project:** AlphaGo
- **Collaborators:** David Silver (co-first), Aja Huang (co-first), Chris J. Maddison, Arthur Guez, Laurent Sifre, George van den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, Sander Dieleman, Dominik Grewe, John Nham, Nal Kalchbrenner, Ilya Sutskever, Timothy Lillicrap, Madeleine Leach, Koray Kavukcuoglu, Thore Graepel
- **Era:** deepmind-ascent
- **Venue:** venue--Nature (front page)
- **Precedes:** paper--mastering-the-game-of-go-without-human-knowledge — AlphaGo Zero removed human game data entirely
- **Precedes:** paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model — AlphaZero generalized across games
- **Builds on:** paper--human-level-control-through-deep-reinforcement-learning — DQN's deep RL methodology
- **Notable quote:** "This is the first time that a computer program has defeated a human professional player in the full-sized game of Go, a feat previously thought to be at least a decade away." (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search §Abstract)

## Honest Gaps
- Metadata lists only 7 co-authors; the actual paper has 20 authors.
- The opponent (Fan Hui, 2p) was a strong European amateur/professional but not a top-ranked player — the Lee Sedol match (5–1, March 2016) was the true landmark but is not described in this paper.
- The distributed version required enormous compute (~1,200 CPUs, 176 GPUs) — not accessible to most researchers.
- The training pipeline was complex (three separate training stages), raising questions about the generality of the approach.
- The value network was trained on self-play data from the RL policy, creating a dependency loop that could amplify biases.
- Move prediction accuracy (57%) means the policy network still disagrees with human experts on ~43% of moves.