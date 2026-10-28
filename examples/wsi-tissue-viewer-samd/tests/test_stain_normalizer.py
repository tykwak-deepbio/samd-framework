"""
Unit and Usability Tests for Stain Normalizer Subsystem.
Verifies compliance with IEC 62304 Clause 5.5 and ISO 14971 Risk Controls.

Traces:
- TC-UNIT-003 (OD clamping function verification)
- TC-SYS-003 (Stain normalization calculation)
- TC-USE-001 (Raw vs. normalized toggle usability)
"""

import unittest
import numpy as np
from src.normalization.stain_normalizer import MacenkoNormalizer


class TestStainNormalizer(unittest.TestCase):

    # Traces: TC-UNIT-003, REQ-SW-009, RCM-003
    def test_od_conversion_and_clamping(self):
        normalizer = MacenkoNormalizer()
        test_img = np.array([
            [[0, 0, 0], [255, 255, 255]],
            [[10, 50, 100], [200, 220, 240]],
        ], dtype=np.uint8)
        
        od = normalizer.rgb_to_od(test_img)
        self.assertTrue(np.all(od >= 0.01))
        self.assertTrue(np.all(od <= 2.50))
        self.assertFalse(np.any(np.isnan(od)))
        self.assertFalse(np.any(np.isinf(od)))

    # Traces: TC-SYS-003, REQ-SW-003
    def test_stain_normalization_effect(self):
        normalizer = MacenkoNormalizer()
        raw_tile = np.full((128, 128, 3), 180, dtype=np.uint8)
        
        norm_tile, is_norm = normalizer.normalize(raw_tile, raw_mode=False)
        self.assertTrue(is_norm)
        self.assertEqual(norm_tile.shape, raw_tile.shape)
        self.assertEqual(norm_tile.dtype, np.uint8)

    # Traces: TC-USE-001, REQ-SW-008, RCM-002
    def test_raw_mode_instant_toggle(self):
        normalizer = MacenkoNormalizer()
        raw_tile = np.full((128, 128, 3), 150, dtype=np.uint8)
        
        output_tile, is_norm = normalizer.normalize(raw_tile, raw_mode=True)
        self.assertFalse(is_norm)
        self.assertTrue(np.array_equal(output_tile, raw_tile))


if __name__ == "__main__":
    unittest.main()
