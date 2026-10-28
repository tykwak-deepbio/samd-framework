# Test Protocol: TC-FR-TOOL-004

> **Test Case ID**: `TC-FR-TOOL-004`  
> **Target Requirement**: `FR-TOOL-004` (Change Impact Analysis & Downstream Invalidation Tool)  
> **Test Level**: System / Automated Test Suite  
> **Verification Method**: Execution & State Invalidation Verification  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `scripts/check_change_impact.py` evaluates file change events, identifies all affected downstream artifacts in the V-model dependency tree, flags them as invalidated, and outputs a formal Change Impact Analysis report.

## 2. Preconditions
- `scripts/check_change_impact.py` is present and executable.
- Test fixture with approved baseline DHF documents.

## 3. Test Execution Steps
1. Run `python3 scripts/check_change_impact.py <approved_dhf_dir>`.
   - Verify exit code is `0` when no files have been modified since baseline.
2. Simulate a change in `DHF-04-Software-Requirements-Specification-SRS.md` by modifying a requirement string.
3. Run `python3 scripts/check_change_impact.py <test_dhf_dir>`.
   - Verify exit code is `2` (Downstream Invalidation Detected).
   - Verify stdout identifies `DHF-04` as the source change.
   - Verify stdout lists downstream invalidated documents: `DHF-07`, `DHF-08`, `DHF-09`, `DHF-10`, `DHF-11`.
   - Verify stdout lists required re-test protocols.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Baseline clean returns 0; upstream modification returns 2 with complete downstream invalidation manifest.
- **FAIL**: Tool fails to detect downstream dependencies or reports clean status despite modified upstream files.
