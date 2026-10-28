# Software Architecture: ARCH-FW-001

> **Component ID**: `ARCH-FW-001`  
> **Title**: Modular Skill Ecosystem, Regulatory Linting Hooks & MCP Proxy  
> **Subsystem**: Core Runtime Architecture  
> **Safety Class**: Class B (IEC 62304 Clause 5.3)  
> **Allocated Requirements**: `FR-SKILL-001`, `FR-SKILL-002`, `FR-SKILL-003` ~ `FR-SKILL-014`, `FR-HOOK-001`, `FR-MCP-001`  
> **Allocated Risk Controls**: `RCM-FW-006`, `RCM-FW-015`  
> **Detailed Design Units**: `docs/detailed_design/DDS-FW-001.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-SKILL-001.md`, `docs/tests/TC-FR-HOOK-001.md`, `docs/tests/TC-FR-MCP-001.md`  

---

## 1. Architectural Overview & Design Rationale
`ARCH-FW-001` governs the runtime extension architecture of the framework:
1. **Progressive Skill Disclosure**: Decouples the monolithic SaMD lifecycle knowledge base into 12 discrete skills (`.agents/skills/<skill-name>/SKILL.md`), keeping context consumption minimal (`RCM-FW-006`).
2. **Event-Driven Regulatory Linting Hooks (`FR-HOOK-001`)**: Intercepts tool calls (`pre-tool-call:write_to_file`) to enforce traceability headers and secret prevention before disk write (`RCM-FW-015`).
3. **Mutual-TLS MCP Server Interface (`FR-MCP-001`)**: Connects agents to vetted regulatory databases (PubMed, FDA, NVD) over an encrypted mTLS tunnel with strict PHI egress blocking (`RCM-FW-015`).

## 2. Component Boundaries & Interfaces
```
+-------------------------------------------------------------------------+
|                  Antigravity Context Window & Dispatcher                |
+-------------------------------------------------------------------------+
       │                                     │                         │
       ▼                                     ▼                         ▼
+──────────────────────────+   +──────────────────────────+  +─────────────────────────+
| Dynamic Skill Loader     |   | Event-Driven Hook Engine |  | mTLS MCP Client Proxy   |
| - On-demand SKILL.md     |   | - pre-tool-call inspect  |  | - Encrypted outbound    |
| - Context budget guard   |   | - Header & secret filter |  | - Zero PHI egress rule  |
+──────────────────────────+   +──────────────────────────+  +─────────────────────────+
```
- **Inbound Interface**: User slash commands, agent tool calls (`write_to_file`), regulatory query requests.
- **Outbound Interface**: Injected prompts, validated file write authorization, structured external regulatory citations.

## 3. Safety Segregation & Data Flows
- **Segregation**: Each skill and MCP tunnel operates in an isolated sandbox.
- **Fail-Safe & Intercept**: If a tool call attempts to write an untagged DHF or disclose credentials, the hook throws an immediate execution abort. Outbound MCP requests strip patient identifiers.

## 4. Technology Stack & Environmental Prerequisites
- Markdown (`SKILL.md`), Antigravity Customization Specification, JSON-RPC 2.0 / MCP Protocol, mTLS 1.3.
