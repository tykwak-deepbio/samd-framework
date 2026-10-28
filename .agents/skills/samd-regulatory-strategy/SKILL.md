---
name: samd-regulatory-strategy
description: Analyzes multi-jurisdiction regulatory requirements (MFDS, FDA, EU IVDR/MDR, IMDRF), determines device classification, clearance pathways, applicable standards, and PCCP strategies. Use this skill when establishing regulatory strategy or authoring DHF-03.
---

# SaMD Regulatory Affairs & Classification Strategy

This skill executes Phase 3 of the SaMD lifecycle, complying with **IMDRF SaMD Framework (N12/N23)**, **Korea MFDS 규정**, **US FDA 21 CFR & Guidance**, and **EU IVDR 2017/746**.

## Goal
Map the target SaMD to relevant medical device classifications in major target markets, identify regulatory submission pathways, determine applicable consensus standards, and author **`DHF-03-Regulatory-Strategy-and-Clearance-Profile.md`**.

## Multi-Jurisdiction Classification Matrix

The agent analyzes the intended use against regional classification rules:

| Jurisdiction | Authority | Key Classification Framework | Typical SaMD Target (WSI / AI Viewer) | Submission Pathway |
| :--- | :--- | :--- | :--- | :--- |
| **South Korea** | **MFDS (식품의약품안전처)** | 의료기기 품목 및 등급 지정에 관한 규정 / 체외진단의료기기법 | Class II (의료영상 전처리/전송 소프트웨어) or Class III (암 진단보조) | 기술문서 심사 및 임상시험 성적서 심사 |
| **United States** | **US FDA (CDRH)** | 21 CFR 864.3700 (Whole slide imaging system) / 21 CFR 892.2050 | Class II (Product Code: PKS, QPN) | 510(k) Premarket Notification (or De Novo if novel) |
| **European Union**| **EU MDR / IVDR** | EU IVDR 2017/746 Annex VIII (Rule 1, Rule 3, Rule 4) | Class B (General IVD SaMD) or Class C (Cancer staging/grading adjunct) | Notified Body Conformity Assessment (CE Mark) |
| **Global** | **IMDRF** | IMDRF N12 (Risk Categorization Matrix) | Category II or III (Impact on patient management) | Global Harmonized Dossier |

## Core Regulatory Work Items

1. **Applicable Consensus Standards Identification**:
   - Quality Management: ISO 13485:2016
   - Risk Management: ISO 14971:2019 / ISO/TR 24971:2020
   - Software Lifecycle: IEC 62304:2006+AMD1:2015 (Declare Class A, B, or C)
   - Usability Engineering: IEC 62366-1:2015+AMD1:2020
   - Cybersecurity: IEC 81001-5-1:2021, ISO 27001/27799, FDA 2023 Cybersecurity
   - Interoperability / Medical Imaging: DICOM (PS 3.1 - 3.22, Supp 145), HL7 FHIR
2. **AI/ML Lifecycle & PCCP (Predetermined Change Control Plan)**:
   - Determine if model updates require pre-clearance under FDA PCCP guidance and MFDS 인공지능 변경허가 가이드라인.
3. **Draft Deliverable**:
   - Populate `templates/DHF-03-Regulatory-Strategy-and-Clearance-Profile.md`.
   - Export regulatory requirements (`REG-REQ-xxx`) for SRS injection.
