# Test Protocol: TC-FR-SKILL-015

> **Test Case ID**: `TC-FR-SKILL-015`  
> **Target Requirement**: `FR-SKILL-015` (Skill Specification - `samd-maintenance`)  
> **Test Level**: System / Post-Market Process Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `samd-maintenance` defines post-market software maintenance (IEC 62304 Cl 6), anomaly resolution and triage (IEC 62304 Cl 9), change impact analysis via `check_change_impact.py`, AI model drift surveillance under PCCP, and compilation of `DHF-13`.

## 2. Preconditions
- `.agents/skills/samd-maintenance/SKILL.md` exists.
- `templates/DHF-13-Software-Maintenance-and-Problem-Resolution.md` exists.
- `scripts/check_change_impact.py` exists.

## 3. Test Execution Steps
1. Parse `.agents/skills/samd-maintenance/SKILL.md`.
2. Verify problem resolution triage definitions (4-tier severity S1~S4).
3. Verify change impact analysis integration calling `check_change_impact.py`.
4. Verify PCCP continuous AI performance drift monitoring rules.
5. Verify `DHF-13` maintenance reporting and Gate 12 exit criteria.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: All 5 maintenance governance steps are fully defined and verifiable.
- **FAIL**: Missing anomaly triage, omitting change impact analysis, or missing `DHF-13` compilation requirements.
