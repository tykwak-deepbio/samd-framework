# Usability Engineering File (UEF)

> **Document ID**: `DHF-12-UEF`  
> **Applicable Standards**: IEC 62366-1:2015+AMD1:2020, ISO 14971:2019, FDA Human Factors Guidance (2016)  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 IEC 62366-1 표준에 따른 소프트웨어 의료기기(SaMD)의 사용적합성 엔지니어링 파일(UEF)입니다.
> - 사용자 프로파일(User Profiles), 사용 환경(Use Environment), 주요 사용 시나리오 및 안전 관련 핵심 작업(Critical Tasks)을 명시합니다.
> - 인지-판단-행동(PCA: Perception, Cognition, Action) 모델에 기반한 사용오류(Use Error) 분석과 형성평가(Formative) 및 최소 15인 임상 총괄평가(Summative) 결과를 기록합니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Usability Engineer / UI Designer | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]` | Lead Clinical Specialist | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]` | Chief Technology / Regulatory Officer | Approved | `[YYYY-MM-DD]` |

---

## 2. User Profiles, Use Environment & Critical Tasks

### 2.1 Intended User Profiles (`USE-REQ-001`)
- **Primary Users**: `[e.g., Board-Certified Pathologists, Histotechnicians]`
- **User Characteristics**: `[e.g., Experience level, visual acuity requirements, training pre-requisites]`

### 2.2 Clinical Use Environment (`USE-REQ-002`)
- **Physical Environment**: `[e.g., Hospital pathology reading room, standardized calibrated medical monitors]`
- **Ambient Constraints**: `[e.g., Ambient lighting <= 100 lux, minimal acoustic distractions]`

### 2.3 Critical Tasks Identification
| Task ID | Task Description | Safety Impact / Potential Hazard | Associated Risk ID |
| :--- | :--- | :--- | :--- |
| `TASK-01` | Reviewing AI tissue segmentation overlay | Missing biopsy tissue fragment if confidence threshold is too strict | `RSK-001` |
| `TASK-02` | Toggling raw unnormalized optical RGB view | Misinterpreting cellular dysplasia if stain color over-corrected | `RSK-002` |

---

## 3. PCA Model-Based Use Error Analysis
| Task ID | Failure Mode (PCA Phase) | Potential Cause | Hazardous Situation & Harm | Usability Mitigation Design |
| :--- | :--- | :--- | :--- | :--- |
| `TASK-01` | **Perception**: Clinician overlooks low-confidence warning | Subdued visual indicator | Relying on unvetted AI boundary | High-contrast pulsing amber warning banner at top of viewport |
| `TASK-02` | **Action**: Clinician forgets whether normalization is ON | Lack of persistent visual state indicator | Grading nuclei on altered colors | On-screen watermark badge "RGB RAW" vs "STAIN NORMALIZED" |

---

## 4. Usability Verification & Validation Summary
- **Formative Evaluations**: `[Summary of early iterative UI prototype reviews with 3-5 users]`
- **Summative Evaluation**: `[Final formal usability testing with >= 15 representative clinical users, 100% critical task completion with zero unmitigated use errors]`
