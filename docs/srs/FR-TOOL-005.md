# Software Requirement: FR-TOOL-005

> **Requirement ID**: `FR-TOOL-005`  
> **Title**: Computerized Software Tool Validation (CSV) & Framework Tool Qualification  
> **Category**: Software Quality Assurance & Tool Qualification (`[TOOL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 13485:2016 Clause 7.5.6 (Validation of Software for Production and Service Provision), FDA General Principles of Software Validation (2002), GAMP 5 Second Edition (Category 5 - Custom Automation Tooling)  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-TOOL-005.md`  

---

## 1. Description & Regulatory Rationale
Under ISO 13485:2016 Clause 7.5.6 and FDA software validation guidance, computer software tools used in the design, development, verification, or automated generation of medical device software must be formally qualified and validated prior to use. When multi-agent systems and automated Python scripts generate, modify, and audit the Design History File (DHF), regulatory auditors require documented objective evidence proving that the toolchain reliably performs its intended functions without silent corruption or undetected non-conformities. The framework shall provide automated self-validation protocols, tool qualification baselines, and execution records (`scripts/test_framework.py`) satisfying GAMP 5 Category 5 validation requirements.

## 2. Detailed Functional Specifications
1. **Automated Tool Qualification (TQ) Protocol**:
   - The framework shall implement an automated tool qualification test harness (`scripts/test_framework.py`) verifying all development and verification tools:
     * `validate_traceability.py`: Positive validation (100% compliant DHF) and negative validation (rejection of orphan requirements, unlinked test cases).
     * `record_audit_event.py`: Cryptographic WORM integrity, tamper detection, and key permission enforcement.
     * `hook_pre_write_guard.py`: Fail-closed security interlocks and write restriction enforcement.
     * `check_change_impact.py`: Transitive dependency invalidation and cyclic reference prevention.
     * `validate_ai_dataset.py`: Patient leakage detection, PSI calculation, and Kappa agreement validation.
     * `verify_grounding.py`: Prompt injection pattern blocking, citation format validation, and temperature clamping.
     * `manage_anomalies.py`: Critical defect triage and gate clearance release blocking.
2. **Tool Qualification Evidence Generation**:
   - Running `scripts/test_framework.py` shall execute all qualification test cases (TS-*) and produce an audit-verifiable execution log with zero failures, exit code 0, timestamps, and environment hashes.
3. **Change Control & Re-Validation Protocol**:
   - Whenever any script under `scripts/` or rule under `AGENTS.md` is modified, the framework shall mandate automated regression re-execution and record the resulting qualification status in the DHF Master Index.

## 3. Inputs, Processing & Outputs
- **Inputs**: Framework tools under `scripts/`, test specifications in `docs/tests/`.
- **Processing**: Automated unit, functional, and negative boundary execution across all Python tools.
- **Outputs**: Tool Qualification Test Report, automated regression logs, PASS/FAIL status.
