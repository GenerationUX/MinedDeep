# Self-Play Is Sufficient for Superhuman Play

**Type:** claim
**Slug:** claim--self-play-sufficiency
**Sources:** mastering-the-game-of-go-without-human-knowledge---hassabis, a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go--hassabis
**Last updated:** 2026-05-13

---

## Summary
A reinforcement learning agent trained entirely through self-play, starting from random initialisation with no human data, can achieve superhuman performance in complex games. The "without human knowledge" argument — that self-play discovers strategies beyond human expertise — is the programmatic claim of the AlphaGo Zero and AlphaZero papers.

## Evidence
- AlphaGo Zero surpassed supervised-learning AlphaGo in 40 days from random play (paper--mastering-the-game-of-go-without-human-knowledge)
- AlphaZero achieved superhuman play in Go, chess, and shogi with identical architecture (paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go)
- AlphaZero's chess play was analysed as containing genuinely creative strategies not found in human play

## Status
Demonstrated for board games with perfect information (Go, chess, shogi). Extended to imperfect-information games (StarCraft II via AlphaStar) and learned environment models (MuZero) but with diminishing returns. Not demonstrated for non-game domains.

## Connections
- **Theme:** theme--self-play, theme--game-playing-AI
- **Projects:** project--AlphaGo (specifically AlphaGo Zero and AlphaZero)
- **Period:** period--deepmind-ascent

## Honest Gaps
- The claim is domain-restricted — no evidence it transfers to open-ended real-world problems.
- Why self-play works so well is not analytically understood in any corpus paper.
- AlphaStar required significant engineering beyond pure self-play (league training, human data for imitation learning phase).