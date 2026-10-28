# Test Protocol: TC-FR-ANOM-002

> **Test Case ID**: `TC-FR-ANOM-002`  
> **Target Requirement**: `FR-ANOM-002` (Software Defect Trend Analysis & Vigilance Reporting)  
> **Test Level**: Quality Management Process Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `FR-ANOM-002` defines IEC 62304 Clause 9.6 defect trend analysis and regulatory adverse event reporting criteria (FDA MDR, MFDS 이상사례).

## 2. Preconditions
- `docs/srs/FR-ANOM-002.md` exists.

## 3. Test Execution Steps
1. Parse `docs/srs/FR-ANOM-002.md`.
2. Verify inclusion of anomaly trend analysis rules (Clause 9.6).
3. Verify statutory vigilance reporting criteria and CAPA integration.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Trend analysis protocols and regulatory reporting rules are defined.
- **FAIL**: Missing IEC 62304 Clause 9.6 reference or vigilance timelines.
