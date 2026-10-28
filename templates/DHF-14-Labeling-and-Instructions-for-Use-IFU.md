# Medical Device Labeling & Instructions for Use (IFU)

> **Document ID**: `DHF-14-LBL`  
> **Applicable Standards**: ISO 13485:2016 Clause 7.2.3 & 7.3.7, IEC 62366-1:2015 Clause 5.9, 21 CFR Part 801, EU MDR (2017/745) / IVDR (2017/746) Annex I Chapter III, MFDS 의료기기 표시·기재 등에 관한 규정  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 ISO 13485:2016 Cl 7.3.7, 21 CFR 801, EU MDR/IVDR Annex I Chapter III 및 한국 식약처 표시·기재 규정에 따른 소프트웨어 의료기기(SaMD)의 정식 라벨링 및 전자 사용설명서(e-IFU) 문서입니다.
> - 제품 식별 정보, 고유식별코드(UDI), 사용 목적(Intended Purpose), 적응증(Indications for Use), 금기사항(Contraindications), 임상적 경고 및 주의사항을 명시합니다.
> - 위험관리파일(`DHF-05B`)에서 도출된 "안전을 위한 정보(Information for Safety)" 형태의 모든 위험통제조치가 본 라벨링 및 설명서에 100% 반영되어야 합니다.
> - 소프트웨어 GUI 내의 "About / 규제 라벨" 대화상자 명세 및 최소/권장 컴퓨팅 하드웨어 환경을 포함합니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Regulatory Affairs / Technical Writer | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]` | Lead Medical / Clinical Specialist | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]` | Chief Regulatory / Quality Officer | Approved | `[YYYY-MM-DD]` |

---

## 2. Device Identification & Regulatory Labeling

### 2.1 Software Identification
- **Proprietary Name**: `[e.g., DeepBio SaMD Pathology Assistant]`
- **Model / System Identifier**: `[e.g., DPA-WSI-100]`
- **Software Version**: `[Major.Minor.Patch, e.g., 1.0.0]`
- **Build / Checksum**: `[SHA-256 build hash]`
- **Legal Manufacturer**: `[Company Name, Address, Contact, Country of Origin]`
- **EU Authorized Representative (EC REP)**: `[Authorized Representative Name, Address]`

### 2.2 Unique Device Identification (UDI)
- **Basic UDI-DI / Device Identifier**: `[e.g., 8809123456789DPA-WSI100]`
- **UDI-PI (Production Identifier)**: Software Version `[1.0.0]` + Release Date `[YYYY-MM-DD]`
- **Label Placement**: GUI "About / System Information" window, splash screen, and electronic distribution package metadata.

---

## 3. Clinical Intent, Indications & Contraindications

### 3.1 Intended Medical Purpose (`USER-REQ-001`)
- `[Detailed description of clinical diagnostic support purpose, target disease, and anatomical site]`

### 3.2 Target Patient Population & Intended Users
- **Target Population**: `[e.g., Adult male patients >= 18 years undergoing prostate needle biopsy]`
- **Intended Users**: `[e.g., Qualified, board-certified anatomical pathologists]`

### 3.3 Absolute & Relative Contraindications
- **Contraindications**:
  1. `[e.g., Not for use with frozen section histology or cytology specimens]`
  2. `[e.g., Not intended for standalone primary diagnosis without human pathologist review]`

---

## 4. Clinical Warnings & Precautions (Risk Control Measure Traceability)

| Warning ID | Statutory Labeling / IFU Warning Text | Associated Risk Hazard | RCM ID |
| :--- | :--- | :--- | :--- |
| `WARN-01` | **CAUTION**: AI tissue detection is an adjunctive aid. Pathologists must inspect entire glass slide before clinical sign-off. | `RSK-FW-001` (False Negative AI Miss) | `RCM-FW-001` |
| `WARN-02` | **WARNING**: Do not evaluate slides with severe scanner blur, air bubbles, or tissue folds exceeding 15% of ROI. | `RSK-FW-002` (Input Image Degradation) | `RCM-FW-002` |
| `WARN-03` | **SECURITY NOTICE**: Ensure DICOM / WSI images are transferred over encrypted TLS 1.3 channels only. | `RSK-FW-005` (Unencrypted PHI Transit) | `RCM-FW-005` |

---

## 5. Technical Requirements & Operating Environment

### 5.1 Computing Hardware & OS Prerequisites
- **Processor**: `[e.g., x86-64 8-Core CPU >= 3.0 GHz]`
- **Memory (RAM)**: `[e.g., Minimum 32GB, Recommended 64GB DDR4/DDR5]`
- **GPU / Accelerator**: `[e.g., NVIDIA RTX 4080 or better, CUDA Compute Capability >= 8.9]`
- **Operating System**: `[e.g., Ubuntu 22.04 LTS / Windows 11 Enterprise 64-bit]`
- **Display**: `[e.g., Medical-grade calibrated monitor >= 4K resolution, 100% sRGB / DCI-P3]`
- **Network Bandwidth**: `[e.g., Dedicated 1 Gbps LAN for PACS / WSI transfer]`

---

## 6. Software Installation, Operation & Maintenance Instructions
- **Installation Verification**: `[Step-by-step instructions for running built-in self-tests (POST) and checksum verification]`
- **Clinical Workflow Guide**: `[Opening cases, navigating WSI viewer, interpreting AI confidence overlays, exporting reports]`
- **Cybersecurity & Data Privacy Guidelines**: `[Role-based access setup, audit trail review, password hygiene]`
- **Troubleshooting & Technical Support**: `[Error codes, manufacturer customer support hotline, email, and anomaly reporting]`
