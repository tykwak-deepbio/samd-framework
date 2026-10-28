# Test Protocol: TC-FR-AI-003

> **Test Case ID**: `TC-FR-AI-003`  
> **Target Requirement**: `FR-AI-003` (Subgroup Bias Auditing & Multi-Center Generalization Robustness)  
> **Test Level**: AI Validation Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `FR-AI-003` specifies demographic subgroup stratification, subgroup performance deviation limits ($\le 5\%$), multi-center testing (minimum 2 external sites), and multi-vendor hardware robustness evaluations.

## 2. Preconditions
- `docs/srs/FR-AI-003.md` exists.

## 3. Test Execution Steps
1. Parse `docs/srs/FR-AI-003.md`.
2. Check subgroup stratification categories: age, biological sex, disease severity.
3. Check performance deviation margin constraint ($\le 5\%$).
4. Check multi-center and multi-vendor hardware validation criteria.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Subgroup stratification rules, deviation margins, and multi-center criteria are defined.
- **FAIL**: Missing subgroup bias thresholds or omitting multi-center validation requirements.
