# Software Architecture: ARCH-FW-011

> **Component ID**: `ARCH-FW-011`  
> **Title**: IEC 62304 Post-Market Maintenance, Configuration Management & Problem Resolution Subsystem  
> **Subsystem**: Lifecycle Maintenance & Quality Subsystem  
> **Safety Class**: Class B (IEC 62304 Clause 5.3)  
> **Allocated Requirements**: `FR-MAINT-001`, `FR-CM-001`, `FR-ANOM-001`, `FR-ANOM-002`, `FR-SOUP-001`, `FR-SOUP-002`, `FR-CYBER-001`, `FR-CYBER-002`, `FR-PMS-001`, `FR-SKILL-015`  
> **Allocated Risk Controls**: `RCM-FW-003`, `RCM-FW-005`, `RCM-FW-010`, `RCM-FW-013`, `RCM-FW-014`  
> **Detailed Design Units**: `docs/detailed_design/DDS-FW-004.md`, `docs/detailed_design/DDS-FW-011.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-MAINT-001.md`, `docs/tests/TC-FR-CM-001.md`, `docs/tests/TC-FR-ANOM-001.md`, `docs/tests/TC-FR-ANOM-002.md`, `docs/tests/TC-FR-SOUP-001.md`, `docs/tests/TC-FR-SOUP-002.md`, `docs/tests/TC-FR-CYBER-001.md`, `docs/tests/TC-FR-CYBER-002.md`, `docs/tests/TC-FR-PMS-001.md`, `docs/tests/TC-FR-SKILL-015.md`  

---

## 1. Architectural Overview & Design Rationale
`ARCH-FW-011` implements the post-market and supporting processes required by IEC 62304 Clauses 6, 8, and 9 and FDA Post-Market Cybersecurity Guidelines. It provides architectural governance for:
1. **Emergency Maintenance & Patches (`FR-MAINT-001`, `RCM-FW-010`)**: Controlled regression testing and cascading change impact re-evaluation.
2. **Configuration Baseline Management (`FR-CM-001`, `RCM-FW-014`)**: Cryptographic SHA-256 locking of model weights, system prompts, and build containers (`CI-xxx`).
3. **Anomaly & CAPA Resolution (`FR-ANOM-001`, `RCM-FW-014`)**: 4-tier defect triage (Catastrophic, Critical, Major, Minor) with mandatory zero-defect release blocks at Gate 10.
4. **Coordinated Vulnerability Disclosure & SOUP Surveillance (`FR-SOUP-001`, `FR-CYBER-001`, `RCM-FW-013`)**: Automated NVD feed monitoring, CVSS $\ge 7.0$ release blockers, and strict SLA engines ($\le 30$ days interim mitigation, $\le 60$ days release patch for CVSS $\ge 9.0$).

## 2. Component Boundaries & Interfaces
```
+-------------------------------------------------------------------------+
|        IEC 62304 Maintenance, CM, SOUP & Cybersecurity Subsystem       |
+-------------------------------------------------------------------------+
       │                             │                         │
       ▼                             ▼                         ▼
+──────────────────────────+   +──────────────────────────+  +─────────────────────────+
| Maintenance & Change CIA |   | Configuration Lock (CI)  |  | CVD & Anomaly Triage    |
| - IEC 62304 Cl 6 flow    |   | - SHA-256 baseline lock  |  | - 30d/60d Patch SLA     |
| - Cascading invalidation |   | - Zero drift guarantee   |  | - Gate 10 zero-bug block|
+──────────────────────────+   +──────────────────────────+  +─────────────────────────+
```
- **Inbound Interface**: Field problem reports, NVD CVE feeds, anomaly tickets, change requests.
- **Outbound Interface**: Maintenance hotfixes, configuration baseline registers (`CI-xxx`), CAPA records (`DHF-13`).

## 3. Safety Segregation & Incident Interlocks
- **Release Interlock (`RCM-FW-014`)**: Releases are unconditionally blocked at Gate 10 if any Catastrophic or Critical anomaly remains open.
- **Vulnerability SLA Interlock (`RCM-FW-013`)**: Automated timer tracks post-market security disclosures; failure to deploy patches within SLA triggers executive quality escalations.

## 4. Technology Stack & Environmental Prerequisites
- Python 3.8+ Standard Library, Git, Markdown, JSON-RPC.
