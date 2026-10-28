# Risk Management & Cybersecurity Parallel Workflow (Phases 5 & 6)

> **Framework Guide**: `WF-02-RISK-CYBER`  
> **Key Agents**: `risk-management-agent`, `cybersecurity-agent`  
> **Applicable Standards**: ISO 14971:2019, IEC 62304 Clause 7, IEC 81001-5-1, FDA 2023 Premarket Cybersecurity  

---

## 1. Continuous Parallel Track Operation

Risk management and cybersecurity are **not** post-development audit gates. They operate continuously and in parallel with architecture design, detailed design, and code implementation.

```
       [Software Requirements (SRS)] ──────► [Architecture Design (SDS)]
                     │                                      │
                     ▼                                      ▼
+──────────────────────────────────────+  +──────────────────────────────────────+
| Phase 5: ISO 14971 Risk Management   |  | Phase 6: Cybersecurity & SBOM        |
| - Preliminary Hazard Analysis (PHA)  |  | - STRIDE Threat Modeling             |
| - Software FMEA (RSK-xxx)            |  | - Security Controls (SEC-CTL-xxx)    |
| - Risk Control Measures (RCM-xxx)    |  | - SBOM Inventory (CycloneDX/SPDX)    |
| - Residual Risk Evaluation           |  | - CVE Vulnerability Scanning         |
+──────────────────────────────────────+  +──────────────────────────────────────+
                     │                                      │
                     └──────────────────┬───────────────────┘
                                        ▼
                      [Risk Controls Injected into SRS & SDS]
                      [Verified in Independent V&V Testing]
```

---

## 2. Risk Management Execution Steps (ISO 14971)

1. **Risk Management Planning (`DHF-05A-RMP`)**:
   - Establish scoring criteria for Severity (S1~S5) and Probability of Occurrence (P1~P5).
   - Define Risk Acceptability boundaries (Broadly Acceptable, ALARP, Unacceptable).
2. **Hazard Identification & Software FMEA (`DHF-05B-FMEA`)**:
   - Trace each failure mode (`RSK-xxx`):
     * What is the initiating software defect?
     * What hazardous situation occurs in the clinic?
     * What is the resulting clinical harm to the patient?
3. **Formulating Risk Control Measures (`RCM-xxx`)**:
   - Apply ISO 14971 priority order:
     * 1) Inherent design safety (e.g. deterministic memory caps).
     * 2) Protective measures (e.g. confidence thresholds, bounds clamping).
     * 3) Information for safety (e.g. low-confidence alert banners, raw image toggle).
4. **Residual Risk Evaluation & Reporting (`DHF-05C-RMR`)**:
   - Verify every residual risk is acceptable.
   - Formulate Benefit-Risk Analysis proving diagnostic benefits exceed residual risk.

---

## 3. Cybersecurity & SBOM Execution Steps (IEC 81001-5-1 & FDA)

1. **STRIDE Threat Modeling (`DHF-06-CYBER`)**:
   - Analyze trust boundaries across client, server, storage, and AI inference.
   - Identify threats (`SEC-THR-xxx`): Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation of Privilege.
2. **Security Controls Formulation (`SEC-CTL-xxx`)**:
   - TLS 1.3 encryption for network communication.
   - Automated de-identification filter scrubbing 21 HIPAA/DICOM tags.
   - Non-root containerized execution and rate limiting.
3. **Software Bill of Materials (SBOM)**:
   - Enumerate all SOUP components (`SOUP-xxx`), exact versions, origins, licenses, and SHA-256 hashes.
   - Cross-check against the NIST NVD database for active CVEs.
4. **Coordinated Vulnerability Disclosure (CVD)**:
   - Establish contact channels and patch deployment procedures.
