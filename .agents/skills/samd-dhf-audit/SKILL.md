---
name: samd-dhf-audit
description: Compiles the bidirectional Requirements Traceability Matrix (RTM), verifies 100% regulatory coverage, identifies orphan items, audits DHF completeness under ISO 13485, and issues the final Quality Audit Report. Use this skill when conducting regulatory audits, verifying traceability, or authoring DHF-10/11.
---

# SaMD DHF Quality & Regulatory Audit

This skill executes Phase 11 of the SaMD lifecycle, complying with **ISO 13485:2016 Clause 7.3.7 (Design History File - DHF)**, **IEC 62304 Clause 5.1.1 / 5.2 / 5.7 / 9 (Software Traceability and Audit)**, and **ISO 14971 Clause 9 (Risk Management Review)**.

## Goal
Verify 100% bidirectional traceability from User Needs to Test Results, ensure no orphan requirements or unverified risk controls exist, compile the formal Design History File (DHF), and author **`DHF-10-Traceability-Matrix-RTM.md`** and **`DHF-11-DHF-Index-and-Quality-Audit-Report.md`**.

## Audit Protocols & Verification Invariants

```
USER-REQ ◄───► REQ-SW ◄───► RSK / RCM ◄───► ARCH / DDS ◄───► CODE ◄───► TC-xxx ◄───► VERIF
```

### 1. Bidirectional Traceability Invariants
The audit tool and agent strictly evaluate the following:
- **Forward Traceability**:
  - Every `USER-REQ-xxx` maps to at least one `REQ-SW-xxx`.
  - Every `REQ-SW-xxx` maps to at least one `ARCH-xxx` or `DDS-xxx`.
  - Every `REQ-SW-xxx` maps to source code implementation.
  - Every `REQ-SW-xxx` maps to at least one test case (`TC-xxx`).
  - Every `TC-xxx` has recorded execution verification (`VERIF-xxx` with status `PASS`).
- **Backward Traceability**:
  - Every line of code and every `TC-xxx` maps back to an approved `REQ-SW-xxx`.
  - No "gold plating" or undocumented features.
- **Safety & Risk Traceability**:
  - Every `RSK-xxx` classified as unacceptable has at least one `RCM-xxx`.
  - Every `RCM-xxx` is specified in `REQ-SW-xxx`, implemented in code, and verified in `TC-xxx`.

### 2. DHF Document Completeness Checklist
- [ ] DHF-00: Design and Development Plan (DDP) signed and approved
- [ ] DHF-01: Intended Use & User Requirements Document (URD)
- [ ] DHF-02: Clinical Evaluation & SOTA Review
- [ ] DHF-03: Regulatory Strategy & Classification Profile
- [ ] DHF-04: Software Requirements Specification (SRS)
- [ ] DHF-05A/B/C: Risk Management Plan, Hazard Analysis/FMEA, Risk Management Report
- [ ] DHF-06: Cybersecurity Threat Modeling (STRIDE) & SBOM
- [ ] DHF-07: Software Architectural Design Specification (SDS)
- [ ] DHF-08: Software Detailed Design Specification (DDS)
- [ ] DHF-09: Software Verification & Validation (V&V) Report
- [ ] DHF-10: Bidirectional Requirements Traceability Matrix (RTM)
- [ ] DHF-11: DHF Index with cryptographic SHA-256 hashes

## Procedure
1. Execute automated traceability script:
   `python3 scripts/validate_traceability.py dhf/`
2. If any orphan or unlinked items are detected, fail the audit and return actionable corrective actions (CAPA).
3. Execute DHF index generator:
   `python3 scripts/generate_dhf_index.py dhf/`
4. Formulate final audit conclusions, sign off on DHF integrity, and issue `DHF-11`.
