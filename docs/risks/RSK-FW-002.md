# Risk Analysis: RSK-FW-002

> **Risk ID**: `RSK-FW-002`  
> **Risk Control Measure ID**: `RCM-FW-002`  
> **Title**: Undetected Traceability Gaps & Orphan Requirements / Untested Features  
> **Standard Reference**: ISO 14971:2019 Clause 5.4, IEC 62304:2006 Clause 5.1.1  
> **Target Requirement**: `FR-TOOL-001`, `FR-DHF-001`, `FR-DHF-002`, `FR-DHF-003`, `FR-SKILL-014`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-004.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-003.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-TOOL-001.md`, `docs/tests/TC-FR-TOOL-002.md`, `docs/tests/TC-FR-TOOL-003.md`  

---

## 1. Hazard, Sequence of Events & Hazardous Situation
- **Hazard**: Ambiguous documentation linking or formatting drift in markdown tables.
- **Sequence of Events**:
  1. A software engineer or agent creates a new software requirement or risk mitigation without linking forward to a verification test case.
  2. A standard manual audit misses the orphan requirement due to voluminous documentation.
- **Hazardous Situation**: Safety-critical risk controls or clinical requirements enter production without objective verification testing.
- **Harm**: Medical software deployed with unverified safety-critical functions, leading to runtime failures during patient examination. (Severity: S4 - Critical, Probability: P3 - Medium $\to$ **Initial Risk: High / Unacceptable**).

## 2. Risk Control Measure: RCM-FW-002
- **Control Measure Description**: The framework provides an automated **Bidirectional Traceability Validator (`scripts/validate_traceability.py`)**.
  - Parses all markdown tables across `DHF-01` through `DHF-10`.
  - Performs bipartite graph connectivity evaluation across `USER-REQ` $\leftrightarrow$ `REQ-SW` $\leftrightarrow$ `RSK`/`RCM` $\leftrightarrow$ `ARCH`/`DDS` $\leftrightarrow$ `CODE` $\leftrightarrow$ `TC`.
  - Strictly returns Exit Code 1 (FAIL) and identifies exact line numbers upon detecting any unmapped user need or unverified software requirement.
- **Control Type**: Inherent Software Verification / Automated Boundary Check.

## 3. Residual Risk Evaluation
- **Residual Severity**: S4.
- **Residual Probability**: P1 (Automated deterministic validator blocks CI/CD and gate sign-off if any orphan exists).
- **Residual Risk Level**: **Low / Acceptable (ALARP satisfied)**.
- **Verification Evidence**: `VERIF-FW-024` via `TC-FR-TOOL-001.md`.
## 4. Evaluation of New Hazards Arising from Risk Control Measures (ISO 14971:2019 Cl 7.3 & IEC 62304 Cl 7.2.2)
- **Potential New Hazards Introduced**:
  - Validation engine false positives blocking urgent bug fixes or emergency hotfix deployments.
  - Parser crash on malformed markdown leading to unhandled runtime exception and pipeline termination.
- **Secondary Risk Mitigations**:
  - Defensive regex compilation and whitespace-tolerant markdown parsing implemented in `DDS-FW-003`.
  - Detailed diagnostic reporting providing line numbers and specific missing tag identifiers to enable immediate developer resolution.
  - Automated CI regression test suite ensuring validator stability across all valid tag schemas.
- **Residual Risk Conclusion**: No unacceptable secondary hazards introduced. Residual risk remains **Acceptable (ALARP satisfied)**.
