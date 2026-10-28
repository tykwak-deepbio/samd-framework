# Medical Device Software (SaMD) Engineering Rules

This workspace operates under strict Quality Management System (QMS) and Software Lifecycle standards for Medical Devices and Software as a Medical Device (SaMD):
- **ISO 13485:2016** (Quality Management Systems - Requirements for Regulatory Purposes, Clause 7.3 Design and Development)
- **IEC 62304:2006+AMD1:2015** (Medical device software - Software life cycle processes)
- **ISO 14971:2019 / ISO/TR 24971:2020** (Application of risk management to medical devices)
- **IEC 62366-1:2015+AMD1:2020** (Application of usability engineering to medical devices)
- **ISO/IEC 27001:2022 & ISO 27799:2016** (Information security management in health informatics)
- **Medical Device Cybersecurity Guidelines** (FDA 2023 Premarket Cybersecurity, IMDRF N60/N73, MFDS 의료기기 사이버보안 가이드라인)
- **AI/ML SaMD Guidelines** (Good Machine Learning Practice (GMLP), FDA PCCP, MFDS 인공지능 의료기기 허가·심사 가이드라인, EU IVDR/MDR)

All agents working in this project MUST strictly follow these rules to ensure the resulting Design History File (DHF) meets global audit and regulatory clearance standards.

---

## 1. Traceability & Unique Identifier Standard
Every artifact generated in this workspace MUST use structured, persistent, and verifiable identifiers. Never reference requirements, risks, or tests ambiguously.

| Prefix | Domain | Description | Example |
| :--- | :--- | :--- | :--- |
| `USER-REQ-xxx` | User Needs | Clinical and end-user requirements | `USER-REQ-001` |
| `USE-REQ-xxx` | Usability | IEC 62366-1 usability and human factors requirements | `USE-REQ-001` |
| `REG-REQ-xxx` | Regulatory | Regulatory and standard compliance mandates | `REG-REQ-002` |
| `REQ-SW-xxx` | Software Specs | IEC 62304 Software Requirements (Functional, Perf, Security) | `REQ-SW-010` |
| `RSK-xxx` | Risk Hazard | Identified risk / hazardous situation (ISO 14971) | `RSK-005` |
| `RCM-xxx` | Risk Control | Risk Control Measure reducing hazard risk | `RCM-005` |
| `SEC-THR-xxx` | Cybersecurity | STRIDE / Threat Modeling identified threat | `SEC-THR-003` |
| `SEC-CTL-xxx` | Cybersecurity | Cybersecurity mitigation control | `SEC-CTL-003` |
| `ARCH-xxx` | Architecture | High-level system / software architectural component | `ARCH-002` |
| `SOUP-xxx` | Third-Party SW | Software of Unknown Provenance / COTS / OSS library | `SOUP-004` |
| `DDS-xxx` | Detailed Design | Module/Unit detailed software design element | `DDS-008` |
| `CI-xxx` | Config Item | Configuration item, model weights, baseline asset | `CI-001` |
| `ANOM-xxx` | Problem/Bug | Software anomaly, defect, CAPA tracking item | `ANOM-002` |
| `TC-xxx` | Test Case | Test specification (`TC-UNIT-`, `TC-INT-`, `TC-SYS-`, `TC-AI-`) | `TC-SYS-001` |
| `TR-xxx` / `VERIF-xxx` | V&V Record | Objective verification execution evidence | `VERIF-001` |

### Bidirectional Traceability Invariant
1. Every `REQ-SW-xxx` MUST link backward to at least one `USER-REQ-xxx` or `REG-REQ-xxx`.
2. Every safety/security-critical requirement MUST link to `RSK-xxx` / `RCM-xxx` or `SEC-THR-xxx` / `SEC-CTL-xxx`.
3. Every `REQ-SW-xxx` MUST link forward to `ARCH-xxx` or `DDS-xxx`, source code location, and at least one `TC-xxx`.
4. **No Orphan Policy**: No requirement may exist without a verification test; no risk control measure may exist without software implementation verification.

---

## 2. IEC 62304 Software Safety Classification
Before detailed design and implementation, the software safety class (Class A, B, or C) MUST be identified and justified in the Software Development Plan:
- **Class A**: No injury or damage to health is possible.
- **Class B**: Non-SERIOUS INJURY is possible.
- **Class C**: Death or SERIOUS INJURY is possible.
*(Note: Most AI/ML diagnostic or triage SaMD fall under Class B or Class C due to the potential consequences of false negatives or delayed diagnoses).*

For Class B and C:
- Architectural segregation between safety-critical and non-safety-critical units is required.
- Software Detailed Design Specification (DDS) is mandatory.
- Independent software verification testing is mandatory.

---

## 3. Parallel Risk Management & Cybersecurity (ISO 14971 & IEC 81001-5-1)
- **Continuous Evaluation**: Risk management is not a one-time gate at the end. Whenever requirements or architectures change, the Risk Management File (`DHF-05B`) and Threat Model (`DHF-06`) must be updated.
- **ALARP / Acceptability**: All residual risks must be evaluated against the pre-defined Risk Acceptability Matrix. If residual risk is unacceptable, a formal Benefit-Risk Analysis (BRA) is required.
- **Cybersecurity Hygiene**:
  - Never hardcode credentials, tokens, or encryption keys in source code.
  - An updated Software Bill of Materials (SBOM) in CycloneDX or SPDX format is required for all third-party dependencies (`SOUP`).
  - Known CVEs in dependencies must be tracked and mitigated or documented as non-exploitable.
  - Patient Health Information (PHI/PII) must be protected with encryption in transit (TLS 1.3) and at rest (AES-256).

---

## 4. AI/ML SaMD Specific Rules (GMLP & Regulatory Guidelines)
When AI/ML models are used within the SaMD:
1. **Data Leakage & Contamination Prevention**: Strict isolation of Training, Validation, and Independent Test sets must be documented.
2. **Ground Truth Quality**: Inter-reader variability and reference standard annotation protocols must be reported.
3. **Clinical Performance Evaluation**: Report not just overall accuracy, but:
   - Sensitivity (Recall) with 95% Confidence Interval (CI)
   - Specificity with 95% CI
   - Positive/Negative Predictive Value (PPV/NPV) based on target disease prevalence
   - Area Under the ROC Curve (AUROC / AUC)
   - Confusion Matrix across critical clinical sub-categories
4. **Robustness & Edge-Case Testing**: Include explicit test cases for low-quality inputs (e.g. scanner artifacts, over-staining, tissue folds, air bubbles).
5. **Fail-Safe & Transparency**: If the AI model output falls below confidence thresholds, the system must clearly notify the user and provide raw/unprocessed viewing capabilities without silent failure.

---

## 5. DHF Documentation Integrity (ISO 13485 Clause 7.3)
- All DHF documents must reside under `dhf/` (or designated project DHF directory).
- Each DHF file must begin with standard document metadata (Document ID, Title, Version, Effective Date, Author, Reviewer, Approver, Status).
- Document changes must increment version numbers (e.g., 0.1 Draft -> 1.0 Released).
- Run `python3 scripts/validate_traceability.py` before any release to guarantee 100% traceability.
- Run `python3 scripts/generate_dhf_index.py` to maintain an authoritative, checksum-verified DHF Index.
