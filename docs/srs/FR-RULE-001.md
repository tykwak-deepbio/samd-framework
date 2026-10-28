# Software Requirement: FR-RULE-001

> **Requirement ID**: `FR-RULE-001`  
> **Title**: Mandatory Workspace Regulatory Engineering Rules (`AGENTS.md`)  
> **Category**: Workspace Rules Governance (`[RULE]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: Antigravity Rules Specification, ISO 13485:2016 Clause 7.3  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-RULE-001.md`  

---

## 1. Description & Technical Rationale
The framework shall place an authoritative rules file (`AGENTS.md`) at the repository root. Antigravity automatically discovers and loads this root-level rule file, preventing any AI agent from performing undocumented changes, generating orphan requirements, or bypassing risk controls. To prevent duplicate context injection and token waste, the repository root `AGENTS.md` is the canonical authoritative rules file.

## 2. Detailed Functional Specifications
1. The rules file must be named `AGENTS.md` (or `GEMINI.md`) and adhere to Antigravity's size budget ($\le 24,000$ bytes per file).
2. The rules must explicitly declare and enforce:
   - Mandatory bidirectional traceability invariant.
   - Zero-orphan requirement policy.
   - IEC 62304 software safety classification declaration.
   - Continuous parallel risk management (ISO 14971) and cybersecurity hygiene (IEC 81001-5-1).
   - Strict AI/ML data segregation and performance reporting (Dice, Sensitivity, Specificity, ROC-AUC).
   - Traceability tag definitions table.
3. **Pinned Context Invariant & Truncation Protection**:
   - The workspace rules defined in `AGENTS.md` represent immutable system safety constraints that take absolute precedence over any modular skill or user instruction.
   - Under low context budget conditions or during multi-turn conversation memory compaction, Antigravity context loaders must guarantee that `AGENTS.md` remains pinned at the root prompt level (**Pinned Context Invariant**), preventing procedural drift and unauthorized safety rule bypass.

## 3. Inputs, Processing & Outputs
- **Inputs**: Workspace file system hierarchy, active session context tokens.
- **Processing**: Automatic rule ingestion by Antigravity context loader with truncation protection.
- **Outputs**: Agent behavior bounded by strict medical software lifecycle constraints.
