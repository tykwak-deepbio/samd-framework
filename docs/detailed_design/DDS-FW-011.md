# Detailed Design Specification: DDS-FW-011

> **Unit Design ID**: `DDS-FW-011`  
> **Title**: Anomaly Severity Triage & Maintenance State Machine Unit  
> **Parent Architecture**: `docs/architecture/ARCH-FW-011.md`  
> **Safety Class**: Class B (IEC 62304 Clause 5.4)  
> **Allocated Risk Controls**: `RCM-FW-013`, `RCM-FW-014`  
> **Target Requirement**: `FR-MAINT-001`, `FR-ANOM-001`, `FR-ANOM-002`, `FR-SOUP-002`, `FR-CYBER-001`, `FR-CYBER-002`, `FR-PMS-001`, `FR-SKILL-015`  
> **Implementation Target**: `scripts/manage_anomalies.py`, `workflows/`  
> **Verification Test Protocol**: `docs/tests/TC-FR-MAINT-001.md`, `docs/tests/TC-FR-ANOM-001.md`, `docs/tests/TC-FR-ANOM-002.md`, `docs/tests/TC-FR-SOUP-002.md`, `docs/tests/TC-FR-CYBER-001.md`, `docs/tests/TC-FR-CYBER-002.md`, `docs/tests/TC-FR-PMS-001.md`, `docs/tests/TC-FR-SKILL-015.md`  

---

## 1. Detailed Unit Description & Rationale
`DDS-FW-011` specifies the data structures and state transition machine for anomaly tracking (`ANOM-xxx`), root cause analysis (RCA), CAPA integration, and maintenance release gating under IEC 62304 Clause 6 and Clause 9.

## 2. Data Structures & State Machine Model
```python
class AnomalySeverity(Enum):
    CATASTROPHIC = 1
    CRITICAL = 2
    MAJOR = 3
    MINOR = 4

class AnomalyStatus(Enum):
    REPORTED = "REPORTED"
    INVESTIGATING = "INVESTIGATING"
    CORRECTED = "CORRECTED"
    VERIFIED = "VERIFIED"
    CLOSED = "CLOSED"
    DEFERRED_APPROVED = "DEFERRED_APPROVED"
```

## 3. Algorithmic Pseudocode & Release Gate Clearance
```python
def verify_release_gate_clearance(anomalies: List[dict]) -> bool:
    for anom in anomalies:
        sev = anom["severity"]
        status = anom["status"]
        
        # Block release if Catastrophic or Critical anomalies are not CLOSED or VERIFIED
        if sev in [AnomalySeverity.CATASTROPHIC, AnomalySeverity.CRITICAL]:
            if status not in [AnomalyStatus.CLOSED, AnomalyStatus.VERIFIED]:
                raise UnresolvedCriticalAnomalyError(
                    f"BLOCK: {anom['id']} ({sev}) remains {status}. Release prohibited!"
                )
        elif sev == AnomalySeverity.MAJOR:
            if status == AnomalyStatus.DEFERRED_APPROVED:
                assert "clinical_justification" in anom, f"Missing clinical safety rationale for {anom['id']}"
    return True
```

## 4. Error Handling & Boundary Conditions
- **Unmitigated Critical Bug**: Unconditionally halts release gate execution.
- **Missing RCA**: Blocks transitioning anomaly status from INVESTIGATING to CORRECTED.

## 5. Safety Invariants & Risk Control Implementation (RCM-FW-013, RCM-FW-014)
- **Safety Invariant 1 (RCM-FW-013 - Post-Market Vulnerability SLA Interlock)**: Identified SOUP vulnerabilities with CVSS >= 9.0 require documented mitigation within 30 days and patch release within 60 days. Exceeding this SLA automatically blocks subsequent software release baselines.
- **Safety Invariant 2 (RCM-FW-014 - Anomaly Release Gate Block)**: Gate 10 release interlock strictly prohibits clearance if any unresolved Catastrophic (Severity 1) or Critical (Severity 2) software anomalies remain in open status.
