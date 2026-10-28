# Risk Analysis: RSK-FW-010

> **Risk ID**: `RSK-FW-010`  
> **Risk Control Measure ID**: `RCM-FW-010`  
> **Title**: Post-Market Data/Concept Drift & Silent Clinical Performance Degradation  
> **Standard Reference**: ISO 14971:2019 Clause 5.4, FDA PCCP Guidance (2023)  
> **Target Requirement**: `FR-AI-004`, `FR-MAINT-001`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-008.md`, `docs/architecture/ARCH-FW-011.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-008.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-AI-004.md`, `docs/tests/TC-FR-MAINT-001.md`  

---

## 1. Hazard, Sequence of Events & Hazardous Situation
- **Hazard**: Real-world demographic or staining protocol shifts altering production data distributions.
- **Sequence of Events**:
  1. A hospital updates its staining reagent or scanner firmware, causing a covariate shift in Whole Slide Images.
  2. The deployed AI SaMD silently suffers elevated false-negative rates without raising runtime errors.
- **Hazardous Situation**: Clinicians rely on degraded AI outputs without realizing diagnostic accuracy has decayed.
- **Harm**: Delayed or missed disease detection causing irreversible progression of patient pathology. (Severity: S4 - Critical, Probability: P3 - Medium $\to$ **Initial Risk: High / Unacceptable**).

## 2. Risk Control Measure: RCM-FW-010
- **Control Measure Description**: The framework mandates **Continuous Statistical Drift Monitoring (KS-test / PSI) & PCCP Interlock**.
  - Deployed systems monitor input data distributions against baseline validation sets.
  - Population Stability Index ($\text{PSI} \ge 0.25$) triggers automatic alerts, operator notifications, and PCCP retraining workflows.
  - Fail-safe fallback permits immediate raw image viewing without AI overlay.
- **Control Type**: Inherent Software Design / MLOps Continuous Surveillance.

## 3. Residual Risk Evaluation
- **Residual Severity**: S4.
- **Residual Probability**: P1 (Real-time telemetry detects drift before clinical harm accumulates).
- **Residual Risk Level**: **Low / Acceptable (ALARP satisfied)**.
- **Verification Evidence**: `VERIF-FW-039` via `TC-FR-AI-004.md`.
## 4. Evaluation of New Hazards Arising from Risk Control Measures (ISO 14971:2019 Cl 7.3 & IEC 62304 Cl 7.2.2)
- **Potential New Hazards Introduced**:
  - False positive drift alerts triggered by benign seasonal or operational staining variations causing unnecessary clinical service suspension.
  - Drift engine computational overhead degrading real-time inference throughput in hospital pathology labs.
- **Secondary Risk Mitigations**:
  - Two-stage drift evaluation (`DDS-FW-008`): warning stage (PSI >= 0.10, notification only) and critical stage (PSI >= 0.25, mandatory verification).
  - Background asynchronous drift computation decoupled from the primary real-time inference pipeline.
  - Fail-safe raw image viewer fallback ensuring uninterrupted clinician access even during algorithm drift suspension.
- **Residual Risk Conclusion**: No unacceptable secondary hazards introduced. Residual risk remains **Acceptable (ALARP satisfied)**.
