# Software Requirement: FR-USE-002

> **Requirement ID**: `FR-USE-002`  
> **Title**: Summative Usability Evaluation & Use Error Risk Protocol  
> **Category**: Usability Engineering (`[USE]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62366-1:2015+AMD1:2020 Clause 5.8, FDA Usability Guidance  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-USE-002.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-007.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-007.md`  

---

## 1. Description & Technical Rationale
The framework shall implement summative usability testing protocols under IEC 62366-1 Clause 5.8 to systematically evaluate human-device interfaces in simulated clinical environments, validating that critical tasks can be performed without dangerous use errors.

## 2. Detailed Functional Specifications
1. **Critical Task Identification**:
   - Define all safety-critical user interactions (e.g., zoom/pan navigation, AI toggle, measurement tools, report generation).
2. **Summative Evaluation Protocol**:
   - Specify representative clinical user groups (pathologists, lab technicians) and realistic testing scenarios.
3. **Use Error Risk Analysis (URRA)**:
   - Record and analyze close calls, use difficulties, and errors, ensuring all residual usability risks are acceptable.

## 3. Inputs, Processing & Outputs
- **Inputs**: User interface designs, User Requirements Document (`DHF-01`), clinical test scenarios.
- **Processing**: Simulated usability session execution, error observation and scoring.
- **Outputs**: Summative Usability Evaluation Report in `DHF-12`.
