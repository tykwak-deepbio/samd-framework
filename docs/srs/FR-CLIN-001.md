# Software Requirement: FR-CLIN-001

> **Requirement ID**: `FR-CLIN-001`  
> **Title**: Statutory Clinical Evaluation Plan & Report (CEP / CER / PER) Dossier Compilation  
> **Category**: Clinical Affairs & Regulatory Clearance (`[CLIN]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: EU MDR (2017/745) Article 61 / Annex XIV, EU IVDR (2017/746) Article 56 / Annex XIII, MEDDEV 2.7/1 rev. 4, IMDRF SaMD N41 (Clinical Evaluation), MFDS 인공지능 의료기기 임상 유효성 평가 가이드라인  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-CLIN-001.md`  

---

## 1. Description & Regulatory Rationale
Under EU MDR Article 61, EU IVDR Article 56, and IMDRF N41, SaMD clearance requires a formal, standalone statutory dossier establishing clinical safety, analytical validity, and clinical performance. Technical V&V testing (`DHF-09`) verifies that software meets its technical specifications, but cannot substitute for a Clinical Evaluation Report (CER) or Performance Evaluation Report (PER). The framework shall provide dedicated governance, agent orchestration, and template structure (`DHF-15`) to synthesize Clinical Evaluation Plans (CEP), State of the Art (SOTA) literature appraisals, clinical equivalence analyses, diagnostic performance metrics, and Post-Market Clinical Follow-up (PMCF) plans into an audit-ready dossier.

## 2. Detailed Functional Specifications
1. **Three Pillars of SaMD Clinical Evidence**:
   - The framework shall enforce structured documentation of the three IMDRF N41 clinical evaluation pillars:
     * **Valid Clinical Association (VCA)**: Biological/pathological plausibility between input digital data and target clinical condition.
     * **Analytical Validity (AV)**: Repeatability, reproducibility, limits of detection, and robustness across scanner vendors, stains, and image artifacts.
     * **Clinical Performance (CP)**: Diagnostic accuracy, sensitivity, specificity, positive/negative predictive value (PPV/NPV), and AUROC with 95% Confidence Intervals across diverse clinical sites.
2. **Statutory CEP / CER Dossier Architecture (`DHF-15`)**:
   - The framework shall compile `templates/DHF-15-Clinical-Evaluation-Report-CER.md` incorporating:
     * Executive Summary & Device Medical Purpose Description.
     * Clinical Background & State of the Art (SOTA) Benchmarking (synthesized from `DHF-02`).
     * Literature Search Protocol & Critical Appraisal (PRISMA methodology).
     * Pre-clinical Verification & Analytical Performance Synthesis (derived from `DHF-09`).
     * Multi-center Clinical Validation Results (multi-reader study, ground truth consensus).
     * Benefit-Risk Determination & Unacceptable Residual Risk Justification (ISO 14971 Cl 7.4).
     * Post-Market Clinical Follow-up (PMCF / PMPF) Plan and continuous safety monitoring triggers.
3. **Automated Cross-Validation with V&V & Risk Data**:
   - The CER generation engine shall automatically verify that clinical performance claims match the statistical verification results in `DHF-09` and that clinical safety conclusions are consistent with the Risk Management Report (`DHF-05C`).

## 3. Inputs, Processing & Outputs
- **Inputs**: Intended Use (`DHF-01`), SOTA Literature Review (`DHF-02`), V&V Test Report (`DHF-09`), Risk Management Report (`DHF-05C`).
- **Processing**: Systematic literature appraisal synthesis, analytical & clinical performance data aggregation, benefit-risk conclusion derivation.
- **Outputs**: Audit-ready `DHF-15-Clinical-Evaluation-Report-CER.md`, mapped to RTM (`DHF-10`).
