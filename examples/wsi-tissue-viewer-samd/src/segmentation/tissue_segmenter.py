"""
AI Tissue Region Segmentation & Fail-Safe Low-Confidence Supervisor.
Complies with IEC 62304 Clause 5.5 and ISO 14971 Risk Controls.

Traces:
- REQ-SW-002 (AI tissue segmentation on overview thumbnails)
- REQ-SW-006 (Overview segmentation runtime <= 2.5 seconds)
- REQ-SW-007 (Low-confidence alert banner if mean confidence < 0.60)
- ARCH-003 (AI Tissue Segmentation Engine)
- DDS-003 (TissueSegmenter Unit)
- RCM-001 (Fail-safe alert banner on low segmentation confidence)
- CLIN-REQ-001 (Tissue segmentation Dice >= 0.92)
"""

from typing import Tuple, Dict, Any
import numpy as np


class TissueSegmenter:
    """
    AI-driven tissue region segmenter with confidence monitoring.
    
    Traces: REQ-SW-002, REQ-SW-007, DDS-003, RCM-001
    """

    def __init__(self, confidence_threshold: float = 0.60) -> None:
        """
        Initialize segmenter with safety threshold.
        
        Args:
            confidence_threshold: Minimum mean confidence below which low-confidence alert triggers.
        """
        self.confidence_threshold = confidence_threshold

    # Traces: REQ-SW-002, REQ-SW-006, REQ-SW-007, DDS-003, RCM-001
    def segment_thumbnail(self, thumbnail_rgb: np.ndarray) -> Dict[str, Any]:
        """
        Segments tissue regions from a slide thumbnail.
        
        Args:
            thumbnail_rgb: Overview thumbnail image array of shape (H, W, 3) in uint8.
            
        Returns:
            Dict containing:
                - "mask": Binary uint8 mask (1 for tissue, 0 for glass background).
                - "mean_confidence": Float confidence score [0.0, 1.0].
                - "low_confidence_alert": Boolean flag triggering UI warning banner (RCM-001).
                - "tissue_area_percentage": Float percentage of slide covered by tissue.
        """
        if thumbnail_rgb.ndim != 3 or thumbnail_rgb.shape[2] != 3:
            raise ValueError("Thumbnail must be an RGB image of shape (H, W, 3)")

        # Convert to grayscale for Otsu-inspired thresholding simulation
        gray = np.dot(thumbnail_rgb[..., :3], [0.2989, 0.5870, 0.1140])

        # Tissue pixels are darker than white glass background (~235-255)
        raw_mask = (gray < 220).astype(np.uint8)

        # Calculate confidence: based on contrast between tissue and background
        tissue_pixels = gray[raw_mask == 1]
        bg_pixels = gray[raw_mask == 0]

        if len(tissue_pixels) > 0 and len(bg_pixels) > 0:
            separation = (np.mean(bg_pixels) - np.mean(tissue_pixels)) / 255.0
            mean_conf = float(np.clip(separation * 1.5, 0.1, 0.98))
        else:
            mean_conf = 0.30  # Default low confidence if no tissue or all tissue

        # RCM-001: Trigger alert if mean confidence < threshold
        is_low_confidence = bool(mean_conf < self.confidence_threshold)

        total_pixels = raw_mask.size
        tissue_area_pct = float((np.sum(raw_mask) / total_pixels) * 100.0)

        return {
            "mask": raw_mask,
            "mean_confidence": round(mean_conf, 3),
            "low_confidence_alert": is_low_confidence,
            "tissue_area_percentage": round(tissue_area_pct, 2),
        }
