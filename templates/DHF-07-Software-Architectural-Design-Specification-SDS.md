# Software Architectural Design Specification (SDS)

> **Document ID**: `DHF-07-SDS`  
> **Applicable Standards**: IEC 62304:2006+AMD1:2015 Clause 5.3, ISO 13485:2016 Clause 7.3.4  
> **Project Name**: `[Project / Device Name]`  
> **Software Safety Class**: `[Class B]` (IEC 62304)  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 IEC 62304 Clause 5.3(소프트웨어 아키텍처 설계)에 따른 고수준 설계명세서(SDS)입니다.
> - 시스템 구조 분해(`ARCH-xxx`), 각 서브시스템 간 인터페이스 및 데이터 흐름, 안전성 격리(Safety Segregation: 안전필수 모듈과 비필수 모듈의 격리 증명), SOUP(기성 소프트웨어) 요구사항 및 이상동작 대책을 기술합니다.
> - 모든 `REQ-SW-xxx`는 최소 1개 이상의 `ARCH-xxx`에 매핑되어야 합니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Principal Software Architect | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Lead Systems Engineer | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Software Engineering Director | Approved | `[YYYY-MM-DD]` |

---

## 2. High-Level System Decomposition (`ARCH-xxx`)

```
+───────────────────────────────────────────────────────────────────────────────────+
|                                    Client Viewport Layer                          |
|             [ARCH-005: Interactive WSI Canvas & Annotation Overlay (UI)]          |
+───────────────────────────────────────────────────────────────────────────────────+
                                         │  HTTPS / WSS (TLS 1.3)
                                         ▼
+───────────────────────────────────────────────────────────────────────────────────+
|                         Backend Core Processing Subsystem                         |
|                                                                                   |
|   ┌────────────────────────┐   ┌────────────────────────┐   ┌───────────────────┐ |
|   | ARCH-001: WSI Loader   |   | ARCH-002: Stain Color  |   | ARCH-003: AI      | |
|   | & Pyramidal Tile Engine|──►| Normalization Engine   |──►| Tissue Detector   | |
|   └────────────────────────┘   └────────────────────────┘   └───────────────────┘ |
|                │                            │                         │           |
|                ▼                            ▼                         ▼           |
|   ┌─────────────────────────────────────────────────────────────────────────────┐ |
|   | ARCH-004: Bounded LRU Tile Cache & Memory Supervisor                        | |
|   └─────────────────────────────────────────────────────────────────────────────┘ |
+───────────────────────────────────────────────────────────────────────────────────+
```

| Component ID | Subsystem Name | Safety Class | Primary Function | Traced Requirements |
| :--- | :--- | :---: | :--- | :--- |
| `ARCH-001` | WSI Pyramidal Ingestion Engine | Class B | Decodes multi-resolution SVS/NDPI/TIFF slides, builds coordinate matrices. | `REQ-SW-001`, `REQ-SW-004` |
| `ARCH-002` | Stain Color Normalization Engine | Class B | Computes Optical Density vectors and normalizes H&E stain chromaticity. | `REQ-SW-003`, `REQ-SW-009` |
| `ARCH-003` | AI Tissue Segmentation Engine | Class B | Deep learning inference extracting valid tissue boundaries and confidence scores. | `REQ-SW-002`, `REQ-SW-007` |
| `ARCH-004` | Memory Supervisor & Bounded Cache | Class B | Manages thread-safe LRU tile memory allocations and evicts stale buffers. | `REQ-SW-005`, `RCM-004` |
| `ARCH-005` | Clinical Viewport & UI Layer | Class A | Renders deep zoom viewport, navigation controls, and low-confidence alert banners. | `REQ-SW-004`, `REQ-SW-008` |
| `ARCH-006` | Security & PHI De-identification Filter | Class B | Scrubs DICOM tags and enforces TLS 1.3 encryption across endpoints. | `REQ-SW-010`, `REQ-SW-011` |

---

## 3. Safety Segregation (IEC 62304 Clause 5.3.5)
- **Segregation of UI (`ARCH-005`, Class A) from Diagnostic Engines (`ARCH-001~003`, Class B)**:
  - The UI layer runs in an isolated browser renderer or decoupled frontend process.
  - Diagnostic rendering calculations (tissue segmentation polygons, normalized pixel arrays) occur inside the backend core with strictly verified mathematical bounds.
  - A crash or freeze in the UI layer cannot alter pixel calculation data; upon UI refresh, the state is deterministically restored from the backend cache.

---

## 4. SOUP Lifecycle & Anomaly Management (IEC 62304 Clause 5.3.3 & 5.3.4)
Each SOUP item (`SOUP-001` through `SOUP-004`) has been integrated through defensive adapter interfaces with hardware prerequisites (AVX2 CPU instructions, 64-bit OS) and unit regression tests.
