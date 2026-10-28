# Framework Master Requirements Traceability Matrix (RTM)

> **Document ID**: `FRAMEWORK-RTM-001`  
> **System Under Design**: Antigravity SaMD Multi-Agent System (Framework)  
> **Target Standards**: ISO 13485:2016 Clause 7.3, IEC 62304:2006+AMD1:2015 Clause 5.1.1, ISO 14971:2019, IEC 62366-1:2015, FDA 21 CFR Part 11, GMLP, FDA Cybersecurity (2023)  
> **Version**: 2.1.0 | **Effective Date**: 2026-10-28  
> **Author**: Antigravity SaMD Framework Engineering Team  
> **Reviewer**: Lead Quality & Regulatory Auditor  
> **Approver**: Medical Device Software Project Director  
> **Status**: Approved (100% Traceability Verified, 0 Orphan Items)  

---

## 1. Overview & Traceability Invariant Standard
This document establishes the authoritative bidirectional traceability matrix for the **Antigravity SaMD Framework itself**. Every functional requirement (`FR-*`) is mapped forward and backward across:
- **Parent Standards / Regulations**: ISO 13485, IEC 62304 (Clauses 5, 6, 7, 8, 9), ISO 14971, IEC 62366-1, FDA 21 CFR Part 11, GMLP, FDA Premarket Cybersecurity, MFDS AI SaMD Guidelines.
- **Risk Hazard & Control**: ISO 14971 Hazard (`RSK-FW-*`) and Risk Control Measure (`RCM-FW-*`).
- **Software Architecture**: IEC 62304 Clause 5.3 Architectural Component (`ARCH-FW-*`).
- **Software Detailed Design**: IEC 62304 Clause 5.4 Detailed Unit Design (`DDS-FW-*`).
- **Implementation Artifact**: Source code scripts, Antigravity skills, agent prompt files, or templates.
- **Test Case Protocol**: 1:1 Mapped Test Specification (`TC-FR-*`).
- **Verification Execution Evidence**: Automated verification evidence ID (`VERIF-FW-*`).

---

## 2. Complete Bidirectional Traceability Matrix Table (60 Requirements)

| Req ID | Title / Domain | Risk Hazard / Control | Architecture ID | Detailed Design ID | Implementation Artifact | Test Protocol ID | Verification Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `FR-ORCH-001` | 12-Phase V-Model Lifecycle & Gate Governance | `RSK-FW-001` / `RCM-FW-001` | `ARCH-FW-003` | `DDS-FW-002` | `.agents/skills/samd-orchestrator/SKILL.md`<br>`workflows/00-v-model-lifecycle-workflow.md` | `TC-FR-ORCH-001` | `VERIF-FW-001` (PASS) |
| `FR-ORCH-002` | 2-Tier HITL Gate Review Human Sign-offs | `RSK-FW-001` / `RCM-FW-001` | `ARCH-FW-003` | `DDS-FW-002` | `workflows/00-v-model-lifecycle-workflow.md` | `TC-FR-ORCH-002` | `VERIF-FW-002` (PASS) |
| `FR-ORCH-003` | Parallel Risk & Security Sync on Change | `RSK-FW-003` / `RCM-FW-003` | `ARCH-FW-003` | `DDS-FW-002` | `workflows/02-risk-and-cybersecurity-parallel-workflow.md` | `TC-FR-ORCH-003` | `VERIF-FW-003` (PASS) |
| `FR-SKILL-001` | 13 Modular Skills & YAML Frontmatter Compliance | `RSK-FW-006` / `RCM-FW-006` | `ARCH-FW-001` | `DDS-FW-001` | `.agents/skills/*/SKILL.md` (13 skills) | `TC-FR-SKILL-001` | `VERIF-FW-004` (PASS) |
| `FR-SKILL-002` | Slash Commands & Semantic Triggering | `RSK-FW-006` / `RCM-FW-006` | `ARCH-FW-001` | `DDS-FW-001` | `.agents/skills/*/SKILL.md` (descriptions) | `TC-FR-SKILL-002` | `VERIF-FW-005` (PASS) |
| `FR-SKILL-003` | Skill Spec: `samd-orchestrator` | `RSK-FW-001` / `RCM-FW-001` | `ARCH-FW-001`, `ARCH-FW-003` | `DDS-FW-002` | `.agents/skills/samd-orchestrator/SKILL.md` | `TC-FR-SKILL-003` | `VERIF-FW-006` (PASS) |
| `FR-SKILL-004` | Skill Spec: `samd-user-needs` | `RSK-FW-012` / `RCM-FW-012` | `ARCH-FW-001`, `ARCH-FW-007` | `DDS-FW-007` | `.agents/skills/samd-user-needs/SKILL.md` | `TC-FR-SKILL-004` | `VERIF-FW-007` (PASS) |
| `FR-SKILL-005` | Skill Spec: `samd-clinical-sota` | `RSK-FW-006` / `RCM-FW-006` | `ARCH-FW-001`, `ARCH-FW-007` | `DDS-FW-007` | `.agents/skills/samd-clinical-sota/SKILL.md` | `TC-FR-SKILL-005` | `VERIF-FW-008` (PASS) |
| `FR-SKILL-006` | Skill Spec: `samd-regulatory-strategy` | `RSK-FW-006` / `RCM-FW-006` | `ARCH-FW-001`, `ARCH-FW-007` | `DDS-FW-007` | `.agents/skills/samd-regulatory-strategy/SKILL.md` | `TC-FR-SKILL-006` | `VERIF-FW-009` (PASS) |
| `FR-SKILL-007` | Skill Spec: `samd-srs` | `RSK-FW-006` / `RCM-FW-006` | `ARCH-FW-001`, `ARCH-FW-004` | `DDS-FW-003`, `DDS-FW-007` | `.agents/skills/samd-srs/SKILL.md` | `TC-FR-SKILL-007` | `VERIF-FW-010` (PASS) |
| `FR-SKILL-008` | Skill Spec: `samd-risk-mgmt` | `RSK-FW-006` / `RCM-FW-006` | `ARCH-FW-001`, `ARCH-FW-004` | `DDS-FW-003`, `DDS-FW-007` | `.agents/skills/samd-risk-mgmt/SKILL.md` | `TC-FR-SKILL-008` | `VERIF-FW-011` (PASS) |
| `FR-SKILL-009` | Skill Spec: `samd-cybersecurity` | `RSK-FW-013` / `RCM-FW-013` | `ARCH-FW-001`, `ARCH-FW-004` | `DDS-FW-003`, `DDS-FW-007` | `.agents/skills/samd-cybersecurity/SKILL.md` | `TC-FR-SKILL-009` | `VERIF-FW-012` (PASS) |
| `FR-SKILL-010` | Skill Spec: `samd-arch-design` | `RSK-FW-006` / `RCM-FW-006` | `ARCH-FW-001`, `ARCH-FW-004` | `DDS-FW-003`, `DDS-FW-007` | `.agents/skills/samd-arch-design/SKILL.md` | `TC-FR-SKILL-010` | `VERIF-FW-013` (PASS) |
| `FR-SKILL-011` | Skill Spec: `samd-detailed-design` | `RSK-FW-006` / `RCM-FW-006` | `ARCH-FW-001`, `ARCH-FW-004` | `DDS-FW-003`, `DDS-FW-007` | `.agents/skills/samd-detailed-design/SKILL.md` | `TC-FR-SKILL-011` | `VERIF-FW-014` (PASS) |
| `FR-SKILL-012` | Skill Spec: `samd-implementation` | `RSK-FW-006` / `RCM-FW-006` | `ARCH-FW-001`, `ARCH-FW-004` | `DDS-FW-003` | `.agents/skills/samd-implementation/SKILL.md` | `TC-FR-SKILL-012` | `VERIF-FW-015` (PASS) |
| `FR-SKILL-013` | Skill Spec: `samd-vnv-testing` | `RSK-FW-004` / `RCM-FW-004` | `ARCH-FW-001`, `ARCH-FW-002` | `DDS-FW-006`, `DDS-FW-007` | `.agents/skills/samd-vnv-testing/SKILL.md` | `TC-FR-SKILL-013` | `VERIF-FW-016` (PASS) |
| `FR-SKILL-014` | Skill Spec: `samd-dhf-audit` | `RSK-FW-002` / `RCM-FW-002` | `ARCH-FW-001`, `ARCH-FW-004`, `ARCH-FW-006` | `DDS-FW-003`, `DDS-FW-005` | `.agents/skills/samd-dhf-audit/SKILL.md` | `TC-FR-SKILL-014` | `VERIF-FW-017` (PASS) |
| `FR-AGENT-001` | 13 Specialist Agent Personas & Prompts | `RSK-FW-004` / `RCM-FW-004` | `ARCH-FW-002` | `DDS-FW-006` | `agents/*.md` (13 files) | `TC-FR-AGENT-001` | `VERIF-FW-018` (PASS) |
| `FR-AGENT-002` | Independence of Verification Persona Guard | `RSK-FW-004` / `RCM-FW-004` | `ARCH-FW-002` | `DDS-FW-006` | `agents/10-vnv-test-engineer-agent.md` | `TC-FR-AGENT-002` | `VERIF-FW-019` (PASS) |
| `FR-AGENT-003` | Subagent RBAC & Read-Only Sandbox Isolation | `RSK-FW-009` / `RCM-FW-009` | `ARCH-FW-002`, `ARCH-FW-009` | `DDS-FW-006` | `agents/*.md` | `TC-FR-AGENT-003` | `VERIF-FW-020` (PASS) |
| `FR-DHF-001` | 16 Standard DHF Markdown Templates | `RSK-FW-002` / `RCM-FW-002` | `ARCH-FW-007` | `DDS-FW-007` | `templates/DHF-*.md` (16 templates) | `TC-FR-DHF-001` | `VERIF-FW-021` (PASS) |
| `FR-DHF-002` | Bilingual Format (English Tables + Korean Tips) | `RSK-FW-002` / `RCM-FW-002` | `ARCH-FW-007` | `DDS-FW-007` | `templates/DHF-*.md` (callout blocks) | `TC-FR-DHF-002` | `VERIF-FW-022` (PASS) |
| `FR-DHF-003` | 15 Persistent Traceability Tag Standard | `RSK-FW-002` / `RCM-FW-002` | `ARCH-FW-004`, `ARCH-FW-007` | `DDS-FW-003`, `DDS-FW-007` | `templates/` & `AGENTS.md` | `TC-FR-DHF-003` | `VERIF-FW-023` (PASS) |
| `FR-TOOL-001` | Automated Bidirectional Traceability Validator | `RSK-FW-002` / `RCM-FW-002` | `ARCH-FW-004` | `DDS-FW-003` | `scripts/validate_traceability.py` | `TC-FR-TOOL-001` | `VERIF-FW-024` (PASS) |
| `FR-TOOL-002` | Cryptographic SHA-256 Master DHF Indexer | `RSK-FW-005` / `RCM-FW-005` | `ARCH-FW-006`, `ARCH-FW-010` | `DDS-FW-005` | `scripts/generate_dhf_index.py` | `TC-FR-TOOL-002` | `VERIF-FW-025` (PASS) |
| `FR-TOOL-003` | Zero External Dependency Standard Library Lock | `RSK-FW-005` / `RCM-FW-005` | `ARCH-FW-004`, `ARCH-FW-005`, `ARCH-FW-006` | `DDS-FW-003`, `DDS-FW-004`, `DDS-FW-005` | `scripts/*.py` | `TC-FR-TOOL-003` | `VERIF-FW-026` (PASS) |
| `FR-TOOL-004` | Cascading Downstream Invalidation Engine | `RSK-FW-003` / `RCM-FW-003` | `ARCH-FW-005` | `DDS-FW-004` | `scripts/check_change_impact.py` | `TC-FR-TOOL-004` | `VERIF-FW-027` (PASS) |
| `FR-RULE-001` | Workspace Rules & 24KB Budget Enforcement | `RSK-FW-007` / `RCM-FW-007` | `ARCH-FW-002` | `DDS-FW-006` | `AGENTS.md` | `TC-FR-RULE-001` | `VERIF-FW-028` (PASS) |
| `FR-MAINT-001` | Software Maintenance & Emergency Patch Governance | `RSK-FW-010` / `RCM-FW-010` | `ARCH-FW-011` | `DDS-FW-011` | `scripts/check_change_impact.py` | `TC-FR-MAINT-001` | `VERIF-FW-029` (PASS) |
| `FR-CM-001` | Configuration Management & Build Reproducibility | `RSK-FW-014` / `RCM-FW-014` | `ARCH-FW-011` | `DDS-FW-005` | `scripts/generate_dhf_index.py` | `TC-FR-CM-001` | `VERIF-FW-030` (PASS) |
| `FR-ANOM-001` | Problem Resolution & Anomaly/CAPA Integration | `RSK-FW-014` / `RCM-FW-014` | `ARCH-FW-011` | `DDS-FW-011` | `workflows/00-v-model-lifecycle-workflow.md` | `TC-FR-ANOM-001` | `VERIF-FW-031` (PASS) |
| `FR-SOUP-001` | SOUP Lifecycle Qualification & CVE Surveillance | `RSK-FW-013` / `RCM-FW-013` | `ARCH-FW-011` | `DDS-FW-003` | `templates/DHF-06-Cybersecurity-Threat-Model-and-SBOM.md` | `TC-FR-SOUP-001` | `VERIF-FW-032` (PASS) |
| `FR-USE-001` | Usability Engineering & PCA Use Error Analysis | `RSK-FW-012` / `RCM-FW-012` | `ARCH-FW-007` | `DDS-FW-007` | `templates/DHF-01-Intended-Use-and-URD.md` | `TC-FR-USE-001` | `VERIF-FW-033` (PASS) |
| `FR-CYBER-001` | Post-Market Cybersecurity IRP & CVD SLA | `RSK-FW-013` / `RCM-FW-013` | `ARCH-FW-011` | `DDS-FW-011` | `templates/DHF-06-Cybersecurity-Threat-Model-and-SBOM.md` | `TC-FR-CYBER-001` | `VERIF-FW-034` (PASS) |
| `FR-PART11-001` | Immutable Audit Trail & Electronic Signature | `RSK-FW-011` / `RCM-FW-011` | `ARCH-FW-010` | `DDS-FW-010` | `scripts/record_audit_event.py`<br>`scripts/generate_dhf_index.py` | `TC-FR-PART11-001` | `VERIF-FW-035` (PASS) |
| `FR-AI-001` | Clinical Data Provenance & Multi-Reader Annotation | `RSK-FW-008` / `RCM-FW-008` | `ARCH-FW-008` | `DDS-FW-008` | `templates/DHF-09-Software-Verification-and-Validation-Report.md` | `TC-FR-AI-001` | `VERIF-FW-036` (PASS) |
| `FR-AI-002` | Independent Test Set Freeze & Leakage Prevention | `RSK-FW-008` / `RCM-FW-008` | `ARCH-FW-008` | `DDS-FW-008` | `scripts/validate_ai_dataset.py`<br>`templates/DHF-09-Software-Verification-and-Validation-Report.md` | `TC-FR-AI-002` | `VERIF-FW-037` (PASS) |
| `FR-AI-003` | Subgroup Bias Auditing & Multi-Center Generalization | `RSK-FW-008` / `RCM-FW-008` | `ARCH-FW-008` | `DDS-FW-008` | `scripts/validate_ai_dataset.py`<br>`templates/DHF-09-Software-Verification-and-Validation-Report.md` | `TC-FR-AI-003` | `VERIF-FW-038` (PASS) |
| `FR-AI-004` | Real-Time Data/Concept Drift & PCCP Trigger | `RSK-FW-010` / `RCM-FW-010` | `ARCH-FW-008` | `DDS-FW-008` | `scripts/validate_ai_dataset.py`<br>`templates/DHF-13-Software-Maintenance-and-Problem-Resolution.md` | `TC-FR-AI-004` | `VERIF-FW-039` (PASS) |
| `FR-LLM-001` | LLM Hallucination Prevention & Regulatory Grounding | `RSK-FW-009` / `RCM-FW-009` | `ARCH-FW-009` | `DDS-FW-009` | `.agents/skills/samd-clinical-sota/SKILL.md` | `TC-FR-LLM-001` | `VERIF-FW-040` (PASS) |
| `FR-LLM-002` | Prompt Injection Defense & Sandbox Security | `RSK-FW-009` / `RCM-FW-009` | `ARCH-FW-009` | `DDS-FW-009` | `scripts/verify_grounding.py`<br>`agents/*.md` | `TC-FR-LLM-002` | `VERIF-FW-041` (PASS) |
| `FR-LLM-003` | Deterministic Agent Execution for Reproducibility | `RSK-FW-009` / `RCM-FW-009` | `ARCH-FW-009` | `DDS-FW-009` | `scripts/verify_grounding.py`<br>`agents/*.md` | `TC-FR-LLM-003` | `VERIF-FW-042` (PASS) |
| `FR-HOOK-001` | Antigravity Event-Driven Regulatory Linting Hooks | `RSK-FW-015` / `RCM-FW-015` | `ARCH-FW-001`, `ARCH-FW-004` | `DDS-FW-003` | `.agents/hooks.json`<br>`scripts/hook_pre_write_guard.py` | `TC-FR-HOOK-001` | `VERIF-FW-043` (PASS) |
| `FR-MCP-001` | Model Context Protocol Interface for Regulatory DBs | `RSK-FW-015` / `RCM-FW-015` | `ARCH-FW-001` | `DDS-FW-001` | `.agents/skills/samd-clinical-sota/SKILL.md` | `TC-FR-MCP-001` | `VERIF-FW-044` (PASS) |
| `FR-TRANS-001` | Design Transfer to Production & DMR Packaging | `RSK-FW-001` / `RCM-FW-001` | `ARCH-FW-010` | `DDS-FW-010` | `templates/DHF-00-Design-and-Development-Plan-DDP.md`<br>`templates/DHF-11-DHF-Index-and-Quality-Audit-Report.md` | `TC-FR-TRANS-001` | `VERIF-FW-045` (PASS) |
| `FR-INT-001` | Software Integration & Subsystem Interface Verification | `RSK-FW-004` / `RCM-FW-004` | `ARCH-FW-005` | `DDS-FW-005` | `tests/integration/test_framework_integration.py` | `TC-FR-INT-001` | `VERIF-FW-046` (PASS) |
| `FR-AI-005` | Explainable AI Saliency Maps & Uncertainty Display | `RSK-FW-008` / `RCM-FW-008` | `ARCH-FW-008` | `DDS-FW-008` | `scripts/verify_grounding.py`<br>`templates/DHF-08-Software-Detailed-Design-Specification-DDS.md` | `TC-FR-AI-005` | `VERIF-FW-047` (PASS) |
| `FR-AI-006` | Input Quality Assessment & OOD Rejection | `RSK-FW-008` / `RCM-FW-008` | `ARCH-FW-008` | `DDS-FW-008` | `scripts/validate_ai_dataset.py`<br>`templates/DHF-08-Software-Detailed-Design-Specification-DDS.md` | `TC-FR-AI-006` | `VERIF-FW-048` (PASS) |
| `FR-AI-007` | Clinical Performance Evaluation with 95% CI | `RSK-FW-008` / `RCM-FW-008` | `ARCH-FW-008` | `DDS-FW-008` | `scripts/validate_ai_dataset.py`<br>`templates/DHF-09-Software-Verification-and-Validation-Report.md` | `TC-FR-AI-007` | `VERIF-FW-049` (PASS) |
| `FR-USE-002` | Summative Usability Evaluation & URRA Protocol | `RSK-FW-012` / `RCM-FW-012` | `ARCH-FW-007` | `DDS-FW-007` | `templates/DHF-12-Usability-Engineering-File-UEF.md` | `TC-FR-USE-002` | `VERIF-FW-050` (PASS) |
| `FR-CYBER-002` | Secure Architecture, Threat Model & SAST/DAST | `RSK-FW-013` / `RCM-FW-013` | `ARCH-FW-011` | `DDS-FW-011` | `templates/DHF-06-Cybersecurity-Threat-Model-and-SBOM.md` | `TC-FR-CYBER-002` | `VERIF-FW-051` (PASS) |
| `FR-PART11-002` | Automated Cryptographic Audit Event Logger | `RSK-FW-011` / `RCM-FW-011` | `ARCH-FW-010` | `DDS-FW-010` | `scripts/record_audit_event.py` | `TC-FR-PART11-002` | `VERIF-FW-052` (PASS) |
| `FR-ANOM-002` | Software Defect Trend Analysis & Vigilance Reporting | `RSK-FW-014` / `RCM-FW-014` | `ARCH-FW-011` | `DDS-FW-011` | `scripts/manage_anomalies.py`<br>`templates/DHF-13-Software-Maintenance-and-Problem-Resolution.md` | `TC-FR-ANOM-002` | `VERIF-FW-053` (PASS) |
| `FR-PMS-001` | Post-Market Clinical Follow-up & PSUR Reporting | `RSK-FW-014` / `RCM-FW-014` | `ARCH-FW-011` | `DDS-FW-011` | `templates/DHF-13-Software-Maintenance-and-Problem-Resolution.md`<br>`templates/DHF-05C-Risk-Management-Report-RMR.md` | `TC-FR-PMS-001` | `VERIF-FW-054` (PASS) |
| `FR-SKILL-015` | Skill Spec: `samd-maintenance` | `RSK-FW-010` / `RCM-FW-010`, `RSK-FW-014` / `RCM-FW-014` | `ARCH-FW-001`, `ARCH-FW-011` | `DDS-FW-011` | `.agents/skills/samd-maintenance/SKILL.md` | `TC-FR-SKILL-015` | `VERIF-FW-055` (PASS) |
| `FR-LBL-001` | Medical Device Labeling & Electronic Instructions for Use (e-IFU) | `RSK-FW-012` / `RCM-FW-012` | `ARCH-FW-007` | `DDS-FW-007` | `templates/DHF-14-Labeling-and-Instructions-for-Use-IFU.md` | `TC-FR-LBL-001` | `VERIF-FW-056` (PASS) |
| `FR-CLIN-001` | Statutory Clinical Evaluation Report & 3-Pillar SOTA Dossier | `RSK-FW-006` / `RCM-FW-006` | `ARCH-FW-008` | `DDS-FW-008` | `templates/DHF-15-Clinical-Evaluation-Report-CER.md` | `TC-FR-CLIN-001` | `VERIF-FW-057` (PASS) |
| `FR-TOOL-005` | Computerized Software Tool Validation & Self-Audit Framework Mode | `RSK-FW-005` / `RCM-FW-005` | `ARCH-FW-004` | `DDS-FW-003` | `scripts/validate_traceability.py` | `TC-FR-TOOL-005` | `VERIF-FW-058` (PASS) |
| `FR-SOUP-002` | Cloud Foundation LLM Supplier Qualification & BAA Governance | `RSK-FW-007` / `RCM-FW-007` | `ARCH-FW-011` | `DDS-FW-011` | `templates/DHF-06-Cybersecurity-Threat-Model-and-SBOM.md`<br>`scripts/manage_anomalies.py` | `TC-FR-SOUP-002` | `VERIF-FW-059` (PASS) |
| `FR-ORCH-004` | Multi-Agent Parallel Concurrency Control & Atomic Shared State Locking | `RSK-FW-001` / `RCM-FW-001` | `ARCH-FW-003` | `DDS-FW-002` | `scripts/record_audit_event.py`<br>`templates/project_state.json` | `TC-FR-ORCH-004` | `VERIF-FW-060` (PASS) |

---

## 3. Detailed Design Risk Control Allocation Table (IEC 62304 Cl 5.4.2 & ISO 14971 Cl 7.1)

| Detailed Design ID | Unit Title | Parent Architecture | Safety Class | Allocated Risk Controls (RCM ID) | Inherent Safety Invariant / Interlock Mechanism | Verification Protocol |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| `DDS-FW-001` | YAML Frontmatter Lexer & Skill Contract Validator Unit | `ARCH-FW-001` | Class B | `RCM-FW-006`, `RCM-FW-015` | Fail-closed regex lexer; context budget bounds; pre-tool-call intercept validation | `TC-FR-SKILL-001`, `TC-FR-HOOK-001`, `TC-FR-MCP-001` |
| `DDS-FW-002` | Orchestration State Machine & Gate Transition Interlock | `ARCH-FW-003` | Class B | `RCM-FW-001`, `RCM-FW-003` | 2-Tier HITL gate interlock requiring cryptographic human APPROVE; event-driven risk sync; atomic state file lock | `TC-FR-ORCH-001`, `TC-FR-ORCH-002`, `TC-FR-ORCH-003`, `TC-FR-ORCH-004` |
| `DDS-FW-003` | Traceability Matrix Graph Engine & Orphan Detection Unit | `ARCH-FW-004` | Class B | `RCM-FW-002`, `RCM-FW-005`, `RCM-FW-015` | Bipartite graph connectivity with zero orphan tolerance; dual-mode CSV self-validation; zero-SOUP native Python standard library | `TC-FR-TOOL-001`, `TC-FR-HOOK-001`, `TC-FR-TOOL-005` |
| `DDS-FW-004` | Downstream Invalidation & Dependency Graph Traversal Engine | `ARCH-FW-005` | Class B | `RCM-FW-003`, `RCM-FW-005` | Tarjan's cycle-free DAG traversal; unbounded transitive downstream invalidation | `TC-FR-TOOL-004` |
| `DDS-FW-005` | DHF Document Indexer & Checksum Verifier Unit | `ARCH-FW-006` | Class B | `RCM-FW-005` | Chunked 64KB SHA-256 stream hashing; newline normalization (`\r\n` -> `\n`); zero external dependencies | `TC-FR-TOOL-002`, `TC-FR-CM-001` |
| `DDS-FW-006` | Subagent Persona Definition & Privilege Sandbox Isolation Unit | `ARCH-FW-002` | Class B | `RCM-FW-004`, `RCM-FW-007` | Read-only OS chroot sandbox for V&V tester; prompt immutability and context limit enforcement | `TC-FR-AGENT-002`, `TC-FR-AGENT-003`, `TC-FR-RULE-001` |
| `DDS-FW-007` | Usability Feedback & Safety Warning Banner Enforcement Unit | `ARCH-FW-007` | Class B | `RCM-FW-012` | High-contrast non-occluding warning banners under IEC 62366-1; primary slide viewport preservation; e-IFU & labeling consistency | `TC-FR-USE-001`, `TC-FR-SKILL-004`, `TC-FR-LBL-001` |
| `DDS-FW-008` | AI Dataset Partitioning & Statistical Drift Detection Unit | `ARCH-FW-008` | Class C | `RCM-FW-008`, `RCM-FW-010` | Salted SHA-256 patient-level isolation (0.00% overlap); real-time KS-test & PSI >= 0.25 threshold; statutory CER dossier equivalence | `TC-FR-AI-002`, `TC-FR-AI-004`, `TC-FR-CLIN-001` |
| `DDS-FW-009` | LLM Medical Safety Guardrails & Adversarial Verification Unit | `ARCH-FW-009` | Class B | `RCM-FW-004`, `RCM-FW-009` | Dual-pass regex and semantic prompt injection filter; automated NLM PubMed citation validation | `TC-FR-LLM-001`, `TC-FR-LLM-002` |
| `DDS-FW-010` | Part 11 Electronic Signature & HMAC Audit Trail Unit | `ARCH-FW-010` | Class B | `RCM-FW-011` | Append-only WORM file descriptors; HMAC-SHA256 signature chain; RFC 3161 monotonic timestamps | `TC-FR-PART11-001` |
| `DDS-FW-011` | Post-Market Vulnerability SLA & Defect Release Block Unit | `ARCH-FW-011` | Class B | `RCM-FW-013`, `RCM-FW-014` | Automated CVSS >= 9.0 30-day/60-day SLA enforcement; Gate 10 release block on unresolved Sev 1/2 anomalies; cloud LLM BAA qualification | `TC-FR-CYBER-001`, `TC-FR-ANOM-001`, `TC-FR-SOUP-002` |

---

## 4. Bidirectional Invariant Verification Summary
- **Total Requirements (`FR-*`)**: 60
- **Total Risk Hazard / Control Items (`RSK-FW-*` / `RCM-FW-*`)**: 15 (Direct 100% allocation, Zero umbrella placeholders)
- **Total Architectural Components (`ARCH-FW-*`)**: 11
- **Total Detailed Design Units (`DDS-FW-*`)**: 11
- **Detailed Design Risk Control Coverage**: **100.0% (15 / 15 RCMs allocated across 11 DDS units)**
- **Total 1:1 Mapped Test Protocols (`TC-FR-*`)**: 60
- **Total Verification Records (`VERIF-FW-*`)**: 60
- **Orphan Requirements**: 0 (0.0%)
- **Untested Requirements**: 0 (0.0%)
- **Traceability Coverage**: **100.0% Comprehensive Bidirectional Compliance**
