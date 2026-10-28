---
name: samd-arch-design
description: Authors high-level system and software architectural designs under IEC 62304 Clause 5.3, including safety segregation, SOUP evaluation, AI pipeline architecture, and hardware/OS interface specifications. Use this skill when designing architecture or authoring DHF-07.
---

# SaMD Software Architectural Design Specification (SDS)

This skill executes Phase 7 of the SaMD lifecycle, complying with **IEC 62304:2006/AMD1:2015 Clause 5.3 (Software architectural design)**.

## Goal
Decompose software requirements into software items and architecture components (`ARCH-xxx`), define interfaces and data flow, enforce safety segregation, evaluate SOUP items, and author **`DHF-07-Software-Architectural-Design-Specification-SDS.md`**.

## Key Architectural Principles

1. **Safety Segregation (IEC 62304 Clause 5.3.5)**:
   - Segregate safety-critical units (e.g. AI tissue segmentation engine, color normalization calculation, image pixel rendering) from non-safety-critical units (e.g. UI theme, user session metrics, export formatting).
   - Ensure a crash or resource leak in a non-critical unit cannot corrupt diagnostic display.
2. **AI/ML Pipeline Architecture**:
   - Ingestion Layer: Multi-resolution WSI reader (OpenSlide/Bio-Formats wrapper).
   - Preprocessing: Downsampled overview generation, background thresholding.
   - Inference Engine: Deep learning segmentation runtime (ONNX Runtime / TensorRT).
   - Post-Processing: Contour extraction, polygon simplification, confidence heatmaps.
   - Normalization Engine: Optical density conversion, stain matrix estimation, color transfer.
   - Display/Streaming Engine: Dynamic multi-threaded tile caching, viewport panning/zooming.
3. **SOUP (Software of Unknown Provenance) Management**:
   - Every third-party library (e.g. OpenSlide, LibTIFF, OpenCV, ONNX Runtime, NumPy) must be identified (`SOUP-xxx`).
   - Document published anomalies, hardware/software prerequisites, and risk control measures.

## Procedure
1. Create architecture block diagrams and component definitions (`ARCH-001`, `ARCH-002`, ...).
2. Trace all `REQ-SW-xxx` to at least one `ARCH-xxx`.
3. Complete SOUP risk assessment table.
4. Populate `templates/DHF-07-Software-Architectural-Design-Specification-SDS.md`.
