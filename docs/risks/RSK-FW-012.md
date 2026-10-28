# Risk Analysis: RSK-FW-012

> **Risk ID**: `RSK-FW-012`  
> **Risk Control Measure ID**: `RCM-FW-012`  
> **Title**: Usability Design Flaws, Cognitive Overload & Clinical Use Errors  
> **Standard Reference**: ISO 14971:2019 Clause 5.4, IEC 62366-1:2015+AMD1:2020 Clause 5  
> **Target Requirement**: `FR-USE-001`, `FR-SKILL-004`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-007.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-007.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-USE-001.md`, `docs/tests/TC-FR-SKILL-004.md`  

---

## 1. Hazard, Sequence of Events & Hazardous Situation
- **Hazard**: Flawed user interface design, confusing alert presentation, or ambiguous clinical workflows causing use error.
- **Sequence of Events**:
  1. Framework fails to mandate systematic usability engineering and PCA (Perception, Cognition, Action) error analysis for SaMD user interfaces.
  2. SaMD displays critical diagnostic AI outputs without clear confidence flags, or places emergency fallback controls in obscure menus.
  3. Clinician misperceives AI bounding box, experiences cognitive fatigue, and misses unsegmented malignant micro-lesions.
- **Hazardous Situation**: Clinical user performs incorrect action or fails to take required diagnostic action due to poor UI/UX design.
- **Harm**: Delayed or erroneous clinical decision, critical patient misdiagnosis. (Severity: S4 - Critical, Probability: P3 - Medium $\to$ **Initial Risk: High / Unacceptable**).

## 2. Risk Control Measure: RCM-FW-012
- **Control Measure Description**: The framework enforces **IEC 62366-1 Usability Engineering & PCA Use Error Protocol**.
  - Mandates explicit identification of Critical Tasks and PCA failure mode modeling in `DHF-01` and `DHF-12`.
  - Enforces low-confidence alert banners ($< 0.60$) and persistent raw-data toggles without modal trapping.
  - Requires formal summative usability testing with at least 15 representative clinical users prior to release.
- **Control Type**: Inherent Safety by Design & Usability Verification Gate.

## 3. Residual Risk Evaluation
- **Residual Severity**: S4.
- **Residual Probability**: P1 (Mitigated by mandatory 15-user clinical summative validation).
- **Residual Risk Level**: **Low / Acceptable (ALARP satisfied)**.
- **Verification Evidence**: `VERIF-FW-033` via `TC-FR-USE-001.md`.
## 4. Evaluation of New Hazards Arising from Risk Control Measures (ISO 14971:2019 Cl 7.3 & IEC 62304 Cl 7.2.2)
- **Potential New Hazards Introduced**:
  - Alert fatigue: Clinicians bombarded with excessive warning banners may develop habituation and ignore critical safety alerts.
  - UI banner occlusion: Prominent safety banners obscuring critical histological morphology on whole-slide viewports.
- **Secondary Risk Mitigations**:
  - IEC 62366-1 usability engineering protocols (`DDS-FW-007`): 3-tier visual hierarchy (Info, Caution, Danger) with distinct color coding and dismiss policies.
  - Non-occluding persistent status bar layout ensuring diagnostic viewport remains 100% unobstructed.
  - Formative and summative usability testing (`DHF-12`) validating zero critical use errors across simulated clinical user groups.
- **Residual Risk Conclusion**: No unacceptable secondary hazards introduced. Residual risk remains **Acceptable (ALARP satisfied)**.
