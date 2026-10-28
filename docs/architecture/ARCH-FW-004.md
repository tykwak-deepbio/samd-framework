# Software Architecture: ARCH-FW-004

> **Component ID**: `ARCH-FW-004`  
> **Title**: Bidirectional Traceability Graph & Invariant Validator  
> **Subsystem**: Regulatory Compliance Subsystem  
> **Safety Class**: Class B (IEC 62304 Clause 5.3)  
> **Allocated Requirements**: `FR-TOOL-001`, `FR-TOOL-003`, `FR-TOOL-005`, `FR-DHF-003`, `FR-SKILL-014`, `FR-HOOK-001`  
> **Allocated Risk Controls**: `RCM-FW-002`, `RCM-FW-005`, `RCM-FW-015`  
> **Detailed Design Units**: `docs/detailed_design/DDS-FW-003.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-TOOL-001.md`, `docs/tests/TC-FR-TOOL-002.md`, `docs/tests/TC-FR-TOOL-003.md`, `docs/tests/TC-FR-TOOL-005.md`, `docs/tests/TC-FR-HOOK-001.md`  

---

## 1. Architectural Overview & Design Rationale
`ARCH-FW-004` implements deterministic verification of the medical device bidirectional traceability matrix and real-time regulatory linting hooks (`FR-HOOK-001`, `RCM-FW-015`). In regulated SaMD development, an orphan user need or untested software requirement is a critical non-conformance. This component scans markdown tables across all DHF documents, constructs a directed bipartite traceability graph, verifies 100% PHA screening completeness, and mathematically verifies total connectivity across all requirement layers.

## 2. Component Boundaries & Interfaces
```
+-------------------------------------------------------------------------+
|                  Markdown DHF File System (DHF-01 ~ DHF-10)             |
+-------------------------------------------------------------------------+
                                     │
                                     ▼
+-------------------------------------------------------------------------+
|               scripts/validate_traceability.py Engine                   |
| 1. Table Parser & ID Lexer                                              |
| 2. Graph Invariant Evaluator (USER-REQ <-> REQ-SW <-> TC / RSK / ARCH)  |
| 3. Orphan & Unverified Feature Detector                                 |
+-------------------------------------------------------------------------+
                                     │
           ┌─────────────────────────┴────────────────────────┐
           ▼                                                  ▼
+─────────────────────────────────────+   +───────────────────────────────+
|      Zero Orphans -> Exit Code 0    |   |    Orphan Found -> Exit Code 1|
|    "REGULATORY AUDIT VERDICT: PASS" |   |     Line-by-line Error Report |
+─────────────────────────────────────+   +───────────────────────────────+
```
- **Inbound Interface**: Command-line path to project `dhf/` directory.
- **Outbound Interface**: Process exit code (0 for PASS, 1 for FAIL), console summary table, and detailed error logs.

## 3. Safety Segregation & Data Flows
- **Zero External Dependencies**: Implemented strictly with standard library `os`, `sys`, `re` to guarantee execution in air-gapped enclaves.
- **Read-Only Operation**: Operates purely non-destructively on DHF markdown files.

## 4. Technology Stack & Environmental Prerequisites
- Python 3.8+ Standard Library (`os`, `sys`, `re`).
