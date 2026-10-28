# Risk Management Plan (RMP)

> **Document ID**: `DHF-05A-RMP`  
> **Applicable Standards**: ISO 14971:2019 Clause 4, ISO/TR 24971:2020, IEC 62304:2006 Clause 7  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 ISO 14971:2019 요구사항에 따른 위험관리계획서(Risk Management Plan)입니다.
> - 위험 평가 기준(심각도 S1~S5, 발생확률 P1~P5, 위험 수용성 매트릭스), 위험 통제 조치 수립 원칙(3단계 우선순위), 위험관리 담당자 자격 요건 및 잔여 위험 평가 기준을 사전 확정합니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Medical Device Risk Officer | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Systems Engineering Lead | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Chief Medical Officer | Approved | `[YYYY-MM-DD]` |

---

## 2. Risk Management Scope & Roles
- **Product Scope**: All software modules, AI models, third-party libraries (SOUP), and user interfaces of `[Product Name]`.
- **Risk Management Team**:
  - Risk Officer: Lead analysis and documentation (`samd-risk-mgmt`).
  - Clinical Pathologist: Severity estimation and clinical harm assessment.
  - Software Architect: Software failure modes and mitigation design.

---

## 3. Risk Evaluation Scoring System

### 3.1 Severity Levels (S)
- **S1 (Negligible)**: Minor inconvenience; diagnostic workflow delayed by $< 1\text{ min}$; no patient impact.
- **S2 (Minor)**: Diagnostic delay requiring slide re-scan; temporary minor clinical inconvenience.
- **S3 (Serious)**: Diagnostic delay $> 24\text{ hours}$ or sub-optimal histology grading requiring re-biopsy; reversible harm.
- **S4 (Critical)**: Misdiagnosis or omission of malignant carcinoma focus leading to delayed cancer treatment; life-threatening.
- **S5 (Catastrophic)**: Direct death or fatal outcome resulting from misdiagnosis.

### 3.2 Probability of Occurrence Levels (P)
- **P1 (Improbable)**: $< 10^{-5}$
- **P2 (Remote)**: $10^{-5} \text{ to } 10^{-4}$
- **P3 (Occasional)**: $10^{-4} \text{ to } 10^{-3}$
- **P4 (Probable)**: $10^{-3} \text{ to } 10^{-2}$
- **P5 (Frequent)**: $> 10^{-2}$

### 3.3 Risk Acceptability Matrix

| Severity \ Prob | P1 (Improbable) | P2 (Remote) | P3 (Occasional) | P4 (Probable) | P5 (Frequent) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **S5 (Catastrophic)**| ALARP | Unacceptable | Unacceptable | Unacceptable | Unacceptable |
| **S4 (Critical)**    | Broadly Acceptable | ALARP | Unacceptable | Unacceptable | Unacceptable |
| **S3 (Serious)**     | Broadly Acceptable | Broadly Acceptable | ALARP | Unacceptable | Unacceptable |
| **S2 (Minor)**       | Broadly Acceptable | Broadly Acceptable | Broadly Acceptable | ALARP | ALARP |
| **S1 (Negligible)**  | Broadly Acceptable | Broadly Acceptable | Broadly Acceptable | Broadly Acceptable | Broadly Acceptable |

- **Broadly Acceptable**: No further risk reduction required.
- **ALARP (As Low As Reasonably Practicable)**: Reduce risk where feasible; requires benefit-risk justification if further reduction is impossible.
- **Unacceptable**: Mandatory risk control measure must be implemented to reduce risk before design release.
