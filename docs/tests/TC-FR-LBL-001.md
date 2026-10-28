# Test Protocol: TC-FR-LBL-001

> **Test Case ID**: `TC-FR-LBL-001`  
> **Target Requirement**: `FR-LBL-001` (SaMD Medical Device Labeling & Instructions for Use e-IFU Generation & Verification)  
> **Test Level**: Regulatory / System Specification Verification  
> **Verification Method**: Inspection & Traceability Cross-Audit  
> **Status**: Approved  

---

## 1. Test Objective
Verify that the framework provides comprehensive governance and validation for SaMD labeling and e-IFU authoring in compliance with ISO 13485:2016 Cl 7.3.7, 21 CFR Part 801, EU MDR/IVDR Annex I Chapter III, and IEC 62366-1 Cl 5.9.

## 2. Preconditions
- `templates/DHF-14-Labeling-and-Instructions-for-Use-IFU.md` exists and is populated.
- Risk Management File (`DHF-05B` / `FRAMEWORK_SW_FMEA.md`) is available.

## 3. Test Execution Steps
1. Inspect `templates/DHF-14-Labeling-and-Instructions-for-Use-IFU.md` for mandatory regulatory sections:
   - Device Identification, Software Version, UDI specification.
   - Intended Use, Indications for Use, Target Population.
   - Contraindications, Warnings, and Precautions.
   - Minimum Hardware/Software Computing Environment.
2. Cross-reference warnings in `DHF-14` against risk control measures (`RCM-*`) in `DHF-05B` designating "Information for Safety / User Manual".
3. Verify that 100% of information-for-safety risk controls appear in the Labeling/IFU document without omissions.
4. Verify that GUI "About / Regulatory Label" dialog specifications match the approved labeling version.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: `DHF-14` contains all statutory labeling sections and achieves 100% coverage of information-for-safety risk controls from the Risk Management File.
- **FAIL**: Any statutory section is missing, or risk control warnings in `DHF-05B` are omitted from `DHF-14`.
