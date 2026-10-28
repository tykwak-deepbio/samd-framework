# Test Protocol: TC-FR-SOUP-001

> **Test Case ID**: `TC-FR-SOUP-001`  
> **Target Requirement**: `FR-SOUP-001` (SOUP Lifecycle Qualification & Automated CVE Surveillance)  
> **Test Level**: Process & Security Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `FR-SOUP-001` specifies SOUP inventory tracking (`SOUP-xxx`), qualification, failure mode isolation, and automated NVD CVE vulnerability monitoring under IEC 62304 Clause 5.3.3 and 7.1.2.

## 2. Preconditions
- `docs/srs/FR-SOUP-001.md` exists.

## 3. Test Execution Steps
1. Parse `docs/srs/FR-SOUP-001.md`.
2. Check `SOUP-xxx` tagging rules and inventory requirements (package, version, license).
3. Check failure mode analysis and architectural isolation requirements.
4. Verify automated NVD CVE surveillance and CVSS $\ge 7.0$ release blocking rule.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: SOUP qualification rules, failure isolation, and CVE surveillance blocking criteria are defined.
- **FAIL**: Missing SOUP qualification requirements or omitting vulnerability surveillance rules.
