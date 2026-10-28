# Test Protocol: TC-FR-SKILL-007

> **Test Case ID**: `TC-FR-SKILL-007`  
> **Target Requirement**: `FR-SKILL-007` (Skill Specification - `samd-srs`)  
> **Test Level**: Unit / Workflow Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `samd-srs` enforces IEC 62304 Clause 5.2 requirement categories, persistent `REQ-SW-xxx` identifiers, mandatory backward links to `USER-REQ-xxx` / `REG-REQ-xxx`, and output generation for `DHF-04`.

## 2. Preconditions
- `.agents/skills/samd-srs/SKILL.md` exists.
- `templates/DHF-04-Software-Requirements-Specification-SRS.md` exists.

## 3. Test Execution Steps
1. Parse `.agents/skills/samd-srs/SKILL.md`.
2. Verify IEC 62304 Clause 5.2 requirement categories (functional, inputs/outputs, interfaces, alarms, cybersecurity, performance, fail-safe).
3. Verify backward linkage requirement (`REQ-SW-xxx` $\to$ `USER-REQ-*` / `REG-REQ-*`).
4. Verify IEC 62304 software safety classification tagging (Class A, B, C).

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: All Clause 5.2 requirement categories, persistent tagging rules, and backward trace rules are present.
- **FAIL**: Missing requirement categories or omitting backward trace mandates.
