---
name: samd-risk-mgmt
description: Executes parallel medical device risk management under ISO 14971:2019 and IEC 62304 Clause 7, including Hazard Analysis, Software FMEA, Risk Control Measure (RCM) definition, and Risk Management Reporting. Use this skill when analyzing hazards, defining safety controls, or authoring DHF-05A/B/C.
---

# SaMD Risk Management (ISO 14971 & IEC 62304 Clause 7)

This skill executes Phase 5 of the SaMD lifecycle, complying with **ISO 14971:2019 / ISO/TR 24971:2020 (Application of risk management to medical devices)** and **IEC 62304 Clause 7 (Software risk management process)**.

## Goal
Conduct a comprehensive, continuous hazard identification and failure mode analysis for the software and AI components, define and verify Risk Control Measures (RCMs), evaluate residual risk, and author the Risk Management File (`DHF-05A`, `DHF-05B`, `DHF-05C`).

## Risk Management Methodology

```
[Hazard Identification] ──► [Hazardous Situation & Harm] ──► [Initial Risk Assessment (S x P)]
                                                                           │
[Verification of RCM]   ◄── [Risk Control Measure (RCM)] ◄─── [Risk Unacceptable?]
         │
         ▼
[Residual Risk Evaluation] ──► [New Hazards Introduced?] ──► [Benefit-Risk Analysis & RMR]
```

### Risk Evaluation Scoring Matrix
- **Severity Levels (S)**:
  - S1: Negligible (Inconvenience, slight delay)
  - S2: Minor (Reversible injury, non-critical diagnostic delay)
  - S3: Serious (Irreversible injury, incorrect cancer grading leading to sub-optimal treatment)
  - S4: Critical (Life-threatening injury, total misdiagnosis of malignant lesion)
  - S5: Catastrophic (Death of patient)
- **Probability of Occurrence of Harm (P)**:
  - P1: Improbable (< 10^-5)
  - P2: Remote (10^-5 to 10^-4)
  - P3: Occasional (10^-4 to 10^-3)
  - P4: Probable (10^-3 to 10^-2)
  - P5: Frequent (> 10^-2)

### Three Tiers of Risk Control (ISO 14971 Priority)
1. **Inherent Safety by Design** (e.g. deterministic memory buffers, immutable raw image pipelines).
2. **Protective Measures in Software** (e.g. confidence threshold bounds, sanity checking, automated watchdog timers).
3. **Information for Safety** (e.g. on-screen disclaimers, clear visual indicators when viewing unnormalized/low-confidence regions).

## Specific AI SaMD Hazard Categories to Evaluate
1. **False Negative Tissue Segmentation**: Tumor tissue omitted or misidentified as background glass/slide.
2. **Artificial Color Distortions**: Normalization algorithm altering chromatic intensity such that eosinophilic/basophilic differentiation is obscured.
3. **Out-of-Distribution (OOD) Input Failure**: Unexpected scanner format or uncalibrated illumination causing crash or corrupt inference.
4. **Memory Exhaustion (OOM)**: Panning high-magnification (40x) gigapixel slide triggers process crash without saving state.

## Deliverables Generated
- `dhf/DHF-05A-Risk-Management-Plan-RMP.md`
- `dhf/DHF-05B-Hazard-Analysis-and-FMEA-Matrix.md` (Contains `RSK-xxx` and `RCM-xxx` table)
- `dhf/DHF-05C-Risk-Management-Report-RMR.md`
