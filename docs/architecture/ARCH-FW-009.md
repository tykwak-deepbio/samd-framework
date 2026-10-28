# Software Architecture: ARCH-FW-009

> **Component ID**: `ARCH-FW-009`  
> **Title**: LLM Safety Guardrails, Anti-Hallucination & RBAC Sandbox Subsystem  
> **Subsystem**: Agent Security & Governance Subsystem  
> **Safety Class**: Class B (IEC 62304 Clause 5.3)  
> **Allocated Requirements**: `FR-LLM-001`, `FR-LLM-002`, `FR-LLM-003`, `FR-AGENT-003`  
> **Allocated Risk Controls**: `RCM-FW-004`, `RCM-FW-009`  
> **Detailed Design Units**: `docs/detailed_design/DDS-FW-006.md`, `docs/detailed_design/DDS-FW-009.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-LLM-001.md`, `docs/tests/TC-FR-LLM-002.md`, `docs/tests/TC-FR-LLM-003.md`, `docs/tests/TC-FR-AGENT-003.md`  

---

## 1. Architectural Overview & Design Rationale
`ARCH-FW-009` implements security, grounding, and permission boundaries for all autonomous LLM subagents. It prevents prompt injection exploits, eliminates clinical hallucinations through real-time bibliographic fact-checking, clamps generation parameters for regulatory reproducibility, and enforces OS-level read-only access on source code for verification agents.

## 2. Component Boundaries & Interfaces
```
                 +---------------------------------------------+
                 |       Agent Execution Gateway / Proxy       |
                 +---------------------------------------------+
                                        │
           ┌────────────────────────────┼───────────────────────────┐
           ▼                            ▼                           ▼
+─────────────────────+      +─────────────────────+     +─────────────────────+
|  Grounding Checker  |      | Injection Sanitizer |     |  RBAC Tool Sandbox  |
| - PubMed PMID Verify|      | - Tag Boundary Wrap |     | - Developer: RW src |
| - Standard Clauses  |      | - Jailbreak Filter  |     | - Tester: RO src    |
| - Hallucination Block      | - Anomaly Turn Abort|     | - Auditor: RO all   |
+─────────────────────+      +─────────────────────+     +─────────────────────+
```
- **Inbound Interface**: Subagent prompts, external web and literature text streams.
- **Outbound Interface**: Sanitized prompt payloads, validated bibliographic references, tool permission filters.

## 3. Safety Segregation & Data Flows
- **Read-Only Code Isolation**: Independent tester and auditor agents run in restricted containers/sandboxes where write system calls to `src/` are denied.
- **Sampling Clamping**: Injects `temperature = 0.0` and `seed = 42` into all API payloads.

## 4. Technology Stack & Environmental Prerequisites
- Python 3.8+ Standard Library, OS Filesystem Permissions.
