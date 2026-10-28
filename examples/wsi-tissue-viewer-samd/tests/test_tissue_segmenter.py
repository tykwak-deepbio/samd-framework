"""
AI Validation and System Tests for Tissue Segmenter Subsystem.
Verifies compliance with IEC 62304 Clause 5.7 and ISO 14971 Risk Controls.

Traces:
- TC-AI-001 (AI clinical tissue segmentation performance)
- TC-SYS-007 (Low-confidence alert banner verification)
"""

import unittest
import numpy as np
from src.segmentation.tissue_segmenter import TissueSegmenter


class TestTissueSegmenter(unittest.TestCase):

    # Traces: TC-AI-001, REQ-SW-002, CLIN-REQ-001
    def test_tissue_segmentation_dice(self):
        segmenter = TissueSegmenter(confidence_threshold=0.60)
        
        # Synthetic slide: white background (245) with tissue region (120) in center
        thumb = np.full((512, 512, 3), 245, dtype=np.uint8)
        thumb[100:400, 100:400] = [140, 80, 120]  # Tissue block
        
        result = segmenter.segment_thumbnail(thumb)
        mask = result["mask"]
        
        # Ground truth
        gt = np.zeros((512, 512), dtype=np.uint8)
        gt[100:400, 100:400] = 1
        
        # Compute Dice coefficient: 2 * |A intersect B| / (|A| + |B|)
        intersection = np.sum((mask == 1) & (gt == 1))
        dice = (2.0 * intersection) / (np.sum(mask) + np.sum(gt))
        
        # CLIN-REQ-001 threshold: Dice >= 0.92
        self.assertGreaterEqual(dice, 0.92)
        self.assertFalse(result["low_confidence_alert"])

    # Traces: TC-SYS-007, REQ-SW-007, RCM-001
    def test_low_confidence_alert_banner(self):
        segmenter = TissueSegmenter(confidence_threshold=0.60)
        
        # Very faint, almost invisible tissue or uniform slide causing low confidence
        faint_thumb = np.full((512, 512, 3), 235, dtype=np.uint8)
        result = segmenter.segment_thumbnail(faint_thumb)
        
        # RCM-001: low_confidence_alert must trigger when separation is minimal
        self.assertTrue(result["low_confidence_alert"])
        self.assertLess(result["mean_confidence"], 0.60)


if __name__ == "__main__":
    unittest.main()
