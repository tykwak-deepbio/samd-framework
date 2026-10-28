# Test Protocol: TC-FR-ORCH-004

> **Test Case ID**: `TC-FR-ORCH-004`  
> **Target Requirement**: `FR-ORCH-004` (Multi-Agent Parallel Concurrency Control & Atomic Shared State Synchronization)  
> **Test Level**: System / Concurrency & Stress Verification  
> **Verification Method**: Concurrent Process Execution & HMAC Hash Chain Audit  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `scripts/record_audit_event.py` and shared state operations enforce atomic file locking (`.dhf.lock`), preventing race conditions and preserving 100% HMAC-SHA256 hash chain validity during concurrent subagent execution.

## 2. Preconditions
- `scripts/record_audit_event.py` is executable.
- Python `subprocess` and `concurrent.futures` / multi-threading test harness.

## 3. Test Execution Steps
1. Initialize a clean test audit log.
2. Spawn 10 concurrent processes/threads simultaneously attempting to record audit events into the same log file.
3. Await completion of all concurrent workers.
4. Verify exit codes of all 10 processes are `0` (all acquired locks within timeout).
5. Run `python3 scripts/record_audit_event.py --verify --log <test_log>`.
   - Verify exit code is `0` (`[PASS] Full audit chain verified`).
   - Verify exactly 10 new entries are present with strictly unbroken HMAC signatures.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: All 10 concurrent writes succeed without collision; full audit chain passes cryptographic verification.
- **FAIL**: Any race condition occurs, corrupted JSON entries are written, or HMAC verification fails.
