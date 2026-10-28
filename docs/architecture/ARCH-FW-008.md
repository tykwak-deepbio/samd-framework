# Software Architecture: ARCH-FW-008

> **Component ID**: `ARCH-FW-008`  
> **Title**: AI/ML Data Governance & MLOps Drift Monitoring Subsystem  
> **Subsystem**: AI/ML Engineering & Validation Subsystem  
> **Safety Class**: Class C (IEC 62304 Clause 5.3)  
> **Allocated Requirements**: `FR-AI-001`, `FR-AI-002`, `FR-AI-003`, `FR-AI-004`, `FR-AI-005`, `FR-AI-006`, `FR-AI-007`, `FR-CLIN-001`  
> **Allocated Risk Controls**: `RCM-FW-008`, `RCM-FW-010`  
> **Detailed Design Units**: `docs/detailed_design/DDS-FW-008.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-AI-001.md` ~ `TC-FR-AI-007.md`, `docs/tests/TC-FR-CLIN-001.md`  

---

## 1. Architectural Overview & Design Rationale
`ARCH-FW-008` governs the lifecycle of AI/ML data assets and operational performance monitoring. It provides architectural mechanisms for tracking clinical dataset provenance, guaranteeing zero patient-level cross-contamination, performing demographic bias auditing, and monitoring live inference streams for covariate and concept drift under FDA PCCP guidelines.

## 2. Component Boundaries & Interfaces
```
+-------------------------------------------------------------------------+
|                  AI/ML Data & Validation Subsystem                      |
+-------------------------------------------------------------------------+
                                     │
           ┌─────────────────────────┼────────────────────────┐
           ▼                         ▼                        ▼
+──────────────────────+  +──────────────────────+  +──────────────────────+
|  Provenance & Split  |  |  Subgroup & Robust   |  |   Statistical Drift  |
|  - IRB & De-id Check |  |  - Stratified Metric |  |   - KS-Test / PSI    |
|  - Patient-ID Isolator| |  - Multi-center Test |  |   - PCCP Retrain     |
|  - Test Hash-Lock    |  |  - Vendor Generalize |  |   - Fail-safe Bypass |
+──────────────────────+  +──────────────────────+  +──────────────────────+
```
- **Inbound Interface**: Raw dataset manifests, patient metadata, production inference telemetry.
- **Outbound Interface**: Partitioned manifests, leakage audit certificates, drift alerts, PCCP triggers.

## 3. Safety Segregation & Data Flows
- **Test Set Isolation**: The test set is physically isolated and locked with SHA-256 digests; model training routines are blocked from accessing test partition paths.
- **Fail-Safe Fallback**: If $\text{PSI} \ge 0.25$, an automated bypass signal is routed to the viewer UI, switching to raw mode.

## 4. Technology Stack & Environmental Prerequisites
- Python 3.8+, Scipy/Numpy for statistical drift calculations.
