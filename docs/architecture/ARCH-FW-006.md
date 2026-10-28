# Software Architecture: ARCH-FW-006

> **Component ID**: `ARCH-FW-006`  
> **Title**: Cryptographic Checksum & Document Control Indexer  
> **Subsystem**: Document Control Subsystem  
> **Safety Class**: Class B (IEC 62304 Clause 5.3)  
> **Allocated Requirements**: `FR-TOOL-002`, `FR-TOOL-003`, `FR-DHF-001`, `FR-SKILL-014`  
> **Allocated Risk Controls**: `RCM-FW-005`  
> **Detailed Design Units**: `docs/detailed_design/DDS-FW-005.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-TOOL-002.md`  

---

## 1. Architectural Overview & Design Rationale
`ARCH-FW-006` provides anti-tampering baseline control and master documentation indexing under ISO 13485 Clause 4.2.4. In regulatory audits, manufacturers must prove that submitted design history files have not been modified after formal sign-off. This component scans all DHF documents, computes SHA-256 cryptographic digests, extracts document control headers, and generates the authoritative Master DHF Index.

## 2. Component Boundaries & Interfaces
```
+-------------------------------------------------------------------------+
|                  Markdown DHF File Collection (DHF-00 ~ DHF-11)         |
+-------------------------------------------------------------------------+
                                     │
                                     ▼
+-------------------------------------------------------------------------+
|                 scripts/generate_dhf_index.py Engine                    |
| 1. Document Control Header Parser (ID, Title, Version, Status)          |
| 2. SHA-256 Block Digest Generator                                       |
| 3. Markdown Master Table Formatter                                      |
+-------------------------------------------------------------------------+
                                     │
                                     ▼
+-------------------------------------------------------------------------+
|     DHF-11-DHF-Index-and-Quality-Audit-Report.md Master Checksum Table  |
+-------------------------------------------------------------------------+
```
- **Inbound Interface**: Command-line path to project `dhf/` directory.
- **Outbound Interface**: Markdown table inserted into `DHF-11` and standard console output with exit code 0.

## 3. Safety Segregation & Data Flows
- **Deterministic Digesting**: Stream-based block hashing (`hashlib.sha256`) processing 64KB blocks, preventing memory spikes.
- **Immutability Assurance**: Captures the exact state of every approved design document.

## 4. Technology Stack & Environmental Prerequisites
- Python 3.8+ Standard Library (`os`, `sys`, `re`, `hashlib`, `datetime`).
