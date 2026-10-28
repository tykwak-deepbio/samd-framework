# Test Protocol: TC-FR-AGENT-003

> **Test Case ID**: `TC-FR-AGENT-003`  
> **Target Requirement**: `FR-AGENT-003` (Subagent RBAC & Read-Only Sandbox Isolation)  
> **Test Level**: Architecture & Security Verification  
> **Verification Method**: Automated Static Inspection (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `FR-AGENT-003` defines role-based access control (RBAC) permission profiles for subagents, revoking write permissions on `src/` for `vnv-test-engineer-agent` and `dhf-lead-auditor-agent`.

## 2. Preconditions
- `docs/srs/FR-AGENT-003.md` exists.

## 3. Test Execution Steps
1. Parse `docs/srs/FR-AGENT-003.md`.
2. Check agent permission matrix (`software-developer-agent` vs `vnv-test-engineer-agent` vs `dhf-lead-auditor-agent`).
3. Check sandbox enforcement mechanism (tool filtering, read-only file mounts).
4. Verify violation handling and process abort rules.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Role-based permission matrix, read-only isolation rules, and violation aborts are specified.
- **FAIL**: Missing read-only constraints for verification agents or omitting permission matrices.
