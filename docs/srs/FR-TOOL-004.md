# Software Requirement: FR-TOOL-004

> **Requirement ID**: `FR-TOOL-004`  
> **Title**: Change Impact Analysis & Downstream Invalidation Tool (`check_change_impact.py`)  
> **Category**: Automated Tooling (`[TOOL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 13485:2016 Clause 7.3.9 (Control of Design Changes), IEC 62304:2006 Clause 8 (Software Change Management)  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-TOOL-004.md`  

---

## 1. Description & Regulatory Rationale
Under ISO 13485 Clause 7.3.9 and IEC 62304 Clause 8, changes to design inputs or software items must be evaluated for their effect on downstream components, test records, and risk assessments before implementation. The framework shall provide a tool (`scripts/check_change_impact.py`) that analyzes modified files, determines affected downstream artifacts, and automatically marks their approval status as invalidated.

## 2. Detailed Functional Specifications
1. The tool shall analyze git diffs or file modification timestamps against baseline hashes recorded in the DHF Master Index.
2. If an upstream artifact (e.g. `DHF-01` or `DHF-04`) has been modified since its baseline approval:
   - Identify all downstream documents and modules in the dependency chain:
     * `DHF-01` (User Needs) modified ➔ Invalidate `DHF-04`, `05B`, `07`, `08`, `09`, `10`, `11`.
     * `DHF-04` (SRS) modified ➔ Invalidate `DHF-05B`, `07`, `08`, `09`, `10`, `11`.
     * `DHF-07` (Architecture) modified ➔ Invalidate `DHF-08`, `09`, `10`, `11`.
     * `DHF-08` (Detailed Design) modified ➔ Invalidate `src/`, `tests/`, `DHF-09`, `10`, `11`.
3. The tool shall print a formal Change Impact Analysis (CIA) report listing:
   - Initiating Change Request / Modified file.
   - List of all invalidated downstream artifacts requiring re-approval.
   - Required re-verification test cases (`TC-*`).
4. Exit code `0` when all artifacts are consistent with current baselines; exit code `2` when downstream invalidations are detected.

## 3. Inputs, Processing & Outputs
- **Inputs**: Target DHF directory, git commit range or baseline checksum table.
- **Processing**: Dependency traversal, state transition evaluation (`APPROVED` ➔ `INVALIDATED_BY_UPSTREAM`).
- **Outputs**: Change Impact Report, exit code indicating invalidation status.
