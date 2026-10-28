# Test Protocol: TC-FR-CYBER-002

> **Test Case ID**: `TC-FR-CYBER-002`  
> **Target Requirement**: `FR-CYBER-002` (Secure Architecture, STRIDE Threat Modeling & SAST/DAST)  
> **Test Level**: Cybersecurity Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `FR-CYBER-002` defines STRIDE threat modeling, static security analysis (SAST), and CVE vulnerability scanning under IEC 81001-5-1.

## 2. Preconditions
- `docs/srs/FR-CYBER-002.md` exists.

## 3. Test Execution Steps
1. Parse `docs/srs/FR-CYBER-002.md`.
2. Verify inclusion of STRIDE threat modeling and boundary definitions.
3. Verify SAST code scanning and continuous CVE tracking requirements.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Threat modeling and automated static/CVE scanning requirements are defined.
- **FAIL**: Missing STRIDE model or SAST verification scope.
