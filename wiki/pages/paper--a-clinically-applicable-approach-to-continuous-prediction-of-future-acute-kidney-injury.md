---
title: "A Clinically Applicable Approach to Continuous Prediction of Future Acute Kidney Injury"
tags:
  - peer-reviewed-paper
  - clinical-ai
  - alphafold-era
  - DeepMind-general
description: "Tomašev, Glorot, Rae, Zielinski, Askham, and colleagues, with Mohamed, and Hassabis (2019) developed a deep learning system for continuously predicting acute…"
date: 2019-01-01
---

# A Clinically Applicable Approach to Continuous Prediction of Future Acute Kidney Injury

**Type:** paper
**Slug:** a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury--hassabis
**Sources:** a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury--hassabis
**Last updated:** 2026-05-13

---

## Summary
Tomašev, Glorot, Rae, Zielinski, Askham, and colleagues, with Mohamed, and Hassabis (2019) developed a deep learning system for continuously predicting acute kidney injury (AKI) up to 48 hours before clinical recognition, using routine electronic health record data from the VA healthcare system. The model achieved high recall (55.8% of inpatient AKI episodes predicted, 90.2% of predicted cases were true positives) across a diverse patient population of over 700,000 individuals.

## Core content

**Problem:** Acute kidney injury affects ~20% of hospitalized patients and is often recognized too late for effective intervention. Earlier detection could enable preventive measures (paper--a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury §Introduction).

**Approach:** A recurrent neural network (LSTM-based) trained on longitudinal EHR data (vitals, labs, demographics, comorbidities) to predict the probability of AKI at future time horizons (paper--a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury §Methods).

**Key design decisions for clinical applicability:**
- **Continuous prediction:** Updated risk scores with each new data point, not a single snapshot (paper--a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury §Methods).
- **High precision prioritized:** 90.2% positive predictive value to minimize false alarm burden on clinicians (paper--a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury §Results).
- **Demographic subgroup analysis:** Explicit evaluation across age, sex, race, and comorbidity subgroups (paper--a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury §Results).

**Results:**
- 55.8% of all inpatient AKI episodes predicted 48 hours in advance (paper--a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury §Results).
- 90.2% of predictions were true positives (paper--a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury §Results).
- Performance was consistent across demographic subgroups (paper--a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury §Results).

## Connections
- **Theme:** clinical-AI
- **Project:** DeepMind-general
- **Collaborators:** Nenad Tomašev (first), Xavier Glorot, Jack W. Rae, Michal Zielinski, Harry Askham, Shakir Mohamed
- **Era:** alphafold-era
- **Venue:** venue--Nature-Medicine
- **Related:** paper--clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease — both emphasize clinical applicability and real-world deployment

## Honest Gaps
- Metadata lists 7 co-authors but the full author list includes additional contributors.
- The model was trained and evaluated on VA data — a predominantly male, older, US veteran population — limiting generalizability.
- No prospective clinical trial was conducted to show that earlier prediction actually improves patient outcomes.
- The high-precision threshold means ~44% of AKI episodes were still missed.
- AKI definitions vary across clinical settings — performance depends on the specific definition used.
- The "clinically applicable" framing is aspirational — deployment barriers (workflow integration, alert fatigue, liability) were not addressed.