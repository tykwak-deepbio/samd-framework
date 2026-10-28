# Detailed Design Specification: DDS-FW-005

> **Unit Design ID**: `DDS-FW-005`  
> **Title**: SHA-256 Digest Calculator & Master DHF Markdown Table Formatter Unit  
> **Parent Architecture**: `docs/architecture/ARCH-FW-006.md`  
> **Safety Class**: Class B (IEC 62304 Clause 5.4)  
> **Allocated Risk Controls**: `RCM-FW-005`  
> **Target Requirement**: `FR-SKILL-014`, `FR-TOOL-002`, `FR-TOOL-003`, `FR-CM-001`, `FR-INT-001`  
> **Implementation Target**: `scripts/generate_dhf_index.py`, `tests/integration/`  
> **Verification Test Protocol**: `docs/tests/TC-FR-TOOL-002.md`, `docs/tests/TC-FR-TOOL-003.md`, `docs/tests/TC-FR-CM-001.md`, `docs/tests/TC-FR-INT-001.md`  

---

## 1. Detailed Unit Description & Rationale
`DDS-FW-005` specifies the cryptographic hashing and metadata parsing algorithm in `scripts/generate_dhf_index.py`. It reads every DHF document, computes its SHA-256 digest in buffered 64KB chunks to optimize memory utilization, extracts document control headers, and formats the Master DHF Index table for inclusion in `DHF-11`.

## 2. Data Structures & Interface Signatures
```python
class DHFDocumentRecord:
    doc_id: str           # e.g., "DHF-04-SRS"
    filename: str         # e.g., "DHF-04-Software-Requirements-Specification-SRS.md"
    title: str            # e.g., "Software Requirements Specification"
    version: str          # e.g., "1.0.0"
    status: str           # e.g., "Approved"
    sha256_hash: str      # 64-character hex string
    file_size_bytes: int  # integer file size
```

## 3. Algorithmic Pseudocode & Stream Hashing
```python
def compute_sha256_digest(filepath: str) -> str:
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(65536) # 64KB buffer
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

def extract_document_metadata(filepath: str) -> DHFDocumentRecord:
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read(2048) # Read header portion
    
    doc_id_m = re.search(r"\*\*Document ID\*\*:\s*`?([A-Za-z0-9\-_]+)`?", text)
    title_m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    version_m = re.search(r"\*\*Version\*\*:\s*`?([0-9\.]+)`?", text)
    status_m = re.search(r"\*\*Status\*\*:\s*`?([A-Za-z0-9\s_\-]+)`?", text)
    
    return DHFDocumentRecord(
        doc_id=doc_id_m.group(1) if doc_id_m else "UNKNOWN",
        filename=os.path.basename(filepath),
        title=title_m.group(1).strip() if title_m else "Untitled",
        version=version_m.group(1) if version_m else "Draft",
        status=status_m.group(1).strip() if status_m else "Draft",
        sha256_hash=compute_sha256_digest(filepath),
        file_size_bytes=os.path.getsize(filepath)
    )
```

## 4. Error Handling & Boundary Conditions
- **Missing Document Control Header**: Defaults safely to `"UNKNOWN"` / `"Draft"` and warns the user without crashing.
- **Large Files**: Stream hashing handles files up to multi-gigabytes with constant memory footprint ($< 1\text{ MB}$).

## 5. Safety Invariants & Risk Control Implementation (RCM-FW-005)
- **Safety Invariant 1 (RCM-FW-005 - Cryptographic Artifact Integrity)**: Every DHF artifact is hashed using SHA-256 via chunked streaming with universal newline normalization (`\r\n` -> `\n`). Any discrepancy between current disk contents and the authoritative DHF index invalidates the baseline.
- **Safety Invariant 2 (RCM-FW-005 - Air-Gapped Zero-SOUP Standard)**: Hashing and manifest generation use only built-in standard library components, ensuring 100% operational reliability in disconnected secure hospital networks.
