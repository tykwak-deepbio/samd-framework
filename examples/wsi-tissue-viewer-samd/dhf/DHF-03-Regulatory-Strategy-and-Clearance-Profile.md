# Regulatory Strategy & Clearance Profile

> **Document ID**: `DHF-03-REG`  
> **Applicable Standards**: IMDRF N12/N23, Korea MFDS 규정, US FDA 21 CFR, EU IVDR 2017/746  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 한국(MFDS), 미국(FDA), 유럽(EU IVDR) 등 주요 목표 시장별 의료기기 품목 분류, 등급 지정, 인허가 심사 경로 및 적용 규격 목록을 수립합니다.
> - 인공지능(AI/ML) 알고리즘 탑재에 따른 변경허가 관리 방안(FDA PCCP, 식약처 인공지능 의료기기 변경허가 가이드라인)을 사전에 정의합니다.
> - 도출된 규제 요구사항(`REG-REQ-xxx`)은 소프트웨어 요구사항명세서(`DHF-04-SRS`)로 전달되어 설계 반영됩니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Regulatory Affairs Specialist | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Head of Regulatory Affairs | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Chief Executive / Quality Director | Approved | `[YYYY-MM-DD]` |

---

## 2. Multi-Jurisdiction Device Classification

| Jurisdiction | Regulatory Body | Classification Code & Description | Device Class | Submission Route |
| :--- | :--- | :--- | :--- | :--- |
| **South Korea** | **MFDS** (식품의약품안전처) | A16020.01 (의료영상전처리소프트웨어) or E05010.02 (세포 및 조직 병리 검사 소프트웨어) | Class II (또는 진단보조 시 Class III) | 기술문서 심사 및 소프트웨어 유효성확인(V&V) 성적서 제출 |
| **United States** | **US FDA** (CDRH) | 21 CFR 864.3700 (Whole Slide Imaging System), Product Code: PKS, QPN | Class II | 510(k) Premarket Notification |
| **European Union**| **EU Competent Auth.** | EU IVDR 2017/746 Annex VIII (Rule 1, Rule 3, Rule 4) | Class B / Class C | Notified Body Technical Documentation Assessment |
| **Global** | **IMDRF** | IMDRF SaMD Framework (N12): Non-serious condition, informs clinical management | Category II | IMDRF Table of Contents (ToC) format |

---

## 3. Applicable Standards & Guidelines Catalog

| Standard / Guideline | Edition / Year | Scope & Applicability |
| :--- | :--- | :--- |
| **ISO 13485** | 2016 | Medical devices - Quality management systems - Requirements for regulatory purposes |
| **IEC 62304** | 2006+AMD1:2015 | Medical device software - Software life cycle processes (Safety Class B) |
| **ISO 14971** | 2019 / TR 24971:2020 | Application of risk management to medical devices |
| **IEC 62366-1** | 2015+AMD1:2020 | Application of usability engineering to medical devices |
| **IEC 81001-5-1** | 2021 | Health software and health IT systems security - Product life cycle |
| **ISO 27001 / 27799** | 2022 / 2016 | Information security & Health informatics cybersecurity |
| **FDA Guidance** | 2023 | Cybersecurity in Medical Devices: Quality System Considerations |
| **MFDS 가이드라인** | 최신판 | 의료기기 사이버보안 허가·심사 가이드라인 & 인공지능 의료기기 허가·심사 가이드라인 |

---

## 4. Regulatory Mandates Catalog (`REG-REQ-xxx`)

| ID | Originating Regulation | Requirement Summary | Software Implementation Impact |
| :--- | :--- | :--- | :--- |
| `REG-REQ-001` | IEC 62304 Cl 5.1.1 | The software safety classification shall be formally assigned (Class B). | Dictates detailed design and independent verification. |
| `REG-REQ-002` | FDA Cybersecurity / MFDS | Software Bill of Materials (SBOM) and vulnerability tracking shall be maintained. | CycloneDX SBOM export, dependency scanning in CI. |
| `REG-REQ-003` | ISO 27799 / HIPAA | Patient identifiable health data (PHI) shall be stripped from slide metadata before export. | De-identification filter in DICOM/WSI ingestion. |
| `REG-REQ-004` | IEC 62366-1 Cl 5 | Safety-related user interface indicators shall be verified via formative/summative tests. | Visual banner for low-confidence tissue detection. |
| `REG-REQ-005` | FDA PCCP / MFDS 변경가이드 | AI model weight retraining boundaries shall be pre-specified in Change Control Plan. | Version-locked model inference container. |
