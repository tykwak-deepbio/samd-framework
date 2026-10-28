# Software Architecture: ARCH-FW-003

> **Component ID**: `ARCH-FW-003`  
> **Title**: 2-Tier HITL Gate Review Controller & V-Model Orchestration Engine  
> **Subsystem**: Lifecycle Orchestration Subsystem  
> **Safety Class**: Class B (IEC 62304 Clause 5.3)  
> **Allocated Requirements**: `FR-ORCH-001`, `FR-ORCH-002`, `FR-ORCH-003`, `FR-ORCH-004`, `FR-SKILL-003`  
> **Allocated Risk Controls**: `RCM-FW-001`, `RCM-FW-003`  
> **Detailed Design Units**: `docs/detailed_design/DDS-FW-002.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-ORCH-001.md`, `docs/tests/TC-FR-ORCH-002.md`, `docs/tests/TC-FR-ORCH-003.md`, `docs/tests/TC-FR-ORCH-004.md`  

---

## 1. Architectural Overview & Design Rationale
`ARCH-FW-003` serves as the gatekeeper of the medical software lifecycle. It prevents unreviewed or defective specifications from flowing downstream by enforcing a 2-Tier Human-in-the-Loop (HITL) gate review model. It coordinates transitions between the 12 V-model phases, requiring objective checklist completion and mandatory human approval at regulatory milestone gates.

## 2. Component Boundaries & Interfaces
```
                 +---------------------------------------------+
                 |       2-Tier Gate Review Controller         |
                 +---------------------------------------------+
                                        │
           ┌────────────────────────────┴───────────────────────────┐
           ▼                                                        ▼
+─────────────────────────────────────+  +─────────────────────────────────────+
|   Tier 1: Major Regulatory Gates    |  |  Tier 2: Milestone Technical Gates  |
| - Gate 1 (URD), Gate 3 (Strategy)   |  | - Gate 2 (SOTA), Gate 6 (Cybersec)  |
| - Gate 4 (SRS), Gate 5 (Risk)       |  | - Gate 7 (Architecture)             |
| - Gate 9 (V&V), Gate 10 (Release)   |  | - Gate 8 (Detailed Design)          |
| -> Unconditional Execution Halt     |  | -> Automated Checklist Verification |
| -> Explicit Human Sign-off Required |  | -> Technical Milestone Progression  |
+─────────────────────────────────────+  +─────────────────────────────────────+
```
- **Inbound Interface**: User approval tokens (`APPROVE GATE-x`), phase completion triggers from specialist agents.
- **Outbound Interface**: State advancement signal, phase execution authorization, or execution block with audit log.

## 3. Safety Segregation & Data Flows
- **Strict Monotonic Progression**: No phase $N+1$ may be entered unless Gate $N$ is in state `APPROVED`.
- **Audit Logging**: Every transition records timestamp, reviewer identity, and gate checklist verification evidence.

## 4. Technology Stack & Environmental Prerequisites
- Markdown workflow specifications (`workflows/00-v-model-lifecycle-workflow.md`), Antigravity conversation context.
