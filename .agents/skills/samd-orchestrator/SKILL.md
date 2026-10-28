---
name: samd-orchestrator
description: Orchestrates the end-to-end SaMD (Software as a Medical Device) development lifecycle following the IEC 62304 V-model, ISO 14971 parallel risk management, and ISO 13485 DHF compilation. Use this skill when initiating or coordinating an entire SaMD project or conducting lifecycle gate reviews.
---

# SaMD V-Model Lifecycle Orchestrator

This skill orchestrates the multi-agent execution of the Software as a Medical Device (SaMD) lifecycle, adhering to **IEC 62304:2006/AMD1:2015**, **ISO 14971:2019**, **ISO 13485:2016 (Clause 7.3)**, **IEC 62366-1:2015**, and **FDA/MFDS/EU IVDR** regulations.

```
                  [V-Model Decomposition & Design]                   [V-Model Integration & Verification]
  Phase 1: User Needs (Intended Use) ────────────── Gate 1 ──────► Phase 11: Design Transfer & Release [Gate 11]
           │                                                                 ▲
  Phase 2: Clinical SOTA & Lit. Review ──────────── Gate 2                   │
           │                                                                 │
  Phase 3: Regulatory Strategy & Profile ────────── Gate 3                   │
           │                                                                 │
  Phase 4: Software Requirements (SRS/UEF) ──────── Gate 4 ──────► Phase 10: Independent V&V Testing [Gate 10]
           │                                                                 ▲
  Phase 7: System & SW Architecture (SDS) ───────── Gate 7 ──────► Phase 10: Integration Testing
           │                                                                 ▲
  Phase 8: Detailed SW Design (DDS) ─────────────── Gate 8 ──────► Phase 9: Unit Verification [Gate 9]
           │                                                                 ▲
           └────────────────► Phase 9: Implementation (Vertex) ──────────────┘

  [Continuous Parallel Track]:
  - Phase 5: Risk Management [Gate 5] (ISO 14971: RMP -> PHA -> FMEA -> RCM -> RMR)
  - Phase 6: Cybersecurity & SBOM [Gate 6] (IEC 81001-5-1, FDA: Threat Model -> SBOM -> CVE Mgmt)

  [Post-Market Maintenance Track]:
  - Phase 12: Post-Market Surveillance, Maintenance & Anomaly Resolution [Gate 12] (IEC 62304 Cl 6/9, ISO 14971 Cl 10, DHF-13)
```

## Lifecycle Gates & Invocation Rules

Before advancing to the next stage, the Orchestrator MUST verify that the formal Gate Review criteria are satisfied.

| Gate | Phase Name | Primary Skill / Agent | Key Deliverable | Gate Exit Criteria |
| :--- | :--- | :--- | :--- | :--- |
| **Gate 1** | User Needs & Intended Use | `samd-user-needs` | `DHF-01-Intended-Use-and-URD.md` | Clear intended purpose, patient population, contraindications, user profiles (`USER-REQ-*`) |
| **Gate 2** | Clinical Literature & SOTA | `samd-clinical-sota` | `DHF-02-Clinical-Literature-and-SOTA.md` | Clinical baseline, SOTA comparison, clinical endpoints defined (`CLIN-REQ-*`) |
| **Gate 3** | Regulatory Strategy | `samd-regulatory-strategy` | `DHF-03-Regulatory-Strategy-and-Clearance-Profile.md` | Target device classifications (MFDS/FDA/IVDR), applicable standards, PCCP strategy |
| **Gate 4** | Software Requirements & Usability | `samd-srs` | `DHF-04-Software-Requirements-Specification-SRS.md`<br>`DHF-12-Usability-Engineering-File-UEF.md` | All `REQ-SW-*` mapped to `USER-REQ-*`, safety class declared (Class A/B/C) |
| **Gate 5** | Risk Management (PHA/FMEA) | `samd-risk-mgmt` | `DHF-05A/B Risk File` | Initial PHA/FMEA completed, RCMs assigned, ISO 14971 acceptability matrix satisfied |
| **Gate 6** | Cybersecurity Architecture & SBOM | `samd-cybersecurity` | `DHF-06-Cybersecurity-Threat-Model-and-SBOM.md` | STRIDE threat mitigations, CycloneDX SBOM initialized, CVE vulnerability scan clean |
| **Gate 7** | System & SW Architecture | `samd-arch-design` | `DHF-07-Software-Architectural-Design-Specification-SDS.md` | Subsystems segregated (Class A/B/C), SOUP risk evaluated, AI pipeline architecture defined |
| **Gate 8** | Detailed Software Design | `samd-detailed-design` | `DHF-08-Software-Detailed-Design-Specification-DDS.md` | Unit interfaces, mathematical formulas, AI inference/preprocessing logic detailed |
| **Gate 9** | Implementation & Unit Verification | `samd-implementation` | Production Code, Unit Tests | Code complies with coding rules, 100% unit tests pass, static analysis clean, $\ge 90\%$ safety unit coverage |
| **Gate 10**| Independent V&V Testing | `samd-vnv-testing` | `DHF-09-Software-Verification-and-Validation-Report.md` | Independent system/integration tests pass, AI metrics (ROC, Sens/Spec) meet acceptance criteria |
| **Gate 11**| Design Transfer & DHF Release | `samd-dhf-audit` | `DHF-10-Traceability-Matrix-RTM.md`<br>`DHF-11-DHF-Index-and-Quality-Audit-Report.md`<br>`DHF-00-Design-and-Development-Plan-DDP.md` | 100% bidirectional coverage (`REQ ↔ RSK ↔ ARCH ↔ TC`), zero orphans, DHF released |
| **Gate 12**| Post-Market Maintenance & Anomalies | `samd-maintenance` | `DHF-13-Software-Maintenance-and-Problem-Resolution.md`<br>`DHF-05C-Risk-Management-Report-RMR.md` | Anomaly triage, defect resolution, PCCP drift monitoring, hotfix verification, PMCF update |

## Orchestrator Workflow Steps

1. **Project Initiation**:
   - Verify workspace directory structure (`dhf/`, `src/`, `tests/`, `scripts/`, `templates/project_state.json`).
   - Create or update `DHF-00-Design-and-Development-Plan-DDP.md`.
2. **Execute Stage Sequentially**:
   - Dispatch the specialized skill/agent for the active gate.
   - Inject the outputs of preceding gates into the agent's context.
3. **Conduct Gate Review**:
   - Check all acceptance criteria.
   - Request user confirmation across all 12 Gates.
   - Record formal sign-off in `dhf/project_state.json` and append HMAC audit event using `python3 scripts/record_audit_event.py`.
4. **Trigger Parallel Tracks**:
   - Ensure `samd-risk-mgmt` and `samd-cybersecurity` are invoked whenever requirements (Phase 4) or architectures (Phase 7) are modified.
5. **Run Automated Integrity Checks**:
   - Execute `python3 scripts/validate_traceability.py dhf/`
   - Execute `python3 scripts/generate_dhf_index.py dhf/`
   - Execute `python3 scripts/check_change_impact.py dhf/` to prevent cascading invalidation drift.
