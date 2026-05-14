# DeepMind Ascent (2015–2018)

**Type:** period
**Slug:** period--deepmind-ascent
**Sources:** a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go--hassabis, artificial-intelligence-chess-match-of-the-century--hassabis, clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease--hassabis, computations-underlying-social-hierarchy-learning--hassabis, human-level-performance-in-3d-multiplayer-games-with-population-based-rl--hassabis, hybrid-computing-using-a-neural-network-with-dynamic-external-memory--hassabis, mastering-the-game-of-go-with-deep-neural-networks-and-tree-search--hassabis, mastering-the-game-of-go-without-human-knowledge---hassabis, neural-mechanisms-of-hierarchical-planning-in-a-virtual-subway-network--hassabis, neural-scene-representation-and-rendering--hassabis, neuroscience-inspired-artificial-intelligence--hassabis, overcoming-catastrophic-forgetting-in-neural-networks--hassabis, prefrontal-cortex-as-a-meta-reinforcement-learning-system--hassabis, semantic-representations-in-the-temporal-pole-predict-false-memories--hassabis, what-learning-systems-do-intelligent-agents-need-complementary-learning-systems-theory-updated--hassabis
**Last updated:** 2026-05-13

---

## Summary
The most prolific and intellectually diverse period in the corpus, with 15 publications across game-playing AI, neuroscience theory, clinical AI, and cognitive neuroscience. The era is anchored by three game-playing milestones — AlphaGo (2016), AlphaGo Zero (2017), and AlphaZero (2018) — but its distinctive intellectual contribution is the neuroscience-AI bridge programme: four papers (Botvinick/Kumaran/Dayan/Dolan collaborations) that explicitly connected hippocampal and prefrontal neuroscience to RL architectures, culminating in the canonical Neuron review "Neuroscience-Inspired Artificial Intelligence" (2017).

## Core content

**The Go sequence (2016–2018):** Three papers trace a rapid evolution. AlphaGo (paper--mastering-the-game-of-go-with-deep-neural-networks-and-tree-search) combined deep neural networks with Monte Carlo tree search, supervised from human expert games, to defeat Fan Hui and Lee Sedol. AlphaGo Zero (paper--mastering-the-game-of-go-without-human-knowledge) removed human data entirely, learning from self-play alone to surpass AlphaGo in 40 days. AlphaZero (paper--a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go) generalised the self-play approach to chess and shogi, achieving superhuman play in all three games with a single architecture. The intellectual arc is from human-guided → self-taught → general.

**The neuroscience-AI bridge (2016–2017):** Four papers with the Botvinick/Kumaran/Dayan/Dolan group. The Neuron review (paper--neuroscience-inspired-artificial-intelligence) is the canonical statement, arguing that neuroscience can contribute specific, implementable ideas to AI (not just vague inspiration). Supporting papers: meta-RL in prefrontal cortex (paper--prefrontal-cortex-as-a-meta-reinforcement-learning-system), complementary learning systems updated for AI agents (paper--what-learning-systems-do-intelligent-agents-need-complementary-learning-systems-theory-updated), and hierarchical planning in the hippocampus (paper--neural-mechanisms-of-hierarchical-planning-in-a-virtual-subway-network).

**Continued hippocampal research (2016):** Two papers extending the PhD programme with new collaborators — social hierarchy learning (paper--computations-underlying-social-hierarchy-learning) and false memory prediction from temporal pole semantics (paper--semantic-representations-in-the-temporal-pole-predict-false-memories).

**AI systems advances (2016–2017):** DNC (paper--hybrid-computing-using-a-neural-network-with-dynamic-external-memory) added differentiable external memory to neural networks. Population-based RL (paper--human-level-performance-in-3d-multiplayer-games-with-population-based-rl) achieved human-level play in Quake III capture-the-flag. GQN (paper--neural-scene-representation-and-rendering) learned to render 3D scenes from novel viewpoints without explicit 3D representation — a construction-system-like approach to visual scenes.

**Continual learning (2017):** Elastic weight consolidation (paper--overcoming-catastrophic-forgetting-in-neural-networks) addressed the catastrophic forgetting problem by selectively slowing learning on important weights, drawing on synaptic consolidation in neuroscience.

**Clinical AI (2016, 2018):** Retinal disease diagnosis (paper--clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease) demonstrated that deep learning could match expert ophthalmologists on referral decisions — DeepMind's first clinical deployment paper.

**Public writing (2016):** A Nature book review (paper--artificial-intelligence-chess-match-of-the-century) on the AlphaGo vs Lee Sedol match, framing it as a test of human creativity.

## Connections
- **Themes:** theme--game-playing-AI, theme--go, theme--chess, theme--neuroscience-AI-bridge, theme--deep-RL, theme--reinforcement-learning, theme--hippocampal-construction, theme--self-play
- **Projects:** project--AlphaGo, project--AlphaGo-Zero, project--AlphaZero, project--DNC, project--GQN, project--hippocampus-research, project--DeepMind-general
- **Collaborators:** David Silver (5 papers), Timothy Lillicrap (4), Koray Kavukcuoglu (3), Dharshan Kumaran (4), Matthew Botvinick (3), Peter Dayan (3), Raymond Dolan (3), Eleanor A. Maguire (2)
- **Venues:** venue--Nature (5), venue--Neuron (3), venue--Science (2), venue--PNAS (2), venue--Current-Biology (1), venue--Nature-Medicine (1)
- **Succeeds:** period--early-deepmind — DQN's deep RL paradigm explodes into multiple domains
- **Precedes:** period--alphafold-era — the self-play and generalisation ideas mature into AlphaFold

## Honest Gaps
- Several 2018 papers (neural-scene-representation, vector-based-navigation) are classified as "alphafold-era" in metadata but chronologically belong here — the era boundary (2018) is fuzzy.
- The neuroscience-AI bridge papers are authored primarily by Botvinick/Kumaran/Dayan/Dolan with Hassabis as senior author — the degree of Hassabis's direct intellectual contribution vs. lab-leadership role is unclear.
- No sources from this period document the internal debate about pursuing games vs. protein folding vs. clinical applications.
- The Lee Sedol match (March 2016) was a major cultural event but only a book review covers it — no primary account from Hassabis.
- The clinical AI paper (retinal disease) sits thematically apart from the rest of the era — no bridge paper connects it to the game-playing or neuroscience work.