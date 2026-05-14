# Human-Level Control Through Deep Reinforcement Learning

**Type:** paper
**Slug:** human-level-control-through-deep-reinforcement-learning--hassabis
**Sources:** human-level-control-through-deep-reinforcement-learning--hassabis
**Last updated:** 2026-05-13

---

## Summary
Mnih, Kavukcuoglu, Silver, Rusu, Veness, Bellemare, Graves, Riedmiller, Fidjeland, Ostrovski, Petersen, Beattie, Sadik, Antonoglou, King, Kumaran, Wierstra, Legg, and Hassabis (2015) introduced the Deep Q-Network (DQN), the first AI system to achieve human-level performance across a diverse range of Atari 2600 games using only raw pixel inputs. The key innovation was combining deep convolutional neural networks with reinforcement learning, stabilized by experience replay and a target network.

## Core content

**Problem:** Previous RL successes required hand-crafted features or were limited to simple domains. Atari games present high-dimensional visual input (210×160 RGB pixels), diverse game mechanics, and partial observability (paper--human-level-control-through-deep-reinforcement-learning §Introduction).

**Architecture:** A deep convolutional neural network takes raw pixels (downsampled to 84×84, last 4 frames stacked) as input and outputs Q-values for each of 18 possible actions. Three convolutional layers followed by two fully connected layers (paper--human-level-control-through-deep-reinforcement-learning §Methods).

**Key innovations:**
- **Experience replay:** Store transitions (s, a, r, s') in a replay buffer and sample random mini-batches for training. Breaks correlations between consecutive experiences and improves data efficiency (paper--human-level-control-through-deep-reinforcement-learning §Methods).
- **Target network:** A separate, periodically-updated copy of the Q-network provides stable targets for the Bellman equation, preventing oscillations and divergence (paper--human-level-control-through-deep-reinforcement-learning §Methods).
- **Reward clipping:** Clip rewards to {−1, 0, +1} to bound error magnitudes across games with different reward scales (paper--human-level-control-through-deep-reinforcement-learning §Methods).
- **Frame skipping and max-pooling:** Skip 4 frames and take max over last 2 to reduce temporal resolution and handle flickering (paper--human-level-control-through-deep-reinforcement-learning §Methods).

**Results:**
- DQN matched or exceeded human expert performance on 29 of 49 games, achieving >75% of human score on 43 games (paper--human-level-control-through-deep-reinforcement-learning §Results).
- On 22 games, DQN achieved >95% of human performance (paper--human-level-control-through-deep-reinforcement-learning §Results).
- Strongest performance on games requiring precise control (Breakout, Pong) and planning (Seaquest); weakest on games requiring long temporal dependencies (Montezuma's Revenge) (paper--human-level-control-through-deep-reinforcement-learning §Results).
- Ablation showed both experience replay and target network were critical — removing either caused training instability (paper--human-level-control-through-deep-reinforcement-learning §Discussion).

**Significance:** First demonstration that deep RL can learn successful policies directly from raw sensory input across diverse tasks. Catalyzed the deep RL field.

## Connections- **Theme:** reinforcement-learning, [theme--deep-RL](pages/theme--deep-RL.md)
- **Project:** DQN
- **Collaborators:** Volodymyr Mnih, Koray Kavukcuoglu, David Silver (co-first), Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg
- **Era:** early-deepmind
- **Venue:** venue--Nature
- **Precedes:** paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search — AlphaGo built on DQN's RL methodology
- **Influences:** Minh et al. (2013) playing Atari with DQN (NIPS workshop); Sutton & Barto (1998); Mnih et al. (2015) human-level control is the journal version
- **Notable quote:** "We demonstrate that a single architecture can successfully learn control policies in a range of different environments with only very minimal prior knowledge." (paper--human-level-control-through-deep-reinforcement-learning §Abstract)

## Honest Gaps
- Metadata lists only 3 co-authors; the actual paper has 19 authors.
- DQN fails on games requiring long-horizon planning (Montezuma's Revenge: 0% of human score) — an acknowledged limitation that motivated later work on curiosity-driven exploration and hierarchical RL.
- The "human-level" claim averages across games; performance on many individual games was well below human level.
- The comparison to "human expert" used a single human player for only ~10 games; the rest used a heuristic baseline or a small number of human sessions.
- Training required 50–200 million frames per game (~50–200 hours of game time), far beyond human learning efficiency.
- No transfer learning between games — a separate network was trained from scratch for each game.