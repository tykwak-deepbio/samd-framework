# DHF Quality Audit & Regulatory Submission Workflow (Phase 11)

> **Framework Guide**: `WF-05-DHF-AUDIT`  
> **Key Agent**: `dhf-lead-auditor-agent`  
> **Applicable Standards**: ISO 13485:2016 Clause 7.3.7, IEC 62304 Clause 5.1.1 / 9, ISO 14971 Clause 9  

---

## 1. DHF Compilation & Bidirectional Traceability

The Design History File (DHF) contains the complete evidence demonstrating that the SaMD was developed in accordance with the approved Design and Development Plan (DDP) and applicable regulatory standards.

```
       [Forward Traceability: Every Need is Implemented & Tested]
USER-REQ ──► REQ-SW ──► ARCH / DDS ──► Production Code ──► TC-xxx ──► VERIF (PASS)
   ▲           ▲           ▲                 ▲              ▲           ▲
   │           │           │                 │              │           │
   └───────────┴───────────┴─────────────────┴──────────────┴───────────┘
      [Backward Traceability: Every Artifact Justified & Verified]
```

---

## 2. Automated Traceability Audit Execution

1. Run the framework's automated traceability validator:
   ```bash
   python3 scripts/validate_traceability.py dhf/
   ```
2. The validator parses all markdown DHF documents in `dhf/` and checks:
   - Does every `USER-REQ-*` map to at least one `REQ-SW-*`?
   - Does every `REQ-SW-*` map to at least one `ARCH-*` or `DDS-*`?
   - Does every `REQ-SW-*` map to a verified test case (`TC-*`)?
   - Does every `RSK-*` with initial unacceptable risk map to an `RCM-*`, and is that `RCM-*` verified in code and tests?
   - Are there any orphan requirements, unlinked risks, or untested code units?
3. If any broken links exist, the script exits with non-zero status and flags the exact line numbers requiring remediation.

---

## 3. Cryptographic DHF Master Index Generation

1. Run the DHF Index generator:
   ```bash
   python3 scripts/generate_dhf_index.py dhf/
   ```
2. The script:
   - Scans all documents from `DHF-00` through `DHF-11`.
   - Computes SHA-256 cryptographic hashes to guarantee tamper evidence.
   - Extracts document version, effective date, and approval status.
   - Updates `dhf/DHF-11-DHF-Index-and-Quality-Audit-Report.md`.

---

## 4. Final Regulatory Clearance Readiness Sign-Off
1. The `dhf-lead-auditor-agent` reviews the consolidated findings against:
   - Korea MFDS 체외진단의료기기/의료기기 기술문서 심사 기준.
   - US FDA 510(k) Premarket Notification Software Documentation criteria.
   - EU IVDR Technical Documentation Annex II / III checklist.
2. If all standards are met with zero major non-conformities, the Lead Auditor, Head of RA, and CEO sign off on the DHF release.
