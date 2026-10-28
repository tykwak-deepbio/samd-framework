# Software Requirement: FR-PART11-001

> **Requirement ID**: `FR-PART11-001`  
> **Title**: Immutable Computer-Generated Audit Trail & Electronic Signature Binding  
> **Category**: Regulatory Records Integrity (`[PART11]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: FDA 21 CFR Part 11 (Electronic Records; Electronic Signatures), ISO 13485:2016 Clause 4.2.5  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-PART11-001.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-010.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-010.md`  

---

## 1. Description & Technical Rationale
To comply with FDA 21 CFR Part 11 and ISO 13485 Clause 4.2.5, the framework shall maintain an independent, computer-generated, time-stamped, append-only audit trail capturing all DHF modifications and gate reviews, and cryptographically bind reviewer electronic signatures to document contents.

## 2. Detailed Functional Specifications
1. **Append-Only Audit Trail**:
   - Every creation, modification, or gate approval of DHF files must generate an immutable log entry in `audit_trail.log`.
   - Log entry fields: UTC Timestamp (ISO 8601), User/Agent ID, Action Type, Target Document, Previous Hash, New Hash, Reason for Change.
   - Prohibit deletion, editing, or overwriting of historical audit trail records.
2. **Cryptographic Electronic Signature Binding**:
   - When a gate approval is signed, the reviewer's identity, digital certificate/HMAC signature, and signing intent (Reviewer, Approver, Author) must be cryptographically bound to the document's SHA-256 digest.
   - Any subsequent alteration of the document invalidates the electronic signature.

## 3. Inputs, Processing & Outputs
- **Inputs**: Document change event, user signing credentials, document digest.
- **Processing**: SHA-256 computation, digital signature generation, append-only ledger write.
- **Outputs**: Immutable audit trail entry, cryptographically signed gate review record.
