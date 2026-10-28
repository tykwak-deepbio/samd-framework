---
name: samd-detailed-design
description: Authors detailed software design specifications under IEC 62304 Clause 5.4 down to software units, algorithmic mathematical definitions, API contracts, data schemas, and fail-safe handlers. Use this skill when authoring detailed unit designs or DHF-08.
---

# SaMD Detailed Software Design Specification (DDS)

This skill executes Phase 8 of the SaMD lifecycle, complying with **IEC 62304:2006/AMD1:2015 Clause 5.4 (Software detailed design)**.

## Goal
Specify the internal logic, algorithms, mathematical equations, data structures, and interfaces of each software unit (`DDS-xxx`), ensuring full traceability from `ARCH-xxx` and authoring **`DHF-08-Software-Detailed-Design-Specification-DDS.md`**.

## Design Requirements for Software Units

1. **Algorithmic & Mathematical Formalism**:
   - Explicitly define image transformations:
     * Optical Density (OD): $OD = -\log_{10}\left(\frac{I + 1}{I_0}\right)$
     * Macenko stain matrix deconvolution and pseudo-inverse calculation.
     * Tensor dimensions, quantization (e.g. FP32 vs INT8), input scaling $[0, 1]$ or $[-1, 1]$.
2. **Interface Specifications & Data Schemas**:
   - Function signatures, parameter types, return values, and exceptions.
   - Tile coordinate systems $(x, y, \text{level}, \text{width}, \text{height})$.
   - GeoJSON polygon format for tissue boundary annotations.
3. **Defensive Error Handling & Bounds Checking**:
   - Division by zero in stain vector calculation.
   - Out-of-bounds tile coordinates outside pyramid extents.
   - Corrupt tile or truncated file stream recovery.
4. **Safety & Usability Details (IEC 62366-1)**:
   - On-screen visual indicators when color correction is toggled on/off.
   - Pathologist warning banner when AI model confidence drops below safety threshold ($< 0.60$).

## Procedure
1. Break down architecture components into detailed software units (`DDS-xxx`).
2. Document class/module definitions, data flows, and state machines.
3. Map every `DDS-xxx` to its parent `ARCH-xxx` and corresponding `REQ-SW-xxx`.
4. Populate `templates/DHF-08-Software-Detailed-Design-Specification-DDS.md`.
