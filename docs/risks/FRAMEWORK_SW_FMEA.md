# Software Failure Modes and Effects Analysis (SW-FMEA)

> **Document ID**: `FRAMEWORK-SW-FMEA-001`  
> **System Under Design**: Antigravity SaMD Multi-Agent Engineering Framework  
> **Applicable Standards**: IEC 62304:2006+AMD1:2015 Clause 7.1.2 & Clause 7.1.3, ISO 14971:2019 Clause 5.4 & Clause 7.1  
> **Lifecycle Milestone**: Post-Software Architectural Design (Phase 7 Gate Clearance)  
> **Revision**: 1.0.0 | **Effective Date**: 2026-10-28  
> **Reviewer**: Lead Regulatory & SaMD Software Quality Auditor  
> **Status**: Approved (11 Architecture Components & Interfaces 100% Screened)  

---

## 1. Scope & Objective
Under **IEC 62304 Clause 7.1.2**, following the completion of the software architectural design (`ARCH-FW-001` through `ARCH-FW-011`), the manufacturer must identify potential causes of software contribution to hazardous situations, specifically examining:
1. Software component functional failures and exceptions;
2. Component-to-component communication interfaces (Hooks bus, MCP pipes, SQLite database, memory caches);
3. Failures or vulnerabilities arising from third-party runtime dependencies (SOUP);
4. Timing, deadlocks, race conditions, and resource exhaustion.

This document establishes the formal **Architectural Software FMEA** for the SaMD framework core.

---

## 2. Risk Evaluation Criteria
- **Severity**: S1 (Negligible), S2 (Minor), S3 (Serious / Compliance Failure), S4 (Critical / Patient Diagnostic Harm).
- **Probability**: P1 (Extremely Unlikely), P2 (Remote), P3 (Occasional), P4 (Frequent).
- **Risk Evaluation**: Unacceptable (Initial S3xP3, S4xP2+), Acceptable/ALARP (S1-S2, S3-S4 with P1).

---

## 3. Architecture-Level Software FMEA Table (11 Components & Interfaces)

| Component ID | Subsystem & Critical Interface | Potential Failure Mode | Potential Root Cause | Local Effect | System Clinical Effect | Initial S x P | Risk Control Measure (RCM ID & Mechanism) | Detailed Design Allocation | Verification Protocol | Residual S x P | Acceptance |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :--- | :--- | :---: | :---: |
| `ARCH-FW-001` | Skill Loader & Hooks Bus (`pre-tool-call`) | Tool-call intercept failure allowing untagged DHF markdown write | Regex parser crash on corrupted YAML frontmatter | Hook fails open; markdown written to disk without traceability header | Unapproved or non-compliant DHF file enters release baseline | S3 x P3 (Unacceptable) | `RCM-FW-015`: Fail-closed interceptor raising synchronous exception on parse error | `DDS-FW-001` | `TC-FR-HOOK-001` | S2 x P1 | Broadly Acceptable |
| `ARCH-FW-001` | mTLS MCP External Client Proxy | Outbound network socket leak exposing hospital PHI | Buffer leak in JSON-RPC serialization | Raw patient biometric data sent to public PubMed query endpoint | Severe HIPAA/GDPR clinical data privacy violation | S4 x P3 (Unacceptable) | `RCM-FW-015`: Client-side sanitization proxy stripping patient identifiers before socket send | `DDS-FW-001` | `TC-FR-MCP-001` | S4 x P1 | Acceptable (ALARP) |
| `ARCH-FW-002` | Subagent Persona Registry & IPC | V&V test agent gaining write privileges to `src/` | Parent process environment variable leakage to worker subagent | V&V agent modifies production Python code or self-approves test | Loss of verification independence; masked critical clinical algorithm defect | S4 x P3 (Unacceptable) | `RCM-FW-004`, `RCM-FW-009`: OS-level read-only chroot sandbox binding on V&V worker tokens | `DDS-FW-006` | `TC-FR-AGENT-002`, `TC-FR-AGENT-003` | S4 x P1 | Acceptable (ALARP) |
| `ARCH-FW-003` | 12-Phase HITL State Machine | Premature phase transition or autonomous self-approval | State machine integer overflow or unhandled async signal | State machine advances to coding before SRS approval | Development proceeding on invalid clinical user requirements | S4 x P4 (Unacceptable) | `RCM-FW-001`: Immutable 2-Tier HITL gate review engine requiring cryptographic human APPROVE token | `DDS-FW-002` | `TC-FR-ORCH-002` | S4 x P1 | Acceptable (ALARP) |
| `ARCH-FW-003` | Parallel Sync Interface | Out-of-sync risk analysis during requirement update | Worker agent executing SRS changes without firing parallel risk notification | Requirement modified without updating FMEA hazard matrix | Clinical hazard unmitigated in modified diagnostic code | S4 x P3 (Unacceptable) | `RCM-FW-003`: Event-driven state invalidation bus dispatching parallel risk review triggers | `DDS-FW-002` | `TC-FR-ORCH-003` | S4 x P1 | Acceptable (ALARP) |
| `ARCH-FW-004` | Bipartite Traceability Validator | False-negative graph validation (reporting pass on orphan) | Regex parser failing on non-standard markdown whitespace | Orphan user need undetected; safety function remains untested | Unverified medical device software released to clinical market | S4 x P3 (Unacceptable) | `RCM-FW-002`: Bipartite graph connectivity algorithm with strict line-by-line whitespace normalization | `DDS-FW-003` | `TC-FR-TOOL-001`, `TC-FR-TOOL-002` | S4 x P1 | Acceptable (ALARP) |
| `ARCH-FW-005` | Downstream Invalidation Engine | Cyclic dependency deadlock in DAG traversal | Recursive graph loop introduced by circular markdown link | Invalidation engine hangs or terminates early, leaving stale approvals valid | Unapproved downstream design artifacts falsely treated as valid | S3 x P3 (Unacceptable) | `RCM-FW-003`: Topological sorting with cycle detection (Tarjan's algorithm) throwing immediate fault on cycle | `DDS-FW-004` | `TC-FR-TOOL-004` | S2 x P1 | Broadly Acceptable |
| `ARCH-FW-006` | SHA-256 DHF Document Indexer | Hash collation mismatch between Windows CRLF and Linux LF | Raw byte hashing without cross-platform newline normalization | DHF index mismatch falsely invalidating approved submissions | Regulatory audit disruption; false tampering alerts | S3 x P4 (Unacceptable) | `RCM-FW-005`: Universal newline normalization (`\r\n` $\to$ `\n`) and UTF-8 BOM stripping before SHA-256 hashing | `DDS-FW-005` | `TC-FR-TOOL-002` | S2 x P1 | Broadly Acceptable |
| `ARCH-FW-007` | 16-DHF Template & Usability Engine | Misinterpretation of bilingual guidance causing clinical use error | Callout formatting rendering issue on mobile/narrow display | Clinician fails to see low-confidence warning or normalization state | Clinician misinterprets dysplasia or overlooks micro-metastasis | S4 x P3 (Unacceptable) | `RCM-FW-012`: High-contrast persistent banners and PCA model use error protocols in `DHF-12` | `DDS-FW-007` | `TC-FR-USE-001` | S4 x P1 | Acceptable (ALARP) |
| `ARCH-FW-008` | AI Data MLOps & Drift Engine | Silent clinical performance degradation from demographic drift | Sensor degradation or hospital staining protocol shift | Model sensitivity drops below clinical baseline unnoticed | Systematic false-negative cancer biopsy triage | S4 x P4 (Unacceptable) | `RCM-FW-010`: Real-time KS-test and Population Stability Index (PSI $\ge 0.25$) trigger with raw image fallback | `DDS-FW-008` | `TC-FR-AI-004` | S4 x P1 | Acceptable (ALARP) |
| `ARCH-FW-008` | Data Leakage Guard | Patient-level cross-contamination between train & test sets | Slice-level random split ignoring multi-slice patient identifiers | Inflated verification accuracy masking real-world clinical failure | Overfitted AI deployed with false confidence to clinic | S4 x P3 (Unacceptable) | `RCM-FW-008`: Automated patient-level 0.00% overlap validation with cryptographic test set hash locking | `DDS-FW-008` | `TC-FR-AI-002` | S4 x P1 | Acceptable (ALARP) |
| `ARCH-FW-009` | LLM Medical Safety Guardrails | Fabricated PubMed citation (hallucination) in clinical DHF | LLM generating plausible-sounding but non-existent clinical PMID | Clinical safety justification based on fake medical evidence | Rejection of 510(k)/PMA; invalid clinical risk assessment | S3 x P4 (Unacceptable) | `RCM-FW-009`: Automated NLM PubMed API cross-check blocking DHF generation on unverified PMID | `DDS-FW-009` | `TC-FR-LLM-001` | S2 x P1 | Broadly Acceptable |
| `ARCH-FW-009` | Prompt Injection Guard | Hostile prompt injection in external clinical data | Untrusted text input concatenated into system instruction stream | Agent executes unauthorized file deletion or data exfiltration | DHF audit trail loss; intellectual property compromise | S3 x P3 (Unacceptable) | `RCM-FW-009`: XML boundary encapsulation (`<untrusted_input>`) and prompt sanitization filter | `DDS-FW-009` | `TC-FR-LLM-002` | S2 x P1 | Broadly Acceptable |
| `ARCH-FW-010` | 21 CFR Part 11 Audit Trail & Sig | Audit trail tampering or undetected log deletion | OS file system permissions allowing direct edit of `audit_trail.log` | Fraudulent alteration of design history or approvals | FDA warning letter, disqualification of regulatory data | S4 x P3 (Unacceptable) | `RCM-FW-011`: Append-only WORM file descriptors and cryptographic HMAC-SHA256 signature binding | `DDS-FW-010` | `TC-FR-PART11-001` | S3 x P1 | Broadly Acceptable |
| `ARCH-FW-011` | Post-Market SOUP & Anomaly Engine | Release of software with known CVSS $\ge 9.0$ vulnerability | Delayed NVD vulnerability ingestion or SLA tracking failure | Ransomware attack compromising hospital pathology network | Clinical network shutdown; patient whole-slide image tampering | S4 x P3 (Unacceptable) | `RCM-FW-013`: Automated NVD CVE feed scanner with mandatory 30-day mitigation / 60-day patch release SLA | `DDS-FW-011` | `TC-FR-CYBER-001`, `TC-FR-SOUP-001` | S4 x P1 | Acceptable (ALARP) |
| `ARCH-FW-011` | Configuration & Defect Release Block | Premature clinical deployment with unresolved Critical bug | Anomaly triage committee misclassifying crash as Minor defect | Software crashes during critical intraoperative biopsy examination | Interrupted clinical procedure; delayed patient diagnosis | S4 x P3 (Unacceptable) | `RCM-FW-014`: Gate 10 automated release block enforcing zero unresolved Catastrophic or Critical anomalies | `DDS-FW-011` | `TC-FR-ANOM-001`, `TC-FR-CM-001` | S4 x P1 | Acceptable (ALARP) |

---

## 4. Verification & Flow-Down Status
All 16 architectural failure modes have been traced directly forward to Software Detailed Design units (`DDS-FW-001` through `DDS-FW-011`) and verified via automated test specifications (`TC-FR-*`). All residual risks are broadly acceptable or reduced to ALARP under ISO 14971:2019.
