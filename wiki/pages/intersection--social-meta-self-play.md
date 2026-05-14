---
title: "Social Meta-Self-Play"
tags:
  - intersection
date: 2026-05-14
---

# Social Meta-Self-Play

**Type:** intersection (second-order)
**Slug:** intersection--social-meta-self-play
**Parents:** intersection--social-hierarchy-self-play, intersection--personality-models-meta-RL
**Last updated:** 2026-05-14
**Epistemic status:** Extrapolative

---

## The convergence
Multi-agent self-play produces internal rank representations of opponents (intersection G). Personality models condition meta-learning on agent identity (intersection L). Combined: **in social environments, meta-self-play discovers socially specialised learning algorithms — different strategies for high-status vs. low-status agents, different exploration rates for cooperative vs. competitive others.**

## Why this isn't obvious from either parent
Social Hierarchy×Self-Play (G) predicts rank representations but doesn't ask whether those representations *condition learning*. Personality×Meta-RL (L) predicts socially conditioned learning but doesn't specify the conditioning variable (it could be personality, relationship history, context). Together: social rank is the conditioning variable. Meta-self-play discovers that rank determines learning strategy — you learn faster from high-status agents (their information is more valuable) and explore differently with low-status agents (more experimentation is safe).

## Generative prediction
In a multi-agent meta-RL setup, the meta-learner should discover that the optimal learning algorithm depends on the opponent's rank. Against high-ranked opponents: low learning rate (don't overreact to rare successful exploits), high exploitation of known good strategies. Against low-ranked opponents: high learning rate (quickly adapt to whatever they're doing), high exploration. If the meta-learner discovers this without being told, social rank has been spontaneously adopted as a meta-learning parameter.

---

**Falsification:** If a meta-learner in social games uses the same strategy regardless of opponent rank (no rank-conditioned learning), the prediction is false.
