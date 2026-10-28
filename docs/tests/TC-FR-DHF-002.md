# Test Protocol: TC-FR-DHF-002

> **Test Case ID**: `TC-FR-DHF-002`  
> **Target Requirement**: `FR-DHF-002` (Global English Submission Format with Korean Guidance & Checklists)  
> **Test Level**: Verification / Content Inspection  
> **Verification Method**: Automated Regex Search (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that all 14 DHF templates adopt the dual language structure: the formal document body and tables in standard global English suitable for FDA/CE submissions, and the top-level guidance tip block in Korean (`> [!TIP]` and `국문 작성 가이드`).

## 2. Preconditions
- Directory `templates/` is populated with 14 DHF templates.

## 3. Test Execution Steps
1. Scan all 14 files in `templates/`.
2. Verify that each file contains the exact callout pattern:
   `> [!TIP]`
   `**국문 작성 가이드 (Korean Guidance)**:`
3. Verify that the table headers and requirements catalogs in each file use English terminology (`Requirement ID`, `Description`, `Verification Method`, `Severity`, `Probability`).

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: 100% of the 14 templates contain the Korean guidance tip callout and standard English tables.
- **FAIL**: Any template lacks the Korean instructional guidance or uses non-standard table formats.
