# Detailed Design Specification: DDS-FW-003

> **Unit Design ID**: `DDS-FW-003`  
> **Title**: Markdown RTM Regex Lexer & Bidirectional Bipartite Graph Extraction Unit  
> **Parent Architecture**: `docs/architecture/ARCH-FW-004.md`  
> **Safety Class**: Class B (IEC 62304 Clause 5.4)  
> **Allocated Risk Controls**: `RCM-FW-002`, `RCM-FW-005`, `RCM-FW-015`  
> **Target Requirement**: `FR-SKILL-007`, `FR-SKILL-008`, `FR-SKILL-009`, `FR-SKILL-010`, `FR-SKILL-011`, `FR-SKILL-012`, `FR-SKILL-014`, `FR-DHF-003`, `FR-TOOL-001`, `FR-TOOL-003`, `FR-TOOL-005`, `FR-SOUP-001`, `FR-HOOK-001`  
> **Implementation Target**: `scripts/validate_traceability.py`  
> **Verification Test Protocol**: `docs/tests/TC-FR-TOOL-001.md`, `docs/tests/TC-FR-TOOL-003.md`, `docs/tests/TC-FR-TOOL-005.md`, `docs/tests/TC-FR-DHF-003.md`, `docs/tests/TC-FR-HOOK-001.md`, `docs/tests/TC-FR-SOUP-001.md`  

---

## 1. Detailed Unit Description & Rationale
`DDS-FW-003` specifies the regex lexical analyzer, graph extraction algorithm, and dual-mode validation engine within `scripts/validate_traceability.py`. It operates in two formal modes: Application Mode (`--mode=app` for target SaMD DHF artifacts) and Framework Mode (`--mode=framework` for self-validating framework governance requirements and test protocols under `FR-TOOL-005`). It reads markdown table rows, extracts structured identifiers using standard patterns, constructs adjacency lists for forward and backward links, and verifies bidirectional coverage without third-party graph libraries.

## 2. Data Structures & Interface Signatures
```python
TAG_PATTERNS = {
    "USER_REQ": re.compile(r"`?(USER-REQ-\d+)`?"),
    "REG_REQ":  re.compile(r"`?(REG-REQ-\d+)`?"),
    "REQ_SW":   re.compile(r"`?(REQ-SW-\d+)`?"),
    "RSK":      re.compile(r"`?(RSK-\d+)`?"),
    "RCM":      re.compile(r"`?(RCM-\d+)`?"),
    "ARCH":     re.compile(r"`?(ARCH-\d+)`?"),
    "DDS":      re.compile(r"`?(DDS-\d+)`?"),
    "TC":       re.compile(r"`?(TC-[A-Z]+-\d+)`?"),
}

class TraceabilityGraph:
    user_reqs: Set[str]
    sw_reqs: Dict[str, Dict[str, Any]] # id -> {parents: [], risks: [], arch: [], tests: []}
    orphans: List[str]
    untested: List[str]
```

## 3. Algorithmic Pseudocode & Parsing Logic
```python
def parse_markdown_table_rows(filepath: str) -> List[List[str]]:
    rows = []
    header_found = False
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|") or not line.endswith("|"):
                continue
            if re.match(r"^\|[\s\-:|]+\|$", line):
                header_found = True
                continue
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if not header_found:
                continue
            rows.append(cols)
    return rows

def evaluate_graph_invariants(graph: TraceabilityGraph) -> bool:
    # Invariant 1: Every USER-REQ must be mapped backward from at least one REQ-SW
    mapped_parents = set()
    for req_id, data in graph.sw_reqs.items():
        mapped_parents.update(data["parents"])
    for ureq in graph.user_reqs:
        if ureq not in mapped_parents:
            graph.orphans.append(ureq)
            
    # Invariant 2: Every REQ-SW must link forward to at least one TC-*
    for req_id, data in graph.sw_reqs.items():
        if not data["tests"] or data["tests"] == ["-"]:
            graph.untested.append(req_id)
            
    return len(graph.orphans) == 0 and len(graph.untested) == 0
```

## 4. Error Handling & Boundary Conditions
- **Missing Table Delimiter**: Ignores non-table lines gracefully.
- **Empty Cells (`-` or `None`)**: Treated as unmapped links, triggering failure if in mandatory link columns.
- **Non-zero Exit**: Exits with code 1 upon encountering any element in `graph.orphans` or `graph.untested`.

## 5. Safety Invariants & Risk Control Implementation (RCM-FW-002, RCM-FW-005, RCM-FW-015)
- **Safety Invariant 1 (RCM-FW-002 - Bipartite Completeness & Orphan Lock)**: The traceability graph engine enforces zero dangling nodes. Any requirement lacking a verification test or any risk control lacking an implementation link triggers an exit code of 1, halting pipeline progression.
- **Safety Invariant 2 (RCM-FW-005, RCM-FW-015 - Zero-SOUP Determinism & Tamper Detection)**: Parsing and matrix generation rely exclusively on the Python standard library, preventing external dependency tampering and ensuring reproducible verification in air-gapped environments.
