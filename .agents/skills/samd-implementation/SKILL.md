---
name: samd-implementation
description: Guides software implementation and unit verification adhering to medical software coding standards, static analysis, defensive programming, and IEC 62304 Clause 5.5 unit verification requirements. Use this skill when implementing production code or writing unit tests.
---

# SaMD Software Implementation & Unit Verification

This skill executes Phase 9 of the SaMD lifecycle, complying with **IEC 62304:2006/AMD1:2015 Clause 5.5 (Software unit implementation and verification)** and **ISO 13485:2016 Clause 7.3.4 (Design Outputs)**.

## Goal
Implement the software according to the Detailed Design Specification (`DDS-xxx`), maintain defensive coding practices, embed bidirectional traceability tags in source comments, and execute unit verification (`TC-UNIT-xxx`).

## Medical Coding Standards & Rules

1. **Traceability in Code**:
   - Every production function/class implementing a requirement or risk control MUST contain docstrings linking to its specification:
     ```python
     # Traces: REQ-SW-003, DDS-002, RCM-001
     def normalize_stain(tile_rgb: np.ndarray, target_od: np.ndarray) -> np.ndarray:
         ...
     ```
2. **Defensive Programming & Bounds Validation**:
   - Check all array shapes, pixel ranges, and non-null guarantees.
   - Guard against numerical instability: `np.clip()`, epsilon addition before $\log$, zero-division guards.
3. **Unit Verification Criteria (IEC 62304 Clause 5.5.3)**:
   - Proper event sequences, data type ranges, memory allocation limits.
   - Code coverage threshold: $\ge 90\%$ branch/statement coverage on safety-critical units (Class B/C).
   - All unit tests must execute deterministically with 100% pass rate.
4. **Static Analysis & Linting**:
   - Zero critical linter warnings (e.g. `flake8`, `mypy --strict`, `bandit` for security).

## Procedure
1. Implement software modules in `src/`.
2. Write unit tests in `tests/test_*.py`.
3. Run tests using `pytest` and verify coverage.
4. Document unit verification evidence (`VERIF-UNIT-xxx`).
