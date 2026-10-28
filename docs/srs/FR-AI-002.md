# Software Requirement: FR-AI-002

> **Requirement ID**: `FR-AI-002`  
> **Title**: Independent Test Set Cryptographic Freeze & Patient-Level Leakage Prevention  
> **Category**: AI/ML Clinical Validation (`[AI]`)  
> **Safety Class**: Class C (IEC 62304)  
> **Parent Standard**: Good Machine Learning Practice (GMLP) Principle 6, FDA AI/ML Premarket Guidance  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-AI-002.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-008.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-008.md`  

---

## 1. Description & Technical Rationale
The framework shall prevent data leakage and clinical over-optimism in AI/ML validation by enforcing patient-level dataset partitioning and cryptographically locking the independent test set prior to model evaluation.

## 2. Detailed Functional Specifications
1. **Patient-Level Partitioning Enforcement**:
   - Guarantee that all slices, patches, tiles, or longitudinal exams from a single patient (Patient ID) are partitioned strictly into either Training, Validation, or Test sets, with 0.00% cross-set leakage.
2. **Cryptographic Test Set Freezing**:
   - Calculate SHA-256 digests for all files in the independent test dataset prior to running validation benchmarks.
   - Record hashes in `DHF-09`. Any discrepancy in test set checksums halts clinical validation execution.
3. **Data Leakage Automated Checker**:
   - Implement an automated scanner verifying zero overlap of Patient IDs across partitioned manifests.

## 3. Inputs, Processing & Outputs
- **Inputs**: Dataset split manifests (`train.csv`, `val.csv`, `test.csv`).
- **Processing**: Patient ID intersection evaluation, test set file hashing.
- **Outputs**: Leakage-free verification certificate, locked test manifest checksum.
