# Software Requirement: FR-SKILL-008

> **Requirement ID**: `FR-SKILL-008`  
> **Title**: Skill Specification - `samd-risk-mgmt` (ISO 14971 Risk Management & Software FMEA)  
> **Category**: Antigravity Skills Ecosystem (`[SKILL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 14971:2019, IEC 62304:2006 Clause 7, ISO/TR 24971:2020  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-SKILL-008.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-001.md`, `docs/architecture/ARCH-FW-004.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-003.md`, `docs/detailed_design/DDS-FW-007.md`  

---

## 1. Description & Technical Rationale
The `samd-risk-mgmt` skill shall execute parallel medical device risk management under ISO 14971:2019 across the software lifecycle, performing preliminary hazard analysis, software failure mode and effects analysis (FMEA), defining risk control measures (`RCM-xxx`), and compiling `DHF-05A`, `DHF-05B`, and `DHF-05C`.

## 2. Detailed Functional Specifications
1. **Risk Management Documentation Suite**:
   - `DHF-05A`: Risk Management Plan (RMP), acceptability matrix, severity/probability scoring scales.
   - `DHF-05B`: Hazard Analysis & Software FMEA Matrix linking Hazard (`RSK-xxx`) $\to$ Cause $\to$ Hazardous Situation $\to$ Harm $\to$ Initial Risk $\to$ Risk Control Measure (`RCM-xxx`) $\to$ Residual Risk.
   - `DHF-05C`: Risk Management Report (RMR) with overall residual risk evaluation and Benefit-Risk Analysis (BRA).
2. **IEC 62304 Clause 7 Software Risk Integration**:
   - Analysis of software contributing causes to hazards.
   - Traceability of risk control measures (`RCM-xxx`) into software requirements (`REQ-SW-xxx`).
   - Re-evaluation of software safety classification post-mitigation.
3. **ALARP & Benefit-Risk Analysis (BRA) Enforcement (ISO 14971:2019 Clause 7.4)**:
   - All residual risks falling in the ALARP or Unacceptable region (e.g. AI diagnostic false negative rates) must trigger a formal clinical Benefit-Risk Analysis (BRA) in `DHF-05C`.
   - The BRA shall quantitatively demonstrate that the clinical diagnostic benefit (e.g. early detection of occult disease, reduction of diagnostic turnaround time by >= 30%) outweighs the residual clinical risk when mitigated by IFU warnings (`DHF-14`) and pathologist confirmation.
   - If residual risk cannot be justified by clinical benefit, the software item shall be rejected at Gate 5.

## 3. Inputs, Processing & Outputs
- **Inputs**: `DHF-01` (Intended Use), `DHF-04` (Software Requirements), architectural components.
- **Processing**: Hazard identification, FMEA scoring, risk control measure derivation, residual risk calculation.
- **Outputs**: Populated `DHF-05A-Risk-Management-Plan-RMP.md`, `DHF-05B-Hazard-Analysis-and-FMEA-Matrix.md`, and `DHF-05C-Risk-Management-Report-RMR.md`.
