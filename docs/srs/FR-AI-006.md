# Software Requirement: FR-AI-006

> **Requirement ID**: `FR-AI-006`  
> **Title**: Input Quality Assessment (IQA) & Out-of-Distribution (OOD) Rejection  
> **Category**: AI/ML Robustness & Defensive Processing (`[AI]`)  
> **Safety Class**: Class C (IEC 62304 Clause 5.4)  
> **Parent Standard**: Good Machine Learning Practice (GMLP), ISO 14971:2019 Clause 7.1  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-AI-006.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-008.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-008.md`  

---

## 1. Description & Technical Rationale
The framework shall incorporate an automated Input Quality Assessment (IQA) filter prior to AI model ingestion to detect corrupted, out-of-focus, over-stained, or out-of-distribution (OOD) samples, halting inference and notifying the clinician to prevent false diagnostic outputs.

## 2. Detailed Functional Specifications
1. **Image Quality Metrics**:
   - Evaluate blur/sharpness (Laplacian variance), contrast distribution, and artifact presence before model execution.
2. **Out-of-Distribution (OOD) Detection**:
   - Screen input embeddings against training distribution manifolds using Mahalanobis distance or energy score.
3. **Fail-Safe Fallback**:
   - If an input fails IQA or OOD criteria, safely reject inference, log the rejection event, and display the raw image without misleading overlays.

## 3. Inputs, Processing & Outputs
- **Inputs**: Raw Whole Slide Images / medical scans, modality calibration profiles.
- **Processing**: Laplacian sharpness scoring, statistical distribution distance calculation.
- **Outputs**: Quality pass/reject verdict, artifact warning log, raw fallback mode.
