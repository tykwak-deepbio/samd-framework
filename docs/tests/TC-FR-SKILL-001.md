# Test Protocol: TC-FR-SKILL-001

> **Test Case ID**: `TC-FR-SKILL-001`  
> **Target Requirement**: `FR-SKILL-001` (13 Modular Antigravity Skills & YAML Frontmatter Compliance)  
> **Test Level**: Unit / Static Schema Verification  
> **Verification Method**: Automated Regex & YAML Parser (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that all 13 skills under `.agents/skills/` exist, contain valid YAML frontmatter delimiters, have matching directory/skill names conforming to `[a-z0-9\-]+`, and provide substantive descriptions (> 20 characters).

## 2. Preconditions
- Directory `.agents/skills/` contains 13 skill directories.

## 3. Test Execution Steps
1. Execute `scripts/test_framework.py` method `test_ts_skill_001_skills_schema`.
2. Inspect directory list:
   `samd-orchestrator`, `samd-user-needs`, `samd-clinical-sota`, `samd-regulatory-strategy`, `samd-srs`, `samd-risk-mgmt`, `samd-cybersecurity`, `samd-arch-design`, `samd-detailed-design`, `samd-implementation`, `samd-vnv-testing`, `samd-dhf-audit`, `samd-maintenance`.
3. Check `SKILL.md` in each directory:
   - Starts with `---\n`.
   - Contains `name: <folder-name>`.
   - Contains `description:` with length > 20 characters.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: All 13 `SKILL.md` files pass schema parsing without assertion errors.
- **FAIL**: Any skill is missing, has invalid characters in `name`, or has an empty/short description.
