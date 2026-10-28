# Test Protocol: TC-FR-AGENT-002

> **Test Case ID**: `TC-FR-AGENT-002`  
> **Target Requirement**: `FR-AGENT-002` (Independent Verification & Validation Role Enforcement)  
> **Test Level**: Regulatory / Process Verification  
> **Verification Method**: Prompt & Role Decoupling Inspection  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `agents/10-vnv-test-engineer-agent.md` enforces technical and organizational independence from `agents/09-software-developer-agent.md`, requiring objective pass/fail criteria and prohibiting unauthorized modifications to production code.

## 2. Preconditions
- `agents/09-software-developer-agent.md` and `agents/10-vnv-test-engineer-agent.md` are present.

## 3. Test Execution Steps
1. Compare the personas and responsibilities of Agent 09 and Agent 10.
2. Verify that Agent 10 prompt states:
   - "You maintain organizational and technical independence from the software development team."
   - "Pre-specify objective pass/fail criteria."
   - "Log any unexpected failure or discrepancy as a formal anomaly rather than modifying source code directly."
3. Verify that `DHF-09` requires independent verification signatures.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: The roles are strictly separated; the V&V agent is explicitly constrained by independence rules under IEC 62304 Clause 5.6.2 and 5.7.2.
- **FAIL**: Developer and tester roles are conflated, or prompt allows subjective test pass override.
