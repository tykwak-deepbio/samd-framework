# Test Protocol: TC-FR-USE-001

> **Test Case ID**: `TC-FR-USE-001`  
> **Target Requirement**: `FR-USE-001` (Usability Engineering & PCA Use Error Analysis)  
> **Test Level**: Usability & Process Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `FR-USE-001` formalizes usability engineering under IEC 62366-1:2015+AMD1:2020, defining `USE-REQ-xxx` tagging, Perception-Cognition-Action (PCA) use error analysis, and formative/summative evaluation requirements.

## 2. Preconditions
- `docs/srs/FR-USE-001.md` exists.

## 3. Test Execution Steps
1. Parse `docs/srs/FR-USE-001.md`.
2. Check `USE-REQ-xxx` tagging rules and safety-critical task identification.
3. Check PCA use error decomposition and FMEA integration.
4. Check formative and summative usability evaluation requirements (minimum 15 clinical participants).

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: PCA use error model, formative/summative evaluation criteria, and `USE-REQ-xxx` tagging are defined.
- **FAIL**: Missing PCA decomposition or omitting summative usability testing rules.
