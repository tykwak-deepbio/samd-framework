# Test Protocol: TC-FR-TOOL-001

> **Test Case ID**: `TC-FR-TOOL-001`  
> **Target Requirement**: `FR-TOOL-001` (Automated Bidirectional Traceability & Orphan Checker)  
> **Test Level**: System / Automated Test Suite  
> **Verification Method**: Execution of Positive & Negative Test Scenarios (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `scripts/validate_traceability.py`:
1. Exits with code `0` and certifies `PASS` when all requirements, hazards, and tests are 100% mapped.
2. Exits with code `1` and identifies the exact orphan ID when an unmapped `USER-REQ-*` is injected.
3. Exits with code `1` and flags a defect when a `REQ-SW-*` lacks a forward test case (`TC-*`).

## 2. Preconditions
- `scripts/validate_traceability.py` is executable.
- Complete reference DHF in `examples/wsi-tissue-viewer-samd/dhf/`.

## 3. Test Execution Steps
1. **Positive Test**: Execute `python3 scripts/validate_traceability.py examples/wsi-tissue-viewer-samd/dhf`.
   - Verify exit code is `0`.
   - Verify output contains `REGULATORY AUDIT VERDICT: PASS`.
2. **Negative Test A (Orphan User Need)**:
   - Copy DHF to a temp folder, inject unmapped `USER-REQ-999` into `DHF-01`.
   - Run validator -> Assert exit code is `1` and error mentions `USER-REQ-999`.
3. **Negative Test B (Untested Requirement)**:
   - In temp folder, remove test case from `REQ-SW-001` in `DHF-10`.
   - Run validator -> Assert exit code is `1` and error flags missing test case.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Positive scenario exits with 0; both negative scenarios exit with 1 and pinpoint specific non-conformities.
- **FAIL**: Script returns 0 on orphaned/untested items or fails on valid DHF.
