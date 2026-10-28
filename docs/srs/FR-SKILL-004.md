# Software Requirement: FR-SKILL-004

> **Requirement ID**: `FR-SKILL-004`  
> **Title**: Skill Specification - `samd-user-needs` (Clinical Q&A & User Needs Discovery)  
> **Category**: Antigravity Skills Ecosystem (`[SKILL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006 Clause 5.1.1, IEC 62366-1:2015 Clause 4.1, ISO 13485:2016 Clause 7.3.2  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-SKILL-004.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-001.md`, `docs/architecture/ARCH-FW-007.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-007.md`  

---

## 1. Description & Technical Rationale
The `samd-user-needs` skill shall conduct interactive clinical discovery interviews with the user to elicit intended use, clinical indications, target patient populations, clinical user profiles, and operational environments, compiling these into a formal User Requirements Document (`DHF-01-Intended-Use-and-URD.md`).

## 2. Detailed Functional Specifications
1. **Interactive Clinical Interviewing**: The skill shall prompt the user through structured inquiries covering:
   - Clinical Intended Use (e.g., screening, diagnosis, triage, monitoring)
   - Target Patient Population (e.g., adult oncology, demographics, exclusions)
   - Clinical User Profile (e.g., certified pathologists, radiologists, clinicians)
   - Clinical Operating Environment (e.g., PACS integration, hospital workstation, cloud laboratory)
2. **Standardized ID Generation**: Every elicited clinical need shall receive a unique, persistent identifier prefixed with `USER-REQ-xxx` (e.g., `USER-REQ-001`).
3. **Traceability Foundation**: Elicited user needs must categorize requirements into functional (`[FUNC]`), clinical usability (`[USE]`), performance (`[PERF]`), or interface (`[INTF]`) domains.
4. **Deliverable Generation**: Shall populate `DHF-01-Intended-Use-and-URD.md` using the framework template with document control metadata and Korean guidance callouts.

## 3. Inputs, Processing & Outputs
- **Inputs**: User conversational responses, product concept descriptions, clinical domain context.
- **Processing**: Requirement extraction, categorization, ambiguity clarification, unique ID generation.
- **Outputs**: Fully populated `DHF-01-Intended-Use-and-URD.md` with structured `USER-REQ-xxx` table.
