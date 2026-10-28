# Software Requirement: FR-TRANS-001

> **Requirement ID**: `FR-TRANS-001`  
> **Title**: Design Transfer to Production & Device Master Record (DMR) Packaging  
> **Category**: Quality Management & Lifecycle (`[TRANS]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 13485:2016 Clause 7.3.8, FDA 21 CFR 820.30(h) / QMSR, Gate 11  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-TRANS-001.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-010.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-010.md`  

---

## 1. Description & Technical Rationale
The framework shall formalize Design Transfer procedures under ISO 13485 Clause 7.3.8, ensuring that verified software baselines, deployment configurations, build manifests, and operational instructions are systematically packaged into the Device Master Record (DMR) prior to commercial distribution.

## 2. Detailed Functional Specifications
1. **Design Transfer Verification Gate (Gate 11)**:
   - Validate that design outputs (source code, container images, model weights, installation manuals) match approved design specifications.
2. **Device Master Record (DMR) Specification**:
   - Generate reproducible build instructions, pinned dependency manifests, cryptographic checksums, and deployment scripts.
3. **Release Packaging Integrity**:
   - Enforce cryptographic signing of release bundles and verification against the approved DHF master index.

## 3. Inputs, Processing & Outputs
- **Inputs**: Verified software build artifacts, DHF-11 quality audit report, deployment templates.
- **Processing**: Automated package integrity verification, DMR manifest compilation.
- **Outputs**: Certified DMR package and Design Transfer Sign-off in `DHF-00` / `DHF-11`.
