# Software Requirement: FR-DHF-003

> **Requirement ID**: `FR-DHF-003`  
> **Title**: 15 Persistent Traceability Identifier Tag Standard  
> **Category**: Regulatory DHF Documentation (`[DHF]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006 Clause 5.1.1, ISO 13485:2016 Clause 7.3.7  
> **Version**: 1.1.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-DHF-003.md`  

---

## 1. Description & Technical Rationale
To guarantee unambiguous, machine-parsable, and audit-verifiable bidirectional traceability across thousands of requirements, hazards, and tests, the framework shall enforce a strict 15-tag prefix identification standard across all files.

## 2. Detailed Functional Specifications
1. The framework shall mandate the following persistent prefixes:
   - `USER-REQ-xxx`: Clinical and user needs (`DHF-01`)
   - `USE-REQ-xxx`: Usability and human factors engineering requirements (`DHF-01`, `DHF-12`)
   - `CLIN-REQ-xxx`: Literature SOTA clinical baselines (`DHF-02`)
   - `REG-REQ-xxx`: Regulatory mandates (`DHF-03`)
   - `REQ-SW-xxx`: Software requirements (`DHF-04`)
   - `RSK-xxx`: Hazards and hazardous situations (`DHF-05B`)
   - `RCM-xxx`: Risk control measures (`DHF-05B`)
   - `SEC-THR-xxx` / `SEC-CTL-xxx`: STRIDE threats and security controls (`DHF-06`)
   - `SOUP-xxx`: Software of Unknown Provenance / COTS libraries (`DHF-06`, `DHF-07`)
   - `ARCH-xxx`: High-level system & software architectural components (`DHF-07`)
   - `DDS-xxx`: Detailed design units and mathematical specifications (`DHF-08`)
   - `CI-xxx`: Configuration items and baseline assets (`DHF-13`)
   - `ANOM-xxx`: Software anomalies, defects and CAPA references (`DHF-13`)
   - `TC-xxx`: Test protocols (`TC-UNIT-`, `TC-INT-`, `TC-SYS-`, `TC-AI-`, `TC-USE-`, `TC-SEC-`) (`DHF-09`)
   - `TR-xxx` / `VERIF-xxx`: Objective test execution evidence records (`DHF-09`)
2. Traceability tags must never be defined or referenced ambiguously (e.g. referencing "the UI requirement" without tag).

## 3. Inputs, Processing & Outputs
- **Inputs**: Text from DHF documents, source code, and test files.
- **Processing**: Regex pattern extraction (`[A-Z]+-[A-Z]+-\d+`).
- **Outputs**: Set of identified traceability entities for matrix cross-referencing.
