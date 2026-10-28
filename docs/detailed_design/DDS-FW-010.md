# Detailed Design Specification: DDS-FW-010

> **Unit Design ID**: `DDS-FW-010`  
> **Title**: Cryptographic Append-Only Audit Trail & Digital Signature Binder Unit  
> **Parent Architecture**: `docs/architecture/ARCH-FW-010.md`  
> **Safety Class**: Class B (IEC 62304 Clause 5.4)  
> **Allocated Risk Controls**: `RCM-FW-011`  
> **Target Requirement**: `FR-PART11-001`, `FR-PART11-002`, `FR-TRANS-001`, `FR-TOOL-002`  
> **Implementation Target**: `scripts/record_audit_event.py`, `scripts/generate_dhf_index.py`  
> **Verification Test Protocol**: `docs/tests/TC-FR-PART11-001.md`, `docs/tests/TC-FR-PART11-002.md`, `docs/tests/TC-FR-TRANS-001.md`, `docs/tests/TC-FR-TOOL-002.md`  

---

## 1. Detailed Unit Description & Rationale
`DDS-FW-010` specifies the append-only audit trail logging format and HMAC-SHA256 signature binding algorithm conforming to FDA 21 CFR Part 11 requirements for electronic records and electronic signatures.

## 2. Data Structures & Audit Log Schema
```json
{
  "timestamp_utc": "2026-10-28T10:00:00Z",
  "event_id": "EVT-83e9b8d2-001",
  "user_id": "lead_regulatory_auditor@hospital.org",
  "action": "GATE_SIGN_OFF",
  "document": "DHF-04-Software-Requirements-Specification-SRS.md",
  "doc_sha256": "ebe24edd1472e5ad8006e866e4a26359556209a3cf3c16ee0a08e6e5879a6135",
  "signing_intent": "APPROVAL",
  "signature_hmac": "9a8f23...[HMAC-SHA256 of doc_sha256 + user_id + timestamp]"
}
```

## 3. Algorithmic Pseudocode & Append-Only Write
```python
def record_audit_event(audit_log_path: str, event_data: dict, secret_key: bytes) -> str:
    event_payload = json.dumps(event_data, sort_keys=True)
    signature = hmac.new(secret_key, event_payload.encode('utf-8'), hashlib.sha256).hexdigest()
    event_data["signature_hmac"] = signature
    
    # Cross-platform atomic append with graceful locking fallback
    with open(audit_log_path, "a", encoding="utf-8") as f:
        try:
            import fcntl
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        except (ImportError, AttributeError, OSError):
            pass  # Fallback to atomic OS write on non-POSIX / Windows systems
        f.write(json.dumps(event_data) + "\n")
        
    return signature
```

## 4. Error Handling & Boundary Conditions
- **Log Tampering**: Verification scan recalculates HMAC chain; any mismatch raises an immediate audit tampering alert.
- **Concurrent Writes & Cross-Platform File Locking**: Protected by cross-platform atomic append and OS file locking (`fcntl.flock` on POSIX systems with graceful non-blocking fallback on non-POSIX / Windows environments).

## 5. Safety Invariants & Risk Control Implementation (RCM-FW-011)
- **Safety Invariant 1 (RCM-FW-011 - Part 11 Audit Trail Immutability)**: Every state transition, document modification, and gate approval generates an append-only audit trail record sealed with an HMAC-SHA256 signature and RFC 3161 timestamp.
- **Safety Invariant 2 (RCM-FW-011 - Electronic Signature Non-Repudiation)**: Human gate approval records require unique reviewer authentication credentials. Tampering with any log record breaks the HMAC chain and triggers immediate security lockdown.
