# Software Requirement: FR-SKILL-006

> **Requirement ID**: `FR-SKILL-006`  
> **Title**: Skill Specification - `samd-regulatory-strategy` (Multi-Jurisdiction Classification & Pathway)  
> **Category**: Antigravity Skills Ecosystem (`[SKILL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IMDRF SaMD N12, FDA 21 CFR 860, MFDS 의료기기법, EU MDR/IVDR Classification Rules  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-SKILL-006.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-001.md`, `docs/architecture/ARCH-FW-007.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-007.md`  

---

## 1. Description & Technical Rationale
The `samd-regulatory-strategy` skill shall determine medical device software classifications, regulatory clearance pathways, harmonized consensus standards, and Predetermined Change Control Plans (PCCP) across major jurisdictions (Korea MFDS, US FDA, EU CE-MDR/IVDR) in `DHF-03-Regulatory-Strategy-and-Clearance-Profile.md`.

## 2. Detailed Functional Specifications
1. **Multi-Jurisdiction Classification Engine**:
   - Korea MFDS: SaMD Class I, II, III, or IV determination based on clinical risk.
   - US FDA: 510(k), De Novo, or PMA pathway identification with Product Code selection.
   - EU IVDR/MDR: Rule-based classification (Class A, B, C, D for IVDR; Class I, IIa, IIb, III for MDR).
2. **Regulatory Requirements Generation**: Every binding statutory or standard obligation shall be codified with a unique identifier prefixed with `REG-REQ-xxx`.
3. **PCCP Strategy Formulation**: If continuous or periodic AI/ML model retraining is anticipated, the skill shall specify FDA PCCP / MFDS 변경허가 면제/신고 전략.
4. **Deliverable Generation**: Shall populate `DHF-03-Regulatory-Strategy-and-Clearance-Profile.md`.

## 3. Inputs, Processing & Outputs
- **Inputs**: Intended use from `DHF-01`, target market jurisdictions, clinical impact severity.
- **Processing**: Statutory rule-based classification evaluation, consensus standard mapping.
- **Outputs**: Fully populated `DHF-03-Regulatory-Strategy-and-Clearance-Profile.md` with structured `REG-REQ-xxx` table.
