# Replay×Hippocampal + Meta-RL×Self-Play

**Type:** intersection (second-order)
**Slug:** intersection--meta-replay
**Parents:** intersection--experience-replay-hippocampal-replay, intersection--meta-RL-self-play
**Last updated:** 2026-05-14
**Epistemic status:** Extrapolative

---

## The combination
Hippocampal replay consolidates past experiences (first intersection). Meta-RL discovers learning algorithms through self-play (second intersection). Combined: **meta-replay — a system that replays past *learning episodes* (not just experiences) to improve its learning algorithm.** The replay buffer becomes a meta-learning curriculum.

## What emerges
Standard replay stores state-action-reward transitions. Meta-replay stores *learning trajectories* — sequences of how the system's learning algorithm performed on a task. By replaying these learning trajectories, the meta-learner improves not just its policy but its *ability to learn*. This is a novel architecture with no existing implementation.

## Gap
No system replays learning episodes rather than task episodes. This is a genuinely new architectural proposal that emerges only from combining the two parent intersections.

## Generative potential
**Architecture:** Store triplets (task, learning-algorithm-state, performance-after-learning) in a meta-replay buffer. During "sleep," sample from this buffer and update the meta-learner. The system gets better at learning by reviewing *how it learned*, not just *what it experienced*.

**Connection to expertise:** Human experts don't just remember experiences — they remember *how they learned* from experiences ("that time I finally understood counterpoint by doing X"). Meta-replay formalises this insight.

---

**Falsification:** If replaying learning episodes does not improve the learning algorithm more than replaying task episodes, the meta-replay advantage is false.
