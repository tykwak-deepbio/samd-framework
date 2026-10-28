---
name: samd-cybersecurity
description: Performs cybersecurity threat modeling (STRIDE), Software Bill of Materials (SBOM) tracking, vulnerability analysis (CVE/CVD), and security controls implementation under IEC 81001-5-1, ISO 27001/27799, and FDA guidelines. Use this skill when conducting security reviews or authoring DHF-06.
---

# SaMD Cybersecurity & SBOM Management

This skill executes Phase 6 of the SaMD lifecycle, complying with **IEC 81001-5-1:2021 (Health software security)**, **ISO 27001 / ISO 27799**, **FDA 2023 Premarket Cybersecurity Guidance**, and **IMDRF N60/N73**.

## Goal
Identify cybersecurity threats across data flows and trust boundaries, implement security controls, track all third-party software dependencies via an SBOM, manage known vulnerabilities (CVEs), and author **`DHF-06-Cybersecurity-Threat-Model-and-SBOM.md`**.

## Cybersecurity Methodology

### 1. STRIDE Threat Modeling
Analyze all system interfaces and data flows:
- **S**poofing: Unauthorized entity claiming user identity or injecting fake slide metadata.
- **T**ampering: Modifying WSI pixel tiles or AI segmentation weights in transit or at rest.
- **R**epudiation: Denying diagnostic actions or audit log manipulation.
- **I**nformation Disclosure: Intercepting patient PHI/PII embedded in DICOM headers.
- **D**enial of Service (DoS): Flooding slide streaming endpoints to crash viewing workstation.
- **E**levation of Privilege: Escalating from viewer client to hospital server admin privileges.

### 2. Software Bill of Materials (SBOM) Generation
- Inventory all software components, runtime libraries, and AI frameworks (`SOUP-xxx`).
- Formats: CycloneDX JSON / XML or SPDX 2.3.
- Data fields required: Component Name, Version, Supplier/Author, License, SHA-256 Hash, Dependencies.
- Scan for known Common Vulnerabilities and Exposures (CVEs) using NIST NVD or automated scanners.

### 3. Security Controls & Post-Market Surveillance Plan
- Assign Security Control IDs (`SEC-CTL-xxx`) mapped to threats (`SEC-THR-xxx`).
- Require TLS 1.3 for network communications and AES-256 for local caching.
- Establish Coordinated Vulnerability Disclosure (CVD) process and patch update procedure.

## Procedure
1. Create Data Flow Diagrams (DFDs) identifying trust boundaries.
2. Formulate STRIDE threat table with likelihood and impact.
3. Export dependencies into SBOM table with vulnerability assessment.
4. Populate `templates/DHF-06-Cybersecurity-Threat-Model-and-SBOM.md`.
