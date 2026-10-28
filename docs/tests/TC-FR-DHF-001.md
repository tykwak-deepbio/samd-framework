# Test Protocol: TC-FR-DHF-001

> **Test Case ID**: `TC-FR-DHF-001`  
> **Target Requirement**: `FR-DHF-001` (16 Standard DHF Markdown Document Templates)  
> **Test Level**: Unit / File System Verification  
> **Verification Method**: Automated File Parser (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `templates/` contains all 16 mandatory DHF document templates (`DHF-00` through `DHF-13`), each having valid markdown formatting, top-level `# Title`, and Document Control metadata block.

## 2. Preconditions
- Directory `templates/` is populated.

## 3. Test Execution Steps
1. Execute `scripts/test_framework.py` method `test_ts_dhf_001_templates_structure`.
2. Verify existence of all 16 files:
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
3. Check each file for `**Document ID**:`, `**Revision**:`, and `**Document Status**:`.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: All 14 files exist and satisfy document control metadata requirements.
- **FAIL**: Any template is missing or lacks required metadata fields.
