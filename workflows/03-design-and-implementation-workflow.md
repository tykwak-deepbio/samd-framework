# Design & Implementation Workflow (Phases 7, 8, 9)

> **Framework Guide**: `WF-03-DESIGN-IMPL`  
> **Key Agents**: `system-architect-agent`, `detailed-design-agent`, `software-developer-agent`  
> **Applicable Standards**: IEC 62304 Clause 5.3, 5.4, 5.5, ISO 13485 Clause 7.3.4  

---

## 1. Phase 7: System & High-Level Software Architecture
1. The `system-architect-agent` partitions software items into functional and architectural components (`ARCH-xxx`).
2. **Safety Segregation (IEC 62304 Clause 5.3.5)**:
   - Formally document the segregation between Class A UI layers and Class B diagnostic engines.
   - Prove that failure or resource exhaustion in UI/telemetry cannot corrupt image calculation or cause hazardous state.
3. **SOUP Evaluation (IEC 62304 Clause 5.3.3 & 5.3.4)**:
   - Identify all third-party libraries (OpenSlide, ONNX Runtime, NumPy, Scikit-Image).
   - Document published anomalies, hardware/software prerequisites, and defensive wrapper boundaries.
4. Output: `dhf/DHF-07-Software-Architectural-Design-Specification-SDS.md`.

---

## 2. Phase 8: Detailed Software Design (DDS)
1. The `detailed-design-agent` refines architecture components down to software units (`DDS-xxx`).
2. Specify exact algorithmic formulas:
   - Optical Density transformation:
     $$OD = -\log_{10}\left(\frac{\max(I, 1)}{255.0}\right)$$
   - Macenko stain matrix deconvolution and pseudo-inverse calculations.
   - Bounded numerical clamping $[0.01, 2.50]$ to prevent black clipping.
3. Define class and function signatures with explicit type hints, parameters, return types, and exceptions.
4. Detail the LRU caching policy and tile eviction algorithm.
5. Output: `dhf/DHF-08-Software-Detailed-Design-Specification-DDS.md`.

---

## 3. Phase 9: Regulated Software Implementation & Unit Verification
1. The `software-developer-agent` implements production code in `src/`.
2. **Traceability in Docstrings**:
   - Every function and class must contain comments tracing back to requirements:
     ```python
     # Traces: REQ-SW-003, DDS-002, RCM-003
     def convert_rgb_to_od(rgb_array: np.ndarray) -> np.ndarray:
         ...
     ```
3. **Defensive Programming Standards**:
   - Bounds validation on all incoming coordinates and array dimensions.
   - NaN, Inf, and zero-division prevention.
   - Non-root containerized execution.
4. **Unit Verification (IEC 62304 Clause 5.5.3)**:
   - Write unit tests in `tests/` covering normal, boundary, and error branches.
   - Execute tests using `pytest` ensuring $\ge 90\%$ branch/statement coverage on safety-critical units.
   - Record unit verification evidence (`VERIF-UNIT-xxx`).
