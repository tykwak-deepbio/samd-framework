# Risk Analysis: RSK-FW-014

> **Risk ID**: `RSK-FW-014`  
> **Risk Control Measure ID**: `RCM-FW-014`  
> **Title**: Configuration Baseline Drift & Unresolved Software Anomaly Release  
> **Standard Reference**: ISO 14971:2019 Clause 5.4, IEC 62304:2006 Clauses 8 & 9, ISO 13485:2016 Clause 7.3.9  
> **Target Requirement**: `FR-CM-001`, `FR-ANOM-001`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-011.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-011.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-CM-001.md`, `docs/tests/TC-FR-ANOM-001.md`  

---

## 1. Hazard, Sequence of Events & Hazardous Situation
- **Hazard**: Uncontrolled software configuration item drift or premature clinical release with unresolved critical anomalies.
- **Sequence of Events**:
  1. Build artifacts, AI model weights, or system prompts are modified without configuration baseline locking (`CI-xxx`).
  2. Software anomalies (`ANOM-xxx`) discovered during testing are misclassified as Minor without proper Root Cause Analysis (RCA).
  3. The software is released into clinical use containing latent algorithmic or memory corruption defects.
- **Hazardous Situation**: Clinical software operates with unverified build binaries or known safety defects in production.
- **Harm**: Diagnostic system crash mid-surgery/biopsy review, silent computational errors causing false diagnostic reports. (Severity: S4 - Critical, Probability: P3 - Medium $\to$ **Initial Risk: High / Unacceptable**).

## 2. Risk Control Measure: RCM-FW-014
- **Control Measure Description**: The framework enforces **Deterministic Configuration Baseline Locking & Zero Critical Anomaly Gate Interlock**.
  - All configuration items (`CI-xxx`) including model weights, prompts, and Docker digest must be cryptographically locked with SHA-256 hashes.
  - Implements a 4-tier anomaly severity classification (Catastrophic, Critical, Major, Minor).
  - Gate 10 (Release) enforces an absolute block: zero unresolved Catastrophic or Critical anomalies allowed, and all Major anomalies require formal CCB (Change Control Board) clinical risk sign-off.
- **Control Type**: Inherent Software Design & Gate Review Interlock.

## 3. Residual Risk Evaluation
- **Residual Severity**: S3.
- **Residual Probability**: P1 (Prevented by automated build hash verification and Gate 10 zero-defect check).
- **Residual Risk Level**: **Low / Acceptable (ALARP satisfied)**.
- **Verification Evidence**: `VERIF-FW-030`, `VERIF-FW-031` via `TC-FR-CM-001.md`, `TC-FR-ANOM-001.md`.
## 4. Evaluation of New Hazards Arising from Risk Control Measures (ISO 14971:2019 Cl 7.3 & IEC 62304 Cl 7.2.2)
- **Potential New Hazards Introduced**:
  - Strict release block on unresolved anomalies incentivizing improper downgrading of bug severity to bypass release gates.
  - Anomaly tracking administrative overhead delaying urgent bug fix delivery.
- **Secondary Risk Mitigations**:
  - Independent Quality Assurance (QA) review and approval required for any anomaly classification or severity modification (`DDS-FW-011`).
  - Automated anomaly classification audit trail logging all changes to defect severity with mandatory rationale.
  - Dual-sign-off requirement (Lead Developer + Quality Auditor) for Gate 10 clearance.
- **Residual Risk Conclusion**: No unacceptable secondary hazards introduced. Residual risk remains **Acceptable (ALARP satisfied)**.
