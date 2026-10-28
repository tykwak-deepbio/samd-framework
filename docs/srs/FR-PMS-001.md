# Software Requirement: FR-PMS-001

> **Requirement ID**: `FR-PMS-001`  
> **Title**: Post-Market Clinical Follow-up (PMCF) & Periodic Safety Update Reporting (PSUR)  
> **Category**: Post-Market Surveillance (`[PMS]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 14971:2019 Clause 10, EU IVDR/MDR Annex XIII / XIV, FDA Postmarket Guidance  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-PMS-001.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-011.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-011.md`  

---

## 1. Description & Technical Rationale
The framework shall establish a continuous Post-Market Surveillance (PMS) framework that actively gathers real-world clinical performance data, evaluates ongoing benefit-risk acceptability, and authors Periodic Safety Update Reports (PSUR) throughout the device lifecycle.

## 2. Detailed Functional Specifications
1. **Post-Market Surveillance Plan**:
   - Define active and passive data collection methods from clinical deployments, registries, and scientific publications.
2. **Risk Management File Feedback Loop**:
   - Feed post-production safety data back into `DHF-05C` to confirm initial risk estimates remain valid.
3. **Periodic Safety Update Report (PSUR)**:
   - Produce regular synthesis reports summarizing clinical outcomes, maintenance updates, and benefit-risk balance.

## 3. Inputs, Processing & Outputs
- **Inputs**: Real-world clinical performance logs, complaint records, literature surveillance.
- **Processing**: Benefit-risk recalculation, statistical incident rate comparison.
- **Outputs**: PMS / PMCF Evaluation Report and Updated Risk File in `DHF-05C` / `DHF-13`.
