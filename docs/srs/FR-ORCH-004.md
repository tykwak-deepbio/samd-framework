# Software Requirement: FR-ORCH-004

> **Requirement ID**: `FR-ORCH-004`  
> **Title**: Multi-Agent Parallel Concurrency Control & Atomic Shared State Synchronization  
> **Category**: Multi-Agent Orchestration & Concurrency (`[ORCH]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006 Clause 5.1.2 (Software Development Plan & Shared Resources), ISO 13485:2016 Clause 4.2.5 (Control of Records)  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-ORCH-004.md`  

---

## 1. Description & Regulatory Rationale
Under IEC 62304 Clause 5.1.2 and ISO 13485 Clause 4.2.5, when multiple autonomous software units or subagents execute concurrently in a shared workspace (`Workspace: "inherit"`), shared mutable resources must be guarded against race conditions, dirty reads, and lost updates. Specifically, when parallel agents simultaneously record audit events (`.audit_trail.jsonl`), update gate statuses (`project_state.json`), or modify the traceability matrix (`FRAMEWORK_RTM.md`), concurrent writes without atomic mutual exclusion cause HMAC hash chain corruption and broken state. The framework shall provide an atomic, cross-platform file locking mechanism (`.dhf.lock`) with timeout controls ensuring serialized, ACID-compliant writes across all concurrent agents.

## 2. Detailed Functional Specifications
1. **Atomic File Locking Protocol (`.dhf.lock`)**:
   - Every agent or tool attempting to write to shared state files (`templates/project_state.json`, `.audit_trail.jsonl`, `docs/traceability/FRAMEWORK_RTM.md`) must acquire an exclusive advisory file lock (`fcntl.flock` on POSIX / lockfile fallback).
   - If the lock is held by another concurrent subagent:
     * Wait with exponential backoff and jitter up to a configurable timeout (default: 10.0 seconds).
     * If timeout expires without lock acquisition, fail closed with exit code 1 and record a concurrency lock timeout event.
2. **Hash Chain Serialization Invariant**:
   - In `scripts/record_audit_event.py`, atomic locking must encompass:
     * Reading the latest record's HMAC signature.
     * Computing the new entry's chained HMAC-SHA256 signature.
     * Appending the new JSON-Lines entry.
     * Releasing the lock.
   - This guarantees strictly linear, tamper-evident hash chaining regardless of subagent concurrency.
3. **Subagent Hibernation & Resume on HITL Gate Blocking**:
   - When an autonomous subagent reaches a gate requiring Human-in-the-Loop approval (`FR-ORCH-002`):
     * The subagent shall serialize its pending task state into `templates/project_state.json` under status `AWAITING_HUMAN_SIGN_OFF`.
     * The subagent terminates gracefully with a clean exit status, avoiding unmonitored idle token burn.
     * Upon user HMAC approval (`APPROVE`), the orchestrator resumes the downstream agent with the restored state payload.

## 3. Inputs, Processing & Outputs
- **Inputs**: Shared state files, concurrent subagent write requests.
- **Processing**: Atomic mutex acquisition, serialized write execution, automatic lock release in `finally` blocks.
- **Outputs**: Serialized audit log entries, race-condition-free `project_state.json`.
