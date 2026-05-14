---
title: "Neural Scene Representation and Rendering"
tags:
  - peer-reviewed-paper
  - reinforcement-learning
  - multi-agent-systems
  - deepmind-ascent
  - GQN
description: "Eslami, Rezende, Besse, Viola, Morcos, Garnelo, Ruderman, Rusu, Danihelka, Gregor, Reichert, Buesing, Weber, Vinyals, Botvinick, Rosenbaum, Rabinowitz, King,…"
date: 2018-01-01
---

# Neural Scene Representation and Rendering

**Type:** paper
**Slug:** neural-scene-representation-and-rendering--hassabis
**Sources:** neural-scene-representation-and-rendering--hassabis
**Last updated:** 2026-05-13

---

## Summary
Eslami, Rezende, Besse, Viola, Morcos, Garnelo, Ruderman, Rusu, Danihelka, Gregor, Reichert, Buesing, Weber, Vinyals, Botvinick, Rosenbaum, Rabinowitz, King, Hadsell, and Hassabis (2018) introduced the Generative Query Network (GQN), a neural system that learns to represent and render 3D scenes from only 2D observations, without any explicit 3D supervision. Given a set of context views of a scene, GQN can generate accurate images of the scene from arbitrary novel viewpoints, demonstrating that scene understanding can emerge purely from observation.

## Core content

**Problem:** Previous approaches to scene understanding required explicit 3D representations (depth maps, point clouds, meshes) or engineering of geometric invariances. Can a system learn to represent scenes and render novel views using only raw 2D observations and the motor commands (camera poses) that produced them? (paper--neural-scene-representation-and-rendering §Introduction)

**Architecture:** Two-network design trained end-to-end (paper--neural-scene-representation-and-rendering §Model):
- **Representation network r:** Takes a variable number of context observations (image + viewpoint) and iteratively builds a compact scene representation vector via an attention-based CNN (paper--neural-scene-representation-and-rendering §Model).
- **Generation network g:** Takes the scene representation + a query viewpoint and renders a predicted image using a transpose CNN with stochastic latent variables for variability (paper--neural-scene-representation-and-rendering §Model).

**Key results:**
- Novel view synthesis quality approached that of graphics renderers despite receiving no 3D supervision (paper--neural-scene-representation-and-rendering §Results).
- The scene representation encodes object identity, position, color, and lighting — demonstrated by systematic manipulation (paper--neural-scene-representation-and-rendering §Results).
- Generalization: trained on procedurally generated environments, GQN could render novel scenes from the same distribution (paper--neural-scene-representation-and-rendering §Results).
- Scene representations exhibited linear structure in object position (interpolation between representations produced smooth camera movements) (paper--neural-scene-representation-and-rendering §Results).

**Significance:** Demonstrated that an end-to-end differentiable system can learn an implicit 3D scene model from 2D observations alone, prefiguring Neural Radiance Fields (NeRF, 2020) and other implicit scene representations.

## Connections
- **Theme:** generative-models, scene-understanding, neural-architecture
- **Project:** GQN
- **Collaborators:** S. M. Ali Eslami (co-first), Danilo J. Rezende (co-first), Frederic Besse, Fabio Viola, Ari S. Morcos, Marta Garnelo, Avraham Ruderman, Andrei A. Rusu, Ivo Danihelka, Karol Gregor, David P. Reichert, Lars Buesing, Theophane Weber, Oriol Vinyals, Matthew Botvinick, Steven Rosenbaum, Noah Rabinowitz, Helen King, Raia Hadsell
- **Era:** deepmind-ascent
- **Venue:** venue--Science
- **Precedes:** NeRF (Mildenhall et al., 2020) — GQN's implicit scene representation was an important precursor
- **Contrasts:** paper--the-construction-system-of-the-brain — both deal with scene construction but from vastly different perspectives (neuroscience vs. AI)

## Honest Gaps
- Metadata incorrectly lists domain as "multi-agent-systems" — this is a generative modeling / computer vision paper with no multi-agent component.
- Metadata incorrectly lists theme as "reinforcement-learning" — the paper uses no RL.
- Metadata lists only 3 co-authors; the actual paper has ~20 authors.
- Scenes are synthetic (simple shapes, controlled lighting) — performance on real-world scenes was not demonstrated.
- Rendering quality, while impressive for 2018, is far below modern NeRF/Gaussian Splatting quality.
- The scene representation is a fixed-size vector, which limits the complexity of scenes that can be represented.
- Computationally expensive: iterative attention over context views scales with number of context images.