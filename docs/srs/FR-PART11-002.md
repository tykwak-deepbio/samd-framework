# Software Requirement: FR-PART11-002

> **Requirement ID**: `FR-PART11-002`  
> **Title**: Automated Cryptographic Audit Event Logger (`record_audit_event.py`) Integration  
> **Category**: Electronic Records & Signatures (`[PART11]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: FDA 21 CFR Part 11 Subpart B, ISO 13485:2016 Clause 4.2.4  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-PART11-002.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-010.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-010.md`  

---

## 1. Description & Technical Rationale
The framework shall provide an executable, zero-dependency audit logging script (`record_audit_event.py`) that generates append-only, HMAC-SHA256 chained audit entries for all gate reviews, document sign-offs, and design modifications, ensuring non-repudiation and tamper detection.

## 2. Detailed Functional Specifications
1. **HMAC Signature Chaining**:
   - Each audit record must include a cryptographic HMAC signature incorporating the previous record's signature, timestamp, actor, and resource hash.
2. **Concurrent Access Protection**:
   - Implement cross-platform advisory file locking (`fcntl` with Windows atomic fallback) to prevent log corruption during concurrent agent operations.
3. **Automated Integrity Verification**:
   - Support a `--verify` execution flag that scans the entire log chain, verifying sequential integrity and detecting any unauthorized record alterations.

## 3. Inputs, Processing & Outputs
- **Inputs**: Actor ID, action type, target resource, human-readable details.
- **Processing**: SHA-256 resource hashing, HMAC chaining calculation, file lock acquisition.
- **Outputs**: Signed append-only log entry in `dhf/audit_trail.log`.
