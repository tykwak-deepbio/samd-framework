# Test Protocol: TC-FR-CM-001

> **Test Case ID**: `TC-FR-CM-001`  
> **Target Requirement**: `FR-CM-001` (Software Configuration Management & Deterministic Build Reproducibility)  
> **Test Level**: Process & Configuration Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `FR-CM-001` specifies configuration item identification (`CI-*`), CCB change control, baseline freezing, and bit-for-bit deterministic build reproducibility under IEC 62304 Clause 8.

## 2. Preconditions
- `docs/srs/FR-CM-001.md` exists.

## 3. Test Execution Steps
1. Parse `docs/srs/FR-CM-001.md`.
2. Verify configuration item scope: source code, AI model weights, prompts, dependency lockfiles.
3. Verify deterministic build reproducibility requirements.
4. Verify baseline freezing rules.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: All Clause 8 configuration management rules and deterministic build criteria are specified.
- **FAIL**: Missing configuration item categories or omitting build reproducibility rules.
