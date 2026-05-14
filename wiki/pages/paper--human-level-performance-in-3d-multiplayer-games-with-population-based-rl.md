# Human-Level Performance in First-Person Multiplayer Games with Population-Based Deep Reinforcement Learning

**Type:** paper
**Slug:** human-level-performance-in-3d-multiplayer-games-with-population-based-rl--hassabis
**Sources:** human-level-performance-in-3d-multiplayer-games-with-population-based-rl--hassabis
**Last updated:** 2026-05-13

---

## Summary
Jaderberg, Czarnecki, Dunning, Marris, Lever, Garcia Castaneda, Beattie, Rabinowitz, Morcos, Ruderman, Sonnerat, Green, Deason, Leibo, Silver, Hassabis, Kavukcuoglu, and Graepel (2019) introduced a population-based deep reinforcement learning approach that achieved human-level performance in Quake III Arena Capture the Flag, a 3D first-person multiplayer game requiring teamwork, real-time decision-making, and diverse strategies. Agents learned end-to-end from raw pixel inputs using a two-timescale architecture.

## Core content

**Challenge:** Quake III Arena CTF requires coordination between two agents on a team (own half of the map, follow/defend), navigation in a 3D environment, and strategic adaptation to opponents — far beyond prior single-agent or two-player turn-based results (paper--human-level-performance-in-3d-multiplayer-games-with-population-based-rl §Introduction).

**Architecture:** Two-timescale design (paper--human-level-performance-in-3d-multiplayer-games-with-population-based-rl §Methods):
- **Fast timescale:** A standard deep RL agent (convolutional encoder + LSTM core + policy/value heads) controlling one player, trained with PPO.
- **Slow timescale:** A population of agents undergoes evolutionary selection, with the best-performing agents selected as ancestors for the next generation.

**Key results:**
- Population-trained agents achieved a win rate comparable to human players (strong-but-not-top human skill level) when matched against both human-human and agent-human teams (paper--human-level-performance-in-3d-multiplayer-games-with-population-based-rl §Results).
- Agents developed emergent behaviors: following teammates, defending the base, camping strategic positions (paper--human-level-performance-in-3d-multiplayer-games-with-population-based-rl §Results).
- Ablation showed population-based training was essential — single-agent training failed to develop cooperative strategies (paper--human-level-performance-in-3d-multiplayer-games-with-population-based-rl §Results).
- Human evaluation with 40 human participants; agents were not distinguishable from human teammates in blind ratings (paper--human-level-performance-in-3d-multiplayer-games-with-population-based-rl §Results).

## Connections- **Theme:** [theme--deep-RL](pages/theme--deep-RL.md), [theme--game-playing-ai](pages/theme--game-playing-ai.md), multi-agent
- **Project:** DeepMind-general
- **Collaborators:** Max Jaderberg (co-first), Wojciech M. Czarnecki (co-first), Iain Dunning (co-first), Luke Marris, Guy Lever, Antonio Garcia Castaneda, Charles Beattie, Neil C. Rabinowitz, Ari S. Morcos, Avraham Ruderman, Nicolas Sonnerat, Tim Green, Louise Deason, Joel Z. Leibo, David Silver, Koray Kavukcuoglu, Thore Graepel
- **Era:** deepmind-ascent
- **Venue:** venue--Science
- **Builds on:** paper--human-level-control-through-deep-reinforcement-learning — extends DQN methodology to 3D multiplayer

## Honest Gaps
- Metadata lists only 3 co-authors (Jaderberg, Silver, Lillicrap); the actual paper has 17 authors and Timothy Lillicrap is NOT among them.
- Agents were trained on a limited set of procedurally generated map layouts, not the full diversity of Quake III maps.
- "Human-level" is qualified — agents matched average human players but were not tested against top competitive players.
- The population-based training required hundreds of millions of environment steps across thousands of agents.
- Internal communication between agents is implicit (shared observations only), not explicit — limiting coordination complexity.