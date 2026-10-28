# Intended Use & User Requirements Document (URD)

> **Document ID**: `DHF-01-URD`  
> **Applicable Standards**: ISO 13485:2016 Clause 7.3.2, IEC 62304:2006 Clause 5.1, IEC 62366-1:2015  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 제품의 사용목적(Intended Use/Purpose)과 임상적 적응증, 대상 환자군, 금기사항 및 사용자의 상위 기능/비기능 요구사항을 기술합니다.
> - 모든 요구사항에는 고유 식별자(`USER-REQ-xxx`)를 부여하며, 각 요구사항은 IEC 62304 소프트웨어 요구사항명세서(`DHF-04-SRS`)의 `REQ-SW-xxx`로 100% 분해/연계되어야 합니다.
> - 식약처(MFDS) 허가신청서 상의 '사용목적' 및 FDA 'Indications for Use (IFU)', EU IVDR 'Intended Purpose' 조항의 기초가 됩니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Medical Product Manager | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Clinical Specialist | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Chief Medical Officer | Approved | `[YYYY-MM-DD]` |

---

## 2. Medical Device Intended Purpose (사용목적)
- **Medical Claim**: `[Provide the exact regulatory intended use statement. E.g., The software is intended to assist qualified pathologists in viewing, navigating, and analyzing digital whole slide images (WSI) by automatically detecting tissue regions and standardizing background color variations to support histological examination.]`
- **Clinical Indications**: `[Diseases, histological conditions, e.g., Biopsy and surgical resection specimens stained with Hematoxylin and Eosin (H&E).]`
- **Target Patient Population**: `[Patient demographic or disease categories. E.g., Patients undergoing histopathological biopsy or surgical evaluation.]`
- **Contraindications & Limitations**: `[Explicit exclusions, e.g., Not intended for autonomous diagnosis without pathologist review; not validated for non-H&E stains or frozen sections unless specifically verified.]`

---

## 3. User Characteristics & Operating Environment (사용자 및 환경)
- **Intended Users**: `[Board-certified pathologists, pathology residents, certified laboratory technicians.]`
- **Use Environment**: `[Hospital pathology reading rooms, clinical laboratories, certified telepathology workstations with calibrated medical displays (sRGB / DCI-P3).]`

---

## 4. User Requirements Catalog (`USER-REQ-xxx`)

| ID | Category | Requirement Description | Clinical / Operational Rationale | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| `USER-REQ-001` | `[FUNC]` | The user shall be able to open and smoothly navigate multi-resolution digital whole slide images. | Essential for replacing optical microscopes in primary diagnosis. | Inspection & Test |
| `USER-REQ-002` | `[FUNC]` | The system shall automatically detect and delineate valid tissue regions on the glass slide. | Eliminates unnecessary inspection of empty glass background. | AI Performance Test |
| `USER-REQ-003` | `[FUNC]` | The system shall standardize background illumination and normalize stain variations across multi-vendor scanners. | Reduces reader fatigue and cross-laboratory diagnostic discordance. | Quantitative Color Test |
| `USER-REQ-004` | `[PERF]` | Pyramidal tile loading latency shall not exceed 200 ms under standard 1 Gbps hospital LAN. | Prevents stutter and workflow interruption during panning/zooming. | Performance Benchmark |
| `USER-REQ-005` | `[SAFE]` | The system shall clearly alert the user when AI detection confidence is low and allow instant toggle to raw unnormalized view. | Prevents diagnostic error caused by algorithm misinterpretation or artifact clipping. | Usability / System Test |
| `USER-REQ-006` | `[SEC]` | The system shall safeguard patient health information (PHI) and restrict access to authorized clinical personnel. | Compliance with HIPAA, GDPR, ISO 27001/27799. | Security Audit |

---

## 5. Traceability Forward
All `USER-REQ-xxx` items must be mapped to Software Requirements in `DHF-04-SRS.md`.
