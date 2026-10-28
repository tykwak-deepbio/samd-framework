# Detailed Design Specification: DDS-FW-007

> **Unit Design ID**: `DDS-FW-007`  
> **Title**: Bilingual Template Formatter & Korean Callout Anchor Unit  
> **Parent Architecture**: `docs/architecture/ARCH-FW-007.md`  
> **Safety Class**: Class B (IEC 62304 Clause 5.4)  
> **Allocated Risk Controls**: `RCM-FW-012`  
> **Target Requirement**: `FR-DHF-001`, `FR-DHF-002`, `FR-DHF-003`, `FR-SKILL-004`, `FR-SKILL-005`, `FR-SKILL-006`, `FR-SKILL-007`, `FR-SKILL-008`, `FR-SKILL-009`, `FR-SKILL-010`, `FR-SKILL-011`, `FR-SKILL-013`, `FR-USE-001`, `FR-USE-002`, `FR-LBL-001`  
> **Implementation Target**: `templates/DHF-*.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-DHF-001.md`, `docs/tests/TC-FR-DHF-002.md`, `docs/tests/TC-FR-DHF-003.md`, `docs/tests/TC-FR-USE-001.md`, `docs/tests/TC-FR-USE-002.md`, `docs/tests/TC-FR-LBL-001.md`, `docs/tests/TC-FR-SKILL-004.md`  

---

## 1. Detailed Unit Description & Rationale
`DDS-FW-007` specifies the layout and formatting contract for all 18 DHF templates under `templates/` (including DHF-14 Medical Device Labeling & IFU and DHF-15 Clinical Evaluation Report). It guarantees that templates present an internationally acceptable English regulatory structure while embedding Korean instructional guidance callouts (`> [!TIP] 국문 작성 가이드`) to assist engineers in complying with South Korean MFDS regulations.

## 2. Data Structures & Template Layout Contract
Every DHF template must conform to the following structural sequence:
1. `# Top-Level Document Title`
2. Blockquote Document Control Header:
   ```markdown
   > **Document ID**: `DHF-xx-...`  
   > **Title**: ...  
   > **Version**: 1.0.0 | **Effective Date**: YYYY-MM-DD  
   > **Author**: ... | **Reviewer**: ... | **Approver**: ...  
   > **Status**: Draft / Approved  
   ```
3. Korean Guidance Callout:
   ```markdown
   > [!TIP] 국문 작성 가이드
   > 본 문서는 [관련 표준 및 식약처 가이드라인]을 충족하도록 작성되어야 합니다...
   ```
4. Formal Markdown Content Sections & Tagged Tables (`REQ-SW-*`, `RSK-*`, `ARCH-*`, etc.)
5. Revision History Table

## 3. Algorithmic Validation Logic
```python
def validate_template_structure(template_path: str) -> bool:
    with open(template_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    assert content.startswith("# "), "Template must start with # Document Title"
    assert "**Document ID**:" in content, "Missing Document ID header"
    assert "**Status**:" in content, "Missing Status header"
    assert "국문 작성 가이드" in content, "Missing Korean guidance callout"
    return True
```

## 4. Error Handling & Boundary Conditions
- **Missing Header**: Triggers failure in `test_framework.py` `test_ts_dhf_001_templates_structure`.
- **Missing Guidance**: Non-conformance flagged if English tables are present without corresponding Korean instructions.

## 5. Safety Invariants & Risk Control Implementation (RCM-FW-012)
- **Safety Invariant 1 (RCM-FW-012 - Usability Error Mitigation Interlock)**: All clinical UI and CLI outputs must adhere to IEC 62366-1 usability standards. Safety-critical states (uncalibrated scanner, low-confidence triage, algorithmic drift) must trigger persistent high-contrast warning banners.
- **Safety Invariant 2 (RCM-FW-012 - Unobstructed Diagnostic Viewport)**: Warning banners must be positioned in dedicated non-occluding UI status regions, preventing clipping or obstruction of primary histological slide features.
