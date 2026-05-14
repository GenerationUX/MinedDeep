# DQN (Deep Q-Network)

**Type:** project
**Slug:** project--DQN
**Sources:** human-level-control-through-deep-reinforcement-learning--hassabis, overcoming-catastrophic-forgetting-in-neural-networks--hassabis
**Last updated:** 2026-05-13

---

## Summary
DQN is the first DeepMind project to demonstrate that deep neural networks combined with reinforcement learning can achieve human-level performance across diverse tasks. Published in Nature (2015), DQN played 29 Atari 2600 games from raw pixel input, achieving human-level or superhuman performance on 23. Its two key innovations — experience replay and target networks — became standard in deep RL. The project established DeepMind as a serious research lab and contributed to Google's 2014 acquisition.

## Core content

**Architecture (paper--human-level-control-through-deep-reinforcement-learning):** A convolutional neural network takes raw 210×160 pixel frames as input, outputs Q-values for each of 18 possible actions. Trained with Q-learning using two stabilisation innovations: (1) experience replay — storing transitions in a replay buffer and sampling random mini-batches to break temporal correlations; (2) target network — a slowly-updated copy of the Q-network that provides stable targets for TD learning.

**Results:** Human-level or superhuman on 23/29 games. Strongest on games requiring precise control (Breakout, Enduro); weakest on games requiring long-horizon planning (Montezuma's Revenge).

**Continual learning extension (paper--overcoming-catastrophic-forgetting-in-neural-networks):** Elastic weight consolidation (EWC) addressed DQN's vulnerability to catastrophic forgetting when learning sequentially across games, drawing on synaptic consolidation in neuroscience.

**Key personnel:** Volodymyr Mnih (first author), Koray Kavukcuoglu, David Silver, Ioannis Antonoglou, Daan Wierstra, Demis Hassabis.

## Connections
- **Theme:** theme--deep-RL, theme--reinforcement-learning, theme--game-playing-AI
- **Period:** period--early-deepmind
- **Precedes:** project--AlphaGo (DQN's deep RL paradigm extended to Go)

## Honest Gaps
- The 2010–2014 development history is entirely absent from the corpus.
- No source documents whether the neuroscience background of the lab influenced DQN's design (e.g., experience replay as analogous to hippocampal replay).
- The actual Nature paper has more authors than listed in metadata.
- No comparison with contemporaneous deep RL approaches from other labs.