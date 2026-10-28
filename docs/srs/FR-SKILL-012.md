# Software Requirement: FR-SKILL-012

> **Requirement ID**: `FR-SKILL-012`  
> **Title**: Skill Specification - `samd-implementation` (Medical Coding Standards & Unit Verification)  
> **Category**: Antigravity Skills Ecosystem (`[SKILL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006+AMD1:2015 Clause 5.5  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-SKILL-012.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-001.md`, `docs/architecture/ARCH-FW-004.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-003.md`  

---

## 1. Description & Technical Rationale
The `samd-implementation` skill shall enforce medical software coding standards (MISRA / PEP 8 / Defensive Programming), conduct static code analysis, and implement software units alongside unit verification tests strictly conforming to IEC 62304 Clause 5.5.

## 2. Detailed Functional Specifications
1. **Defensive Coding Standard Enforcement**:
   - Zero unhandled exceptions or implicit null pointer dereferences.
   - Comprehensive input validation and boundary checking on all external parameters.
   - Strict typing and docstrings referencing target unit design `DDS-xxx`.
2. **Clause 5.5 Unit Verification**:
   - For every software unit, require an automated unit test suite (`tests/test_*.py`).
   - Verify proper execution against boundaries, nominal conditions, and error/fault injection conditions.
   - Prohibit premature deployment without passing unit verification records.
3. **No Hardcoded Secrets Invariant**: Systematically prohibit embedded credentials, API keys, or private certificates in source files.

## 3. Inputs, Processing & Outputs
- **Inputs**: `DHF-08` (Detailed Design), unit test specifications.
- **Processing**: Source code implementation, static analysis, unit test execution and assertion evaluation.
- **Outputs**: Verified production source code modules under `src/` and unit test suites under `tests/`.
