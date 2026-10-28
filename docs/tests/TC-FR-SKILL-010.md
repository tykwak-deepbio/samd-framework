# Test Protocol: TC-FR-SKILL-010

> **Test Case ID**: `TC-FR-SKILL-010`  
> **Target Requirement**: `FR-SKILL-010` (Skill Specification - `samd-arch-design`)  
> **Test Level**: Unit / Workflow Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `samd-arch-design` defines architectural decomposition into `ARCH-xxx` components, enforces safety segregation between critical and non-critical modules under IEC 62304 Clause 5.3, and evaluates SOUP in `DHF-07`.

## 2. Preconditions
- `.agents/skills/samd-arch-design/SKILL.md` exists.
- `templates/DHF-07-Software-Architectural-Design-Specification-SDS.md` exists.

## 3. Test Execution Steps
1. Parse `.agents/skills/samd-arch-design/SKILL.md`.
2. Verify architectural decomposition rules and `ARCH-xxx` unique identification.
3. Verify safety segregation rules isolating safety-critical software units (Class B/C).
4. Verify SOUP prerequisites, operating system interfaces, and `DHF-07` compilation.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Architectural decomposition, safety segregation, SOUP evaluation, and `ARCH-xxx` tagging are fully specified.
- **FAIL**: Missing safety segregation mandates or omitting `ARCH-xxx` identification.
