# Software Requirement: FR-CYBER-001

> **Requirement ID**: `FR-CYBER-001`  
> **Title**: Post-Market Cybersecurity Incident Response & CVD Governance  
> **Category**: Medical Cybersecurity (`[CYBER]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: FDA 2023 Premarket Cybersecurity Guidelines, IEC 81001-5-1:2021 Clause 8, ISO/IEC 29147 / 30111  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-CYBER-001.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-011.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-011.md`  

---

## 1. Description & Technical Rationale
The framework shall formalize post-market cybersecurity operations, establishing a Coordinated Vulnerability Disclosure (CVD) process, Incident Response Plan (IRP), and vulnerability remediation service-level agreements (SLAs) mandated by US FDA and South Korea MFDS premarket cybersecurity requirements.

## 2. Detailed Functional Specifications
1. **Coordinated Vulnerability Disclosure (CVD)**:
   - Provide a formal vulnerability intake channel (e.g. `security.txt`, dedicated intake form).
   - Establish communication protocols with external security researchers and CERT/CC.
2. **Remediation SLA Enactment**:
   - Critical vulnerabilities (CVSS $\ge 9.0$): Interim mitigation within 30 days, commercial patch release within 60 days.
   - Immediate customer notification via Security Advisory bulletins.
3. **Incident Response Drills**:
   - Mandate annual table-top simulation exercises testing containment, patch deployment, and regulatory reporting procedures.
4. **Machine-Readable SBOM & Continuous Vulnerability Tracking**:
   - The cybersecurity management system shall maintain an active machine-readable SBOM (CycloneDX JSON or SPDX format) continuously correlated with public vulnerability advisories (NVD, OSV, CISA KEV).
   - Vulnerability Exploitability eXchange (VEX) records must be documented to provide clinical justifications for any non-exploitable CVEs in medical environments.

## 3. Inputs, Processing & Outputs
- **Inputs**: External vulnerability disclosure, incident telemetry, machine-readable SBOM manifests.
- **Processing**: CVSS scoring, exploitability triage, incident workflow execution, VEX documentation.
- **Outputs**: Incident response record, customer security advisory, validated security patch, updated machine-readable SBOM/VEX baseline.
