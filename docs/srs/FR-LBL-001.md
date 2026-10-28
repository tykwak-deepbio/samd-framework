# Software Requirement: FR-LBL-001

> **Requirement ID**: `FR-LBL-001`  
> **Title**: SaMD Medical Device Labeling & Instructions for Use (e-IFU) Generation & Verification  
> **Category**: Regulatory Compliance & Usability (`[LBL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 13485:2016 Clause 7.2.3 & 7.3.7, IEC 62366-1:2015 Clause 5.9, 21 CFR Part 801, EU MDR/IVDR Annex I Chapter III, MFDS 의료기기 표시·기재 등에 관한 규정  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-LBL-001.md`  

---

## 1. Description & Regulatory Rationale
Under ISO 13485 Clause 7.3.7, 21 CFR Part 801, EU MDR/IVDR Annex I Chapter III, and MFDS regulations, medical software is not legally qualified for commercial release without verified labeling, electronic Instructions for Use (e-IFU), contraindications, clinical warnings, and user manual documentation. The framework shall provide automated mechanisms and DHF template governance (`DHF-14`) to author, verify, and trace SaMD labeling and clinical claims directly against the Risk Management File (`DHF-05B`) and Usability Engineering File (`DHF-12`).

## 2. Detailed Functional Specifications
1. **Mandatory Labeling Content Governance**:
   - The framework shall generate and maintain a standardized SaMD Labeling & IFU dossier (`templates/DHF-14-Labeling-and-Instructions-for-Use-IFU.md`) containing:
     * Proprietary device name, software version, release date, and Unique Device Identification (UDI / Basic UDI-DI).
     * Intended clinical purpose, target patient population, clinical user profile, and operational environment.
     * Absolute and relative contraindications, limitations of use, and clinical warnings linked directly to `RSK-FW-*` / `RCM-FW-*`.
     * Minimum and recommended computing hardware, OS, GPU/CPU, network bandwidth, display resolution, and browser/runtime prerequisites.
     * Software installation, configuration, verification, cybersecurity hygiene, and troubleshooting instructions.
2. **Clinical Warning & Risk Control Synchronization**:
   - Every risk control measure classified as "Information for safety / Warning in IFU" (ISO 14971:2019 Clause 7.1) in `DHF-05B` must be automatically mapped and verified within `DHF-14`.
3. **e-IFU Accessibility & Electronic Labeling Integrity**:
   - The framework shall verify that software GUI includes an accessible "About / Regulatory Label" dialog displaying the frozen software version, legal manufacturer details, CE mark / regulatory clearance status, and direct link to the approved e-IFU.
4. **Usability & Comprehension Verification**:
   - In accordance with IEC 62366-1 Clause 5.9, the framework shall mandate verification of user comprehension for critical warning labels during summative usability evaluation (`FR-USE-002`).

## 3. Inputs, Processing & Outputs
- **Inputs**: Device Intended Use (`DHF-01`), Risk Management File (`DHF-05B`), Usability Engineering File (`DHF-12`), Software Version Metadata.
- **Processing**: Automated cross-referencing between safety risk warnings and IFU text; consistency audit.
- **Outputs**: Verified `DHF-14-Labeling-and-Instructions-for-Use-IFU.md`, bidirectional mapping to RTM (`DHF-10`).
