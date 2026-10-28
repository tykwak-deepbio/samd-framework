# Test Protocol: TC-FR-SKILL-004

> **Test Case ID**: `TC-FR-SKILL-004`  
> **Target Requirement**: `FR-SKILL-004` (Skill Specification - `samd-user-needs`)  
> **Test Level**: Unit / Workflow Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `samd-user-needs` defines structured clinical Q&A prompts, enforces `USER-REQ-xxx` identifier generation, and targets `DHF-01-Intended-Use-and-URD.md`.

## 2. Preconditions
- `.agents/skills/samd-user-needs/SKILL.md` exists.
- `templates/DHF-01-Intended-Use-and-URD.md` exists.

## 3. Test Execution Steps
1. Parse `.agents/skills/samd-user-needs/SKILL.md`.
2. Verify clinical inquiry sections: Intended Use, Target Patient Population, User Profile, Operational Environment.
3. Verify mandatory output formatting of requirements into `USER-REQ-xxx` with category tags `[FUNC]`, `[USE]`, `[PERF]`, `[INTF]`.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Skill definition contains clinical discovery categories and enforces `USER-REQ-xxx` generation for `DHF-01`.
- **FAIL**: Missing clinical inquiry sections or non-conforming identifier formats.
