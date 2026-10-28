# Software Requirements Specification (SRS)

> **Document ID**: `DHF-04-SRS`  
> **Applicable Standards**: IEC 62304:2006+AMD1:2015 Clause 5.2, ISO 13485:2016 Clause 7.3.3  
> **Project Name**: `[Project / Device Name]`  
> **Software Safety Class**: `[Class B]` (IEC 62304)  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 IEC 62304 Clause 5.2(소프트웨어 요구사항 분석)에 따라 작성되는 기술적 핵심 문서입니다.
> - 사용자 요구사항(`USER-REQ-*`), 규제 요구사항(`REG-REQ-*`), 임상 요구사항(`CLIN-REQ-*`), 위험통제조치(`RCM-*`)를 소프트웨어 기능, 성능, 인터페이스, 안전성, 사이버보안 요구사항으로 구체화합니다.
> - 모든 요구사항에는 고유 번호(`REQ-SW-xxx`)를 부여하며, 애매모호한 표현을 배제하고 객관적으로 테스트 가능한(Testable/Verifiable) 판정 기준을 명시해야 합니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Lead Software Systems Analyst | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Software Architecture Lead | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Software Quality Assurance Director | Approved | `[YYYY-MM-DD]` |

---

## 2. Software Safety Classification Justification
- **Assigned Safety Class**: **Class B** (under IEC 62304 Clause 4.3).
- **Justification**: In the event of a software failure or incorrect output (e.g. tissue false-negative or color distortion), non-serious injury or diagnostic delay is possible, but death or irreversible serious injury is precluded because the final diagnostic determination rests with the certified pathologist.

---

## 3. Software Requirements Catalog (`REQ-SW-xxx`)

### 3.1 Functional Requirements (`[FUNC]`)

| ID | Description | Safety Class | Traces Backward | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| `REQ-SW-001` | The software shall ingest multi-resolution pyramidal WSI files in SVS, NDPI, and generic TIFF formats. | Class B | `USER-REQ-001` | System Test (`TC-SYS-001`) |
| `REQ-SW-002` | The software shall execute AI tissue segmentation on downsampled overview thumbnails, outputting polygon contours of valid tissue areas. | Class B | `USER-REQ-002`, `CLIN-REQ-001` | AI Performance Test (`TC-AI-001`) |
| `REQ-SW-003` | The software shall apply Optical Density (OD) stain deconvolution (Macenko method) to normalize background illumination and H&E chromogen intensity. | Class B | `USER-REQ-003`, `CLIN-REQ-003` | Algorithm Test (`TC-SYS-003`) |
| `REQ-SW-004` | The software shall provide deep zoom and panning navigation across pyramid magnification levels (1.25x to 40x). | Class A | `USER-REQ-001` | Integration Test (`TC-INT-001`) |

### 3.2 Performance Requirements (`[PERF]`)

| ID | Description | Acceptance Criteria | Traces Backward | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| `REQ-SW-005` | Pyramidal tile fetch and render latency. | $\le 150\text{ ms}$ for $512\times 512$ tile at 20x magnification. | `USER-REQ-004` | Benchmark Test (`TC-SYS-005`) |
| `REQ-SW-006` | Total slide overview tissue segmentation runtime. | $\le 2.5\text{ seconds}$ on standard clinical GPU workstation. | `USER-REQ-004` | Benchmark Test (`TC-SYS-006`) |

### 3.3 Safety & Fail-Safe Requirements (`[SAFE]`)

| ID | Description | Rationale / Risk Control | Traces Backward | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| `REQ-SW-007` | If mean AI tissue segmentation confidence is below 0.60, the system shall display a visible on-screen warning banner. | Prevents silent omission of faint or pale biopsy tissue. | `USER-REQ-005`, `RCM-001` | System Test (`TC-SYS-007`) |
| `REQ-SW-008` | The user interface shall provide an instant toggle switch allowing immediate viewing of unnormalized raw RGB pixels. | Mitigates risk of diagnostic confusion due to over-correction. | `USER-REQ-005`, `RCM-002` | Usability Test (`TC-USE-001`) |
| `REQ-SW-009` | The stain normalization engine shall clamp OD saturation vectors to $[0.01, 2.50]$ to prevent pixel clipping. | Prevents loss of nuclear chromatin detail in dense areas. | `RCM-003` | Unit Test (`TC-UNIT-003`) |

### 3.4 Interface & Security Requirements (`[INTF]`, `[SEC]`)

| ID | Description | Standards Compliance | Traces Backward | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| `REQ-SW-010` | The software shall scrub all patient identifiable information (PHI) from DICOM/WSI headers prior to caching. | ISO 27799 / HIPAA | `USER-REQ-006`, `REG-REQ-003` | Security Test (`TC-SEC-001`) |
| `REQ-SW-011` | Client-server communication shall mandate TLS 1.3 with AES-256-GCM cipher suites. | IEC 81001-5-1 | `USER-REQ-006`, `REG-REQ-002` | Security Test (`TC-SEC-002`) |
