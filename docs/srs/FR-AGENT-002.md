# Software Requirement: FR-AGENT-002

> **Requirement ID**: `FR-AGENT-002`  
> **Title**: Independent Verification & Validation (V&V) Role Enforcement  
> **Category**: Subagent Architecture (`[AGENT]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006 Clause 5.6.2 & 5.7.2, ISO 13485:2016 Clause 7.3.6  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-AGENT-002.md`  

---

## 1. Description & Regulatory Rationale
Under IEC 62304 Clause 5.6/5.7 and ISO 13485 Clause 7.3.6, software verification for Class B and C medical devices must maintain appropriate technical and organizational independence from implementation. The agent tasked with testing must be decoupled from the developer agent.

## 2. Detailed Functional Specifications
1. The framework shall strictly separate `software-developer-agent` (Phase 9 implementation) and `vnv-test-engineer-agent` (Phase 10 independent verification).
2. The `vnv-test-engineer-agent` prompt shall instruct the agent:
   - To operate independently without bias toward passing code.
   - To mandate objective, pre-defined pass/fail criteria prior to running tests.
   - To record anomalies formally rather than silently modifying production source code to pass tests.
3. Test protocols must be established and frozen prior to test execution evidence recording.

## 3. Inputs, Processing & Outputs
- **Inputs**: Test protocols (`TC-*`), build artifacts, production code.
- **Processing**: Independent execution and comparison against acceptance criteria.
- **Outputs**: Objective Verification Evidence (`VERIF-*`), Software Test Report (`DHF-09`).
