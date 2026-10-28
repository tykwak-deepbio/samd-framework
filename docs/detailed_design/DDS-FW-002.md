# Detailed Design Specification: DDS-FW-002

> **Unit Design ID**: `DDS-FW-002`  
> **Title**: 2-Tier Gate State Machine & Exit Checklist Transition Unit  
> **Parent Architecture**: `docs/architecture/ARCH-FW-003.md`  
> **Safety Class**: Class B (IEC 62304 Clause 5.4)  
> **Allocated Risk Controls**: `RCM-FW-001`, `RCM-FW-003`  
> **Target Requirement**: `FR-ORCH-001`, `FR-ORCH-002`, `FR-ORCH-003`, `FR-ORCH-004`, `FR-SKILL-003`  
> **Implementation Target**: `.agents/skills/samd-orchestrator/SKILL.md`, `workflows/00-v-model-lifecycle-workflow.md`, `scripts/record_audit_event.py`  
> **Verification Test Protocol**: `docs/tests/TC-FR-ORCH-001.md`, `docs/tests/TC-FR-ORCH-002.md`, `docs/tests/TC-FR-ORCH-003.md`, `docs/tests/TC-FR-ORCH-004.md`, `docs/tests/TC-FR-SKILL-003.md`  

---

## 1. Detailed Unit Description & Rationale
`DDS-FW-002` specifies the discrete state transition machine governing the 11 lifecycle phases and 10 review gates. It enforces the distinction between Tier 1 Major Gates (requiring human interaction) and Tier 2 Technical Gates (evaluating technical invariants).

## 2. Data Structures & State Machine Model
```
State: Enum(PHASE_1_URD, GATE_1_REVIEW, PHASE_2_SOTA, GATE_2_REVIEW, ..., PHASE_11_DHF_AUDIT, GATE_10_RELEASE, COMPLETED)
GateType: Enum(TIER_1_MAJOR_REGULATORY, TIER_2_TECHNICAL_MILESTONE)
GateStatus: Enum(PENDING_REVIEW, APPROVED, INVALIDATED)
```

## 3. Transition Logic & Algorithmic Rules
```
Gate Transition Table:
+--------+--------------------------+------------------------------+------------------------------------+
| Gate   | Target Phase Deliverable | Gate Type                    | Exit Requirement to Advance        |
+--------+--------------------------+------------------------------+------------------------------------+
| Gate 1 | DHF-01 (URD)             | TIER_1_MAJOR_REGULATORY      | Explicit Human Sign-off Recorded   |
| Gate 2 | DHF-02 (SOTA)            | TIER_2_TECHNICAL_MILESTONE   | Clinical SOTA Matrix Complete      |
| Gate 3 | DHF-03 (Strategy)        | TIER_1_MAJOR_REGULATORY      | Target Jurisdiction Profile Signed |
| Gate 4 | DHF-04 (SRS)             | TIER_1_MAJOR_REGULATORY      | Human SRS Review & Approval        |
| Gate 5 | DHF-05A/B/C (Risk)       | TIER_1_MAJOR_REGULATORY      | ALARP / Residual Risk Acceptance   |
| Gate 6 | DHF-06 (Cybersecurity)   | TIER_2_TECHNICAL_MILESTONE   | Threat Model & SBOM Complete       |
| Gate 7 | DHF-07 (Architecture)    | TIER_2_TECHNICAL_MILESTONE   | Safety Segregation Validated       |
| Gate 8 | DHF-08 (Detailed Design) | TIER_2_TECHNICAL_MILESTONE   | Algorithm & Unit Signatures Frozen |
| Gate 9 | DHF-09 (V&V Testing)     | TIER_1_MAJOR_REGULATORY      | Independent V&V Report Signed      |
| Gate 10| DHF-10/11 (Master DHF)   | TIER_1_MAJOR_REGULATORY      | 100% RTM & Audit Report Approved   |
+--------+--------------------------+------------------------------+------------------------------------+

Transition Guard Rule:
def transition_to_next_phase(current_gate: Gate) -> bool:
    if current_gate.type == TIER_1_MAJOR_REGULATORY:
        if not user_explicit_approval_received():
            raise HaltExecutionError("HALT: Tier 1 Major Gate requires explicit human sign-off")
    if not current_gate.checklist_items_all_checked():
        raise IncompleteGateError("HALT: Gate exit criteria not satisfied")
    current_gate.status = APPROVED
    return True
```

## 4. Error Handling & Boundary Conditions
- **Missing Human Sign-off at Tier 1**: Execution halts immediately; autonomous bypass is rejected.
- **Unchecked Criteria**: Emits warning listing missing checklist items and prevents phase increment.

## 5. Safety Invariants & Risk Control Implementation (RCM-FW-001, RCM-FW-003)
- **Safety Invariant 1 (RCM-FW-001 - 2-Tier HITL Gate Interlock)**: Transitions across Tier 1 gates (Gates 1, 3, 4, 5, 9, 10) are physically blocked unless an external, authenticated human approval token is provided with ISO 8601 timestamp. Autonomous self-transitions by agents are programmatically rejected.
- **Safety Invariant 2 (RCM-FW-003 - Parallel Risk Synchronization Interlock)**: When an upstream requirement or design artifact changes, the state engine marks dependent risk controls as invalidated, preventing advance until parallel risk re-assessment is confirmed.
- **Safety Invariant 3 (RCM-FW-001 / FR-ORCH-004 - Atomic Shared State Interlock)**: Any modification to `project_state.json` or gate approval transitions must acquire an exclusive OS-level advisory file lock (`fcntl.flock`). Concurrent agent writes are serialized to eliminate race conditions and split-brain lifecycle states.
