---
name: samd-vnv-testing
description: Generates and executes independent software verification protocols, integration tests, system tests, and AI/ML clinical performance validations under IEC 62304 Clause 5.6/5.7 and IEC 62366-1. Use this skill when authoring test protocols, executing test suites, or drafting DHF-09.
---

# SaMD Independent Verification & Validation (V&V) Testing

This skill executes Phase 10 of the SaMD lifecycle, complying with **IEC 62304:2006/AMD1:2015 Clause 5.6 (Software integration and integration testing)**, **Clause 5.7 (Software system testing)**, **ISO 13485 Clause 7.3.6 (Design Verification) / 7.3.7 (Design Validation)**, and **IEC 62366-1:2015**.

## Goal
Perform independent verification and validation against all software requirements (`REQ-SW-*`) and risk control measures (`RCM-*`), validate AI/ML clinical performance metrics, and author **`DHF-09-Software-Verification-and-Validation-Report.md`**.

## Testing Levels & Protocols

```
[System Testing (TC-SYS-*)]       ◄── Evaluates against ──► [Software Requirements (REQ-SW-*)]
            ▲
[Integration Testing (TC-INT-*)]  ◄── Evaluates against ──► [Architecture & Interfaces (ARCH-*)]
            ▲
[AI Performance Valid. (TC-AI-*)] ◄── Evaluates against ──► [Clinical SOTA & Baselines (CLIN-*)]
            ▲
[Unit Testing (TC-UNIT-*)]        ◄── Evaluates against ──► [Detailed Unit Design (DDS-*)]
```

### 1. Integration & System Test Protocols (`TC-SYS-xxx`, `TC-INT-xxx`)
- Objective, reproducible test scripts with step-by-step procedures.
- Precise pass/fail criteria (no qualitative or subjective judgments).
- Negative testing: Corrupt files, network drops, out-of-memory triggers, unexpected file extensions.

### 2. AI/ML Clinical Performance Validation (`TC-AI-xxx`)
- Execute inference on locked, independent test set (never seen during training/validation).
- Compute and verify against acceptance criteria:
  - Dice Similarity Coefficient (DSC) $\ge 0.92$
  - Intersection-over-Union (IoU) $\ge 0.85$
  - Sensitivity / Recall $\ge 95\%$
  - Specificity $\ge 90\%$
  - Delta E color error $\le 3.5$
- Sub-group performance breakdown across multi-vendor scanners (e.g. Aperio, Hamamatsu, Leica, 3DHISTECH).

### 3. Usability Summative Evaluation (`TC-USE-xxx`)
- Validate absence of critical use errors:
  - Pathologist confusion between raw vs. normalized modes.
  - Failure to observe low-confidence warning indicators.

## Procedure
1. Create Test Protocol defining all test cases (`TC-xxx`).
2. Execute automated test suites and capture terminal logs/results.
3. Record discrepancies and bug tickets (if any) with root cause analysis.
4. Populate `templates/DHF-09-Software-Verification-and-Validation-Report.md`.
