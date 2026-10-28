# Software Requirement: FR-USE-001

> **Requirement ID**: `FR-USE-001`  
> **Title**: Usability Engineering & PCA Use Error Analysis  
> **Category**: Usability Engineering (`[USE]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62366-1:2015+AMD1:2020 (Application of usability engineering to medical devices)  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-USE-001.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-007.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-007.md`  

---

## 1. Description & Technical Rationale
The framework shall formalize usability engineering under IEC 62366-1:2015+AMD1:2020. It shall identify user profiles, operating environments, primary operating functions, evaluate use errors using the Perception-Cognition-Action (PCA) model, and mandate formative and summative usability evaluations.

## 2. Detailed Functional Specifications
1. **Usability Requirements & Critical Tasks**:
   - Tag usability requirements with `USE-REQ-xxx`.
   - Identify safety-critical tasks where user interaction failure could result in patient harm.
2. **PCA Use Error Analysis**:
   - Decompose interactions into **Perception** (e.g. illegible text, unobserved alert), **Cognition** (e.g. misinterpreting diagnostic indicator), and **Action** (e.g. accidental click, wrong button press).
   - Feed identified use errors into `DHF-05B` FMEA matrix.
3. **Formative & Summative Usability Evaluations**:
   - Specify formative evaluation protocols during iterative UI design.
   - Mandate summative evaluation protocols with representative clinical users (minimum 15 participants) in a simulated clinical environment prior to Gate 9 release.

## 3. Inputs, Processing & Outputs
- **Inputs**: User interface mockups, clinical user profiles, intended use.
- **Processing**: PCA cognitive walkthrough, use error hazard mapping, evaluation scoring.
- **Outputs**: Usability Engineering File, summative usability test report (`DHF-09`).
