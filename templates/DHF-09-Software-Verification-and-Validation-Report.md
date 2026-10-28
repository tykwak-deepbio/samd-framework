# Software Verification and Validation (V&V) Report

> **Document ID**: `DHF-09-VNV`  
> **Applicable Standards**: IEC 62304:2006+AMD1:2015 Clause 5.6 & 5.7, ISO 13485:2016 Clause 7.3.6 & 7.3.7, IEC 62366-1:2015  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 IEC 62304 Clause 5.6(통합테스트) 및 5.7(시스템테스트), 그리고 ISO 13485 설계 검증(Verification) 및 유효성확인(Validation) 결과를 집대성한 종합 V&V 보고서입니다.
> - 단위 테스트(`TC-UNIT-*`), 통합 테스트(`TC-INT-*`), 시스템 테스트(`TC-SYS-*`), AI 성능평가(`TC-AI-*`), 사용적합성 테스트(`TC-USE-*`), 보안 테스트(`TC-SEC-*`)의 실행 결과 및 증적(`VERIF-xxx`), 결함(Anomaly) 처리 내역을 기술합니다.
> - 테스트 책임자는 개발자로부터 독립된 검증 담당자(Independent Tester)이어야 합니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Independent V&V Test Engineer | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Software Quality Assurance Manager | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Chief Technology Officer | Approved | `[YYYY-MM-DD]` |

---

## 2. Test Execution Summary

| Test Level | Total Test Cases | Passed | Failed | Blocked | Pass Rate |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Unit Verification (`TC-UNIT-`)** | `[e.g., 18]` | `[18]` | 0 | 0 | **100%** |
| **Integration Testing (`TC-INT-`)**| `[e.g., 6]` | `[6]` | 0 | 0 | **100%** |
| **System Testing (`TC-SYS-`)** | `[e.g., 8]` | `[8]` | 0 | 0 | **100%** |
| **AI Validation (`TC-AI-`)** | `[e.g., 4]` | `[4]` | 0 | 0 | **100%** |
| **Cybersecurity Testing (`TC-SEC-`)**| `[e.g., 4]`| `[4]` | 0 | 0 | **100%** |
| **Usability Evaluation (`TC-USE-`)** | `[e.g., 3]` | `[3]` | 0 | 0 | **100%** |
| **Total** | `[43]` | `[43]` | **0** | **0** | **100%** |

---

## 3. Detailed Verification Protocol & Results (`TC-xxx` & `VERIF-xxx`)

| Test Case ID | Test Level & Target Requirement | Test Objective & Execution Procedure | Expected Acceptance Criteria | Actual Result | Verification Evidence ID | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `TC-SYS-001` | System (`REQ-SW-001`) | Ingest standard multi-resolution WSI formats (SVS, NDPI, TIFF). | Successful header parse, levels $> 3$, dimensions loaded without error. | All 3 formats parsed correctly. | `VERIF-001` | **PASS** |
| `TC-SYS-003` | System (`REQ-SW-003`) | Apply Macenko stain normalization on multi-scanner test slides. | Background illumination normalized, stain variation reduced ($\Delta E_{00} \le 3.0$). | Mean $\Delta E_{00} = 2.45 \le 3.0$. | `VERIF-002` | **PASS** |
| `TC-SYS-005` | System (`REQ-SW-005`, `RCM-004`) | Measure tile rendering latency and memory cache ceiling under heavy panning. | Latency $\le 150\text{ ms}$, memory usage $\le 2048\text{ MB}$. | Mean latency: $84\text{ ms}$; Peak RAM: $1840\text{ MB}$. | `VERIF-003` | **PASS** |
| `TC-SYS-007` | System (`REQ-SW-007`, `RCM-001`) | Inject artificially degraded/faint slide with low segmentation confidence ($< 0.60$). | Display low-confidence warning banner and show unsegmented view. | Banner displayed; raw slide accessible. | `VERIF-004` | **PASS** |
| `TC-AI-001` | AI Valid. (`REQ-SW-002`, `CLIN-REQ-001`) | Evaluate tissue segmentation on independent multi-scanner test cohort ($N=100$). | Dice $\ge 0.92$, IoU $\ge 0.85$, False positive rate $\le 2.5\%$. | Mean Dice: 0.948; Mean IoU: 0.891; FPR: 1.8%. | `VERIF-005` | **PASS** |
| `TC-UNIT-003`| Unit (`REQ-SW-009`, `RCM-003`) | Test OD clamping function against extreme high/low RGB inputs. | Clamps all values to $[0.01, 2.50]$; no NaN/Inf or black clipping. | 100% outputs within bounds $[0.01, 2.50]$. | `VERIF-006` | **PASS** |
| `TC-SEC-001` | Security (`REQ-SW-010`, `SEC-CTL-002`) | Inspect outbound image metadata stream for DICOM patient tags. | Zero PHI tags present in serialized JSON/cache. | 0 PHI fields detected. | `VERIF-007` | **PASS** |
| `TC-USE-001` | Usability (`REQ-SW-008`, `RCM-002`) | Pathologist evaluation of raw vs. normalized toggle responsiveness. | Instant switch without lag; clear indicator active. | Pathologist rated $5/5$ clarity; zero mode confusion. | `VERIF-008` | **PASS** |

---

## 4. Anomaly Tracking & Resolution (IEC 62304 Clause 9)
- Total Anomalies Discovered: `[0 open]`
- All identified test discrepancies during preliminary runs were resolved and successfully re-verified via regression tests.

---

## 5. Independent V&V Conclusion
The software has successfully satisfied all functional, performance, safety, security, and usability requirements. The design outputs conform strictly to the design inputs, verifying compliance with IEC 62304 and ISO 13485.
