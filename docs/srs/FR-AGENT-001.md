# Software Requirement: FR-AGENT-001

> **Requirement ID**: `FR-AGENT-001`  
> **Title**: 13 Subagent Personas & Executable System Prompt Specifications  
> **Category**: Subagent Architecture (`[AGENT]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006 Clause 5.1.2, ISO 13485:2016 Clause 7.3.2  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-AGENT-001.md`  

---

## 1. Description & Technical Rationale
The framework shall specify 13 discrete subagent roles in the `agents/` directory. Each specification file must contain an authoritative persona description, regulatory domain responsibilities, and a ready-to-inject system prompt suitable for execution via `define_subagent` or `invoke_subagent`.

## 2. Detailed Functional Specifications
1. The framework shall provide exactly 13 agent specification files:
   - `00-samd-orchestrator-agent.md`, `01-user-needs-agent.md`, `02-clinical-sota-agent.md`, `03-regulatory-affairs-agent.md`, `04-srs-analyst-agent.md`, `05-risk-management-agent.md`, `06-cybersecurity-agent.md`, `07-system-architect-agent.md`, `08-detailed-design-agent.md`, `09-software-developer-agent.md`, `10-vnv-test-engineer-agent.md`, `11-dhf-lead-auditor-agent.md`, `12-postmarket-maintenance-agent.md`.
2. Each file must contain three mandatory structural sections:
   - `## 1. Persona & Profile`: Name, Role Title, Domain Expertise, Behavioral Principles.
   - `## 2. Responsibilities`: Primary duties, standards governed, inputs and outputs. Special regulatory responsibilities must be explicitly assigned:
     * Usability engineering (IEC 62366-1) across `01-user-needs-agent.md` and `10-vnv-test-engineer-agent.md`.
     * Post-market software maintenance, anomaly resolution, and CAPA (IEC 62304 Cl 6/9) across `09-software-developer-agent.md` and `11-dhf-lead-auditor-agent.md`.
     * AI/ML drift monitoring and PCCP execution across `07-system-architect-agent.md` and `10-vnv-test-engineer-agent.md`.
   - `## 3. System Prompt for Subagent Definition`: A fenced markdown codeblock containing the full system prompt.
3. **Context Window Overflow & Pinned Context Invariant**:
   - The agent execution runtime shall continuously track context window buffer consumption.
   - When conversation history exceeds 80% of model context capacity, context compaction (summarization) must preserve the agent persona, role constraints, and mandatory medical device safety rules at the top of the context buffer (**Pinned Context Invariant**).
   - Silent truncation or dropping of regulatory engineering rules or system prompts during long-running DHF compilation sessions is strictly prohibited.

## 3. Inputs, Processing & Outputs
- **Inputs**: Agent markdown specification file, active conversation context tokens.
- **Processing**: Section structure parser, prompt extraction, context buffer budget tracking.
- **Outputs**: Agent configuration object ready for instantiation with pinned safety invariant enforcement.
