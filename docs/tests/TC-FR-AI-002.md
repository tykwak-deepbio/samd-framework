# Test Protocol: TC-FR-AI-002

> **Test Case ID**: `TC-FR-AI-002`  
> **Target Requirement**: `FR-AI-002` (Independent Test Set Cryptographic Freeze & Patient-Level Leakage Prevention)  
> **Test Level**: AI Validation Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `FR-AI-002` specifies patient-level dataset partitioning with 0.00% leakage, cryptographic SHA-256 test set freezing, and automated leakage detection scanners.

## 2. Preconditions
- `docs/srs/FR-AI-002.md` exists.

## 3. Test Execution Steps
1. Parse `docs/srs/FR-AI-002.md`.
2. Check patient-level partitioning mandates (all slices/exams of same Patient ID kept in same partition).
3. Check SHA-256 cryptographic locking requirements for test sets.
4. Verify data leakage scanner requirements.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Patient-level partitioning, cryptographic test set locking, and leakage scanner rules are specified.
- **FAIL**: Missing patient-level partitioning mandates or omitting test set hash locking.
