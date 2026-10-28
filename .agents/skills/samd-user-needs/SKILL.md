---
name: samd-user-needs
description: Conducts interactive user and clinical requirement discovery Q&A to capture intended use, target patient population, clinical environment, and high-level functional/non-functional requirements. Use this skill when defining product concept, user requirements, or authoring DHF-01.
---

# SaMD User Needs & Intended Purpose Discovery

This skill executes Phase 1 of the SaMD lifecycle, complying with **ISO 13485:2016 Clause 7.3.2 (Design Inputs)**, **IEC 62304 Clause 5.1**, and **IEC 62366-1:2015 (Usability Engineering User Profile)**.

## Goal
Conduct a structured Q&A session with the project stakeholders/user to extract comprehensive clinical and technical requirements, producing the formal **`DHF-01-Intended-Use-and-URD.md`** document.

## Interactive Discovery Protocol (Core Questions)

The agent MUST present the following structured inquiry to the user (or retrieve from project briefs):

1. **Intended Purpose / Medical Purpose (사용목적)**:
   - What specific medical, diagnostic, or therapeutic task does this software perform?
   - Is it an adjunct/triage tool, diagnostic aid (CADe/CADx), or autonomous diagnostic device?
2. **Clinical Indications & Specimen/Modality (적응증 및 대상 검체)**:
   - What disease/condition, organ tissue, or biological specimen is analyzed?
   - What input formats are ingested (e.g. WSI formats: SVS, NDPI, TIFF, DICOM Supplement 145)?
3. **Target Patient Population & Contraindications (환자군 및 금기사항)**:
   - What is the target demographic (adults, pediatrics, all patients)?
   - What are the explicit contraindications (e.g. frozen sections, thick cytology, heavy artifacts)?
4. **Intended User Profile & Operating Environment (사용자 및 사용환경)**:
   - Who interacts with the software (board-certified pathologists, lab techs, oncologists)?
   - Where is it deployed (hospital intranet, secure cloud, pathology viewing workstations)?
5. **High-Level Functional Requirements (상위 기능 요구사항)**:
   - Image ingestion, multi-resolution pyramid navigation, panning/zooming.
   - AI algorithms: tissue boundary segmentation, background/glass artifact filtering.
   - Image processing: stain/color normalization across multi-vendor scanners.
6. **Non-Functional Requirements (성능, 안전성, 사용성 요건)**:
   - Tile rendering latency (e.g., < 200ms per 512x512 tile), peak memory usage.
   - Data privacy (anonymization/de-identification of patient metadata).
   - Display color accuracy and fidelity.

## Procedure

1. **Conduct Q&A**: Solicit missing items from user or review project documentation.
2. **Assign Unique Identifiers**:
   - Every requirement must have a tag: `USER-REQ-001`, `USER-REQ-002`, etc.
   - Categorize by: Functional (`[FUNC]`), Performance (`[PERF]`), Usability (`[USE]`), Safety (`[SAFE]`), Interface (`[INTF]`).
3. **Draft Deliverable**:
   - Populate `templates/DHF-01-Intended-Use-and-URD.md`.
   - Save to `dhf/DHF-01-Intended-Use-and-URD.md`.
4. **Verification**:
   - Confirm all core questions are answered without ambiguous phrases (e.g. "fast", "user-friendly" must be quantified).
