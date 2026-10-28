# Risk Analysis: RSK-FW-015

> **Risk ID**: `RSK-FW-015`  
> **Risk Control Measure ID**: `RCM-FW-015`  
> **Title**: External Regulatory MCP Data Exfiltration & Regulatory Linting Bypass  
> **Standard Reference**: ISO 14971:2019 Clause 5.4, IEC 81001-5-1:2021 Clause 6, ISO 27001:2022  
> **Target Requirement**: `FR-MCP-001`, `FR-HOOK-001`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-001.md`, `docs/architecture/ARCH-FW-004.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-001.md`, `docs/detailed_design/DDS-FW-003.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-MCP-001.md`, `docs/tests/TC-FR-HOOK-001.md`  

---

## 1. Hazard, Sequence of Events & Hazardous Situation
- **Hazard**: Malicious or unauthenticated MCP communication exfiltrating clinical PHI or unauthorized bypass of Antigravity regulatory linting hooks.
- **Sequence of Events**:
  1. An agent queries an external regulatory MCP server (e.g., PubMed, FDA DB, NVD) over an unencrypted or spoofed endpoint.
  2. Proprietary medical device algorithms or patient clinical metadata are transmitted outside the secure boundary.
  3. Alternatively, an automated agent writes non-compliant DHF markdown directly by circumventing pre-tool-call inspection hooks.
- **Hazardous Situation**: Clinical data breach or untracked non-conforming design documentation bypassing QMS gatekeepers.
- **Harm**: HIPAA / GDPR regulatory penalties, loss of IP, clearance revocation due to unvetted design history. (Severity: S3 - Serious, Probability: P3 - Medium $\to$ **Initial Risk: High / Unacceptable**).

## 2. Risk Control Measure: RCM-FW-015
- **Control Measure Description**: The framework establishes **mTLS-Enforced MCP Proxy & Event-Driven Regulatory Linting Hooks**.
  - MCP communication mandates mutual TLS 1.3 (mTLS) with client certificates; outbound requests are strictly limited to vetted regulatory query schemas (PMID, CVE ID, 510(k) numbers), with zero transmission of PHI or source files.
  - Antigravity event-driven lifecycle hooks (`pre-tool-call:write_to_file`) inspect all file writes for missing traceability headers and hardcoded secrets, terminating execution with an exception upon rule violation.
- **Control Type**: Inherent Network & File-System Security Interlocks.

## 3. Residual Risk Evaluation
- **Residual Severity**: S2.
- **Residual Probability**: P1 (Mitigated by cryptographic mTLS handshake and pre-write hook interceptors).
- **Residual Risk Level**: **Low / Acceptable (ALARP satisfied)**.
- **Verification Evidence**: `VERIF-FW-043`, `VERIF-FW-044` via `TC-FR-HOOK-001.md`, `TC-FR-MCP-001.md`.
## 4. Evaluation of New Hazards Arising from Risk Control Measures (ISO 14971:2019 Cl 7.3 & IEC 62304 Cl 7.2.2)
- **Potential New Hazards Introduced**:
  - Mutual TLS (mTLS) certificate expiration causing sudden disconnection of clinical external tools or regulatory linters.
  - Pre-tool-call hook latency overhead delaying real-time interactive agent responsiveness.
- **Secondary Risk Mitigations**:
  - Automated certificate lifecycle management (`DDS-FW-001`, `DDS-FW-003`) with proactive renewal alerts 30 days prior to expiry.
  - Lightweight local hook execution with microsecond-level regex parsing and asynchronous non-blocking auditing.
  - Fail-secure default behavior: hook failure defaults to safe operation abort, preventing unverified or untrusted tool execution.
- **Residual Risk Conclusion**: No unacceptable secondary hazards introduced. Residual risk remains **Acceptable (ALARP satisfied)**.
