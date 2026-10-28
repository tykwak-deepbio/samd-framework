# SaMD IEC 62304 V-Model Lifecycle & Gate Review Workflow

> **Framework Guide**: `WF-00-LIFECYCLE`  
> **Applicable Standards**: IEC 62304:2006+AMD1:2015, ISO 13485:2016 Clause 7.3, ISO 14971:2019  

---

## 1. Overview & High-Level Lifecycle Flow

The Antigravity SaMD Framework governs the end-to-end development of Software as a Medical Device (SaMD) through a formal **12-Phase V-Model lifecycle** with continuous parallel risk management and cybersecurity surveillance.

```
       [Decomposition & Design]                                       [Integration & Verification]

  [Gate 1] Phase 1: User Needs (URD) ───────────── Traceability ──────► Phase 11: Design Transfer & DHF Release [Gate 11]
              │                                                                    ▲
  [Gate 2] Phase 2: Clinical SOTA Review                                           │
              │                                                                    │
  [Gate 3] Phase 3: Regulatory Strategy Profile                                    │
              │                                                                    │
  [Gate 4] Phase 4: Software Requirements (SRS/UEF) Traceability ─────► Phase 10: System & Usability V&V [Gate 10]
              │                                                                    ▲
  [Gate 7] Phase 7: System Architecture (SDS) ──── Traceability ──────► Phase 10: Integration Testing
              │                                                                    ▲
  [Gate 8] Phase 8: Detailed Software Design (DDS)  Traceability ──────► Phase 9: Unit Verification [Gate 9]
              │                                                                    ▲
              └────────────────► Phase 9: Implementation (Vertex) ─────────────────┘

  [Continuous Parallel Track]:
  - Phase 5: ISO 14971 Risk Management [Gate 5] (RMP -> PHA -> FMEA -> RCM -> RMR)
  - Phase 6: Cybersecurity & SBOM [Gate 6] (IEC 81001-5-1, FDA: Threat Modeling -> SBOM -> CVE)

  [Post-Market Maintenance Track]:
  - Phase 12: Post-Market Surveillance, Maintenance & Anomaly Resolution [Gate 12] (IEC 62304 Cl 6/9, ISO 14971 Cl 10, DHF-13)
```

---

## 2. Multi-Tier Human-in-the-Loop (HITL) Gate Governance

A "Gate Review" is a formal quality control checkpoint under ISO 13485 Clause 7.3.5.
To ensure comprehensive governance, the framework classifies all 12 Gates into **Tier 1 (Major Regulatory Sign-Offs)** and **Tier 2 (Engineering Milestone Sign-Offs)**. Downstream phases MUST NOT proceed without explicit user approval.

| Gate | Tier | Focus / Scope | Responsible Agent & Skill | Required Deliverable | HITL Review & Exit Criteria |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **Gate 1** | **Tier 1 (Major)** | User Needs & Medical Intended Use | `user-needs-agent`<br>`samd-user-needs` | `DHF-01-Intended-Use-and-URD.md` | **Mandatory User Sign-off**: Medical claim, target population, contraindications, and `USER-REQ-*` agreed. |
| **Gate 2** | **Tier 2 (Milestone)** | Clinical SOTA & Baselines | `clinical-sota-agent`<br>`samd-clinical-sota` | `DHF-02-Clinical-Literature-and-SOTA.md` | **Clinical Review**: Literature benchmarks, predicate devices, and clinical targets (`CLIN-REQ-*`) confirmed. |
| **Gate 3** | **Tier 1 (Major)** | Regulatory Strategy & Safety Class | `regulatory-affairs-agent`<br>`samd-regulatory-strategy` | `DHF-03-Regulatory-Strategy-and-Clearance-Profile.md` | **Mandatory User Sign-off**: Safety Classification (Class A/B/C) and submission pathway (MFDS/FDA/IVDR) frozen. |
| **Gate 4** | **Tier 1 (Major)** | Software Requirements Baseline & Usability | `srs-analyst-agent`<br>`samd-srs` | `DHF-04-Software-Requirements-Specification-SRS.md`<br>`DHF-12-Usability-Engineering-File-UEF.md` | **Mandatory User Sign-off**: 100% backward traceability to User Needs, all `REQ-SW-*` testable and frozen. |
| **Gate 5** | **Tier 1 (Major)** | Risk Acceptability & Control Measures | `risk-management-agent`<br>`samd-risk-mgmt` | `DHF-05A/B Risk File` | **Mandatory User Sign-off**: All unacceptable initial risks assigned `RCM-*`, ISO 14971 matrix compliance verified. |
| **Gate 6** | **Tier 1 (Major)** | Cybersecurity Architecture & SBOM | `cybersecurity-agent`<br>`samd-cybersecurity` | `DHF-06-Cybersecurity-Threat-Model-and-SBOM.md` | **Mandatory User Sign-off**: STRIDE threat mitigations, CycloneDX SBOM, and CVE analysis accepted. |
| **Gate 7** | **Tier 2 (Milestone)** | Architecture & Safety Segregation | `system-architect-agent`<br>`samd-arch-design` | `DHF-07-Software-Architectural-Design-Specification-SDS.md` | **Architecture Review**: Class A / Class B / Class C segregation proven, SOUP items and defensive wrappers accepted. |
| **Gate 8** | **Tier 2 (Milestone)** | Detailed Design & Math Formulas | `detailed-design-agent`<br>`samd-detailed-design` | `DHF-08-Software-Detailed-Design-Specification-DDS.md` | **Design Freeze**: Unit algorithms (OD, Macenko, AI input tensors, bounds checking) frozen before coding. |
| **Gate 9** | **Tier 2 (Milestone)** | Implementation & Unit Verification | `software-developer-agent`<br>`samd-implementation` | Production Code (`src/`) & Unit Tests (`tests/`) | **Code Review**: Docstring traceability verified, static analysis clean, $\ge 90\%$ safety-critical unit coverage. |
| **Gate 10**| **Tier 1 (Major)** | Independent V&V Acceptance & Usability | `vnv-test-engineer-agent`<br>`samd-vnv-testing` | `DHF-09-Software-Verification-and-Validation-Report.md` | **Mandatory User Sign-off**: Independent test report accepted, 100% test pass rate, AI clinical metrics meet thresholds. |
| **Gate 11**| **Tier 1 (Major)** | Design Transfer, DHF Release & Clearance | `dhf-lead-auditor-agent`<br>`samd-dhf-audit` | `DHF-10-Traceability-Matrix-RTM.md`<br>`DHF-11-DHF-Index-and-Quality-Audit-Report.md`<br>`DHF-00-Design-and-Development-Plan-DDP.md` | **Executive QMS Sign-off**: 0 orphans, SHA-256 master index certified, regulatory submission dossier released. |
| **Gate 12**| **Tier 1 (Major)** | Post-Market Maintenance & Anomaly Resolution | `postmarket-maintenance-agent`<br>`samd-maintenance` | `DHF-13-Software-Maintenance-and-Problem-Resolution.md`<br>`DHF-05C-Risk-Management-Report-RMR.md` | **Post-Market Sign-off**: Anomaly triage, PCCP drift surveillance, hotfix verification, and PMCF risk updates certified. |

---

## 3. Cascading Invalidation Principle (연쇄적 승인 무효화 규칙)

Under ISO 13485 Clause 7.3.9 and IEC 62304 Clause 8, medical software design is strictly hierarchical.
**Any modification to an upstream artifact automatically REVOKES the approved status of all downstream artifacts.**

```
[Change in DHF-04 (SRS)]
         │
         ▼
[Automatic Status Transition] ──► DHF-05B (Risk Matrix):       INVALIDATED (APPROVAL REVOKED)
                               ──► DHF-07  (Architecture):      INVALIDATED (APPROVAL REVOKED)
                               ──► DHF-08  (Detailed Design):   INVALIDATED (APPROVAL REVOKED)
                               ──► src/    (Implementation):    INVALIDATED (CODE UNVERIFIED)
                               ──► DHF-09  (V&V Report):        INVALIDATED (RE-TEST REQUIRED)
                               ──► DHF-10  (Traceability RTM):  INVALIDATED (RE-AUDIT REQUIRED)
                               ──► DHF-11  (DHF Master Index):  INVALIDATED (RELEASE REVOKED)
```

### Invalidation Enforcement Workflow
1. When a document changes (detected via hash discrepancy or git commit), run:
   ```bash
   python3 scripts/check_change_impact.py dhf/
   ```
2. The script returns exit code `2` and displays a formal **Change Impact Analysis (CIA)** report.
3. No downstream artifact can be submitted or approved until the upstream change is formally signed off and sequential re-verification down the V-model is completed.

---

## 4. Change History & Version Control Strategy (이력 및 버전 관리 방안)

### 4.1 Document Versioning Standard (문서 버전 번호 체계)
- **Draft Stages**: `v0.1`, `v0.2`, `v0.3` ... (Under initial drafting, pre-gate review).
- **Approved Baseline**: `v1.0` (Formal sign-off at gate review).
- **Minor Revisions**: `v1.1`, `v1.2` ... (Formatting, typo fixes, non-functional clarifications without risk or interface impact).
- **Major Revisions**: `v2.0`, `v3.0` ... (Scope changes, algorithmic modifications, new clinical indications, new hazards, requiring full Change Request `CR-xxx`).

### 4.2 Document Revision History Table (문서 내 변경 이력표 표준)
Every DHF document must contain a standardized revision history block:
```markdown
## Document Revision History
| Version | Release Date | Author | CR / ECO ID | Change Description & Clinical Rationale | Approver |
| :---: | :---: | :--- | :--- | :--- | :--- |
| `0.1` | YYYY-MM-DD | [Author] | - | Initial draft for Gate Review. | In-Review |
| `1.0` | YYYY-MM-DD | [Author] | `CR-001` | Formal baseline approved at Gate 4. | [Approver] |
```

### 4.3 Git-Based Change Control & Baseline Tagging
1. **Commit Message Format**:
   `[CR-xxx] [Gate-x] [Tag-ID] Detailed explanation of design change`
2. **Cryptographic Baseline Freezing**:
   When a gate review is approved, freeze the baseline using git tags and hash manifests:
   ```bash
   python3 scripts/check_change_impact.py dhf/ --save-baseline
   git tag -a v1.0-gate4-srs-approved -m "Gate 4 SRS Approved Baseline"
   ```
3. **Automated Tamper Detection**:
   Any deviation from `.dhf_baseline.json` is flagged by `check_change_impact.py`, guaranteeing full audit-trail integrity.
