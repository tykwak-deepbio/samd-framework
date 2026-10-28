# Detailed Design Specification: DDS-FW-008

> **Unit Design ID**: `DDS-FW-008`  
> **Title**: Patient-Level Split Validator & Dataset Hash Locker Unit  
> **Parent Architecture**: `docs/architecture/ARCH-FW-008.md`  
> **Safety Class**: Class C (IEC 62304 Clause 5.4)  
> **Allocated Risk Controls**: `RCM-FW-008`, `RCM-FW-010`  
> **Target Requirement**: `FR-AI-001`, `FR-AI-002`, `FR-AI-003`, `FR-AI-004`, `FR-AI-005`, `FR-AI-006`, `FR-AI-007`, `FR-CLIN-001`  
> **Implementation Target**: `scripts/validate_ai_dataset.py`, `tests/`  
> **Verification Test Protocol**: `docs/tests/TC-FR-AI-001.md` ~ `TC-FR-AI-007.md`, `docs/tests/TC-FR-CLIN-001.md`  

---

## 1. Detailed Unit Description & Rationale
`DDS-FW-008` specifies the unit algorithm for verifying patient-level split isolation across AI training, validation, and test datasets, and computing the Population Stability Index (PSI) to detect covariate drift during inference.

## 2. Data Structures & Interface Signatures
```python
class DatasetManifest:
    patient_ids: Set[str]
    sample_ids: List[str]
    file_hashes: Dict[str, str] # sample_path -> sha256

def verify_zero_patient_leakage(train_manifest: DatasetManifest, test_manifest: DatasetManifest) -> bool:
    overlap = train_manifest.patient_ids.intersection(test_manifest.patient_ids)
    if overlap:
        raise DataLeakageError(f"CRITICAL: Found {len(overlap)} overlapping patients between train and test!")
    return True
```

## 3. Algorithmic Pseudocode & Statistical Drift
```python
def calculate_psi(baseline_counts: List[float], live_counts: List[float]) -> float:
    # Population Stability Index: sum((actual - expected) * ln(actual / expected))
    total_baseline = sum(baseline_counts)
    total_live = sum(live_counts)
    
    # Boundary Guard: Zero-Division & Empty Dataset Protection
    if total_baseline <= 0 or total_live <= 0:
        raise ValueError("Invalid distribution counts: total_baseline and total_live must be positive (>0). Fallback to raw viewer mode.")
        
    psi = 0.0
    for b, l in zip(baseline_counts, live_counts):
        p_base = max(b / total_baseline, 1e-6)
        p_live = max(l / total_live, 1e-6)
        psi += (p_live - p_base) * math.log(p_live / p_base)
        
    return psi
```

## 4. Error Handling & Boundary Conditions
- **Patient Overlap**: Raises immediate fatal exception with list of overlapping IDs.
- **Zero Counts / Zero-Division Protection**: If total baseline or live counts equal 0, raises `ValueError` and immediately triggers unassisted raw image viewer fallback without throwing unhandled exceptions.
- **Critical Drift ($\text{PSI} \ge 0.25$)**: Emits critical telemetry alert and raises `DriftThresholdExceededException` to activate fallback raw mode.

## 5. Safety Invariants & Risk Control Implementation (RCM-FW-008, RCM-FW-010)
- **Safety Invariant 1 (RCM-FW-008 - Zero Data Leakage Invariant)**: Dataset partitioning enforces patient-level isolation using salted SHA-256 patient identifiers. Intersection between training, validation, and test patient sets must evaluate strictly to empty set (0.00% overlap).
- **Safety Invariant 2 (RCM-FW-010 - Statistical Drift Trigger)**: Population Stability Index (PSI) and Kolmogorov-Smirnov (KS) tests are evaluated continuously. A PSI >= 0.25 triggers an automatic drift alert and switches the clinical pipeline to unassisted raw viewing mode.
