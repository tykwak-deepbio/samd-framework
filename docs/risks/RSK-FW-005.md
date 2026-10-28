# Risk Analysis: RSK-FW-005

> **Risk ID**: `RSK-FW-005`  
> **Risk Control Measure ID**: `RCM-FW-005`  
> **Title**: Supply Chain Vulnerability or Breakage in Regulated Air-Gapped Environments  
> **Standard Reference**: ISO 14971:2019 Clause 5.4, ISO 27001/27799, IEC 81001-5-1 Clause 5.3  
> **Target Requirement**: `FR-TOOL-002`, `FR-TOOL-003`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-004.md`, `docs/architecture/ARCH-FW-005.md`, `docs/architecture/ARCH-FW-006.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-003.md`, `docs/detailed_design/DDS-FW-004.md`, `docs/detailed_design/DDS-FW-005.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-TOOL-003.md`  

---

## 1. Hazard, Sequence of Events & Hazardous Situation
- **Hazard**: External package dependency failure, unverified third-party libraries, or network outage in hospital/regulated air-gapped enclaves.
- **Sequence of Events**:
  1. A validation or audit script relies on external pip packages (e.g. `pandas`, `requests`, `networkx`).
  2. The medical software development environment operates in an isolated, air-gapped regulatory enclave without public internet access.
  3. The audit script crashes or fails to execute during a critical audit inspection.
- **Hazardous Situation**: Inability to verify DHF integrity or execute validation controls in regulated validation environments.
- **Harm**: Delayed regulatory audit submission or compromised verification audit trail. (Severity: S2 - Minor, Probability: P4 - High $\to$ **Initial Risk: Medium / ALARP**).

## 2. Risk Control Measure: RCM-FW-005
- **Control Measure Description**: The framework establishes a **Zero External Dependency Standard Library Lock**.
  - All validation and audit automation scripts (`validate_traceability.py`, `generate_dhf_index.py`, `check_change_impact.py`, `test_framework.py`) must execute purely on Python 3 standard library modules (`os`, `sys`, `re`, `hashlib`, `json`, `subprocess`, `ast`, `unittest`).
  - An automated AST-based import scanner in `scripts/test_framework.py` checks all scripts to guarantee zero non-standard imports.
- **Control Type**: Inherent Software Architecture / Standard Library Conformance.

## 3. Residual Risk Evaluation
- **Residual Severity**: S1 - Negligible.
- **Residual Probability**: P1 (Standard library guaranteed to be present across all Python 3 installations).
- **Residual Risk Level**: **Negligible / Acceptable**.
- **Verification Evidence**: `VERIF-FW-026` via `TC-FR-TOOL-003.md`.
## 4. Evaluation of New Hazards Arising from Risk Control Measures (ISO 14971:2019 Cl 7.3 & IEC 62304 Cl 7.2.2)
- **Potential New Hazards Introduced**:
  - Performance bottlenecks and I/O latency from running zero-dependency native Python cryptographic indexers on very large WSI pathology files.
  - Hash collision or file-lock contention during concurrent multi-agent read/write access.
- **Secondary Risk Mitigations**:
  - Chunked 64KB block hashing (`DDS-FW-005`) maintaining low memory footprint regardless of artifact file size.
  - Strict zero-external-dependency standard utilizing Python standard library (`hashlib`, `os`, `sys`), eliminating external SOUP supply chain risk.
  - Read-shared file locks with atomic temporary file swapping for index generation.
- **Residual Risk Conclusion**: No unacceptable secondary hazards introduced. Residual risk remains **Acceptable (ALARP satisfied)**.
