# Software Requirement: FR-TOOL-001

> **Requirement ID**: `FR-TOOL-001`  
> **Title**: Automated Bidirectional Traceability & Orphan Checker (`validate_traceability.py`)  
> **Category**: Automated Tooling (`[TOOL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006 Clause 5.1.1, ISO 13485:2016 Clause 7.3.7  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-TOOL-001.md`  

---

## 1. Description & Regulatory Rationale
The framework shall provide an automated command-line tool (`scripts/validate_traceability.py`) to systematically parse all markdown documents in the project DHF, reconstruct the bidirectional traceability matrix, verify 100% link coverage, and fail immediately if any orphan or unlinked items exist.

## 2. Detailed Functional Specifications
1. The tool shall parse the RTM table in `DHF-10-Traceability-Matrix-RTM.md` and extract all traceability relations.
2. The tool shall verify the following invariants:
   - **User Needs Forward**: Every `USER-REQ-xxx` maps to at least one `REQ-SW-xxx`.
   - **Software Requirements Forward**: Every `REQ-SW-xxx` maps to `ARCH-xxx` or `DDS-xxx`, source code, and at least one `TC-xxx`.
   - **Risk Control Verification**: Every unacceptable hazard (`RSK-xxx`) maps to an `RCM-xxx`, which maps to a verified `REQ-SW-xxx` and passing test case.
   - **Orphan Item Rejection**: If any `USER-REQ-*` is defined in `DHF-01` but not mapped, or if any `REQ-SW-*` lacks a test case, the tool shall flag an error.
3. **Execution Exit Codes**:
   - Exit code `0`: All traceability invariants satisfied (100% coverage, 0 orphans).
   - Exit code `1`: Broken links or orphan items detected, accompanied by exact error messages.

## 3. Inputs, Processing & Outputs
- **Inputs**: Path to DHF directory (e.g. `dhf/`).
- **Processing**: Table parsing, entity extraction, bidirectional link graph validation.
- **Outputs**: Terminal summary table, exit code (0 or 1).
