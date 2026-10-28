# Software Maintenance & Problem Resolution Record

> **Document ID**: `DHF-13-MAINT`  
> **Applicable Standards**: IEC 62304:2006+AMD1:2015 Clauses 6, 8 & 9, ISO 13485:2016 Clauses 7.3.9 & 8.5  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 IEC 62304 제6조(유지보수), 제8조(형상관리) 및 제9조(문제해결 프로세스)에 따른 사후 유지보수, 결함 추적 및 형상 기준선 관리 기록부입니다.
> - 이상현상(`ANOM-xxx`)의 심각도(Catastrophic/Critical/Major/Minor) 분류, 근본 원인 분석(RCA), 변경 통제(CCB) 승인 내역 및 형상항목(`CI-xxx`) 동결 정보를 기록합니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Maintenance / QA Engineer | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]` | Lead Software Architect | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]` | Chief Quality & Regulatory Officer | Approved | `[YYYY-MM-DD]` |

---

## 2. Configuration Items Baseline Registry (`CI-xxx`)
| Config Item ID | Item Description | File Path / Repository Reference | Cryptographic SHA-256 Digest | Status |
| :--- | :--- | :--- | :--- | :--- |
| `CI-001` | Release Production Docker Image | `registry.hospital.org/samd:1.0.0` | `sha256:7f83b1657ff1...` | Frozen |
| `CI-002` | Segmentation Model Weights | `models/tissue_segmenter_v1.onnx` | `sha256:3a41b2c45e6f...` | Frozen |
| `CI-003` | Grounded System Prompts | `prompts/clinical_eval_prompt.json` | `sha256:1b2c3d4e5f6a...` | Frozen |

---

## 3. Anomaly & Problem Resolution Log (`ANOM-xxx`)
| Anomaly ID | Severity Level | Defect Description | Root Cause Analysis (RCA) | Corrective Action & Verification | CCB Approval |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `ANOM-001` | `Critical` | Tile cache memory leak under rapid 40x panning | Missing unbounded dictionary eviction in caching loop | Implemented bounded LRU cache with 2.0GB cap; verified via `TC-SYS-005` | Approved |
| `ANOM-002` | `Minor` | Minor status bar text clipping on 1080p display | Fixed pixel width in CSS style | Converted layout to responsive Flexbox; verified via `TC-USE-002` | Approved |

---

## 4. Maintenance Patch Release History
| Release Version | Patch Type | Associated Anomaly / CR ID | Regression Test Pass Rate | Release Sign-off |
| :--- | :--- | :--- | :--- | :--- |
| `v1.0.1` | Bugfix Hotfix | `ANOM-001` | 100% (All 10 Verification Suites Passed) | Approved |
