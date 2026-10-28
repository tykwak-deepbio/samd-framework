# Test Protocol: TC-FR-AI-006

> **Test Case ID**: `TC-FR-AI-006`  
> **Target Requirement**: `FR-AI-006` (Input Quality Assessment & OOD Rejection)  
> **Test Level**: AI Robustness Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `FR-AI-006` defines pre-inference Input Quality Assessment (IQA) and Out-of-Distribution (OOD) sample detection with fail-safe raw viewing.

## 2. Preconditions
- `docs/srs/FR-AI-006.md` exists.

## 3. Test Execution Steps
1. Parse `docs/srs/FR-AI-006.md`.
2. Verify sharpness/quality assessment criteria.
3. Verify OOD detection and raw fallback bypass mechanism.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: IQA criteria, OOD screening, and raw viewing fallback are defined.
- **FAIL**: Missing IQA metrics or fail-safe bypass specification.
