# AlphaGo

**Type:** project
**Slug:** project--AlphaGo
**Sources:** mastering-the-game-of-go-with-deep-neural-networks-and-tree-search--hassabis, mastering-the-game-of-go-without-human-knowledge---hassabis, a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go--hassabis, artificial-intelligence-chess-match-of-the-century--hassabis
**Last updated:** 2026-05-13

---

## Summary
AlphaGo is the DeepMind project that defeated human Go champions, spanning three major systems: AlphaGo (2016, supervised + RL), AlphaGo Zero (2017, pure self-play), and AlphaZero (2018, general game-playing). The project demonstrated that deep RL could master Go — a game long considered intractable for AI due to its vast search space (10^170 positions) and the difficulty of evaluating board positions. The intellectual arc from AlphaGo to AlphaZero is the clearest progression in the corpus: from human-guided → self-taught → general.

## Core content

**AlphaGo (2016, paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search):** Three networks — a policy network (select moves), a value network (evaluate positions), and a fast rollout policy — combined with Monte Carlo tree search. The policy network was pre-trained on human expert games from the KGS Go server, then refined with self-play RL. Defeated Fan Hui 5-0 (October 2015) and Lee Sedol 4-1 (March 2016). Lee Sedol's Game 4 "hand of God" move exploited a blind spot in AlphaGo's evaluation.

**AlphaGo Zero (2017, paper--mastering-the-game-of-go-without-human-knowledge):** Eliminated human data entirely. A single network alternately plays policy and value roles, trained from random initialisation through self-play. Surpassed AlphaGo Lee Sedol in 40 days. The "without human knowledge" argument: self-play discovers strategies that humans never found.

**AlphaZero (2018, paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go):** Generalised the AlphaGo Zero architecture to chess and shogi with zero game-specific changes. Achieved superhuman play in all three. In chess, AlphaZero played in a distinctly non-human style (sacrificial, positional) that was analysed as genuinely creative.

**Public reception (2016, paper--artificial-intelligence-chess-match-of-the-century):** Hassabis's Nature book review framed the Lee Sedol match as testing human creativity, not just machine competence — a framing that shaped public discourse.

## Connections
- **Theme:** theme--game-playing-AI, theme--go, theme--chess, theme--self-play, theme--deep-RL
- **Period:** period--deepmind-ascent
- **Projects:** project--AlphaGo-Zero, project--AlphaZero (successor projects)
- **Collaborators:** David Silver, Aja Huang, Chris Maddison, Arthur Guez

## Honest Gaps
- No primary account from Hassabis about the Lee Sedol match experience — only a book review.
- The internal decision to pursue Go (vs. other games) is not documented.
- Game 4's "hand of God" move and the team's reaction are not described in any corpus source.
- The computational cost of training AlphaGo Zero is stated but not contextualised against AlphaGo v1.