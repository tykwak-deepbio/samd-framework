# Software Requirement: FR-DHF-001

> **Requirement ID**: `FR-DHF-001`  
> **Title**: 16 Standard DHF Markdown Document Templates (DHF-00 to DHF-13)  
> **Category**: Regulatory DHF Documentation (`[DHF]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 13485:2016 Clause 7.3.7, IEC 62304:2006 Clause 5  
> **Version**: 1.1.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-DHF-001.md`  

---

## 1. Description & Regulatory Rationale
The framework shall provide 16 complete, standard markdown document templates representing the full Design History File (DHF) required by global medical device regulatory authorities (Korea MFDS, US FDA, EU Notified Bodies).

## 2. Detailed Functional Specifications
1. The framework shall include 16 standardized templates in `templates/`:
   - `DHF-00-Design-and-Development-Plan-DDP.md`
   - `DHF-01-Intended-Use-and-URD.md`
   - `DHF-02-Clinical-Literature-and-SOTA.md`
   - `DHF-03-Regulatory-Strategy-and-Clearance-Profile.md`
   - `DHF-04-Software-Requirements-Specification-SRS.md`
   - `DHF-05A-Risk-Management-Plan-RMP.md`
   - `DHF-05B-Hazard-Analysis-and-FMEA-Matrix.md`
   - `DHF-05C-Risk-Management-Report-RMR.md`
   - `DHF-06-Cybersecurity-Threat-Model-and-SBOM.md`
   - `DHF-07-Software-Architectural-Design-Specification-SDS.md`
   - `DHF-08-Software-Detailed-Design-Specification-DDS.md`
   - `DHF-09-Software-Verification-and-Validation-Report.md`
   - `DHF-10-Traceability-Matrix-RTM.md`
   - `DHF-11-DHF-Index-and-Quality-Audit-Report.md`
   - `DHF-12-Usability-Engineering-File-UEF.md`
   - `DHF-13-Software-Maintenance-and-Problem-Resolution.md`
2. Every template shall start with a top-level `# Title`, followed by a standard Document Control Metadata block (`Document ID`, `Applicable Standards`, `Revision`, `Effective Date`, `Status`).

## 3. Inputs, Processing & Outputs
- **Inputs**: Template file paths.
- **Processing**: Header existence and document control metadata verification.
- **Outputs**: Validated DHF template ready for project instantiation.
