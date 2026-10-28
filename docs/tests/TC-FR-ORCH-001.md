# Test Protocol: TC-FR-ORCH-001

> **Test Case ID**: `TC-FR-ORCH-001`  
> **Target Requirement**: `FR-ORCH-001` (11-Phase IEC 62304 V-Model Lifecycle & Gate Review Administration)  
> **Test Level**: System / Verification Test  
> **Verification Method**: Inspection & Automated Script Analysis  
> **Status**: Approved  

---

## 1. Test Objective
Verify that the SaMD framework provides an orchestrator skill (`.agents/skills/samd-orchestrator/SKILL.md`) and orchestrator agent (`agents/00-samd-orchestrator-agent.md`) that explicitly sequences all 11 phases of the IEC 62304 lifecycle and defines formal Gate Review Exit Criteria for each phase.

## 2. Preconditions
- The framework repository contains `.agents/skills/samd-orchestrator/SKILL.md` and `agents/00-samd-orchestrator-agent.md`.
- `workflows/00-v-model-lifecycle-workflow.md` is present.

## 3. Test Execution Steps
1. Parse `.agents/skills/samd-orchestrator/SKILL.md` and search for lifecycle table.
2. Verify all 11 phases (Phase 1 to Phase 11) and 10 Gates (Gate 1 to Gate 10) are explicitly defined.
3. Verify each gate defines:
   - Responsible skill / subagent.
   - Required deliverable (`DHF-01` through `DHF-11`).
   - Explicit objective Gate Exit Criteria.
4. Verify that `workflows/00-v-model-lifecycle-workflow.md` details the sequencing and review procedures.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: All 11 phases and 10 gates are enumerated with required deliverables and gate exit criteria.
- **FAIL**: Any phase is missing, unassigned, or lacks exit criteria.
