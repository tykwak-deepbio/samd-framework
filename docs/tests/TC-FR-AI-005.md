# Test Protocol: TC-FR-AI-005

> **Test Case ID**: `TC-FR-AI-005`  
> **Target Requirement**: `FR-AI-005` (Explainable AI & Saliency Map Verification)  
> **Test Level**: AI Feature Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `FR-AI-005` defines Explainable AI (XAI) feature attribution generation and visual uncertainty warning indicators for low-confidence inferences.

## 2. Preconditions
- `docs/srs/FR-AI-005.md` exists.

## 3. Test Execution Steps
1. Parse `docs/srs/FR-AI-005.md`.
2. Verify inclusion of feature attribution (saliency / heatmaps).
3. Verify uncertainty threshold warning specification ($\tau < 0.70$).

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: XAI heatmap generation and uncertainty warning thresholds are defined.
- **FAIL**: Missing XAI attribution or confidence warning rules.
