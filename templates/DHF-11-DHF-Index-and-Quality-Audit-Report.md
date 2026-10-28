# Design History File (DHF) Index & Quality Audit Report

> **Document ID**: `DHF-11-AUDIT`  
> **Applicable Standards**: ISO 13485:2016 Clause 7.3.7 & 8.2.4, IEC 62304:2006 Clause 5.1.1 / 9, ISO 14971:2019 Clause 9  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 ISO 13485:2016 Clause 7.3.7에 따른 설계이력파일(Design History File: DHF) 총괄 색인(Index)이자 최종 규제/품질 감사 보고서입니다.
> - 프로젝트 내 생성된 모든 DHF 문서(DHF-00부터 DHF-11까지)의 공식 문서명, 버전, 유효일자, 승인자, 위변조 방지를 위한 암호학적 해시값(SHA-256)을 편철합니다.
> - `python3 scripts/generate_dhf_index.py`를 실행하여 문서 상태 및 해시값을 자동 생성 및 검증할 수 있습니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Lead Auditor** | `[Auditor Name]` | Lead Medical Device Quality Auditor | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Head of Regulatory Affairs | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Chief Executive Officer / QMS Management Rep | Approved | `[YYYY-MM-DD]` |

---

## 2. Design History File (DHF) Master Index

| DHF ID | Document Title | Version | Effective Date | Status | Cryptographic Hash (SHA-256) |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `DHF-00` | Design and Development Plan (DDP) | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-01` | Intended Use & User Requirements Document (URD) | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-02` | Clinical Literature Review & SOTA Report | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-03` | Regulatory Strategy & Clearance Profile | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-04` | Software Requirements Specification (SRS) | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-05A`| Risk Management Plan (RMP) | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-05B`| Hazard Analysis & Software FMEA Matrix | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-05C`| Risk Management Report (RMR) | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-06` | Cybersecurity Threat Model & SBOM | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-07` | Software Architectural Design Specification (SDS) | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-08` | Software Detailed Design Specification (DDS) | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-09` | Software Verification & Validation (V&V) Report | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-10` | Requirements Traceability Matrix (RTM) | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |
| `DHF-11` | DHF Index & Quality Audit Report | 1.0 | `YYYY-MM-DD` | Approved | `[Auto-generated SHA-256]` |

---

## 3. Regulatory & Quality Audit Findings

### 3.1 Standards Compliance Checklist

| Standard | Clause / Section | Compliance Status | Audit Evidence & Observation |
| :--- | :--- | :---: | :--- |
| **ISO 13485:2016** | 7.3.2 Design Inputs | **COMPLIANT** | Clear intended use, user needs, regulatory mandates captured in DHF-01 & 03. |
| **ISO 13485:2016** | 7.3.3 Design Outputs | **COMPLIANT** | Architectural & detailed design specifications and code verified in DHF-07 & 08. |
| **ISO 13485:2016** | 7.3.6 / 7.3.7 V&V | **COMPLIANT** | 100% test pass rate recorded in independent V&V report DHF-09. |
| **IEC 62304:2006** | 5.0 Software Lifecycle | **COMPLIANT** | Full V-model decomposition, implementation, and verification executed. |
| **ISO 14971:2019** | 4.0 - 9.0 Risk Mgmt | **COMPLIANT** | Complete RMP, PHA, FMEA, RCM verification, and RMR executed with 0 open risks. |
| **IEC 62366-1:2015**| Usability Engineering | **COMPLIANT** | Critical user errors mitigated via visual indicators and raw mode overrides. |
| **FDA Cybersecurity**| Premarket Guidance | **COMPLIANT** | STRIDE threat model, SBOM catalog, and TLS 1.3 controls verified in DHF-06. |

### 3.2 Non-Conformity & CAPA Summary
- Major Non-Conformities: **0**
- Minor Non-Conformities: **0**
- Observations / Recommendations: **0**

---

## 4. Final Regulatory Clearance Readiness Certification
The Quality Assurance and Regulatory Audit team certifies that the Design History File (DHF) for `[Project / Device Name]` is complete, consistent, and fully verified. The product is **CERTIFIED READY** for regulatory submission dossiers to South Korea MFDS, US FDA (510(k)), and EU Notified Bodies (IVDR CE).
