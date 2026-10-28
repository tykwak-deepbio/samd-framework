# Risk Analysis: RSK-FW-013

> **Risk ID**: `RSK-FW-013`  
> **Risk Control Measure ID**: `RCM-FW-013`  
> **Title**: Post-Market Vulnerability Disclosure Delays & Unmitigated SOUP CVEs  
> **Standard Reference**: ISO 14971:2019 Clause 5.4, IEC 81001-5-1:2021, FDA Premarket Cybersecurity (2023)  
> **Target Requirement**: `FR-CYBER-001`, `FR-SOUP-001`, `FR-SKILL-009`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-011.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-011.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-CYBER-001.md`, `docs/tests/TC-FR-SOUP-001.md`  

---

## 1. Hazard, Sequence of Events & Hazardous Situation
- **Hazard**: Unmonitored third-party SOUP dependencies and delayed security patch response.
- **Sequence of Events**:
  1. An open-source dependency (SOUP) used in the SaMD pipeline discloses a critical zero-day remote code execution or data corruption vulnerability (CVSS $\ge 9.0$).
  2. The organization lacks a Coordinated Vulnerability Disclosure (CVD) process and post-market surveillance.
  3. Attackers compromise hospital clinical workstations or alter whole-slide image diagnostic data in transit.
- **Hazardous Situation**: Tampered patient diagnostic imagery or clinical service outage due to unpatched known cyber vulnerabilities.
- **Harm**: Misdiagnosis, unauthorized disclosure of sensitive PHI, hospital network disruption. (Severity: S4 - Critical, Probability: P3 - Medium $\to$ **Initial Risk: High / Unacceptable**).

## 2. Risk Control Measure: RCM-FW-013
- **Control Measure Description**: The framework establishes a **Post-Market Cybersecurity IRP & Continuous SOUP Surveillance Engine**.
  - Enforces `security.txt` and designated reporting inbox (`security@company.com`) with mandatory PGP key.
  - Mandates strict SLAs: initial triage $\le 7$ business days, interim clinical mitigation $\le 30$ calendar days, tested patch release $\le 60$ calendar days for CVSS $\ge 9.0$.
  - Enforces automated CycloneDX/SPDX SBOM generation and blocks releases if any SOUP has unresolved CVSS $\ge 7.0$ without documented justification.
- **Control Type**: Inherent Software Architecture & Incident Response Interlock.

## 3. Residual Risk Evaluation
- **Residual Severity**: S3.
- **Residual Probability**: P1 (Controlled by automated SBOM tracking and strict patch SLAs).
- **Residual Risk Level**: **Low / Acceptable (ALARP satisfied)**.
- **Verification Evidence**: `VERIF-FW-032`, `VERIF-FW-034` via `TC-FR-SOUP-001.md`, `TC-FR-CYBER-001.md`.
## 4. Evaluation of New Hazards Arising from Risk Control Measures (ISO 14971:2019 Cl 7.3 & IEC 62304 Cl 7.2.2)
- **Potential New Hazards Introduced**:
  - Strict 30-day/60-day vulnerability SLA forcing rushed patch deployments without sufficient regression and clinical validation testing.
  - False positive CVE reports against dormant code branches halting production release schedules.
- **Secondary Risk Mitigations**:
  - Formal Vulnerability Exploitability eXchange (VEX) assessment framework (`DDS-FW-011`) allowing documented justification of non-exploitability in clinical context.
  - Automated regression test suite execution required prior to any security patch integration.
  - Tiered SLA enforcement prioritizing remotely exploitable critical vulnerabilities (CVSS >= 9.0) with clinical impact.
- **Residual Risk Conclusion**: No unacceptable secondary hazards introduced. Residual risk remains **Acceptable (ALARP satisfied)**.
