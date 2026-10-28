# Test Protocol: TC-FR-ORCH-003

> **Test Case ID**: `TC-FR-ORCH-003`  
> **Target Requirement**: `FR-ORCH-003` (Continuous Parallel Risk Management & Cybersecurity Sync)  
> **Test Level**: Process / Integration Verification  
> **Verification Method**: Inspection & Automated Dependency Verification  
> **Status**: Approved  

---

## 1. Test Objective
Verify that the framework binds ISO 14971 Risk Management (`DHF-05A/B/C`) and IEC 81001-5-1 Cybersecurity (`DHF-06`) directly to Requirements (`DHF-04`) and Architecture (`DHF-07`), ensuring any requirement or design change triggers parallel risk and security re-evaluations.

## 2. Preconditions
- `workflows/02-risk-and-cybersecurity-parallel-workflow.md` is present.
- `DHF-05B` and `DHF-06` templates define bidirectional links to `REQ-SW-*` and `ARCH-*`.

## 3. Test Execution Steps
1. Inspect `workflows/02-risk-and-cybersecurity-parallel-workflow.md` to verify parallel trigger protocol.
2. Verify that `DHF-05B-Hazard-Analysis-and-FMEA-Matrix.md` contains explicit columns linking every `RSK-*` to `RCM-*` and `REQ-SW-*`.
3. Verify that `DHF-06-Cybersecurity-Threat-Model-and-SBOM.md` contains explicit columns linking every `SEC-THR-*` to `SEC-CTL-*` and `REQ-SW-*`.
4. Verify that `validate_traceability.py` checks that every unacceptable hazard has a verified risk control measure.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Requirements and architecture are cross-linked with risk hazards, RCMs, and cybersecurity controls; traceability tool checks risk control verification status.
- **FAIL**: Risk management or cybersecurity is treated as an isolated end-stage checklist without links to requirements.
