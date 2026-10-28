# Cybersecurity Threat Model & Software Bill of Materials (SBOM)

> **Document ID**: `DHF-06-CYBER`  
> **Applicable Standards**: IEC 81001-5-1:2021, ISO 27001:2022, ISO 27799:2016, FDA 2023 Premarket Cybersecurity, IMDRF N60/N73  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 FDA 사이버보안 가이드라인 및 식약처 의료기기 사이버보안 허가심사 가이드라인에 따른 사이버보안 위협 모델링(STRIDE) 및 소프트웨어 자재명세서(SBOM) 문서입니다.
> - 데이터 흐름도(DFD), 신뢰 경계(Trust Boundaries), 6대 위협(Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege)에 대한 보안 통제 조치(`SEC-CTL-xxx`)를 수립합니다.
> - 모든 외부 라이브러리/오픈소스(SOUP)에 대한 SBOM(버전, 공급자, 라이선스, SHA256 해시, 알려진 CVE 취약점 분석)을 포함합니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Cybersecurity Engineer | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Systems Architecture Lead | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Chief Information Security Officer | Approved | `[YYYY-MM-DD]` |

---

## 2. System Architecture & Trust Boundaries (STRIDE)
- **Trust Boundary 1**: Public Internet / Untrusted Network <--> Hospital Reverse Proxy.
- **Trust Boundary 2**: Viewer Client Browser <--> SaMD Backend Tile Streaming Server.
- **Trust Boundary 3**: Backend Server <--> PACS / WSI Storage Archive.
- **Trust Boundary 4**: Backend Server <--> AI Model Inference Runtime.

---

## 3. Threat Modeling & Security Controls (`SEC-THR-xxx` & `SEC-CTL-xxx`)

| Threat ID | STRIDE Category | Threat Description & Attack Vector | Impacted Asset | Risk Level | Security Mitigation Control (`SEC-CTL-xxx`) | Traced Requirement | Verification Test |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| `SEC-THR-001` | **Tampering** | Man-in-the-Middle modifies slide tiles or AI segmentation polygon coordinates during transmission. | Image tile stream | High | `SEC-CTL-001`: Enforce TLS 1.3 with AES-256-GCM cipher suite and SHA-256 tile integrity verification. | `REQ-SW-011` | `TC-SEC-002` |
| `SEC-THR-002` | **Info Disclosure** | Interception of DICOM WSI headers containing sensitive patient identifiers (PHI/PII). | Patient PHI | Critical | `SEC-CTL-002`: Implement automated de-identification scrubbing all 21 HIPAA/DICOM Patient tags before ingestion/caching. | `REQ-SW-010` | `TC-SEC-001` |
| `SEC-THR-003` | **Elevation of Priv.** | Unauthorized user attempts to execute arbitrary code via malicious uploaded image header payload. | Backend Server | High | `SEC-CTL-003`: Strict image header parser sanitization and containerized sandbox isolation with non-root user execution. | `REQ-SW-001` | `TC-SEC-003` |
| `SEC-THR-004` | **Denial of Service** | Flooding backend tile API endpoints with out-of-bounds coordinate requests exhausts server memory. | Viewing Service | Medium | `SEC-CTL-004`: Rate-limiting (max 100 req/sec per token) and coordinate boundary validation before tile dispatch. | `REQ-SW-005` | `TC-SEC-004` |

---

## 4. Software Bill of Materials (SBOM) & Vulnerability Catalog

| SOUP ID | Component Name | Version | Supplier / Origin | License | Cryptographic Hash (SHA-256) | Known CVEs | Vulnerability Assessment & Mitigation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `SOUP-001` | OpenSlide / TiffFile | 3.4.1 | OpenSlide Team | LGPL-2.1 | `e3b0c442...` | None active | Safe for WSI pyramidal decoding. Isolated in sandboxed worker. |
| `SOUP-002` | ONNX Runtime | 1.16.3 | Microsoft Corp. | MIT | `a1b2c3d4...` | None active | Model weights verified with SHA-256 before loading. |
| `SOUP-003` | NumPy | 1.24.4 | NumPy Developers | BSD-3-Clause | `f5e6d7c8...` | None active | Standard numerical computing library. |
| `SOUP-004` | Scikit-Image | 0.22.0 | Scikit-Image Team| BSD-3-Clause | `1234abcd...` | None active | Color space transformation and morphological filtering. |

---

## 5. Post-Market Vulnerability Management Plan
- Monthly automated CVE scanning against NIST National Vulnerability Database (NVD).
- Coordinated Vulnerability Disclosure (CVD) email: `security@company.com`.
- Critical security patch SLA: Patch release within 14 calendar days for CVSS $\ge 7.0$.
