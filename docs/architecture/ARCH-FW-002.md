# Software Architecture: ARCH-FW-002

> **Component ID**: `ARCH-FW-002`  
> **Title**: Multi-Agent Persona & System Prompt Registry  
> **Subsystem**: Agent Governance Architecture  
> **Safety Class**: Class B (IEC 62304 Clause 5.3)  
> **Allocated Requirements**: `FR-AGENT-001`, `FR-AGENT-002`, `FR-AGENT-003`, `FR-RULE-001`, `FR-SKILL-013`  
> **Allocated Risk Controls**: `RCM-FW-004`, `RCM-FW-007`  
> **Detailed Design Units**: `docs/detailed_design/DDS-FW-006.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-AGENT-001.md`, `docs/tests/TC-FR-AGENT-002.md`, `docs/tests/TC-FR-AGENT-003.md`, `docs/tests/TC-FR-RULE-001.md`  

---

## 1. Architectural Overview & Design Rationale
`ARCH-FW-002` implements the role-based multi-agent persona architecture for medical software lifecycle processes. Under IEC 62304 and ISO 13485, individuals performing verification and quality audits must be independent of those creating the design and implementation. This component defines 12 specialized agent roles in `agents/*.md` and enforces workspace-wide engineering invariants via `AGENTS.md`.

## 2. Component Boundaries & Interfaces
```
+-------------------------------------------------------------------------+
|                  Workspace Rules Engine (AGENTS.md)                     |
|         Enforces Persistent Tagging Invariants & Size Budget            |
+-------------------------------------------------------------------------+
                                     │
           ┌─────────────────────────┼────────────────────────┐
           ▼                         ▼                        ▼
+──────────────────────+  +──────────────────────+  +──────────────────────+
| Left-Wing Agents     |  | Implementation Agent |  | Right-Wing & Audit   |
| (Requirements, SOTA, |  | (Developer, MISRA,   |  | (Independent V&V,    |
| Risk, Architecture)  |  | Static Analysis)     |  | DHF Lead Auditor)    |
+──────────────────────+  +──────────────────────+  +──────────────────────+
```
- **Inbound Interface**: Subagent invocation via `invoke_subagent` and `define_subagent`.
- **Outbound Interface**: Pre-configured system prompts injected with regulatory authority roles and restricted permissions.

## 3. Safety Segregation & Data Flows
- **Independence Segregation**: The V&V Agent (`10-vnv-test-engineer-agent`) and Lead Auditor (`11-dhf-lead-auditor-agent`) cannot modify implementation source files (`src/`); their outputs are strictly partitioned to test protocols and audit reports.
- **Rule Guard**: The workspace rule file `AGENTS.md` is strictly bounded to $\le 24,000$ bytes to ensure constant activation across all agent personas.

## 4. Technology Stack & Environmental Prerequisites
- Markdown system prompt specifications, Antigravity Agent Runtime.
