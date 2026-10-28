# Independent Verification & Validation (V&V) Workflow (Phase 10)

> **Framework Guide**: `WF-04-VNV-TESTING`  
> **Key Agent**: `vnv-test-engineer-agent`  
> **Applicable Standards**: IEC 62304 Clause 5.6 & 5.7, ISO 13485 Clause 7.3.6 & 7.3.7, IEC 62366-1  

---

## 1. Principle of Independent Verification
Under **IEC 62304 Clause 5.6 & 5.7** and **ISO 13485 Clause 7.3.6**, software verification for Class B and Class C software must be performed with appropriate organizational and technical independence:
- The `vnv-test-engineer-agent` operates independently from the software developer.
- All test protocols must be pre-specified with objective, quantifiable pass/fail criteria prior to test execution.

---

## 2. Multi-Level Testing Strategy

```
+─────────────────────────────────────────────────────────────────────────────+
| System Verification Testing (TC-SYS-xxx)                                    |
| - Verifies all REQ-SW-xxx against functional, performance, & safety criteria |
+─────────────────────────────────────────────────────────────────────────────+
                                       ▲
+─────────────────────────────────────────────────────────────────────────────+
| Integration Testing (TC-INT-xxx)                                            |
| - Verifies subsystem interfaces and data flow across ARCH-xxx components    |
+─────────────────────────────────────────────────────────────────────────────+
                                       ▲
+─────────────────────────────────────────────────────────────────────────────+
| AI/ML Clinical Performance Validation (TC-AI-xxx)                           |
| - Validates model accuracy, sensitivity, specificity, & Dice on test cohorts|
+─────────────────────────────────────────────────────────────────────────────+
                                       ▲
+─────────────────────────────────────────────────────────────────────────────+
| Usability Summative Testing (TC-USE-xxx)                                    |
| - Verifies absence of critical use errors under IEC 62366-1                |
+─────────────────────────────────────────────────────────────────────────────+
```

---

## 3. Test Execution & Reporting Steps

1. **Protocol Authoring**:
   - Establish formal Test Protocols assigning unique `TC-xxx` identifiers.
   - Specify preconditions, test inputs, execution steps, expected outputs, and acceptance criteria.
2. **Automated Test Execution**:
   - Run integration and system test suites against built software artifacts.
   - Run AI performance evaluation on locked, independent multi-scanner test datasets.
3. **Capture Objective Verification Evidence**:
   - Generate execution records with timestamp and output metrics (`VERIF-xxx`).
   - If actual output $\ne$ expected criteria, record a formal Anomaly with severity classification.
4. **Compile V&V Report**:
   - Tabulate pass/fail metrics across all test levels.
   - Confirm 100% test pass rate with zero unresolved high-severity anomalies.
   - Output: `dhf/DHF-09-Software-Verification-and-Validation-Report.md`.
