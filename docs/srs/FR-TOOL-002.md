# Software Requirement: FR-TOOL-002

> **Requirement ID**: `FR-TOOL-002`  
> **Title**: Cryptographic SHA-256 DHF Master Index Generator (`generate_dhf_index.py`)  
> **Category**: Automated Tooling (`[TOOL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: ISO 13485:2016 Clause 4.2.4 (Control of Documents) & Clause 7.3.7  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-TOOL-002.md`  

---

## 1. Description & Regulatory Rationale
Under ISO 13485 Clause 4.2.4 and 7.3.7, medical device quality documentation must be controlled against unintended alteration or tampering. The framework shall provide an automated tool (`scripts/generate_dhf_index.py`) that extracts document control metadata and computes cryptographic SHA-256 hashes for all DHF markdown files.

## 2. Detailed Functional Specifications
1. The tool shall scan all `.md` files in the specified DHF directory.
2. For each document, it shall extract:
   - Document ID (from `**Document ID**:`)
   - Document Title (from top-level `# Title`)
   - Revision Version (from `**Revision**:`)
   - Effective Date (from `**Effective Date**:`)
   - Approval Status (from `**Document Status**:`)
3. It shall compute the standard SHA-256 cryptographic digest of the complete file content after normalizing line endings (standardizing CRLF to LF and stripping UTF-8 BOM) to guarantee cross-OS hash reproducibility across Windows, macOS, and Linux.
4. It shall format and output an authoritative markdown index table ready for inclusion in `DHF-11-DHF-Index-and-Quality-Audit-Report.md`.
5. Exit code `0` on successful generation; non-zero on I/O error.

## 3. Inputs, Processing & Outputs
- **Inputs**: Path to DHF directory.
- **Processing**: File hashing (SHA-256), regex metadata extraction, markdown table assembly.
- **Outputs**: Formatted DHF Master Index table printed to stdout.
