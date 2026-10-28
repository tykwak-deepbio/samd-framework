# Test Protocol: TC-FR-SKILL-006

> **Test Case ID**: `TC-FR-SKILL-006`  
> **Target Requirement**: `FR-SKILL-006` (Skill Specification - `samd-regulatory-strategy`)  
> **Test Level**: Unit / Workflow Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `samd-regulatory-strategy` defines multi-jurisdiction SaMD classification logic (MFDS, FDA, EU IVDR/MDR), consensus standards mapping, `REG-REQ-xxx` generation, and PCCP planning in `DHF-03`.

## 2. Preconditions
- `.agents/skills/samd-regulatory-strategy/SKILL.md` exists.
- `templates/DHF-03-Regulatory-Strategy-and-Clearance-Profile.md` exists.

## 3. Test Execution Steps
1. Parse `.agents/skills/samd-regulatory-strategy/SKILL.md`.
2. Check jurisdiction rules: MFDS Class I-IV, FDA 510(k)/De Novo/PMA, EU IVDR Class A-D / MDR Class I-III.
3. Check `REG-REQ-xxx` identifier tagging requirement.
4. Verify PCCP (Predetermined Change Control Plan) strategy instructions.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: All 3 jurisdictions, `REG-REQ-xxx` tag rules, and PCCP strategies are articulated.
- **FAIL**: Missing jurisdiction criteria or omitting `REG-REQ-xxx` specification.
