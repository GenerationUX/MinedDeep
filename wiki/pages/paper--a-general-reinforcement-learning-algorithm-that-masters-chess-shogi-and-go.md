---
title: "A General Reinforcement Learning Algorithm That Masters Chess, Shogi, and Go Through Self-Play"
tags:
  - peer-reviewed-paper
  - self-play
  - game-playing-ai
  - chess
  - go
  - deep-rl
  - reinforcement-learning
  - deepmind-ascent
  - AlphaZero
description: "Silver, Schrittwieser, Antonoglou, Guez, Lanctot, and colleagues, with Simonyan, Kavukcuoglu, and Hassabis (2017) introduced AlphaZero, a single reinforcement…"
date: 2018-01-01
---

# A General Reinforcement Learning Algorithm That Masters Chess, Shogi, and Go Through Self-Play

**Type:** paper
**Slug:** a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go--hassabis
**Sources:** a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go--hassabis
**Last updated:** 2026-05-13

---

## Summary
Silver, Schrittwieser, Antonoglou, Guez, Lanctot, and colleagues, with Simonyan, Kavukcuoglu, and Hassabis (2017) introduced AlphaZero, a single reinforcement learning algorithm that achieved superhuman performance in chess, shogi, and Go using only self-play and no domain-specific knowledge beyond the game rules. AlphaZero learned each game from scratch in hours, defeated the previous state-of-the-art programs (Stockfish, Elmo, AlphaGo Zero), and demonstrated that a general-purpose RL algorithm can match or exceed hand-crafted solutions across diverse game domains.

## Core content

**Key departure from prior work:** Unlike AlphaGo (which used human expert data and hand-crafted features) or traditional chess engines (which use alpha-beta search with extensive human-engineered heuristics), AlphaZero uses a single neural network trained entirely through self-play (paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go §Introduction).

**Algorithm:**
- **Neural network:** Residual network taking the board state as input, outputting both a policy (move probabilities) and a value (expected outcome) (paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go §Methods).
- **MCTS with learned policy:** Monte Carlo tree search guided by the neural network's policy for prior probabilities and value for leaf evaluation (paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go §Methods).
- **Self-play training:** The network is updated from self-play games, with MCTS as the policy improvement operator and the network as the value function approximator (paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go §Methods).

**Results:**
- **Chess:** Defeated Stockfish (TCEC season 9 champion) 64-36 in a 100-game match after just 4 hours of self-play training (paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go §Results).
- **Shogi:** Defeated Elmo (world champion program) 90-8 in a 100-game match after 2 hours of training (paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go §Results).
- **Go:** Defeated AlphaGo Zero (which itself defeated Lee Sedol) 60-40, after just 8 hours of training (paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go §Results).

**Significance:** Demonstrated that deep RL can discover sophisticated strategies from first principles, without any human knowledge. AlphaZero's chess play was described as "alien" — developing openings and strategies that humans had never considered.

## Connections- **Theme:** [theme--self-play](pages/theme--self-play.md), [theme--game-playing-ai](pages/theme--game-playing-ai.md), chess, go, [theme--deep-RL](pages/theme--deep-RL.md)
- **Project:** AlphaZero
- **Collaborators:** David Silver (first), Julian Schrittwieser, Ioannis Antonoglou, Arthur Guez, Marc Lanctot, Timothy Lillicrap, Karen Simonyan
- **Era:** deepmind-ascent
- **Venue:** venue--Science
- **Supersedes:** paper--mastering-the-game-of-go-without-human-knowledge — AlphaZero is the generalized successor to AlphaGo Zero
- **Notable quote:** "The tabula rasa approach of AlphaZero yields a novel and distinctive playing style." (paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go §Discussion)

## Honest Gaps
- Metadata lists 7 co-authors but the actual paper has additional authors.
- The PDF extraction has scanning artefacts with merged/jammed text — some sections may be hard to parse.
- AlphaZero required enormous compute (5,000 first-generation TPUs for training, 64 second-generation TPUs for MCTS).
- The match conditions against Stockfish favored AlphaZero (fixed search time per move rather than fixed total time).
- AlphaZero learns from scratch each time — it cannot transfer knowledge between games despite using the same architecture.
- No code or trained models were released.