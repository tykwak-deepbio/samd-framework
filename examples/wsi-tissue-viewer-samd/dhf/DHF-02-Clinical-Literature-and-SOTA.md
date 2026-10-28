# Clinical Literature Review & State of the Art (SOTA) Report

> **Document ID**: `DHF-02-SOTA`  
> **Applicable Standards**: EU IVDR 2017/746 Annex XIII, MDCG 2020-1, IMDRF N41, MEDDEV 2.7/1 rev 4  
> **Project Name**: `[Project / Device Name]`  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 최신 의료기술 현황(State of the Art: SOTA), 임상 문헌 고찰, 유사 제품(Predicate Devices)과의 기술적/임상적 벤치마크 결과를 정리합니다.
> - EU IVDR(Annex XIII 성능평가보고서: PER) 및 식약처/FDA 심사 시 '임상적 유효성 및 성능의 타당성'을 입증하는 핵심 근거가 됩니다.
> - 알고리즘(조직 검출, 색상 정규화)의 임상적 수용 기준(예: Dice 계수, 민감도, 특이도, 색차 Delta E)을 문헌 근거를 바탕으로 도출해야 합니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Clinical Research Scientist | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Medical Pathologist Advisor | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Chief Medical Officer | Approved | `[YYYY-MM-DD]` |

---

## 2. Systematic Literature Search Protocol
- **Search Terms**: `("whole slide image" OR "digital pathology") AND ("tissue segmentation" OR "background correction" OR "stain normalization") AND ("deep learning" OR "AI")`
- **Databases Queried**: PubMed / Medline, IEEE Xplore, Google Scholar, ClinicalTrials.gov
- **Search Timeframe**: `[e.g., 2018 - 2025]`
- **Inclusion Criteria**: Peer-reviewed clinical pathology studies, multicenter datasets, clear diagnostic concordance metrics.
- **Exclusion Criteria**: Non-histological imaging, purely animal studies without translational relevance, non-validated algorithms.

---

## 3. Predicate & Benchmark Devices Comparison

| Device / Software Name | Manufacturer | Regulatory Status (FDA / MFDS / CE) | Core Features | Known Limitations |
| :--- | :--- | :--- | :--- | :--- |
| `[Predicate A]` | `[Vendor A]` | FDA 510(k) (DEN160056) / CE IVD | WSI display, manual tissue framing | No automated stain normalization |
| `[Predicate B]` | `[Vendor B]` | MFDS Class II / CE IVD | Cloud viewer, basic thresholding | High false positive on pen marks |
| `[Subject SaMD]`| `[Our Company]` | Target: FDA 510(k), MFDS Class II, IVDR Class B | AI tissue segmentation + Macenko stain normalization | Validated on multi-scanner cohort |

---

## 4. State of the Art (SOTA) Algorithm Review
1. **Tissue Region Segmentation**:
   - Classic approaches (Otsu thresholding, HSV filtering): Sensitive to background illumination gradients and pen marks.
   - SOTA Deep Learning (Lightweight U-Net / MobileNet / SegFormer): Robust to slide artifacts, air bubbles, and cover glass borders.
2. **Background Color & Stain Normalization**:
   - Optical Density (OD) decomposition (Macenko et al., 2009; Vahadane et al., 2016): Deconvolves Hematoxylin and Eosin stain vectors, standardizing illumination and stain saturation.
   - SOTA benchmark: Preserves cellular morphology while reducing inter-scanner color variation ($\Delta E_{00} \le 3.5$).

---

## 5. Clinical Performance Baselines & Requirements (`CLIN-REQ-xxx`)

| ID | Parameter | Literature SOTA Baseline | Subject Device Target | Clinical Rationale |
| :--- | :--- | :--- | :--- | :--- |
| `CLIN-REQ-001` | Tissue Segmentation Dice | $\ge 0.90$ (Literature mean) | $\ge 0.92$ (IoU $\ge 0.85$) | Minimizes omission of tissue edges. |
| `CLIN-REQ-002` | Artifact Misclassification | $\le 5\%$ false positive | $\le 2.5\%$ false positive | Prevents pathologist inspection of dust/glass. |
| `CLIN-REQ-003` | Stain Normalization Delta E | $\Delta E_{00} \le 4.0$ | $\Delta E_{00} \le 3.0$ | Preserves nuclear chromatin texture. |
| `CLIN-REQ-004` | Diagnostic Concordance | Non-inferior to optical microscope ($\kappa \ge 0.90$) | Cohen's Kappa $\kappa \ge 0.92$ | Guarantees diagnostic safety. |
