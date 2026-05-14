# Grandmaster Level in StarCraft II Using Multi-Agent Reinforcement Learning

**Type:** paper
**Slug:** grandmaster-level-in-starcraft-ii-using-multi-agent-rl--hassabis
**Sources:** grandmaster-level-in-starcraft-ii-using-multi-agent-rl--hassabis
**Last updated:** 2026-05-13

---

## Summary
Vinyals, Babuschkin, Czarnecki, Mathieu, and 36 colleagues, with Apps, Lillicrap, Kavukcuoglu, Hassabis, and Silver (2019) developed AlphaStar, an AI system that achieved grandmaster level in StarCraft II, a real-time strategy game considered one of the most challenging AI benchmarks. AlphaStar used a multi-agent league training system where diverse agents played against each other, combined with a deep neural network architecture that processed the game's raw feature maps.

## Core content

**Why StarCraft II is hard:** Imperfect information (fog of war), enormous action space (~10^26 possible actions per step), real-time decision-making (not turn-based), and the need for long-term strategic planning alongside tactical micro-management (paper--grandmaster-level-in-starcraft-ii-using-multi-agent-rl §Introduction).

**Architecture:** A deep neural network with a transformer torso processing game features (unit types, positions, visibility), an LSTM core for temporal reasoning, and separate heads for action selection and autoregressive action argument generation (paper--grandmaster-level-in-starcraft-ii-using-multi-agent-rl §Methods).

**Multi-agent league training:**
- **Main agents:** Trained via self-play with supervised learning initialization from human replays (paper--grandmaster-level-in-starcraft-ii-using-multi-agent-rl §Methods).
- **League exploitation:** "League" of diverse agents with different objectives (main agents, league exploiters, main exploiters) that prevent strategic cycles and ensure coverage of diverse strategies (paper--grandmaster-level-in-starcraft-ii-using-multi-agent-rl §Methods).
- This approach addressed the rock-paper-scissors dynamics that plagued prior StarCraft AI efforts (paper--grandmaster-level-in-starcraft-ii-using-multi-agent-rl §Discussion).

**Results:**
- Defeated 99.8% of active human players on official Battle.net ladders (paper--grandmaster-level-in-starcraft-ii-using-multi-agent-rl §Results).
- Achieved grandmaster rank (top 0.2% of human players) on all three StarCraft II races (paper--grandmaster-level-in-starcraft-ii-using-multi-agent-rl §Results).
- Live matches against professional players showed strong but not superhuman performance (paper--grandmaster-level-in-starcraft-ii-using-multi-agent-rl §Results).

## Connections- **Theme:** [theme--game-playing-ai](pages/theme--game-playing-ai.md), starcraft
- **Project:** AlphaStar
- **Collaborators:** Oriol Vinyals (co-first), Igor Babuschkin (co-first), Wojciech M. Czarnecki (co-first), Michaël Mathieu (co-first), Chris Apps (co-first), David Silver (co-first), Max Jaderberg, Aja Huang, Timothy Lillicrap, Koray Kavukcuoglu, and ~30 additional authors
- **Era:** alphafold-era
- **Venue:** venue--Nature
- **Related:** paper--a-general-[theme--deep-RL](pages/theme--deep-RL.md)-algorithm-that-masters-chess-shogi-and-go — both use [theme--self-play](pages/theme--self-play.md), but AlphaStar adds league training for strategic diversity

## Honest Gaps
- Metadata lists only 3 co-authors; the actual paper has ~44 authors.
- APM (actions per minute) was uncapped in initial versions, leading to superhuman micro that human critics argued was unrealistic. This was later addressed with an APM cap.
- AlphaStar was trained on a single map and matchup at a time — generalization across maps was not demonstrated.
- The live matches against professional players (TLO, MaNa) showed some weaknesses, particularly in unusual strategies.
- The league training system is computationally extremely expensive.
- No code or model was released.