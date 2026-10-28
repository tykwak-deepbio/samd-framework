# Software Requirement: FR-SKILL-014

> **Requirement ID**: `FR-SKILL-014`  
> **Title**: Skill Specification - `samd-dhf-audit` (Bidirectional RTM & Master DHF Quality Audit)  
> **Category**: Antigravity Skills Ecosystem (`[SKILL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 13485:2016 Clause 4.2.4 & 7.3.7, IEC 62304 Clause 5.1.1  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-SKILL-014.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-001.md`, `docs/architecture/ARCH-FW-004.md`, `docs/architecture/ARCH-FW-006.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-003.md`, `docs/detailed_design/DDS-FW-005.md`  

---

## 1. Description & Technical Rationale
The `samd-dhf-audit` skill shall compile the comprehensive bidirectional Requirements Traceability Matrix (`DHF-10-Traceability-Matrix-RTM.md`), audit DHF documentation integrity, identify orphan or unverified items, generate the cryptographic DHF Index (`DHF-11`), and formulate the final Quality Audit Report.

## 2. Detailed Functional Specifications
1. **Bidirectional RTM Compilation**:
   - Synthesize linkages across User Needs (`USER-REQ-*`) $\leftrightarrow$ SRS (`REQ-SW-*`) $\leftrightarrow$ Hazards/Controls (`RSK-*`/`RCM-*`) $\leftrightarrow$ Architecture/Design (`ARCH-*`/`DDS-*`) $\leftrightarrow$ Implementation Code $\leftrightarrow$ Test Protocols (`TC-*`).
2. **Zero-Orphan Audit Verification**:
   - Execute `scripts/validate_traceability.py` to ensure zero unmapped user needs and zero unverified software requirements.
   - Halt DHF release if any orphan item is detected.
3. **Cryptographic Checksum Indexing**:
   - Execute `scripts/generate_dhf_index.py` to calculate SHA-256 digests for all 14 DHF documents, guaranteeing anti-tampering baseline control.
4. **Final Gate 10 Sign-Off**: Compile `DHF-11-DHF-Index-and-Quality-Audit-Report.md` providing an authoritative clearance recommendation for regulatory submission.

## 3. Inputs, Processing & Outputs
- **Inputs**: Complete set of DHF markdown documents (`DHF-00` through `DHF-09`), test execution logs.
- **Processing**: Traceability matrix parsing, orphan detection, SHA-256 calculation, audit checklist evaluation.
- **Outputs**: Populated `DHF-10-Traceability-Matrix-RTM.md` and `DHF-11-DHF-Index-and-Quality-Audit-Report.md`.
