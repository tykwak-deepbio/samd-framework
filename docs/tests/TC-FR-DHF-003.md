# Test Protocol: TC-FR-DHF-003

> **Test Case ID**: `TC-FR-DHF-003`  
> **Target Requirement**: `FR-DHF-003` (10 Persistent Traceability Identifier Tag Standard)  
> **Test Level**: Verification / Content Inspection  
> **Verification Method**: Tag Regex Parser & Matrix Linkage Verification  
> **Status**: Approved  

---

## 1. Test Objective
Verify that the framework documents, templates, rules, and validation tools strictly enforce the 10 persistent tag prefixes:
`USER-REQ-`, `CLIN-REQ-`, `REG-REQ-`, `REQ-SW-`, `RSK-`, `RCM-`, `SEC-THR-`, `SEC-CTL-`, `ARCH-`, `DDS-`, `TC-`, `VERIF-`.

## 2. Preconditions
- `AGENTS.md` and `templates/DHF-10-Traceability-Matrix-RTM.md` are present.

## 3. Test Execution Steps
1. Parse `AGENTS.md` and verify the Traceability Tag Standards table enumerates all prefixes.
2. Verify that `templates/DHF-10-Traceability-Matrix-RTM.md` table contains dedicated columns for each tag category.
3. Verify that `scripts/validate_traceability.py` parses each of these prefixes via regex patterns.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: All 10 persistent identifier prefixes are fully supported across rules, templates, and validation scripts.
- **FAIL**: Any tag prefix is omitted or incompatible with automated parsing.
