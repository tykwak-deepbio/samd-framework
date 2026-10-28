# Test Protocol: TC-FR-RULE-001

> **Test Case ID**: `TC-FR-RULE-001`  
> **Target Requirement**: `FR-RULE-001` (Mandatory Workspace Regulatory Engineering Rules)  
> **Test Level**: System / Static Constraint Verification  
> **Verification Method**: Automated File Size & Rule Token Audit (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `AGENTS.md` exists at repository root, does not exceed Antigravity's 24,000-byte per-file limit, and contains mandatory constraints covering traceability invariants, safety classification, continuous risk management, and cybersecurity hygiene without duplicate token waste.

## 2. Preconditions
- `AGENTS.md` exists at repository root.

## 3. Test Execution Steps
1. Execute `scripts/test_framework.py` method `test_ts_skill_002_agents_rules`.
2. Check file size of `AGENTS.md` ($\le 24,000\text{ bytes}$).
3. Verify presence of all required regulatory keywords and invariant sections:
   - "Traceability & Unique Identifier Standard"
   - "IEC 62304 Software Safety Classification"
   - "Parallel Risk Management & Cybersecurity"
   - "No Orphan Policy"
   - Identifier prefix table (`USER-REQ`, `REQ-SW`, `RSK`, `RCM`, `ARCH`, `TC`, etc.)

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: File size is within 24KB limit and all mandatory regulatory sections and tags are present.
- **FAIL**: File size exceeds 24,000 bytes or any mandatory invariant section is missing.
