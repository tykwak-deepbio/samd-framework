# Test Protocol: TC-FR-MAINT-001

> **Test Case ID**: `TC-FR-MAINT-001`  
> **Target Requirement**: `FR-MAINT-001` (Post-Market Software Maintenance & Emergency Patch Governance)  
> **Test Level**: Process & Lifecycle Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `FR-MAINT-001` establishes post-market maintenance workflows under IEC 62304 Clause 6, including problem report analysis, change impact evaluation via `check_change_impact.py`, and regression test execution prior to patch release.

## 2. Preconditions
- `docs/srs/FR-MAINT-001.md` exists and is approved.
- `scripts/check_change_impact.py` is executable.

## 3. Test Execution Steps
1. Parse `docs/srs/FR-MAINT-001.md`.
2. Verify explicit references to IEC 62304 Clause 6.1, 6.2, and 6.3.
3. Verify mandatory integration with `check_change_impact.py` for maintenance releases.
4. Verify requirement for 100% regression test pass before patch deployment.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: All Clause 6 maintenance lifecycle stages, regression test mandates, and change impact traversal directives are defined.
- **FAIL**: Missing maintenance clauses or omitting regression testing rules.
