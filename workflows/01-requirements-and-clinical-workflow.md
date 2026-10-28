# Requirements & Clinical Workflow (Phases 1, 2, 3, 4)

> **Framework Guide**: `WF-01-REQUIREMENTS`  
> **Key Agents**: `user-needs-agent`, `clinical-sota-agent`, `regulatory-affairs-agent`, `srs-analyst-agent`  

---

## 1. Phase 1: User & Clinical Needs Discovery
1. The `user-needs-agent` initiates a dialogue with project stakeholders to establish the clinical premise:
   - What pathology task is being performed?
   - What scanner formats and staining protocols are used?
   - What are the diagnostic risks if the software malfunctions?
2. Structure all clinical and user needs into atomic statements tagged with `USER-REQ-xxx`.
3. Output: `dhf/DHF-01-Intended-Use-and-URD.md`.

---

## 2. Phase 2: Clinical Literature & SOTA Analysis
1. The `clinical-sota-agent` performs a systematic literature query across PubMed, IEEE Xplore, and clinical registries.
2. Evaluates state-of-the-art algorithms:
   - Tissue segmentation models (U-Net, SegFormer, MobileNetV3).
   - Stain normalization methods (Macenko SVD vs. Vahadane sparse non-negative matrix factorization).
3. Identifies predicate devices (FDA 510(k), CE IVD, MFDS cleared).
4. Establishes quantitative clinical thresholds (`CLIN-REQ-xxx`):
   - Dice coefficient threshold: $\ge 0.92$.
   - False positive tissue detection rate: $\le 2.5\%$.
   - CIE Delta E color deviation: $\le 3.0$.
5. Output: `dhf/DHF-02-Clinical-Literature-and-SOTA.md`.

---

## 3. Phase 3: Regulatory Strategy & Classification
1. The `regulatory-affairs-agent` maps the device to regulatory systems:
   - **MFDS (Korea)**: 의료영상 전처리 소프트웨어 (Class II) / 체외진단의료기기.
   - **FDA (USA)**: 21 CFR 864.3700 Whole Slide Imaging System (Class II, 510(k)).
   - **EU IVDR**: Annex VIII Rule 1 / Rule 4 (Class B).
2. Identifies all applicable standards (ISO 13485, IEC 62304, ISO 14971, IEC 62366-1, ISO 27001, IEC 81001-5-1).
3. Generates regulatory requirements (`REG-REQ-xxx`):
   - Software Safety Class B declaration.
   - Cybersecurity SBOM export requirement.
   - DICOM PHI scrubbing requirement.
4. Output: `dhf/DHF-03-Regulatory-Strategy-and-Clearance-Profile.md`.

---

## 4. Phase 4: Software Requirements Specification (SRS)
1. The `srs-analyst-agent` synthesizes `USER-REQ-*`, `CLIN-REQ-*`, and `REG-REQ-*` into `REQ-SW-xxx`.
2. Group into:
   - `[FUNC]` Functional requirements (tile loading, deep zoom, segmentation, color normalization).
   - `[PERF]` Performance requirements (tile latency $\le 150\text{ ms}$, overview runtime $\le 2.5\text{ s}$).
   - `[SAFE]` Safety & fail-safe requirements (low-confidence banner, raw toggle, OD clamp).
   - `[INTF]` / `[SEC]` Interface & security requirements (WSI formats, TLS 1.3, PHI de-identification).
3. Verify 100% backward traceability to input requirements.
4. Output: `dhf/DHF-04-Software-Requirements-Specification-SRS.md`.
