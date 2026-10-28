# Risk Analysis: RSK-FW-008

> **Risk ID**: `RSK-FW-008`  
> **Risk Control Measure ID**: `RCM-FW-008`  
> **Title**: AI Model Data Contamination & Patient-Level Leakage Over-optimism  
> **Standard Reference**: ISO 14971:2019 Clause 5.4, GMLP Principle 6  
> **Target Requirement**: `FR-AI-001`, `FR-AI-002`, `FR-AI-003`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-008.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-008.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-AI-002.md`  

---

## 1. Hazard, Sequence of Events & Hazardous Situation
- **Hazard**: Cross-partition data leakage during AI dataset splitting.
- **Sequence of Events**:
  1. Image patches or time-series slices from the same patient are distributed into both training and independent test partitions.
  2. The AI model memorizes patient-specific idiosyncrasies rather than generalizable disease pathology.
- **Hazardous Situation**: Clinical validation reports falsely elevated sensitivity and specificity, masking real-world diagnostic incompetence.
- **Harm**: Medical diagnostic software deployed to hospitals misdiagnoses patients, leading to missed malignant lesions or inappropriate treatments. (Severity: S4 - Critical, Probability: P3 - Medium $\to$ **Initial Risk: High / Unacceptable**).

## 2. Risk Control Measure: RCM-FW-008
- **Control Measure Description**: The framework mandates **Patient-Level Split Verification & Cryptographic Test Set Locking**.
  - All splits must be grouped strictly by unique Patient ID (0.00% cross-set leakage).
  - An automated leakage detector scans split manifests prior to training and validation.
  - The independent test set is cryptographically locked with SHA-256 digests in `DHF-09` before validation commences.
- **Control Type**: Inherent Software Design / Automated Partitioning Gate.

## 3. Residual Risk Evaluation
- **Residual Severity**: S4.
- **Residual Probability**: P1 (Automated checker halts pipeline if any Patient ID overlap exists).
- **Residual Risk Level**: **Low / Acceptable (ALARP satisfied)**.
- **Verification Evidence**: `VERIF-FW-036`, `VERIF-FW-037`, `VERIF-FW-038` via `TC-FR-AI-001.md` ~ `003.md`.
## 4. Evaluation of New Hazards Arising from Risk Control Measures (ISO 14971:2019 Cl 7.3 & IEC 62304 Cl 7.2.2)
- **Potential New Hazards Introduced**:
  - Rigid patient-level data partitioning resulting in skewed class/prevalence distribution between training and test sets.
  - Overly restrictive split filters causing legitimate multi-center clinical validation data to be rejected.
- **Secondary Risk Mitigations**:
  - Stratified patient-level hashing (`DDS-FW-008`) ensuring proportional distribution of diagnostic sub-categories across partitions.
  - Cryptographic split manifest generation (`data_split_manifest.json`) recording patient hash sets with SHA-256 integrity verification.
  - Automated statistical distribution parity check (Chi-square / KS-test) verifying clinical representation across sets.
- **Residual Risk Conclusion**: No unacceptable secondary hazards introduced. Residual risk remains **Acceptable (ALARP satisfied)**.
