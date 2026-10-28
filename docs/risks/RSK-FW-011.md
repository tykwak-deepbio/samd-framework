# Risk Analysis: RSK-FW-011

> **Risk ID**: `RSK-FW-011`  
> **Risk Control Measure ID**: `RCM-FW-011`  
> **Title**: Non-compliance with 21 CFR Part 11 Electronic Records & Signature Tampering  
> **Standard Reference**: ISO 14971:2019 Clause 5.4, FDA 21 CFR Part 11, ISO 13485:2016 Clause 4.2.5  
> **Target Requirement**: `FR-PART11-001`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-010.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-010.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-PART11-001.md`  

---

## 1. Hazard, Sequence of Events & Hazardous Situation
- **Hazard**: Uncontrolled document modifications without audit trail or forged electronic signatures.
- **Sequence of Events**:
  1. A user or rogue script edits approved DHF markdown documents directly on disk.
  2. The changes are not recorded in a computer-generated audit log, or electronic signatures remain attached to altered text.
- **Hazardous Situation**: Inability to demonstrate design history integrity during FDA or Notified Body regulatory inspections.
- **Harm**: Warning letters, premarket submission rejections, suspension of CE/MFDS clearance. (Severity: S3 - Serious, Probability: P3 - Medium $\to$ **Initial Risk: High / Unacceptable**).

## 2. Risk Control Measure: RCM-FW-011
- **Control Measure Description**: The framework implements **Append-Only Computer-Generated Audit Trail & Cryptographic Signature Binding**.
  - All file changes and gate sign-offs write an immutable record to `audit_trail.log` with SHA-256 before/after hashes.
  - Reviewer electronic signatures are cryptographically bound to the document's SHA-256 digest, rendering any subsequent edits immediately invalid.
- **Control Type**: Inherent Cryptographic Integrity Control.

## 3. Residual Risk Evaluation
- **Residual Severity**: S2.
- **Residual Probability**: P1 (Cryptographic signature verification exposes any unrecorded edit).
- **Residual Risk Level**: **Low / Acceptable (ALARP satisfied)**.
- **Verification Evidence**: `VERIF-FW-035` via `TC-FR-PART11-001.md`.
## 4. Evaluation of New Hazards Arising from Risk Control Measures (ISO 14971:2019 Cl 7.3 & IEC 62304 Cl 7.2.2)
- **Potential New Hazards Introduced**:
  - HMAC key management complexity: compromise, loss, or expiration of signing keys could invalidate legitimate audit logs.
  - Disk space exhaustion from verbose, immutable append-only audit trail logging in high-throughput deployments.
- **Secondary Risk Mitigations**:
  - Secure hardware security module (HSM) or OS keystore integration (`DDS-FW-010`) with automated key rollover and archival.
  - Log rotation with cryptographic chaining: rotated audit segments are sealed with Merkle root hashes, preserving complete non-repudiation.
  - Monotonic system clock verification preventing backdating or forward-dating of electronic records.
- **Residual Risk Conclusion**: No unacceptable secondary hazards introduced. Residual risk remains **Acceptable (ALARP satisfied)**.
