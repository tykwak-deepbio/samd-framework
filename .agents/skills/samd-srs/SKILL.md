---
name: samd-srs
description: Transforms user needs, regulatory mandates, and clinical requirements into formal, verifiable software requirements conforming to IEC 62304 Clause 5.2. Use this skill when drafting or updating the Software Requirements Specification (SRS) or DHF-04.
---

# SaMD Software Requirements Specification (SRS) Authoring

This skill executes Phase 4 of the SaMD lifecycle, complying with **IEC 62304:2006/AMD1:2015 Clause 5.2 (Software requirements analysis)**, **ISO 13485:2016 Clause 7.3.3 (Design Inputs)**, and **IEEE 830 / ISO/IEC/IEEE 29148**.

## Goal
Translate User Needs (`USER-REQ-*`), Regulatory Requirements (`REG-REQ-*`), and Clinical Requirements (`CLIN-REQ-*`) into clear, unambiguous, testable software requirements, and author **`DHF-04-Software-Requirements-Specification-SRS.md`**.

## Requirement Categorization Standard

Every software requirement MUST be assigned a unique ID (`REQ-SW-xxx`) and categorized:

1. **Functional Requirements (`[FUNC]`)**:
   - WSI pyramidal tile ingestion, deep zoom / pan rendering.
   - AI tissue boundary detection, polygon contour extraction.
   - Background illumination & stain color normalization (e.g. Macenko decomposition).
2. **Performance Requirements (`[PERF]`)**:
   - Latency thresholds (e.g. tile response time < 150ms over 1Gbps LAN).
   - Throughput (e.g. processing whole slide thumbnail < 3.0s).
   - Resource consumption limits (RAM < 8GB, GPU VRAM < 6GB).
3. **Safety & Fail-Safe Requirements (`[SAFE]`)**:
   - Detection failure fallback (notify pathologist if tissue confidence < 0.60, display unsegmented slide).
   - Color normalization clamp limits (prevent clipping or artificial saturation shifts).
4. **Interface & Data Requirements (`[INTF]`, `[DATA]`)**:
   - Ingestion: SVS, NDPI, TIFF, DICOM PS 3.3.
   - Export: GeoJSON / DICOM-ANN annotation format, PNG/JPEG snapshots.
5. **Security & Privacy Requirements (`[SEC]`)**:
   - De-identification of patient tags in DICOM headers before AI cloud processing.
   - Role-based access control (RBAC), TLS 1.3 encryption.
6. **Usability Requirements (`[USE]`)**:
   - Color blindness palette options, zoom level indicator, split-screen raw vs. normalized view.

## Verification Checklist

For each requirement:
- [ ] Is it uniquely numbered (`REQ-SW-xxx`)?
- [ ] Does it map directly to at least one `USER-REQ-xxx` or `REG-REQ-xxx`?
- [ ] Is it objectively verifiable (verifiable by unit, integration, or system test)?
- [ ] Is safety classification specified for each requirement?
- [ ] Is `DHF-04-Software-Requirements-Specification-SRS.md` generated and committed?
