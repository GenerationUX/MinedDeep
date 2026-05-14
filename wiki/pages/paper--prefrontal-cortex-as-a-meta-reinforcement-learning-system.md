# Prefrontal Cortex as a Meta-Reinforcement Learning System

**Type:** paper
**Slug:** prefrontal-cortex-as-a-meta-reinforcement-learning-system--hassabis
**Sources:** prefrontal-cortex-as-a-meta-reinforcement-learning-system--hassabis
**Last updated:** 2026-05-13

---

## Summary
Wang, Kurth-Nelson, Kumaran, Tirumala, Soyer, Leibo, Hassabis, and Botvinick (2018) proposed that the prefrontal cortex functions as a meta-reinforcement learning system, where dopamine-dependent plasticity in PFC implements a slow learning process that configures a faster, task-specific learning system. Computational modeling and fMRI showed that PFC activity patterns are consistent with meta-RL: the PFC learns "how to learn" within a task, explaining how humans can rapidly adapt to new reward structures.

## Core content

**Meta-RL concept:** In standard RL, an agent learns a policy directly. In meta-RL, a slow learning process (meta-learner) adjusts the parameters of a fast learning process (base learner), enabling the agent to learn new tasks quickly. The authors propose that PFC implements the meta-learner via slow dopamine-dependent plasticity (paper--prefrontal-cortex-as-a-meta-reinforcement-learning-system §Introduction).

**Computational model:** A two-process architecture where a slow RL process (analogous to PFC dopamine plasticity) configures the working memory and action biases of a fast RL process (analogous to striatal learning) (paper--prefrontal-cortex-as-a-meta-reinforcement-learning-system §Model).

**fMRI experiment:** Participants performed a two-step Markov decision task with changing reward contingencies. PFC activity patterns were analyzed for evidence of meta-RL signatures (paper--prefrontal-cortex-as-a-meta-reinforcement-learning-system §Methods).

**Key findings:**
- PFC BOLD signals showed signatures consistent with meta-RL — activity patterns changed slowly across blocks but facilitated rapid within-block adaptation (paper--prefrontal-cortex-as-a-meta-reinforcement-learning-system §Results).
- The model's meta-learning component captured behavioral patterns that standard model-free and model-based RL could not explain (paper--prefrontal-cortex-as-a-meta-reinforcement-learning-system §Results).
- PFC representation of state-action values showed task-structure-dependent patterns that persisted across trials within a block (paper--prefrontal-cortex-as-a-meta-reinforcement-learning-system §Results).

## Connections- **Theme:** [theme--deep-RL](pages/theme--deep-RL.md), [theme--neuroscience-AI-bridge](pages/theme--neuroscience-AI-bridge.md)
- **Project:** N/A
- **Collaborators:** Jane X. Wang (co-first), Zeb Kurth-Nelson (co-first), Dharshan Kumaran, Dhruva Tirumala, Hubert Soyer, Joel Z. Leibo, Matthew Botvinick
- **Era:** deepmind-ascent
- **Venue:** venue--PNAS
- **Related:** paper--[theme--deep-RL](pages/theme--deep-RL.md)-fast-and-slow — both propose dual-process RL architectures
- **Related:** paper--neuroscience-inspired-artificial-intelligence — meta-RL as a neuroscience-AI bridge example

## Honest Gaps
- Metadata lists Kurth-Nelson, Kumaran, Botvinick, Dolan as co-authors; actual authors are Wang, Kurth-Nelson, Kumaran, Tirumala, Soyer, Leibo, Hassabis, Botvinick. Raymond Dolan is not an author; Wang, Tirumala, Soyer, and Leibo are missing.
- The fMRI evidence is correlational — it cannot definitively establish that PFC implements meta-RL vs. alternative explanations.
- The computational model is simplified compared to the complexity of real PFC circuits.
- The two-step task is a well-studied paradigm; it's unclear whether meta-RL generalizes to more complex or open-ended learning scenarios.