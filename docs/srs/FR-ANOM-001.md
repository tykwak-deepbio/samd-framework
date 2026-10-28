# Software Requirement: FR-ANOM-001

> **Requirement ID**: `FR-ANOM-001`  
> **Title**: Software Problem Resolution & Anomaly/CAPA Integration  
> **Category**: Problem Resolution (`[ANOM]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006 Clause 9 (Software problem resolution), ISO 13485:2016 Clause 8.5.2 (Corrective Action)  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-ANOM-001.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-011.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-011.md`  

---

## 1. Description & Technical Rationale
The framework shall formalize software problem resolution under IEC 62304 Clause 9, logging software defects and anomalies under unique `ANOM-xxx` identifiers, classifying severity, conducting root cause analysis, evaluating safety impacts in the FMEA, and enforcing zero unaddressed critical anomalies prior to release.

## 2. Detailed Functional Specifications
1. **Anomaly Triage & Identification**:
   - Assign every reported bug or test failure an identifier prefixed with `ANOM-xxx`.
   - Categorize severity: Catastrophic, Critical, Major, Minor.
2. **Investigation & Root Cause Analysis (Clause 9.2~9.4)**:
   - Identify whether the defect stems from requirement errors, design flaws, coding bugs, or SOUP.
   - Cross-reference with ISO 14971 Risk Management (`DHF-05B`) to evaluate new hazards.
3. **Corrective & Preventive Action (CAPA) Linkage**:
   - Link recurring anomalies to formal QMS CAPA procedures.
4. **Release Gate Threshold**:
   - Zero Catastrophic or Critical anomalies allowed at Gate 10 release.
   - All open Major/Minor anomalies must have formal clinical safety justifications in `DHF-11`.

## 3. Inputs, Processing & Outputs
- **Inputs**: Test failure reports, anomaly tickets, field defect reports.
- **Processing**: Severity categorization, root cause analysis, risk impact assessment.
- **Outputs**: Anomaly report ledger, CAPA linkage record, release clearance status.
