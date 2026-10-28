# Software Requirement: FR-ORCH-002

> **Requirement ID**: `FR-ORCH-002`  
> **Title**: Multi-Gate Human-in-the-Loop (HITL) Governance & Cascading Invalidation  
> **Category**: Orchestration & Lifecycle Governance (`[ORCH]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 13485:2016 Clause 7.3.5 (Design Review) & Clause 7.3.9 (Control of Design Changes), IEC 62304:2006 Clause 8 (Software Change Management)  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-ORCH-002.md`  

---

## 1. Description & Clinical/Regulatory Rationale
The framework shall enforce explicit Human-in-the-Loop (HITL) review and approval across all lifecycle gates. Furthermore, to maintain design control integrity, any upstream modification (e.g. changing a requirement in Phase 4) shall trigger **Cascading Invalidation**, automatically revoking all downstream approvals and mandating sequential re-review.

## 2. Detailed Functional Specifications
1. **Multi-Gate HITL Review Checkpoints**:
   - The framework shall mandate formal user review and sign-off at 12 discrete gates, categorized into Tier 1 (Major Regulatory Gates) and Tier 2 (Engineering Milestone Gates):
     * **Gate 1 (Tier 1 - Major)**: User Needs & Medical Intended Use Sign-off (`DHF-01`).
     * **Gate 2 (Tier 2 - Milestone)**: Clinical SOTA Baselines & Literature Review Sign-off (`DHF-02`).
     * **Gate 3 (Tier 1 - Major)**: Regulatory Device Classification & Software Safety Class (Class A/B/C) Sign-off (`DHF-03`).
     * **Gate 4 (Tier 1 - Major)**: Software Requirements Specification (SRS) & Usability Baseline (`DHF-04`, `DHF-12`).
     * **Gate 5 (Tier 1 - Major)**: ISO 14971 Risk Acceptability (PHA/FMEA) Sign-off (`DHF-05A/B`).
     * **Gate 6 (Tier 1 - Major)**: Cybersecurity Architecture, STRIDE Threat Model & SBOM Sign-off (`DHF-06`).
     * **Gate 7 (Tier 2 - Milestone)**: Software Architectural Design & Safety Segregation Sign-off (`DHF-07`).
     * **Gate 8 (Tier 2 - Milestone)**: Detailed Software Design (DDS) & Algorithm Freezing (`DHF-08`).
     * **Gate 9 (Tier 2 - Milestone)**: Implementation, Static Analysis & Unit Coverage ($\ge 90\%$) Sign-off (`src/`, `tests/`).
     * **Gate 10 (Tier 1 - Major)**: Independent Verification & Validation (V&V) Report Acceptance (`DHF-09`).
     * **Gate 11 (Tier 1 - Major)**: Design Transfer, Final Traceability Matrix & DHF Release Approval (`DHF-00`, `DHF-10`, `DHF-11`).
     * **Gate 12 (Tier 1 - Major)**: Post-Market Maintenance, Problem Resolution & Safety Update Sign-off (`DHF-13`, `DHF-05C`).
2. **Cascading Invalidation (연쇄적 승인 무효화)**:
   - When an artifact at Phase $M$ is modified after having been approved, the framework shall immediately transition the status of all downstream artifacts (Phase $M+1$ to Phase 12) to `INVALIDATED (APPROVAL REVOKED)`.
   - The framework shall mandate Change Impact Analysis (CIA) to identify all affected software items, test cases, and risk controls.
   - Downstream phases must be re-verified and re-approved sequentially down the V-model. No downstream artifact may be released while its upstream input is in an unapproved state.

## 3. Inputs, Processing & Outputs
- **Inputs**: Document change event (git diff or hash modification), gate review requests.
- **Processing**: Dependency graph evaluation, revocation of approval flags for all dependent downstream artifacts.
- **Outputs**: Invalidation alert, Change Impact Report, reset gate review status.
