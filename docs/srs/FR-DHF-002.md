# Software Requirement: FR-DHF-002

> **Requirement ID**: `FR-DHF-002`  
> **Title**: Global English Submission Format with Korean Guidance & Checklists  
> **Category**: Regulatory DHF Documentation (`[DHF]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 13485:2016 Clause 7.3.7, MFDS/FDA/IVDR Submissions  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-DHF-002.md`  

---

## 1. Description & Technical Rationale
To support both global premarket submissions (US FDA 510(k), EU IVDR CE mark) and domestic South Korean clearance (MFDS 기술문서 심사), all DHF templates shall employ a dual format: the core documentation structure and tables in standard global English, accompanied by comprehensive Korean instructional guidance tips and audit checklists.

## 2. Detailed Functional Specifications
1. Every DHF template shall contain an instructional callout alert block directly below the metadata header:
   ```markdown
   > [!TIP]
   > **국문 작성 가이드 (Korean Guidance)**:
   > - ...
   ```
2. The Korean guidance section must detail:
   - Purpose and regulatory standard clause mapping.
   - Domestic Korea MFDS submission requirements and review points.
   - Practical authoring guidance, examples, and checklist criteria.
3. The formal document body (tables, requirements catalogs, FMEA matrices) must use standard English terminology to permit direct export to FDA/CE submission dossiers.

## 3. Inputs, Processing & Outputs
- **Inputs**: DHF template file content.
- **Processing**: Regex search for `> [!TIP]` callout and `국문 작성 가이드` substring.
- **Outputs**: Verified bilingual compliance documentation template.
