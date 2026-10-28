# Test Protocol: TC-FR-SKILL-014

> **Test Case ID**: `TC-FR-SKILL-014`  
> **Target Requirement**: `FR-SKILL-014` (Skill Specification - `samd-dhf-audit`)  
> **Test Level**: System / Regulatory Audit Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `samd-dhf-audit` defines bidirectional RTM compilation (`DHF-10`), orphan defect detection via `validate_traceability.py`, cryptographic SHA-256 indexing via `generate_dhf_index.py`, and final quality audit reporting in `DHF-11`.

## 2. Preconditions
- `.agents/skills/samd-dhf-audit/SKILL.md` exists.
- `templates/DHF-10-Traceability-Matrix-RTM.md` and `DHF-11` exist.
- `scripts/validate_traceability.py` and `scripts/generate_dhf_index.py` exist.

## 3. Test Execution Steps
1. Parse `.agents/skills/samd-dhf-audit/SKILL.md`.
2. Verify full bidirectional traceability coverage requirements (`USER-REQ` $\leftrightarrow$ `REQ-SW` $\leftrightarrow$ `RSK`/`RCM` $\leftrightarrow$ `ARCH`/`DDS` $\leftrightarrow$ `CODE` $\leftrightarrow$ `TC`).
3. Verify zero-orphan enforcement mechanism invoking `validate_traceability.py`.
4. Verify SHA-256 index generation invoking `generate_dhf_index.py`.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Traceability matrix generation, automated validator integration, SHA-256 indexing, and `DHF-11` reporting are defined.
- **FAIL**: Missing validator invocation or omitting zero-orphan criteria.
