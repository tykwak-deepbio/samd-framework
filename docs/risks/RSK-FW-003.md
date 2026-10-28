# Risk Analysis: RSK-FW-003

> **Risk ID**: `RSK-FW-003`  
> **Risk Control Measure ID**: `RCM-FW-003`  
> **Title**: Stale Downstream Approvals Remaining Active Post-Upstream Modification  
> **Standard Reference**: ISO 14971:2019 Clause 5.4, ISO 13485:2016 Clause 7.3.9  
> **Target Requirement**: `FR-TOOL-004`, `FR-ORCH-003`, `FR-SKILL-003`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-005.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-004.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-TOOL-004.md`, `docs/tests/TC-FR-ORCH-003.md`  

---

## 1. Hazard, Sequence of Events & Hazardous Situation
- **Hazard**: Silent configuration drift and inconsistent V-Model state.
- **Sequence of Events**:
  1. A clinical requirement in `DHF-01` or software requirement in `DHF-04` is revised or added late in the lifecycle.
  2. Downstream architecture (`DHF-07`), detailed design (`DHF-08`), and test reports (`DHF-09`) retain their previously approved status without re-evaluation.
- **Hazardous Situation**: Inconsistencies between requirements and design/tests go unnoticed; previously verified code does not satisfy modified clinical needs.
- **Harm**: System deployed with undetected discrepancies, risking device recalls, regulatory audit sanctions, or incorrect diagnostic outputs. (Severity: S3 - Serious, Probability: P4 - High $\to$ **Initial Risk: High / Unacceptable**).

## 2. Risk Control Measure: RCM-FW-003
- **Control Measure Description**: The framework implements an automated **Cascading Downstream Invalidation Engine (`scripts/check_change_impact.py`)**.
  - Models the V-Model dependency graph:
    `DHF-00` $\to$ `01` $\to$ `02` $\to$ `03` $\to$ `04` $\to$ (`05B`/`05C`, `06`, `07`) $\to$ `08` $\to$ `09` $\to$ `10` $\to$ `11`.
  - When an upstream document changes against the approval baseline, automatically marks all transitive downstream documents as `INVALIDATED (APPROVAL REVOKED)`.
  - Exits with return code 2 to immediately block CI/CD pipeline progression until all invalidated stages are re-approved.
- **Control Type**: Inherent Software Design / Automated Dependency Traversal.

## 3. Residual Risk Evaluation
- **Residual Severity**: S3.
- **Residual Probability**: P1 (Algorithmic graph traversal ensures 100% of downstream dependencies are revoked).
- **Residual Risk Level**: **Low / Acceptable (ALARP satisfied)**.
- **Verification Evidence**: `VERIF-FW-003`, `VERIF-FW-025` via `TC-FR-ORCH-003.md`, `TC-FR-TOOL-002.md`.
## 4. Evaluation of New Hazards Arising from Risk Control Measures (ISO 14971:2019 Cl 7.3 & IEC 62304 Cl 7.2.2)
- **Potential New Hazards Introduced**:
  - Topological sorting recursion / cyclic graph traversal leading to infinite loop or stack overflow during downstream invalidation.
  - Over-invalidation cascading across unrelated phases, destroying valid verification records unnecessarily.
- **Secondary Risk Mitigations**:
  - Cycle detection using Tarjan's strongly connected components algorithm (`DDS-FW-004`) aborting traversal immediately if circular dependencies occur.
  - Strict phase boundary scoping limiting invalidation propagation strictly to downstream dependent artifacts.
  - Dry-run invalidation preview mode allowing impact assessment prior to physical artifact status revocation.
- **Residual Risk Conclusion**: No unacceptable secondary hazards introduced. Residual risk remains **Acceptable (ALARP satisfied)**.
