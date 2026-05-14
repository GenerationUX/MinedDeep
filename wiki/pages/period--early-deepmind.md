---
title: "Early DeepMind (2010–2015)"
tags:
  - period
description: "The period from DeepMind's founding (2010) through its first landmark publication (2015) is represented in the corpus by a single paper — the DQN paper in…"
date: 2026-05-13
---

# Early DeepMind (2010–2015)

**Type:** period
**Slug:** period--early-deepmind
**Sources:** human-level-control-through-deep-reinforcement-learning--hassabis
**Last updated:** 2026-05-13

---

## Summary
The period from DeepMind's founding (2010) through its first landmark publication (2015) is represented in the corpus by a single paper — the DQN paper in Nature — but this paper's impact vastly exceeds its solitary status. Human-level control through deep reinforcement learning (paper--human-level-control-through-deep-reinforcement-learning) demonstrated that a single neural network architecture, trained end-to-end with RL, could achieve human-level performance across 29 Atari games. This result validated DeepMind's foundational bet that deep learning and reinforcement learning could be unified into a general-purpose learning system.

## Core content

**The DQN result (2015):** A convolutional neural network trained with Q-learning and experience replay learned to play 29 Atari 2600 games from raw pixel input, achieving human-level or superhuman performance on 23 of them (paper--human-level-control-through-deep-reinforcement-learning). Two key technical innovations made this possible: experience replay (storing and sampling past transitions to break temporal correlations) and a target network (a slowly-updated copy of the Q-network to stabilise training).

**Intellectual context:** While the corpus has no publications from 2010–2014, the DQN paper's approach reflects ideas traceable to the PhD period — the construction system's emphasis on recombining stored elements (experience replay as a form of constructive memory) and the neuroscience literature on model-free reinforcement learning that Hassabis would have encountered in the Maguire/Dolan labs.

**Impact profile:** This paper is both field-defining and top-cited. It established DeepMind as a serious research lab, contributed to Google's acquisition (2014), and set the template for the "deep RL" paradigm that dominated the next five years of the lab's output.

## Connections
- **Theme:** theme--deep-RL, theme--reinforcement-learning
- **Project:** project--DQN
- **Collaborators:** Volodymyr Mnih (first author), Koray Kavukcuoglu, David Silver
- **Venue:** venue--Nature
- **Succeeds:** period--postdoc-period (5-year publication gap)
- **Precedes:** period--deepmind-ascent — the DQN approach is extended and generalised across the next era's papers
- **Precedes:** paper--overcoming-catastrophic-forgetting — directly addresses DQN's stability limitations

## Honest Gaps
- The 2010–2014 publication gap is the largest in the corpus. No papers, essays, or public statements from DeepMind's founding years are present.
- No sources document the intellectual transition from hippocampal construction to deep RL — how (or whether) the neuroscience ideas explicitly informed DQN's design.
- The DQN paper has ~6 authors in metadata but the actual Nature paper lists more — co-author undercount likely.
- No blog posts, interviews, or technical reports from this period are in the corpus, despite DeepMind being publicly active.
- This is the only period where the corpus is essentially a single data point — any synthesis is necessarily speculative.