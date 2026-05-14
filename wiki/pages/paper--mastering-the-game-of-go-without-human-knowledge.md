# Mastering the Game of Go without Human Knowledge

**Type:** paper
**Slug:** mastering-the-game-of-go-without-human-knowledge---hassabis
**Sources:** mastering-the-game-of-go-without-human-knowledge---hassabis
**Last updated:** 2026-05-13

---

## Summary
Silver, Schrittwieser, Simonyan, Antonoglou, Huang, Guez, Hubert, Baker, Lai, Bolton, Chen, Lillicrap, Fan Hui, Sifre, van den Driessche, Graepel, and Hassabis (2017) introduced AlphaGo Zero, which achieved superhuman Go playing entirely from self-play reinforcement learning with no human game data. Starting from random play, AlphaGo Zero trained for 40 days defeated the previously published AlphaGo (which used human expert data) by 100–0, and defeated the version that beat Lee Sedol 3–0. A single neural network was trained end-to-end to predict both move probabilities and position values.

## Core content

**Key simplification:** Unlike the original AlphaGo's three-stage pipeline (SL policy → RL policy → value network), AlphaGo Zero uses a single residual CNN that outputs both a policy (move probabilities) and a value (win probability), trained purely by self-play (paper--mastering-the-game-of-go-without-human-knowledge §Methods).

**Training:** Self-play games are generated continuously. The network is trained to maximize the likelihood of its own search-improved moves (policy loss) and minimize the error between its predicted value and the game outcome (value loss), plus an L2 regularization term (paper--mastering-the-game-of-go-without-human-knowledge §Methods).

**Search:** MCTS using the neural network for both prior probabilities and leaf evaluation — no random rollouts (paper--mastering-the-game-of-go-without-human-knowledge §Methods).

**Key results:**
- After 36 hours of self-play, AlphaGo Zero defeated the version of AlphaGo that beat Fan Hui (paper--mastering-the-game-of-go-without-human-knowledge §Results).
- After 40 days, defeated the Lee Sedol version 100–0 (paper--mastering-the-game-of-go-without-human-knowledge §Results).
- Achieved Elo ~5,000+ (far above human professional level of ~3,500) (paper--mastering-the-game-of-go-without-human-knowledge §Results).
- Trained on 4 TPUs (29 million self-play games) — far less compute than distributed AlphaGo (paper--mastering-the-game-of-go-without-human-knowledge §Methods).
- Learned classic Go openings (fuseki) and joseki patterns from scratch, discovering some known human patterns and novel ones (paper--mastering-the-game-of-go-without-human-knowledge §Results).

**Significance:** Demonstrated that human knowledge is not necessary for superhuman performance — pure self-play suffices. Simplified the architecture and reduced compute requirements dramatically.

## Connections- **Theme:** [theme--self-play](pages/theme--self-play.md), [theme--game-playing-ai](pages/theme--game-playing-ai.md), go, [theme--deep-RL](pages/theme--deep-RL.md)
- **Project:** AlphaGo-Zero
- **Collaborators:** David Silver (co-first), Julian Schrittwieser (co-first), Karen Simonyan (co-first), Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton, Yutian Chen, Timothy Lillicrap, Fan Hui, Laurent Sifre, George van den Driessche, Thore Graepel
- **Era:** deepmind-ascent
- **Venue:** venue--Nature (front page)
- **Supersedes:** paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search
- **Precedes:** paper--mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model — AlphaZero generalized to chess and shogi

## Honest Gaps
- Metadata lists only 4 co-authors; the actual paper has 17 authors.
- The comparison to Lee Sedol's AlphaGo is against a single-network version, not the exact distributed system used in the match.
- While "no human knowledge" is technically true, the architecture (residual CNN + MCTS) and reward design (win/loss) encode significant prior structural assumptions.
- The claim that AlphaGo Zero "rediscovered" human Go knowledge is based on post-hoc pattern matching rather than formal analysis.
- 40 days of 4-TPU training still represents substantial compute (~$170K+ in cloud costs at 2017 prices).