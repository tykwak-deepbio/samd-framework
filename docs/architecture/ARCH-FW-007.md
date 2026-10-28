# Software Architecture: ARCH-FW-007

> **Component ID**: `ARCH-FW-007`  
> **Title**: Standard DHF Template Repository, Bilingual Guidance & Usability Engineering Architecture  
> **Subsystem**: Documentation Template & Human Factors Subsystem  
> **Safety Class**: Class B (IEC 62304 Clause 5.3)  
> **Allocated Requirements**: `FR-DHF-001`, `FR-DHF-002`, `FR-DHF-003`, `FR-USE-001`, `FR-USE-002`, `FR-LBL-001`, `FR-SKILL-004`  
> **Allocated Risk Controls**: `RCM-FW-002`, `RCM-FW-012`  
> **Detailed Design Units**: `docs/detailed_design/DDS-FW-007.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-DHF-001.md`, `docs/tests/TC-FR-DHF-002.md`, `docs/tests/TC-FR-DHF-003.md`, `docs/tests/TC-FR-USE-001.md`, `docs/tests/TC-FR-USE-002.md`, `docs/tests/TC-FR-LBL-001.md`, `docs/tests/TC-FR-SKILL-004.md`  

---

## 1. Architectural Overview & Design Rationale
`ARCH-FW-007` standardizes the artifact formats produced across all 12 lifecycle phases (providing 18 complete DHF templates `DHF-00` ~ `DHF-15`) and establishes the **IEC 62366-1 Usability Engineering, Labeling & PCA Error Architecture (`FR-USE-001`, `FR-LBL-001`, `RCM-FW-012`)**. 
To satisfy international clearance bodies (US FDA, EU Notified Bodies) while serving domestic manufacturers, the architecture establishes a 2-tier bilingual structure: formal tables and section headers in standard global English, accompanied by Korean instructional callouts (`> [!TIP] 국문 작성 가이드`) and MFDS compliance tips.

## 2. Component Boundaries & Interfaces
```
+-------------------------------------------------------------------------+
|                  Standard DHF Template Repository (templates/)          |
+-------------------------------------------------------------------------+
       │                                     │                         │
       ▼                                     ▼                         ▼
+──────────────────────────+   +──────────────────────────+  +─────────────────────────+
| Global English DHF Core  |   | Korean Guidance Tips     |  | Usability & PCA Engine  |
| - 16 DHF Standard Schemas|   | - > [!TIP] 국문 가이드   |  | - Critical Tasks & PCA  |
| - PHA 100% Screening Tab |   | - MFDS 심사 요령 & 점검표|  | - 15-User Summative UEF |
+──────────────────────────+   +──────────────────────────+  +─────────────────────────+
```
- **Inbound Interface**: Specialist agent requests for lifecycle stage documentation templates and usability error models.
- **Outbound Interface**: Pre-structured markdown files ready for project-specific customization under `dhf/`.

## 3. Safety Segregation & Usability Control Flows
- **Template Isolation**: Modifying a template file under `templates/` does not alter active project DHF instances until explicitly copied.
- **Usability Fail-Safe (`RCM-FW-012`)**: `DHF-12-UEF` enforces systematic identification of Critical Tasks and cognitive error mitigation (e.g. low-confidence alert banners and persistent unnormalized optical RGB toggles) before release approval.

## 4. Technology Stack & Environmental Prerequisites
- Markdown (GFM), GitHub Callout Extensions (`> [!TIP]`), IEC 62366-1 PCA modeling schemas.
