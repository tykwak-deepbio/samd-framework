# Risk Analysis: RSK-FW-006

> **Risk ID**: `RSK-FW-006`  
> **Risk Control Measure ID**: `RCM-FW-006`  
> **Title**: Agent Context Window Exhaustion Leading to Procedural Drift & Hallucination  
> **Standard Reference**: ISO 14971:2019 Clause 5.4, IEC 62304:2006 Clause 5.1.2  
> **Target Requirement**: `FR-SKILL-001`, `FR-SKILL-002`, `FR-SKILL-005`, `FR-SKILL-006`, `FR-SKILL-007`, `FR-SKILL-008`, `FR-SKILL-010`, `FR-SKILL-011`, `FR-SKILL-012`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-001.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-001.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-SKILL-001.md`, `docs/tests/TC-FR-SKILL-002.md`  

---

## 1. Hazard, Sequence of Events & Hazardous Situation
- **Hazard**: LLM context window saturation and instruction truncation.
- **Sequence of Events**:
  1. All 14 regulatory standards and 11 lifecycle workflows are injected simultaneously into the agent's prompt context.
  2. The LLM context window overflows, causing earlier medical device safety constraints and formatting rules to be truncated or forgotten.
  3. The agent hallucinates non-compliant markdown structures or omits safety tags.
- **Hazardous Situation**: Inconsistent DHF documents generated with missing regulatory fields.
- **Harm**: Inadequate DHF documentation failing ISO 13485 audit or regulatory premarket clearance review. (Severity: S2 - Minor, Probability: P4 - High $\to$ **Initial Risk: Medium / ALARP**).

## 2. Risk Control Measure: RCM-FW-006
- **Control Measure Description**: The framework adopts the **Antigravity Skills Progressive Disclosure Architecture**.
  - Skills are segregated into 12 discrete directories under `.agents/skills/<name>/SKILL.md`.
  - Only the metadata (`name`, `description`) is loaded at startup.
  - Full instructions are loaded on-demand only when a specific phase or slash command is triggered, preserving token budget and preventing instruction loss.
- **Control Type**: Inherent Architecture / Progressive Loading Design.

## 3. Residual Risk Evaluation
- **Residual Severity**: S1 - Negligible.
- **Residual Probability**: P1 (Context budget kept minimal per phase).
- **Residual Risk Level**: **Negligible / Acceptable**.
- **Verification Evidence**: `VERIF-FW-004` via `TC-FR-SKILL-001.md`.
## 4. Evaluation of New Hazards Arising from Risk Control Measures (ISO 14971:2019 Cl 7.3 & IEC 62304 Cl 7.2.2)
- **Potential New Hazards Introduced**:
  - Skill truncation / context budget clamping dropping critical edge-case safety instructions.
  - Agent instruction fragmentation across multiple modular skills leading to conflicting operational guidance.
- **Secondary Risk Mitigations**:
  - YAML frontmatter contract enforcement (`DDS-FW-001`) guaranteeing skill compactness and mandatory reference pointers to authoritative DHF documents.
  - Workspace rule hierarchy (`AGENTS.md`) acting as immutable global baseline superseding any modular skill instruction.
  - Static linting verifying skill description length, name formatting, and absence of redundant tokens.
- **Residual Risk Conclusion**: No unacceptable secondary hazards introduced. Residual risk remains **Acceptable (ALARP satisfied)**.
