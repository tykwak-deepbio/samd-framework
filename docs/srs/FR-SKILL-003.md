# Software Requirement: FR-SKILL-003

> **Requirement ID**: `FR-SKILL-003`  
> **Title**: Skill Specification - `samd-orchestrator` (V-Model Lifecycle & Gate Governance)  
> **Category**: Antigravity Skills Ecosystem (`[SKILL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006+AMD1:2015 Clause 5.1, ISO 13485:2016 Clause 7.3  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-SKILL-003.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-001.md`, `docs/architecture/ARCH-FW-003.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-002.md`  

---

## 1. Description & Technical Rationale
The `samd-orchestrator` skill shall coordinate the entire 12-phase SaMD development lifecycle conforming to the IEC 62304 V-Model. It acts as the central lifecycle controller that evaluates phase entry/exit criteria, enforces mandatory 2-tier Human-in-the-Loop (HITL) gate reviews, and triggers parallel risk/security synchronizations.

## 2. Detailed Functional Specifications
1. **12-Phase Lifecycle Management**: The skill shall govern transitions across all 12 lifecycle phases:
   - Phase 1: User Needs Discovery & Clinical Intended Use (`DHF-01`)
   - Phase 2: Clinical Literature & SOTA Medical Technology (`DHF-02`)
   - Phase 3: Regulatory Strategy & Classification Profile (`DHF-03`)
   - Phase 4: Software Requirements Specification (`DHF-04`)
   - Phase 5: Parallel Risk Management (`DHF-05A`, `05B`, `05C`)
   - Phase 6: Medical Device Cybersecurity & SBOM (`DHF-06`)
   - Phase 7: Software Architectural Design & Segregation (`DHF-07`)
   - Phase 8: Software Detailed Design (`DHF-08`)
   - Phase 9: Medical Coding & Unit Verification (`src/`, `tests/unit/`)
   - Phase 10: Independent Integration & System V&V (`DHF-09`)
   - Phase 11: Traceability Audit & Master DHF Release (`DHF-10`, `DHF-11`)
   - Phase 12: Post-Market Maintenance, Continuous Monitoring & Anomaly Resolution (`DHF-13`)
2. **2-Tier HITL Gate Review Enforcement**:
   - Tier 1 Major Gates (Gates 1, 3, 4, 5, 9, 10, 12): Shall halt automated execution and mandate formal human sign-off with recorded timestamp and reviewer name.
   - Tier 2 Technical Milestones (Gates 2, 6, 7, 8, 11): Shall evaluate objective technical checklists before proceeding.
3. **Cascading Invalidation Invocation**: When an upstream artifact (e.g. `DHF-04`) is modified, the skill shall invoke `scripts/check_change_impact.py` and revoke approvals of all downstream dependent artifacts.

## 3. Inputs, Processing & Outputs
- **Inputs**: Current project DHF status, user gate approval commands, upstream modification events.
- **Processing**: Gate checklist validation, phase transition state machine, downstream impact analysis invocation.
- **Outputs**: Phase advancement status, gate review audit logs, and invocation of specialized subagents/skills.
