# Requirements Traceability Matrix (RTM)

> **Document ID**: `DHF-10-RTM`  
> **Applicable Standards**: IEC 62304:2006+AMD1:2015 Clause 5.1.1, 5.2, 5.7, ISO 13485:2016 Clause 7.3.7  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 사용자 요구사항(`USER-REQ`), 규제 요구사항(`REG-REQ`), 소프트웨어 요구사항(`REQ-SW`), 위험요인 및 위험통제조치(`RSK/RCM`), 사이버보안 통제(`SEC-CTL`), 아키텍처 및 상세설계(`ARCH/DDS`), 소스코드 및 검증 테스트(`TC-*`)를 100% 양방향으로 연결하는 추적성 매트릭스(Traceability Matrix)입니다.
> - 식약처, FDA, EU IVDR 기술문서 심사관이 가장 먼저 검토하는 핵심 문서로, 단 하나의 누락이나 고립(Orphan) 항목도 존재하지 않아야 합니다.
> - `python3 scripts/validate_traceability.py`를 실행하여 정합성을 자동 검증할 수 있습니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Lead Quality Assurance Auditor | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Software Development Lead | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Chief Regulatory Officer | Approved | `[YYYY-MM-DD]` |

---

## 2. Complete Bidirectional Traceability Matrix

| User / Reg Need ID | Software Requirement ID (`REQ-SW`) | Risk / Hazard ID (`RSK / RCM`) | Security ID (`SEC-THR / CTL`) | Architecture ID (`ARCH`) | Detailed Design ID (`DDS`) | Implementation File(s) | Verification Test Case (`TC`) | Verification Record (`VERIF`) | Verification Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `USER-REQ-001` | `REQ-SW-001` | - | `SEC-THR-003` / `SEC-CTL-003` | `ARCH-001` | `DDS-001` | `src/imaging/tile_streamer.py` | `TC-SYS-001` | `VERIF-001` | **PASS** |
| `USER-REQ-002`, `CLIN-REQ-001` | `REQ-SW-002` | - | - | `ARCH-003` | `DDS-003` | `src/segmentation/tissue_segmenter.py` | `TC-AI-001` | `VERIF-005` | **PASS** |
| `USER-REQ-003`, `CLIN-REQ-003` | `REQ-SW-003` | - | - | `ARCH-002` | `DDS-002` | `src/normalization/stain_normalizer.py` | `TC-SYS-003` | `VERIF-002` | **PASS** |
| `USER-REQ-001` | `REQ-SW-004` | - | - | `ARCH-001`, `ARCH-005` | `DDS-001` | `src/imaging/tile_streamer.py` | `TC-INT-001` | `VERIF-001` | **PASS** |
| `USER-REQ-004` | `REQ-SW-005` | `RSK-004` / `RCM-004` | `SEC-THR-004` / `SEC-CTL-004` | `ARCH-004` | `DDS-001` | `src/imaging/tile_streamer.py` | `TC-SYS-005` | `VERIF-003` | **PASS** |
| `USER-REQ-004` | `REQ-SW-006` | - | - | `ARCH-003` | `DDS-003` | `src/segmentation/tissue_segmenter.py` | `TC-SYS-006` | `VERIF-005` | **PASS** |
| `USER-REQ-005` | `REQ-SW-007` | `RSK-001` / `RCM-001` | - | `ARCH-003`, `ARCH-005` | `DDS-003` | `src/segmentation/tissue_segmenter.py` | `TC-SYS-007` | `VERIF-004` | **PASS** |
| `USER-REQ-005` | `REQ-SW-008` | `RSK-002` / `RCM-002` | - | `ARCH-005` | `DDS-002` | `src/normalization/stain_normalizer.py` | `TC-USE-001` | `VERIF-008` | **PASS** |
| `RCM-003` | `REQ-SW-009` | `RSK-003` / `RCM-003` | - | `ARCH-002` | `DDS-002` | `src/normalization/stain_normalizer.py` | `TC-UNIT-003` | `VERIF-006` | **PASS** |
| `USER-REQ-006`, `REG-REQ-003` | `REQ-SW-010` | - | `SEC-THR-002` / `SEC-CTL-002` | `ARCH-006` | `DDS-004` | `src/security/deidentifier.py` | `TC-SEC-001` | `VERIF-007` | **PASS** |
| `USER-REQ-006`, `REG-REQ-002` | `REQ-SW-011` | - | `SEC-THR-001` / `SEC-CTL-001` | `ARCH-006` | `DDS-004` | `src/security/deidentifier.py` | `TC-SEC-002` | `VERIF-007` | **PASS** |

---

## 3. Traceability Metrics & Coverage Analysis
- **User Needs Coverage**: 100% (6/6 `USER-REQ-*` mapped to verified software requirements).
- **Software Requirements Coverage**: 100% (11/11 `REQ-SW-*` mapped to designs and passing tests).
- **Risk Control Coverage**: 100% (4/4 `RCM-*` verified in code and tests).
- **Cybersecurity Control Coverage**: 100% (4/4 `SEC-CTL-*` verified).
- **Orphan Items Detected**: **0 items (Zero-Orphan Policy Satisfied)**.
