# Design and Development Plan (DDP)

> **Document ID**: `DHF-00-DDP`  
> **Applicable Standards**: ISO 13485:2016 Clause 7.3.2, IEC 62304:2006+AMD1:2015 Clause 5.1  
> **Project Name**: `[Project / Device Name]`  
> **Software Safety Class**: `[Class A / Class B / Class C]` (IEC 62304)  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 의료기기 설계 및 개발의 최상위 계획서(Design & Development Plan)입니다.
> - ISO 13485 7.3.2 및 IEC 62304 5.1의 요구사항에 따라 개발 단계, 담당 조직/역할, 게이트 리뷰(Design Review) 기준, 변경 관리 및 문서화 규칙을 정의합니다.
> - 특히 소프트웨어 안전성 등급(Class A/B/C)을 본 문서에서 최초로 지정하고 타당한 사유를 기재해야 합니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Medical Software Engineer | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Quality Assurance Manager | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Head of R&D / Medical Officer | Approved | `[YYYY-MM-DD]` |

---

## 2. Scope & Device Identification
- **Proprietary Name**: `[Commercial Trade Name]`
- **Model / Version Identifier**: `[e.g., PathoView-AI v1.0.0]`
- **Software Safety Classification (IEC 62304)**: `[Class A / B / C]`
  - *Justification*: `[State why this classification is chosen based on possible harm severity prior to risk controls]`

---

## 3. Development Lifecycle Model & Stages
This project implements the **IEC 62304 V-Model** with continuous parallel risk management (ISO 14971) and cybersecurity engineering (IEC 81001-5-1).

| Phase # | Lifecycle Stage | Primary Deliverable | Review Gate |
| :--- | :--- | :--- | :--- |
| **Phase 1** | User Needs & Intended Purpose | `DHF-01-Intended-Use-and-URD.md` | Gate 1 Review |
| **Phase 2** | Clinical Literature & SOTA | `DHF-02-Clinical-Literature-and-SOTA.md` | Gate 2 Review |
| **Phase 3** | Regulatory Strategy Profile | `DHF-03-Regulatory-Strategy-and-Clearance-Profile.md` | Gate 3 Review |
| **Phase 4** | Software Requirements (SRS) | `DHF-04-Software-Requirements-Specification-SRS.md` | Gate 4 Review |
| **Phase 5** | Parallel Risk Management | `DHF-05A/B/C Risk Management File` | Gate 5 Review |
| **Phase 6** | Cybersecurity & SBOM | `DHF-06-Cybersecurity-Threat-Model-and-SBOM.md` | Gate 5 Review |
| **Phase 7** | System & SW Architecture | `DHF-07-Software-Architectural-Design-Specification-SDS.md` | Gate 6 Review |
| **Phase 8** | Detailed Software Design | `DHF-08-Software-Detailed-Design-Specification-DDS.md` | Gate 7 Review |
| **Phase 9** | Implementation & Unit Verif | Source Code & Unit Test Evidence | Gate 8 Review |
| **Phase 10**| Independent V&V Testing | `DHF-09-Software-Verification-and-Validation-Report.md` | Gate 9 Review |
| **Phase 11**| Final Traceability & DHF Audit| `DHF-10-Traceability-Matrix-RTM.md` & `DHF-11-Audit-Report.md` | Gate 10 Release |

---

## 4. Multi-Agent Organization & Responsibilities

| Agent / Subagent | Assigned Role in Project | Key Standard Covered |
| :--- | :--- | :--- |
| `samd-orchestrator` | Project Lead & Gate Review Administrator | ISO 13485 Cl 7.3, IEC 62304 Cl 5.1 |
| `user-needs-agent` | Product Manager & Clinical Requirements Lead | ISO 13485 Cl 7.3.2, IEC 62366-1 |
| `clinical-sota-agent` | Clinical Evaluation Specialist | EU IVDR Annex XIII, MDCG 2020-1 |
| `regulatory-affairs-agent` | Global RA Lead | MFDS, FDA 21 CFR, EU IVDR |
| `srs-analyst-agent` | Lead Software Requirements Analyst | IEC 62304 Cl 5.2 |
| `risk-management-agent` | Medical Device Risk Management Officer | ISO 14971:2019, IEC 62304 Cl 7 |
| `cybersecurity-agent` | Cybersecurity & DevSecOps Lead | IEC 81001-5-1, FDA Cybersecurity |
| `system-architect-agent` | Principal System Architect | IEC 62304 Cl 5.3 |
| `detailed-design-agent` | Senior Detailed Design Engineer | IEC 62304 Cl 5.4 |
| `software-developer-agent` | Regulated Software Developer | IEC 62304 Cl 5.5 |
| `vnv-test-engineer-agent` | Independent V&V Lead | IEC 62304 Cl 5.6/5.7 |
| `dhf-lead-auditor-agent` | Lead Quality Assurance Auditor | ISO 13485 Cl 7.3.7, DHF Audit |

---

## 5. Design Review & Gate Checklists
Each gate requires formal verification that:
1. All input deliverables are complete and version-controlled.
2. Traceability tags are maintained without broken links.
3. Automated validation script passes: `python3 scripts/validate_traceability.py`.
4. Reviewer and Approver electronic signatures are recorded.
