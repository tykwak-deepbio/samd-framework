# Test Protocol: TC-FR-TOOL-005

> **Test Case ID**: `TC-FR-TOOL-005`  
> **Target Requirement**: `FR-TOOL-005` (Computerized Software Tool Validation CSV & Framework Tool Qualification)  
> **Test Level**: System / Tool Qualification Verification  
> **Verification Method**: Automated Test Execution & Negative Boundary Testing  
> **Status**: Approved  

---

## 1. Test Objective
Verify that all framework development and verification tools (`scripts/*.py`) undergo formal Computerized System Validation (CSV) satisfying ISO 13485:2016 Cl 7.5.6 and GAMP 5 Category 5.

## 2. Preconditions
- Python 3 standard library environment.
- Test suite `scripts/test_framework.py` and integration suite `tests/integration/test_framework_integration.py`.

## 3. Test Execution Steps
1. Execute full tool qualification suite: `python3 scripts/test_framework.py -v`.
   - Verify all test cases pass with exit code 0.
2. Verify positive and negative boundary validation for core tools:
   - Traceability validator rejects orphan user requirements and untested software requirements.
   - Audit logger detects tampered log entries.
   - Pre-write hook rejects unauthorized writes and corrupted payloads (Fail-Closed).
   - AI dataset validator rejects patient leakage.
   - Grounding verifier rejects prompt injections.
   - Anomaly manager blocks gate clearance on unresolved critical defects.
3. Execute integration suite: `python3 tests/integration/test_framework_integration.py -v`.
   - Verify exit code 0.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: 100% of tool qualification test cases pass with exit code 0; all negative boundary safety interlocks trigger as expected.
- **FAIL**: Any tool test fails or negative boundary condition fails to trigger defensive rejection.
