# Software Requirement: FR-SKILL-010

> **Requirement ID**: `FR-SKILL-010`  
> **Title**: Skill Specification - `samd-arch-design` (IEC 62304 Architecture & Safety Segregation)  
> **Category**: Antigravity Skills Ecosystem (`[SKILL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006+AMD1:2015 Clause 5.3, ISO 13485:2016 Clause 7.3.4  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-SKILL-010.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-001.md`, `docs/architecture/ARCH-FW-004.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-003.md`, `docs/detailed_design/DDS-FW-007.md`  

---

## 1. Description & Technical Rationale
The `samd-arch-design` skill shall author high-level system and software architectural designs conforming to IEC 62304 Clause 5.3, establishing software architectural items (`ARCH-xxx`), safety segregation barriers between critical and non-critical units, and SOUP evaluations in `DHF-07-Software-Architectural-Design-Specification-SDS.md`.

## 2. Detailed Functional Specifications
1. **Architectural Decomposition**: Decompose the software system into major functional components, assigning each a unique identifier `ARCH-xxx` (e.g., `ARCH-001`).
2. **Safety Segregation (Class B/C)**: Identify safety-critical items (e.g. AI inference engine, clinical calculation) and define physical/logical segregation from non-safety-critical items (e.g. UI widgets, logging).
3. **SOUP Evaluation & Hardware/OS Interfaces**:
   - Explicitly list each SOUP library, intended use, hardware/operating system prerequisites, and failure mode isolation.
4. **Bidirectional Mapping**: Ensure each `ARCH-xxx` links backward to corresponding `REQ-SW-xxx` requirements and forward to detailed design `DDS-xxx`.
5. **Deliverable Generation**: Shall populate `DHF-07-Software-Architectural-Design-Specification-SDS.md`.

## 3. Inputs, Processing & Outputs
- **Inputs**: `DHF-04` (Software Requirements), `DHF-05B` (Hazard Analysis), `DHF-06` (Cybersecurity).
- **Processing**: Component boundary definition, interface protocol design, segregation barrier specification.
- **Outputs**: Populated `DHF-07-Software-Architectural-Design-Specification-SDS.md`.
