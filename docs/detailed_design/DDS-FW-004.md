# Detailed Design Specification: DDS-FW-004

> **Unit Design ID**: `DDS-FW-004`  
> **Title**: Topological Dependency Traversal & Status Invalidation Unit  
> **Parent Architecture**: `docs/architecture/ARCH-FW-005.md`  
> **Safety Class**: Class B (IEC 62304 Clause 5.4)  
> **Allocated Risk Controls**: `RCM-FW-003`, `RCM-FW-005`  
> **Target Requirement**: `FR-TOOL-003`, `FR-TOOL-004`  
> **Implementation Target**: `scripts/check_change_impact.py`  
> **Verification Test Protocol**: `docs/tests/TC-FR-TOOL-003.md`, `docs/tests/TC-FR-TOOL-004.md`  

---

## 1. Detailed Unit Description & Rationale
`DDS-FW-004` specifies the topological traversal algorithm in `scripts/check_change_impact.py` that maps the V-Model dependency graph and propagates approval revocation downwards whenever an upstream file's SHA-256 hash deviates from the saved baseline.

## 2. Data Structures & Graph Representation
```python
V_MODEL_DEPENDENCIES: Dict[str, List[str]] = {
    "DHF-00-Design-and-Development-Plan-DDP.md": [
        "DHF-01-Intended-Use-and-URD.md"
    ],
    "DHF-01-Intended-Use-and-URD.md": [
        "DHF-02-Clinical-Literature-and-SOTA.md",
        "DHF-03-Regulatory-Strategy-and-Clearance-Profile.md",
        "DHF-04-Software-Requirements-Specification-SRS.md",
        "DHF-05A-Risk-Management-Plan-RMP.md",
    ],
    "DHF-04-Software-Requirements-Specification-SRS.md": [
        "DHF-05B-Hazard-Analysis-and-FMEA-Matrix.md",
        "DHF-05C-Risk-Management-Report-RMR.md",
        "DHF-06-Cybersecurity-Threat-Model-and-SBOM.md",
        "DHF-07-Software-Architectural-Design-Specification-SDS.md",
    ],
    "DHF-07-Software-Architectural-Design-Specification-SDS.md": [
        "DHF-08-Software-Detailed-Design-Specification-DDS.md",
    ],
    "DHF-08-Software-Detailed-Design-Specification-DDS.md": [
        "DHF-09-Software-Verification-and-Validation-Report.md",
    ],
    "DHF-09-Software-Verification-and-Validation-Report.md": [
        "DHF-10-Traceability-Matrix-RTM.md",
    ],
    "DHF-10-Traceability-Matrix-RTM.md": [
        "DHF-11-DHF-Index-and-Quality-Audit-Report.md",
    ]
}
```

## 3. Algorithmic Pseudocode & Transitive Invalidation
```python
def find_all_downstream(modified_files: List[str], graph: Dict[str, List[str]]) -> Set[str]:
    invalidated: Set[str] = set()
    queue = list(modified_files)
    
    while queue:
        current = queue.pop(0)
        direct_children = graph.get(current, [])
        for child in direct_children:
            if child not in invalidated:
                invalidated.add(child)
                queue.append(child)
    return invalidated

def execute_impact_check(dhf_dir: str, modified_arg: Optional[str]) -> int:
    modified_files = []
    if modified_arg:
        modified_files.append(modified_arg)
    else:
        modified_files = detect_hash_mismatches_against_baseline(dhf_dir)
        
    if not modified_files:
        print("[INFO] All current approvals remain VALID. (Exit 0)")
        return 0
        
    invalidated = find_all_downstream(modified_files, V_MODEL_DEPENDENCIES)
    print(f"[ALERT] CASCADING DOWNSTREAM INVALIDATION DETECTED! {len(invalidated)} files revoked.")
    for inv in sorted(invalidated):
        print(f"  -> REVOKED: {inv} [STATUS: INVALIDATED (APPROVAL REVOKED)]")
    return 2 # Non-zero exit code specifically flagging approval revocation
```

## 4. Error Handling & Boundary Conditions
- **Cyclic Dependencies**: Guarded by `if child not in invalidated` check.
- **Return Code Contract**:
  - `0`: All approvals valid.
  - `2`: Cascading invalidation detected (used in CI/CD pipeline blocking).

## 5. Safety Invariants & Risk Control Implementation (RCM-FW-003, RCM-FW-005)
- **Safety Invariant 1 (RCM-FW-003 - Transitive Invalidation Invariant)**: Invalidation traversal guarantees that any upstream modification cascades to all reachable downstream nodes in topological order. Invalidation depth is unbounded until terminal nodes are reached.
- **Safety Invariant 2 (RCM-FW-005 - Cycle-Free DAG Guarantee)**: Dependency graphs must be strictly acyclic. Tarjan's strongly connected components algorithm executes prior to invalidation, immediately terminating on any circular loop.
