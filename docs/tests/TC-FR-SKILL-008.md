# Test Protocol: TC-FR-SKILL-008

> **Test Case ID**: `TC-FR-SKILL-008`  
> **Target Requirement**: `FR-SKILL-008` (Skill Specification - `samd-risk-mgmt`)  
> **Test Level**: Unit / Workflow Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `samd-risk-mgmt` implements ISO 14971 parallel risk management across RMP (`DHF-05A`), Hazard Analysis/Software FMEA (`DHF-05B`), and RMR (`DHF-05C`), generating structured `RSK-xxx` and `RCM-xxx` identifiers.

## 2. Preconditions
- `.agents/skills/samd-risk-mgmt/SKILL.md` exists.
- `templates/DHF-05A-Risk-Management-Plan-RMP.md`, `DHF-05B`, and `DHF-05C` exist.

## 3. Test Execution Steps
1. Parse `.agents/skills/samd-risk-mgmt/SKILL.md`.
2. Verify hazard analysis fields: Hazard (`RSK-xxx`), Cause, Hazardous Situation, Harm, Initial P/S, Control Measure (`RCM-xxx`), Residual P/S.
3. Verify IEC 62304 Clause 7 software hazard analysis integration.
4. Verify ALARP evaluation and Benefit-Risk Analysis triggering criteria.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: ISO 14971 workflow, 3-part DHF suite (`DHF-05A/B/C`), and `RSK-*`/`RCM-*` tagging are defined.
- **FAIL**: Missing FMEA columns, missing ALARP rules, or missing RMR generation.
