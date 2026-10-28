# Test Protocol: TC-FR-ORCH-002

> **Test Case ID**: `TC-FR-ORCH-002`  
> **Target Requirement**: `FR-ORCH-002` (Multi-Gate HITL Governance & Cascading Invalidation)  
> **Test Level**: System / Automated Test  
> **Verification Method**: Automated Fault Injection & State Transition Verification  
> **Status**: Approved  

---

## 1. Test Objective
Verify that the framework enforces 10 discrete HITL review gates (Tier 1 Major & Tier 2 Milestone), and that modifying an approved upstream artifact immediately revokes all downstream approvals (Cascading Invalidation).

## 2. Preconditions
- Framework workflow documentation exists.
- Invalidation analysis script `scripts/check_change_impact.py` is present.
- A fully approved baseline DHF is available in a test fixture.

## 3. Test Execution Steps
1. Verify that `workflows/00-v-model-lifecycle-workflow.md` mandates user review at:
   - Gates 1, 3, 4, 5, 9, 10 (Tier 1 Major Regulatory Sign-offs).
   - Gates 2, 6, 7, 8 (Tier 2 Milestone Technical Sign-offs).
2. **Negative / Invalidation Test**:
   - In a temporary workspace with approved DHF files, modify an upstream requirement in `DHF-04-SRS`.
   - Execute `python3 scripts/check_change_impact.py <test_dhf_dir>`.
   - Verify that all downstream artifacts (`DHF-07`, `DHF-08`, `DHF-09`, `DHF-10`, `DHF-11`) are flagged as `INVALIDATED (APPROVAL REVOKED)`.
   - Verify that the tool returns exit code `2` indicating pending invalidations.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Modifying `DHF-04` triggers automatic revocation of approvals for all downstream items; script returns exit code `2` with full invalidation list.
- **FAIL**: Downstream items remain marked approved despite upstream modifications.
