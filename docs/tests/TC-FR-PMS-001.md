# Test Protocol: TC-FR-PMS-001

> **Test Case ID**: `TC-FR-PMS-001`  
> **Target Requirement**: `FR-PMS-001` (Post-Market Clinical Follow-up & Surveillance)  
> **Test Level**: Post-Market Quality Process Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `FR-PMS-001` defines ISO 14971 Clause 10 post-market surveillance procedures, real-world data collection, and Periodic Safety Update Reports (PSUR).

## 2. Preconditions
- `docs/srs/FR-PMS-001.md` exists.

## 3. Test Execution Steps
1. Parse `docs/srs/FR-PMS-001.md`.
2. Verify reference to ISO 14971 Clause 10 and real-world clinical monitoring.
3. Verify PSUR reporting requirements and risk file feedback loops.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Post-market surveillance plans, PSUR synthesis, and risk updates are defined.
- **FAIL**: Missing ISO 14971 Clause 10 reference or PSUR requirements.
