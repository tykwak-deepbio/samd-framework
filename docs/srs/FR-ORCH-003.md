# Software Requirement: FR-ORCH-003

> **Requirement ID**: `FR-ORCH-003`  
> **Title**: Continuous Parallel Risk Management (ISO 14971) & Cybersecurity Sync  
> **Category**: Orchestration & Lifecycle Governance (`[ORCH]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 14971:2019 Clause 4.4, IEC 62304:2006 Clause 7, IEC 81001-5-1:2021  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-ORCH-003.md`  

---

## 1. Description & Clinical/Regulatory Rationale
The framework shall execute risk management and cybersecurity threat analysis in continuous parallel synchronization with system development, rather than as an isolated retrospective audit. Whenever requirements or software architectures are modified, risk and security evaluations must be triggered automatically.

## 2. Detailed Functional Specifications
1. The framework shall link Phase 5 (ISO 14971 Risk Management) and Phase 6 (Cybersecurity) directly to Phase 4 (SRS) and Phase 7 (Architecture).
2. Any new functional requirement (`REQ-SW-*`) or architectural module (`ARCH-*`) shall trigger:
   - Hazard identification & Software FMEA review (`RSK-*`).
   - Risk Control Measure assignment (`RCM-*`).
   - STRIDE cybersecurity threat modeling (`SEC-THR-*`).
   - Third-party library inventory update in the Software Bill of Materials (SBOM) (`SOUP-*`).
3. Gate 6 (Architecture) and Gate 8 (Implementation) clearance shall be blocked if any identified hazard has an unverified or unassigned risk control measure.

## 3. Inputs, Processing & Outputs
- **Inputs**: Updated `DHF-04` (SRS) or `DHF-07` (Architecture).
- **Processing**: Automated synchronization check against `DHF-05B` (FMEA) and `DHF-06` (STRIDE/SBOM).
- **Outputs**: Parallel sync status, pending hazard notification.
