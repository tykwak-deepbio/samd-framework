# Test Protocol: TC-FR-SKILL-003

> **Test Case ID**: `TC-FR-SKILL-003`  
> **Target Requirement**: `FR-SKILL-003` (Skill Specification - `samd-orchestrator`)  
> **Test Level**: System Integration / Workflow Verification  
> **Verification Method**: Automated Static Analysis & Workflow Simulation (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `samd-orchestrator` correctly implements the 11-phase IEC 62304 V-model lifecycle, enforces 2-tier HITL gate exit checkpoints, and integrates with `scripts/check_change_impact.py` for cascading invalidation.

## 2. Preconditions
- `.agents/skills/samd-orchestrator/SKILL.md` exists and is registered.
- `workflows/00-v-model-lifecycle-workflow.md` is accessible.

## 3. Test Execution Steps
1. Inspect `.agents/skills/samd-orchestrator/SKILL.md` for definitions of all 11 lifecycle phases.
2. Verify explicit 2-tier HITL checkpoint specifications:
   - Tier 1 Major Gates (Gates 1, 3, 4, 5, 9, 10) requiring explicit human sign-offs.
   - Tier 2 Technical Gates (Gates 2, 6, 7, 8) with technical checklist validation.
3. Verify integration with `check_change_impact.py` for downstream revocation on requirement edits.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: All 11 phases, 10 gates with 2-tier classification, and cascading invalidation directives are present in `samd-orchestrator/SKILL.md`.
- **FAIL**: Any lifecycle phase is missing, or gate classification criteria are omitted.
