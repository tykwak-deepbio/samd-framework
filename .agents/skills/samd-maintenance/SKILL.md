---
name: samd-maintenance
description: Governs post-market software maintenance, anomaly resolution, CAPA, change impact analysis, and continuous AI model monitoring under IEC 62304 Clause 6/9 and ISO 14971 Clause 10. Use this skill when investigating post-market issues, planning software patches, or authoring DHF-13.
---

# SaMD Software Maintenance & Problem Resolution

This skill executes Phase 12 of the SaMD lifecycle, complying with **IEC 62304:2006+AMD1:2015 Clause 6 (Software Maintenance Process)**, **Clause 9 (Software Problem Resolution Process)**, **ISO 14971:2019 Clause 10 (Production and Post-Production Information)**, and **ISO 13485:2016 Clause 8.2 / 8.5 (CAPA)**.

## Goal
Establish and maintain the software problem resolution pipeline, analyze user feedback and anomaly reports (`ANOM-xxx`), evaluate safety impact, execute change impact analysis, ensure regression testing, and maintain **`DHF-13-Software-Maintenance-and-Problem-Resolution.md`**.

## Key Workflows & Invariants

```
Feedback / Bug / CVE ──► ANOM-xxx Record ──► Safety & Root Cause Analysis ──► Change Impact Analysis (CIA)
                                                                                     │
DHF-05C Risk Update ◄── Regulatory Vigilance / CAPA ◄── Regression V&V Test ◄────────┘
```

### 1. Problem Resolution Process (IEC 62304 Clause 9)
1. **Anomaly Registration**: Log all anomalies with a unique identifier (`ANOM-xxx`).
2. **Investigation & Triage**:
   - Assess safety criticality (Death/Serious injury, Minor injury, Cosmetic/Non-safety).
   - Determine if the anomaly is a symptom of an unknown hazard or an invalid risk control measure.
3. **Trend Analysis (Clause 9.6)**:
   - Identify repeat occurrences, cluster analysis, and potential systemic architecture defects.
4. **Vigilance & Adverse Event Reporting**:
   - Evaluate against FDA Medical Device Reporting (21 CFR Part 803) and MFDS 의료기기 부작용 보고 기준.

### 2. Software Maintenance & Change Control (IEC 62304 Clause 6)
1. **Change Impact Analysis (CIA)**:
   - Run `python3 scripts/check_change_impact.py dhf/` to identify invalidated upstream and downstream artifacts.
2. **Design Modification**:
   - Update `REQ-SW-xxx`, `ARCH-xxx`, or `DDS-xxx` as necessary.
3. **Verification & Regression**:
   - Execute all targeted unit and integration tests.
   - Run full regression test suite (`scripts/test_framework.py`).
4. **Audit Trail Recording**:
   - Record maintenance release sign-off in `dhf/project_state.json` and append cryptographic HMAC record via `python3 scripts/record_audit_event.py`.

### 3. Deliverables
- `dhf/DHF-13-Software-Maintenance-and-Problem-Resolution.md`
- Updates to `dhf/DHF-05C-Risk-Management-Report-RMR.md`
