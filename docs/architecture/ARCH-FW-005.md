# Software Architecture: ARCH-FW-005

> **Component ID**: `ARCH-FW-005`  
> **Title**: Cascading Downstream Invalidation & Dependency Traversal Engine  
> **Subsystem**: Configuration & Change Management Subsystem  
> **Safety Class**: Class B (IEC 62304 Clause 5.3)  
> **Allocated Requirements**: `FR-TOOL-004`, `FR-TOOL-003`, `FR-ORCH-003`, `FR-INT-001`  
> **Allocated Risk Controls**: `RCM-FW-003`, `RCM-FW-005`  
> **Detailed Design Units**: `docs/detailed_design/DDS-FW-004.md`, `docs/detailed_design/DDS-FW-005.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-TOOL-004.md`, `docs/tests/TC-FR-INT-001.md`  

---

## 1. Architectural Overview & Design Rationale
`ARCH-FW-005` guarantees that any modification to an approved upstream artifact (such as user needs or software requirements) automatically revokes the approval status of all downstream dependent engineering artifacts across the V-model. This prevents obsolete specifications from silently persisting in the DHF and mandates systematic re-approval down the lifecycle.

## 2. Component Boundaries & Interfaces
```
+-------------------------------------------------------------------------+
|                  V-Model Dependency Directed Acyclic Graph              |
| DHF-00 -> 01 -> 02 -> 03 -> 04 -> [05B/C, 06, 07] -> 08 -> 09 -> 10 -> 11|
+-------------------------------------------------------------------------+
                                     │
                                     ▼
+-------------------------------------------------------------------------+
|                scripts/check_change_impact.py Engine                    |
| 1. Baseline Approval State Comparator                                    |
| 2. Topological Downstream Traversal                                     |
| 3. Approval Invalidation & Audit Report                                 |
+-------------------------------------------------------------------------+
                                     │
           ┌─────────────────────────┴────────────────────────┐
           ▼                                                  ▼
+─────────────────────────────────────+   +───────────────────────────────+
|   No Upstream Changes -> Exit Code 0|   | Downstream Invalidation -> 2  |
|      "Approvals remain VALID"       |   | "APPROVAL REVOKED" Warning    |
+─────────────────────────────────────+   +───────────────────────────────+
```
- **Inbound Interface**: Command-line path to DHF directory and optional `--modified <filename>` flag.
- **Outbound Interface**: Exit code 0 (clean) or Exit code 2 (cascading invalidation detected).

## 3. Safety Segregation & Data Flows
- **Fail-Safe Exit Code 2**: Returns a distinct non-zero exit code (2) specifically to allow CI/CD runners to halt pipelines when approvals are invalidated.
- **Transitive Closure**: Downstream invalidation is recursive, ensuring full transitive coverage.

## 4. Technology Stack & Environmental Prerequisites
- Python 3.8+ Standard Library (`os`, `sys`, `re`, `json`, `hashlib`).
