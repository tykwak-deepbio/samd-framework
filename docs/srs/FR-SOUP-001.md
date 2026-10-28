# Software Requirement: FR-SOUP-001

> **Requirement ID**: `FR-SOUP-001`  
> **Title**: SOUP Lifecycle Qualification & Automated CVE Surveillance  
> **Category**: Third-Party Software Governance (`[SOUP]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006 Clause 5.3.3 & Clause 7.1.2, IEC 81001-5-1:2021  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-SOUP-001.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-011.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-003.md`  

---

## 1. Description & Technical Rationale
The framework shall govern Software of Unknown Provenance (SOUP) and third-party Commercial-Off-The-Shelf (COTS) libraries across their lifecycle, documenting functional requirements, system prerequisites, failure modes, and conducting continuous Common Vulnerabilities and Exposures (CVE) surveillance.

## 2. Detailed Functional Specifications
1. **SOUP Inventory & Tagging**:
   - Every third-party library must receive a unique tag `SOUP-xxx` in `DHF-06` and `DHF-07`.
   - Record exact package name, version, license, publisher, and functional purpose.
2. **Qualification & Failure Isolation (Clause 5.3.3)**:
   - Document hardware/software prerequisites.
   - Analyze failure modes in `DHF-05B` and design architectural isolation mechanisms.
3. **Automated Vulnerability Surveillance**:
   - Cross-check all `SOUP-xxx` items against the National Vulnerability Database (NVD) and GitHub Advisory DB.
   - Any dependency with unmitigated Critical CVE (CVSS score $\ge 7.0$) shall block release gates.
4. **Machine-Readable SBOM Generation (CycloneDX & SPDX)**:
   - In addition to the human-readable markdown table in `DHF-06`, the framework shall automatically generate an authoritative machine-readable Software Bill of Materials (SBOM) conforming to CycloneDX (JSON v1.4/v1.5) or SPDX (ISO/IEC 5962:2021) international standards.
   - The SBOM file must capture package identifiers, cryptographic SHA-256 hashes, exact version numbers, licensing details, and direct/transitive dependency relationships to satisfy US FDA Premarket Cybersecurity (2023) and MFDS regulatory submission mandates.

## 3. Inputs, Processing & Outputs
- **Inputs**: Dependency manifest files (`requirements.txt`, `package.json`), CVE feeds.
- **Processing**: Dependency extraction, CVE matching, qualification criteria validation, CycloneDX/SPDX generation.
- **Outputs**: Qualified SOUP inventory in `DHF-06`, machine-readable SBOM (`sbom.cyclonedx.json` / `sbom.spdx.json`), CVE vulnerability report.
