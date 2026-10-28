# Test Protocol: TC-FR-SKILL-002

> **Test Case ID**: `TC-FR-SKILL-002`  
> **Target Requirement**: `FR-SKILL-002` (Slash Command Integration & 3rd-Person Semantic Triggering)  
> **Test Level**: Verification / Inspection  
> **Verification Method**: Text Analysis & Semantic Phrasing Audit  
> **Status**: Approved  

---

## 1. Test Objective
Verify that all 12 skill descriptions are written in objective 3rd-person phrasing (e.g. "Authors...", "Executes...", "Guides...") and clearly state both what the skill does and when the agent should activate it, enabling seamless slash command triggering and semantic matching.

## 2. Preconditions
- All 12 `.agents/skills/*/SKILL.md` files are accessible.

## 3. Test Execution Steps
1. Read the `description` field of all 12 skills.
2. Check that none start with 1st-person pronouns ("I will...", "We provide...").
3. Check that each description includes triggering guidance (e.g., "Use this skill when...").
4. Verify that each skill name is valid for slash command invocation (e.g. `/samd-orchestrator`, `/samd-srs`).

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: 100% of skills use 3rd-person phrasing with explicit "Use this skill when..." guidance.
- **FAIL**: Any skill uses ambiguous conversational tone or lacks triggering context.
