# Detailed Design Specification: DDS-FW-006

> **Unit Design ID**: `DDS-FW-006`  
> **Title**: Persona Role Guard & System Prompt Composition Unit  
> **Parent Architecture**: `docs/architecture/ARCH-FW-002.md`  
> **Safety Class**: Class B (IEC 62304 Clause 5.4)  
> **Allocated Risk Controls**: `RCM-FW-004`, `RCM-FW-007`  
> **Target Requirement**: `FR-SKILL-013`, `FR-AGENT-001`, `FR-AGENT-002`, `FR-AGENT-003`, `FR-RULE-001`  
> **Implementation Target**: `agents/*.md`, `AGENTS.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-AGENT-001.md`, `docs/tests/TC-FR-AGENT-002.md`, `docs/tests/TC-FR-AGENT-003.md`, `docs/tests/TC-FR-RULE-001.md`, `docs/tests/TC-FR-SKILL-013.md`  

---

## 1. Detailed Unit Description & Rationale
`DDS-FW-006` specifies the persona definition structure, system prompt format, and role segregation invariants that guarantee independent verification across all 12 agent roles.

## 2. Data Structures & Specification Format (`agents/*.md`)
Each agent file must contain exactly 3 standard top-level markdown sections:
```markdown
# Agent Specification: [Role Title]
## 1. Persona & Profile
- Identity, Regulatory Mandates, Safety Focus
## 2. Responsibilities & Expected Outputs
- Primary Outputs (DHF deliverables, code, test protocols)
- Prohibited Actions (e.g. V&V cannot edit source code)
## 3. System Prompt
```markdown
[Self-contained executable system prompt with instructions, invariant rules, and output templates]
```
```

## 3. Invariant Enforcement & Independence Logic
```python
def verify_agent_independence(agent_file: str) -> bool:
    with open(agent_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    assert "## 1. Persona & Profile" in content
    assert "## 2. Responsibilities" in content
    assert "## 3. System Prompt" in content
    
    # Specific rule for 10-vnv-test-engineer-agent
    if "10-vnv-test-engineer-agent" in agent_file:
        assert "independent" in content.lower()
        assert "objective" in content.lower()
    return True
```

## 4. Error Handling & Boundary Conditions
- **Missing Required Sections**: Flagged as invalid agent specification during automated test execution.
- **Rule File Budget Violation**: If `AGENTS.md` exceeds 24,000 bytes, `test_framework.py` raises an explicit assertion failure.

## 5. Safety Invariants & Risk Control Implementation (RCM-FW-004, RCM-FW-007)
- **Safety Invariant 1 (RCM-FW-004 - Verification Independence Interlock)**: V&V testing personas (`samd_vnv_tester`, `samd_dhf_auditor`) operate under read-only sandboxes over implementation source code and cannot execute modifying commands or self-approve design gates.
- **Safety Invariant 2 (RCM-FW-007 - Persona Immutability & Context Budget)**: Agent specifications in `agents/*.md` enforce strict section headers (Persona, Responsibilities, System Prompt) and cannot be dynamically overwritten during runtime.
