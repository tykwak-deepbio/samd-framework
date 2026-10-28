# Test Protocol: TC-FR-SKILL-009

> **Test Case ID**: `TC-FR-SKILL-009`  
> **Target Requirement**: `FR-SKILL-009` (Skill Specification - `samd-cybersecurity`)  
> **Test Level**: Unit / Workflow Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `samd-cybersecurity` specifies STRIDE threat modeling, `SEC-THR-xxx` and `SEC-CTL-xxx` tagging, CycloneDX/SPDX SBOM generation, CVE tracking, and delivery into `DHF-06`.

## 2. Preconditions
- `.agents/skills/samd-cybersecurity/SKILL.md` exists.
- `templates/DHF-06-Cybersecurity-Threat-Model-and-SBOM.md` exists.

## 3. Test Execution Steps
1. Parse `.agents/skills/samd-cybersecurity/SKILL.md`.
2. Verify STRIDE categories (Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege).
3. Verify machine-readable SBOM tracking and SOUP CVE evaluation instructions.
4. Verify cryptographic hygiene controls (TLS 1.3, AES-256) and CVD process.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: All 6 STRIDE categories, SBOM requirements, CVE tracking, and `SEC-THR-*`/`SEC-CTL-*` identifiers are defined.
- **FAIL**: Missing STRIDE analysis, missing SBOM guidance, or omitting `DHF-06`.
