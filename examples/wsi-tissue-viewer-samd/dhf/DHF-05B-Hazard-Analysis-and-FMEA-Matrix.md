# Hazard Analysis & Software FMEA Matrix

> **Document ID**: `DHF-05B-FMEA`  
> **Applicable Standards**: ISO 14971:2019 Clause 5 & 7, IEC 62304:2006 Clause 7  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 예비위해요인분석(PHA) 및 소프트웨어 고장 형태 및 영향 분석(SW-FMEA) 매트릭스입니다.
> - 위험 항목(`RSK-xxx`)마다 위해요인, 고장원인, 위험상황, 임상적 위해(Harm), 초기 위험도(S x P), 위험통제조치(`RCM-xxx`), 통제 후 잔여 위험도 및 검증방법(`TC-xxx`)을 1:1로 매핑합니다.
> - 소프트웨어 의료기기(SaMD)의 특성상 AI 위음성(False Negative), 색상 왜곡, 타일 로딩 실패, 메모리 고갈(OOM) 등의 위해요인이 필수로 분석되어야 합니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Risk Management Engineer | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Clinical Pathologist | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Chief Quality Officer | Approved | `[YYYY-MM-DD]` |

---

## 2. Hazard Analysis & FMEA Table (`RSK-xxx` & `RCM-xxx`)

| Risk ID | Hazard / Failure Mode | Sequence of Events & Hazardous Situation | Resulting Harm | Initial S x P (Risk) | Risk Control Measure (RCM ID & Description) | Implemented In (SRS / Design) | Verification Test (TC ID) | Residual S x P (Risk) | Status |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- | :--- | :---: | :--- |
| `RSK-001` | False-negative tissue segmentation | AI model classifies faint biopsy fragment as glass background; pathologist relies on bounding box and fails to review fragment. | Delayed diagnosis of early micro-metastasis (Harm). | S4 x P4 (Unacceptable) | `RCM-001`: If segmentation confidence $< 0.60$, trigger low-confidence visual alert banner and display raw uncropped slide. | `REQ-SW-007`, `DDS-004` | `TC-SYS-007` | S4 x P1 (Broadly Acceptable) | Verified |
| `RSK-002` | Excessive chromatic alteration during stain normalization | Stain matrix deconvolution algorithm over-corrects hue, altering nuclear-to-cytoplasmic contrast. | Pathologist misinterprets dysplasia or nuclear atypia grade. | S3 x P3 (Unacceptable) | `RCM-002`: Provide an instant one-click toggle to view raw unnormalized optical RGB pixels; add on-screen normalization indicator. | `REQ-SW-008`, `DDS-005` | `TC-USE-001` | S3 x P1 (Broadly Acceptable) | Verified |
| `RSK-003` | Pixel value clipping in Optical Density conversion | OD transformation produces values exceeding float bounds, clipping dense chromatin textures to black. | Loss of diagnostic cellular chromatin detail. | S3 x P4 (Unacceptable) | `RCM-003`: Enforce strict mathematical bounding clamp $[0.01, 2.50]$ in OD transformation unit. | `REQ-SW-009`, `DDS-002` | `TC-UNIT-003` | S3 x P1 (Broadly Acceptable) | Verified |
| `RSK-004` | Out-of-Memory (OOM) crash during 40x rapid panning | Pyramidal tile cache expands uncontrollably without eviction, crashing application mid-diagnosis. | Loss of unsaved diagnostic notes and clinic workflow disruption. | S2 x P4 (ALARP) | `RCM-004`: Implement LRU (Least Recently Used) bounded memory cache capped at 2.0 GB with proactive garbage collection. | `REQ-SW-005`, `DDS-001` | `TC-SYS-005` | S2 x P1 (Broadly Acceptable) | Verified |

---

## 3. Verification of Risk Control Measures
All `RCM-xxx` measures have been implemented in software and independently verified via the designated test cases with 100% pass rate.
