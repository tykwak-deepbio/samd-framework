# SaMD Post-Market Maintenance & Problem Resolution Workflow (Phase 12)

> **Framework Guide**: `WF-06-POSTMARKET`  
> **Key Agent**: `postmarket-maintenance-agent`  
> **Key Skill**: `samd-maintenance`  
> **Applicable Standards**: IEC 62304:2006+AMD1:2015 Clause 6 & 9, ISO 14971:2019 Clause 10, ISO 13485:2016 Clause 8.2/8.5, FDA PCCP  

---

## 1. Post-Market Surveillance & Problem Ingestion Flow

Following commercial deployment, software issues, customer complaints, third-party vulnerability notifications (CVEs), and clinical feedback must be governed under strict regulatory processes:

```
[Incoming Signal]
  - Customer Complaint
  - Bug Report / Crash Dump ──► [Anomaly Record: ANOM-xxx] ──► [Severity & Safety Triage]
  - Security Vulnerability (CVE)                                      │
  - AI Model Metric Drift                                             ▼
                                                      [Safety Critical / Unacceptable Risk?]
                                                       ├── YES: Trigger Vigilance & Emergency Patch
                                                       └── NO : Route to Scheduled Maintenance
```

---

## 2. IEC 62304 Clause 9 Problem Resolution Execution

1. **Problem Logging (`ANOM-xxx`)**:
   - Assign unique identifier (e.g., `ANOM-2026-001`).
   - Record operating conditions, inputs, stack trace, and software version.
2. **Investigation & Root-Cause Analysis**:
   - Determine whether the anomaly is algorithmic, architectural, data-dependent, or environment-specific.
   - Assess patient risk: does this failure induce false negatives, false positives, or delayed diagnosis?
3. **Trend Analysis (IEC 62304 Clause 9.6)**:
   - Run quarterly trend analyses across all logged anomalies.
   - Flag systemic patterns to the Quality Management team for CAPA initiation.
4. **Adverse Event Reporting**:
   - If an anomaly caused or contributed to a serious adverse event, report to authorities (FDA MDR 21 CFR 803, MFDS 의료기기 부작용 보고) within mandatory statutory timeframes (5, 10, or 30 days).

---

## 3. IEC 62304 Clause 6 Maintenance & Change Impact Analysis

When a software change or patch is developed:
1. **Change Impact Analysis (CIA)**:
   ```bash
   python3 scripts/check_change_impact.py dhf/
   ```
   - Automatically computes affected downstream artifacts.
   - For example, if `DHF-04` (SRS) or `src/` is touched, all downstream verification protocols and risk files are flagged as invalidated.
2. **Regression Verification**:
   - Execute all targeted unit and integration tests.
   - Execute the entire automated test suite:
     ```bash
     python3 scripts/test_framework.py -v
     ```
3. **Traceability Re-Validation**:
   - Verify that the patch does not introduce orphan requirements or unverified risk controls:
     ```bash
     python3 scripts/validate_traceability.py dhf/
     ```

---

## 4. AI/ML Drift Monitoring & PCCP Compliance

For AI-enabled SaMD:
1. **Continuous Clinical Metric Tracking**:
   - Monitor live inference telemetry for distribution shifts (e.g., stain intensity, scanner make/model distribution changes).
   - Evaluate model confidence histograms against baseline validation distributions.
2. **Predetermined Change Control Plan (PCCP)**:
   - If model retraining is required, ensure updates remain strictly within pre-approved PCCP bounds.
   - If retraining exceeds PCCP bounds, treat as a Major Revision requiring new regulatory clearance.

---

## 5. Gate 12 Review & Exit Checklist

To certify Gate 12 (Maintenance & Patch Release):
- [ ] All reported anomalies resolved or formally accepted as non-safety defects with clinical justification.
- [ ] Root causes documented in `dhf/DHF-13-Software-Maintenance-and-Problem-Resolution.md`.
- [ ] Residual risk re-evaluated and recorded in `dhf/DHF-05C-Risk-Management-Report-RMR.md`.
- [ ] Regression testing achieved 100% pass rate with zero orphan requirements.
- [ ] Formal sign-off recorded in `dhf/project_state.json` and HMAC audit trail appended:
  ```bash
  python3 scripts/record_audit_event.py --record --action "GATE_12_APPROVAL" --reviewer "QA_LEAD" --details "Maintenance release 1.0.1 certified"
  ```
