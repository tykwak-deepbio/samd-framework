# Test Protocol: TC-FR-TOOL-002

> **Test Case ID**: `TC-FR-TOOL-002`  
> **Target Requirement**: `FR-TOOL-002` (Cryptographic SHA-256 DHF Master Index Generator)  
> **Test Level**: System / Automated Test Suite  
> **Verification Method**: Execution & Hash Comparison (`scripts/test_framework.py`)  
> **Status**: Approved  

---

## 1. Test Objective
Verify that `scripts/generate_dhf_index.py` correctly scans all 14 DHF markdown documents, computes exact SHA-256 cryptographic digests, parses document control metadata, and produces a valid markdown index table.

## 2. Preconditions
- `scripts/generate_dhf_index.py` is executable.
- Complete reference DHF in `examples/wsi-tissue-viewer-samd/dhf/`.

## 3. Test Execution Steps
1. Execute `python3 scripts/generate_dhf_index.py examples/wsi-tissue-viewer-samd/dhf`.
2. Verify exit code is `0`.
3. Verify stdout output contains:
   - "Processing 14 DHF documents"
   - Master DHF Index markdown table starting with `| DHF ID | Document Title | ... |`
   - Valid 64-character SHA-256 hex string prefixes for each file.
4. Independent verification: Compute SHA-256 using `hashlib.sha256()` directly and compare against script output.

## 4. Expected Acceptance Criteria (Pass/Fail)
- **PASS**: Exit code 0, all 14 files hashed and formatted into valid markdown table.
- **FAIL**: Any document omitted, incorrect hash calculation, or non-zero exit code.
