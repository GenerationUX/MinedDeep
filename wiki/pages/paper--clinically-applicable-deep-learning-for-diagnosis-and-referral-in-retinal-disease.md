---
title: "Clinically Applicable Deep Learning for Diagnosis and Referral in Retinal Disease"
tags:
  - peer-reviewed-paper
  - clinical-ai
  - deepmind-ascent
  - DeepMind-general
description: "De Fauw, Ledsam, Romera-Paredes, Nikolov, Tomašev, and colleagues, with Keane, and Hassabis (2018) developed a deep learning system for analyzing retinal OCT…"
date: 2018-01-01
---

# Clinically Applicable Deep Learning for Diagnosis and Referral in Retinal Disease

**Type:** paper
**Slug:** clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease--hassabis
**Sources:** clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease--hassabis
**Last updated:** 2026-05-13

---

## Summary
De Fauw, Ledsam, Romera-Paredes, Nikolov, Tomašev, and colleagues, with Keane, and Hassabis (2018) developed a deep learning system for analyzing retinal OCT scans to diagnose and triage patients with sight-threatening retinal diseases. Evaluated in a clinical setting at Moorfields Eye Hospital, the system achieved referral recommendations matching expert ophthalmologists in 94% of cases, demonstrating one of the first real-world deployments of AI-assisted diagnosis in healthcare.

## Core content

**Problem:** Retinal diseases (age-related macular degeneration, diabetic eye disease, glaucoma) are leading causes of preventable blindness. OCT imaging is essential for diagnosis but requires specialist interpretation, creating bottlenecks in referral pathways (paper--clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease §Introduction).

**Approach:** A two-stage deep neural network architecture:
1. **Segmentation network:** Identifies anatomical features in OCT scans (retinal layers, fluid, lesions) (paper--clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease §Methods).
2. **Classification network:** Uses segmentation outputs alongside raw OCT data to produce triage recommendations (urgent, semi-urgent, routine, observation only) (paper--clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease §Methods).

**Clinical evaluation:**
- Tested on ~1,000 patients in a simulated clinical setting at Moorfields Eye Hospital (paper--clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease §Results).
- Referral decisions matched senior ophthalmologists in 94% of cases (paper--clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease §Results).
- Did not miss any urgent referrals that experts identified (paper--clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease §Results).
- Performance was robust across different OCT machine types and patient demographics (paper--clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease §Results).

**Clinical applicability design:**
- The system outputs explainable recommendations with highlighted image features, not just binary diagnoses (paper--clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease §Discussion).
- Designed to fit into existing clinical workflows rather than replacing clinicians (paper--clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease §Discussion).

## Connections
- **Theme:** clinical-AI
- **Project:** DeepMind-general
- **Collaborators:** Jeffrey De Fauw (first), Joseph R. Ledsam, Bernardino Romera-Paredes, Stanislav Nikolov, Nenad Tomašev, Pearse Keane (Moorfields Eye Hospital)
- **Era:** deepmind-ascent
- **Venue:** venue--Nature-Medicine
- **Related:** paper--a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury — both "clinically applicable" AI papers from DeepMind Health

## Honest Gaps
- Metadata lists only 4 co-authors; the actual paper has ~12 authors.
- The extraction includes an embargo notice from the pre-print version — this is an artefact.
- The evaluation was a retrospective simulation, not a prospective clinical trial — real-world performance may differ.
- Tested only at Moorfields Eye Hospital (a world-leading specialist center) — generalization to community optometry settings is unproven.
- The "94% match" metric is somewhat generous — disagreements with experts may have been counted as "acceptable clinical variation."
- No evidence that the system actually reduced waiting times or improved patient outcomes in practice.