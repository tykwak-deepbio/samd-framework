# Software Requirement: FR-MAINT-001

> **Requirement ID**: `FR-MAINT-001`  
> **Title**: Post-Market Software Maintenance & Emergency Patch Governance  
> **Category**: Software Maintenance (`[MAINT]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006+AMD1:2015 Clause 6 (Software maintenance process), ISO 13485:2016 Clause 7.3.9  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-MAINT-001.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-011.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-011.md`  

---

## 1. Description & Technical Rationale
The framework shall formalize post-market software maintenance under IEC 62304 Clause 6. It shall provide structured procedures for receiving field feedback, analyzing problem reports, conducting change impact analysis, performing regression testing, and releasing hotfixes without compromising DHF integrity.

## 2. Detailed Functional Specifications
1. **Maintenance Plan Formulation (Clause 6.1)**: The framework shall establish maintenance procedures specifying roles, release approvals, and customer notification protocols in `DHF-13-Software-Maintenance-and-Problem-Resolution.md`.
2. **Problem & Modification Analysis (Clause 6.2)**: Every maintenance request must:
   - Identify affected software items and associated hazards.
   - Execute `scripts/check_change_impact.py` to identify invalidated downstream components.
   - Re-evaluate the software safety classification.
3. **Modification Implementation & Regression Testing (Clause 6.3)**:
   - Mandate automated execution of the full regression test suite prior to release.
   - Record maintenance release notes, modified file digests, and user communication packages.

## 3. Inputs, Processing & Outputs
- **Inputs**: Field problem report, anomaly record (`ANOM-xxx`), proposed patch code.
- **Processing**: Change impact traversal, regression test execution, DHF re-baselining.
- **Outputs**: Maintenance release package, updated DHF index, regression verification report.
