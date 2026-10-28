# Software Detailed Design Specification (DDS)

> **Document ID**: `DHF-08-DDS`  
> **Applicable Standards**: IEC 62304:2006+AMD1:2015 Clause 5.4, ISO 13485:2016 Clause 7.3.4  
> **Project Name**: `[Project / Device Name]`  
> **Software Safety Class**: `[Class B]` (IEC 62304)  
> **Revision**: `[e.g., 1.0]` | **Effective Date**: `[YYYY-MM-DD]`  
> **Document Status**: `[Draft / In-Review / Approved]`  

---

> [!TIP]
> **국문 작성 가이드 (Korean Guidance)**:
> - 본 문서는 IEC 62304 Clause 5.4(소프트웨어 상세 설계)에 따라 작성되는 컴포넌트/단위(Unit) 수준의 상세 설계서입니다.
> - 소프트웨어 유닛(`DDS-xxx`)의 알고리즘 수식(OD 변환, Macenko 분해 등), 클래스/함수 시그니처, 데이터 타입, 매개변수 범위, 예외처리 및 방어적 프로그래밍 로직을 구체적으로 명시합니다.
> - 본 문서는 소프트웨어 개발자가 코드를 구현하고 단위 테스트(`TC-UNIT-xxx`)를 작성하는 기준이 됩니다.

---

## 1. Document Control & Approvals

| Role | Name | Title / Department | Signature / Approval | Date |
| :--- | :--- | :--- | :--- | :--- |
| **Author** | `[Author Name]` | Senior Software Engineer | Approved | `[YYYY-MM-DD]` |
| **Reviewer** | `[Reviewer Name]`| Principal Software Architect | Approved | `[YYYY-MM-DD]` |
| **Approver** | `[Approver Name]`| Software Engineering Lead | Approved | `[YYYY-MM-DD]` |

---

## 2. Software Units Detailed Specification (`DDS-xxx`)

### 2.1 Unit: `DDS-001` - Pyramidal Tile Streamer & LRU Cache (`ARCH-001`, `ARCH-004`)
- **Module**: `src/imaging/tile_streamer.py`
- **Class / Functions**:
  ```python
  class TileStreamer:
      def __init__(self, slide_path: str, max_cache_mb: int = 2048) -> None: ...
      def get_tile(self, level: int, x: int, y: int, tile_size: int = 512) -> np.ndarray: ...
  ```
- **Bounds Checking**:
  - Validates $0 \le \text{level} < \text{level\_count}$.
  - Validates $0 \le x < \text{level\_dimensions}[0]$ and $0 \le y < \text{level\_dimensions}[1]$.
  - Raises `TileOutOfBoundsError` on invalid requests.
- **LRU Memory Management**:
  - Evicts oldest unreferenced tile buffers when cache size exceeds `max_cache_mb`.

### 2.2 Unit: `DDS-002` - Optical Density (OD) & Macenko Normalizer (`ARCH-002`)
- **Module**: `src/normalization/stain_normalizer.py`
- **Class / Functions**:
  ```python
  class MacenkoNormalizer:
      def __init__(self, target_stain_matrix: np.ndarray, target_concentrations: np.ndarray) -> None: ...
      def rgb_to_od(self, rgb: np.ndarray) -> np.ndarray: ...
      def normalize(self, rgb: np.ndarray) -> np.ndarray: ...
  ```
- **Mathematical Specification**:
  - Optical Density Conversion:
    $$OD = -\log_{10}\left(\frac{\max(I, 1)}{255.0}\right)$$
  - Numerical Bounding: Clamps OD values: $OD_{\text{clamped}} = \operatorname{clip}(OD, 0.01, 2.50)$ to prevent black clipping.
  - Pseudo-Inverse Stain Deconvolution:
    $$C = S_{\text{pseudo}}^{-1} \cdot OD$$

### 2.3 Unit: `DDS-003` - AI Tissue Region Segmenter (`ARCH-003`)
- **Module**: `src/segmentation/tissue_segmenter.py`
- **Class / Functions**:
  ```python
  class TissueSegmenter:
      def __init__(self, model_path: str, confidence_threshold: float = 0.60) -> None: ...
      def segment_thumbnail(self, thumbnail_rgb: np.ndarray) -> Tuple[np.ndarray, float, bool]: ...
  ```
- **Logic & Fail-Safe Specification**:
  - Downsamples slide to thumbnail ($2048\times 2048$).
  - Evaluates inference tensor through ONNX model.
  - Computes `mean_confidence`. If $\text{mean\_confidence} < 0.60$, sets `is_low_confidence = True` triggering user alert banner (`RCM-001`).

### 2.4 Unit: `DDS-004` - DICOM De-Identification Filter (`ARCH-006`)
- **Module**: `src/security/deidentifier.py`
- **Class / Functions**:
  ```python
  def sanitize_metadata(header_dict: Dict[str, Any]) -> Dict[str, Any]: ...
  ```
- **Sanitization Rule**: Deletes all 21 HIPAA identifiers (Patient Name, Patient ID, Birth Date, Institution, etc.) before memory caching.
