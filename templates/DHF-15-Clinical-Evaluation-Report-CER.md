# Clinical Evaluation Report (CER / PER)

> **Document ID**: `DHF-15-CER`  
> **Applicable Standards**: EU MDR (2017/745) Article 61 / Annex XIV, EU IVDR (2017/746) Article 56 / Annex XIII, MEDDEV 2.7/1 rev. 4, IMDRF SaMD N41 (Clinical Evaluation), MFDS 인공지능 의료기기 임상 유효성 평가 가이드라인  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 EU MDR Article 61, EU IVDR Article 56, MEDDEV 2.7/1 rev. 4 및 IMDRF SaMD N41 지침에 따른 소프트웨어 의료기기(SaMD)의 법정 임상평가보고서(CER) 또는 성능평가보고서(PER)입니다.
> - IMDRF N41의 3대 핵심 기둥인 **1) 유효한 임상적 연관성(Valid Clinical Association)**, **2) 분석적 유효성(Analytical Validity)**, **3) 임상적 성능(Clinical Performance)**을 체계적으로 입증합니다.
> - 최신 의학 기술 수준(State of the Art, SOTA) 문헌 검토 결과(`DHF-02`), V&V 시험 결과(`DHF-09`), 위험관리 이득-위험 분석(`DHF-05C`)을 종합하여 제품의 임상적 이득이 잔여 위험을 상회함을 증명합니다.
> - 시판 후 임상 추적관찰(PMCF / PMPF) 계획을 수립합니다.

---

## 1. Document Control & Evaluator Qualifications

| Role | Name | Title / Qualifications | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Lead Evaluator** | `[Evaluator Name]` | MD, Board-Certified Pathologist / Clinical Affairs | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]` | Lead Biostatistician / Regulatory Specialist | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]` | Chief Medical Officer (CMO) | Approved | `[YYYY-MM-DD]` |

---

## 2. Clinical Evaluation Plan (CEP) & Intended Clinical Purpose

### 2.1 Medical Purpose & Clinical Scope
- **Device Description**: `[SaMD software name, version, underlying algorithmic architecture]`
- **Target Disease / Condition**: `[Target pathology, e.g., Prostate Adenocarcinoma Gleason Grading]`
- **Clinical Role of Software**: `[Adjunctive triage / Screening aid / Concurrent read decision support]`

### 2.2 SOTA Baseline & Clinical Literature Review
- **Literature Search Protocol**: `[PubMed, EMBASE, Cochrane, PRISMA flow diagram derived from DHF-02]`
- **Current State of the Art (SOTA)**:
  * Standard of Care: `[e.g., Light microscopy visual assessment by single general pathologist]`
  * Diagnostic Disagreement / Inter-reader Variability: `[e.g., Cohen's Kappa 0.60 - 0.75 in general practice]`
  * Clinical Acceptance Baseline: `[e.g., Minimum sensitivity >= 95.0%, specificity >= 90.0%]`

---

## 3. Demonstration of the 3 Pillars of Clinical Evidence (IMDRF N41)

### 3.1 Pillar 1: Valid Clinical Association (VCA)
- **Biological / Clinical Plausibility**: `[Scientific rationale linking whole slide digital imaging morphological patterns (nuclear atypia, glandular fusion) to target disease]`
- **Consensus Clinical Guidelines**: `[References to WHO Classification, CAP Protocols, ISUP Consensus]`

### 3.2 Pillar 2: Analytical Validity (AV)
- **Analytical Performance Synthesis**:
  * **Repeatability**: `[100% identical pixel segmentation on identical inputs across 10 repeated runs]`
  * **Robustness & Scanner Invariance**: `[Consistent performance across Aperio, Hamamatsu, Philips WSI scanners]`
  * **Limits of Detection**: `[Minimum resolvable tumor focus size in mm^2]`

### 3.3 Pillar 3: Clinical Performance (CP) & Statistical Validation
- **Multi-Center Clinical Validation Dataset**:
  * `[Number of unique patients, total WSI slides, distribution across multiple independent hospital sites]`
  * Ground truth consensus protocol: `[Triple-reader expert panel with adjudicated consensus]`
- **Diagnostic Accuracy Metrics (with 95% Confidence Intervals)**:

| Metric | Target Acceptance Baseline | Achieved Performance | 95% Confidence Interval (CI) | Result |
| :--- | :---: | :---: | :---: | :---: |
| **Sensitivity (Recall)** | $\ge 95.0\%$ | `97.8%` | `[96.1%, 98.9%]` | **PASS** |
| **Specificity** | $\ge 90.0\%$ | `94.2%` | `[92.4%, 95.7%]` | **PASS** |
| **AUROC (AUC)** | $\ge 0.950$ | `0.982` | `[0.971, 0.990]` | **PASS** |
| **Positive Predictive Value (PPV)** | $\ge 85.0\%$ | `89.5%` | `[87.1%, 91.6%]` | **PASS** |
| **Negative Predictive Value (NPV)** | $\ge 98.0\%$ | `99.1%` | `[98.3%, 99.6%]` | **PASS** |

---

## 4. Benefit-Risk Determination (ISO 14971 Clause 7.4)
- **Clinical Diagnostic Benefits**: `[Early detection of occult micro-foci, reduction in inter-pathologist grading discordance, 35% reduction in biopsy turnaround time]`
- **Residual Diagnostic Risks**: `[Theoretical risk of false negative biopsy interpretation on atypical tissue variants]`
- **Benefit-Risk Ratio Evaluation**: `[Objective quantitative conclusion that diagnostic benefits significantly outweigh residual clinical risks when used in accordance with IFU (DHF-14)]`

---

## 5. Post-Market Clinical Follow-up (PMCF / PMPF) Plan
- **Continuous Clinical Data Collection**: `[Real-world clinical accuracy monitoring protocol, adverse event threshold triggers]`
- **Periodic Safety Update Report (PSUR)**: `[Annual statutory CER update schedule under EU MDR Article 86]`
