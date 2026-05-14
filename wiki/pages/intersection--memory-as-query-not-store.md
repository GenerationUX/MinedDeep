---
title: "Memory as Query, Not Store"
tags:
  - intersection
date: 2026-05-14
---

# Memory as Query, Not Store

**Type:** intersection (feedback loop)
**Slug:** intersection--memory-as-query-not-store
**Parents:** paper--decoding-individual-episodic-memory-traces-in-the-human-hippocampus, intersection--GQN-hippocampal-construction, intersection--complete-artificial-hippocampus
**Last updated:** 2026-05-14
**Epistemic status:** Conjectural

---

## The feedback loop
The Decoding Individual Traces paper shows individual episodic memories are neurally separable in hippocampus — different patterns for different memories. GQN×Construction (A) shows a single scene representation can support many renderings via different query vectors. The Complete Hippocampus (P) says the fast store (DNC) is a temporary buffer, not a permanent archive. Combined: **individual episodic "traces" aren't stored memories — they're query parameters into a consolidated scene representation.** You don't retrieve a memory; you reconstruct it by querying the scene grammar with the right parameters.

## Why this requires reinterpreting a whole literature
The hippocampal decoding literature (2005–present, hundreds of papers) interprets separable neural patterns as evidence for *stored individual memories*. "We decoded which memory the participant was recalling" implies the memory was stored and retrieved. This intersection says the separable patterns are *query vectors*, not *stored contents*. The decoding study's success reflects separability of query parameters, not separability of stored traces.

## The key prediction that distinguishes the accounts
If memories are stored traces, they should be *stable* — decoding accuracy for a specific memory should be constant regardless of what else the participant learns. If memories are query parameters into a shared scene grammar, decoding accuracy should *change* as the underlying grammar changes through consolidation. Specifically:
- After learning a new episode that shares elements with an old one, the "trace" of the old episode should shift — because the scene grammar has been updated, and the same query now produces a different rendering.
- After consolidation (sleep), traces should shift more than before consolidation — because the grammar has been compressed.

This predicts that hippocampal "memory traces" are *not stable over time* in the way that stored representations should be. Early evidence from reconsolidation studies supports this (memory traces change after retrieval), but it's interpreted as "updating the stored trace" rather than "the trace was never a store; it's a query into a changing grammar."

## Connection back to GQN
In GQN, changing the scene representation changes all renderings — even with the same query. If the hippocampus works this way, then any experience that updates the scene grammar changes *all related memories simultaneously*. This predicts a phenomenon never looked for: learning new information about a place should subtly shift memories of *all previous events in that place*, even ones not directly related to the new information. This "spreading grammar update" would look like memory distortion but is actually grammar-consistent reconstruction.

## What makes this non-trivial
This isn't an incremental improvement to memory theory — it's a paradigm inversion. The standard view: memory = store + retrieval. This view: memory = grammar + query. The stored representations are *general* (scene grammars), the specific representations are *generated* (queries). If correct, the entire decoding literature needs reinterpretation, and the "engram" debate (where are memories stored?) is asking the wrong question — the question should be "what grammar generates the memory when queried?"

---

**Falsification:** If hippocampal decoding patterns for a specific memory are stable before and after consolidation sleep, the query-not-store claim is false.
