# Software Architecture: ARCH-FW-010

> **Component ID**: `ARCH-FW-010`  
> **Title**: 21 CFR Part 11 Append-Only Audit Trail & Electronic Signature Engine  
> **Subsystem**: Regulatory Records & Compliance Subsystem  
> **Safety Class**: Class B (IEC 62304 Clause 5.3)  
> **Allocated Requirements**: `FR-PART11-001`, `FR-PART11-002`, `FR-TOOL-002`, `FR-TRANS-001`  
> **Allocated Risk Controls**: `RCM-FW-001`, `RCM-FW-011`  
> **Detailed Design Units**: `docs/detailed_design/DDS-FW-010.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-PART11-001.md`, `docs/tests/TC-FR-PART11-002.md`, `docs/tests/TC-FR-TOOL-002.md`, `docs/tests/TC-FR-TRANS-001.md`  

---

## 1. Architectural Overview & Design Rationale
`ARCH-FW-010` establishes regulatory record integrity conforming to US FDA 21 CFR Part 11 and ISO 13485 Clause 4.2.5. It provides an append-only, tamper-evident audit trail capturing every DHF modification and lifecycle gate decision, cryptographically binding electronic signatures to document SHA-256 digests.

## 2. Component Boundaries & Interfaces
```
+-------------------------------------------------------------------------+
|                  Part 11 Records & Signature Controller                 |
+-------------------------------------------------------------------------+
                                     │
           ┌─────────────────────────┴────────────────────────┐
           ▼                                                  ▼
+─────────────────────────────────────+   +───────────────────────────────+
|     Append-Only Audit Ledger        |   |   Electronic Signature Binder |
| - audit_trail.log (Append-only)     |   | - Reviewer Identity & Intent  |
| - UTC Timestamp & User ID           |   | - Cryptographic HMAC/RSA Bind |
| - Previous / New File SHA-256       |   | - Signature Invalidation Check|
+─────────────────────────────────────+   +───────────────────────────────+
```
- **Inbound Interface**: Gate sign-off requests, file modification notifications.
- **Outbound Interface**: Signed DHF document metadata, append-only audit trail records.

## 3. Safety Segregation & Data Flows
- **Tamper Evidence**: If an audit record is deleted or modified out of band, cryptographic chain verification detects the alteration and halts the framework.
- **Bi-directional Binding**: Signatures cannot be copied or transferred to another document without hash mismatch.

## 4. Technology Stack & Environmental Prerequisites
- Python 3.8+ Standard Library (`hashlib`, `hmac`, `datetime`).
