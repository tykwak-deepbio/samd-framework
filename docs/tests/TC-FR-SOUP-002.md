# Test Protocol: TC-FR-SOUP-002

> **Test Case ID**: `TC-FR-SOUP-002`  
> **Target Requirement**: `FR-SOUP-002` (Third-Party Cloud Foundation Model & External LLM Provider Qualification)  
> **Test Level**: System / Supplier & Interface Verification  
> **Verification Method**: Configuration Inspection & Network Disconnection Simulation  
> **Status**: Approved  

---

## 1. Test Objective
Verify that the framework enforces supplier qualification, model version pinning, PHI zero-retention guarantees, and offline graceful degradation fail-safe handling for cloud foundation models.

## 2. Preconditions
- Cloud foundation model configuration files and SOUP registry (`DHF-06`).
- Test harness capable of simulating API network timeout/disconnection.

## 3. Test Execution Steps
1. Inspect SOUP configuration in `DHF-06` for cloud LLM providers:
   - Verify signed BAA/DPA reference and PHI non-retention policy.
   - Verify model version string is explicitly pinned to an immutable snapshot (not `latest`).
2. Simulate external API network failure / timeout (HTTP 503 / connection drop).
3. Verify that system executes graceful degradation:
   - System does not crash or corrupt active patient session.
   - System displays non-modal warning notification.
   - Core manual viewing functionality remains 100% available without deadlock.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Model version is pinned; BAA records verified; network loss triggers graceful degradation without crash.
- **FAIL**: Unpinned model tags detected (`latest`) or network timeout leads to crash or unhandled exception.
