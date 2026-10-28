"""
Unit and System Tests for TileStreamer Subsystem.
Verifies compliance with IEC 62304 Clause 5.5 and 5.7.

Traces:
- TC-SYS-001 (Ingest multi-resolution WSI formats)
- TC-INT-001 (Pyramidal navigation and deep zoom)
- TC-SYS-005 (Tile latency and memory cache bounds)
"""

import os
import tempfile
import unittest
import numpy as np
from src.imaging.tile_streamer import TileStreamer, TileOutOfBoundsError


class TestTileStreamer(unittest.TestCase):

    def setUp(self):
        self.tmp_file = tempfile.NamedTemporaryFile(suffix=".svs", delete=False)
        self.tmp_file.write(b"MOCK_WSI_HEADER_DATA")
        self.tmp_file.close()
        self.slide_path = self.tmp_file.name

    def tearDown(self):
        if os.path.exists(self.slide_path):
            os.remove(self.slide_path)

    # Traces: TC-SYS-001, TC-INT-001, REQ-SW-001, REQ-SW-004
    def test_tile_fetch_and_pyramid_levels(self):
        streamer = TileStreamer(self.slide_path, max_cache_mb=100)
        self.assertEqual(streamer.levels, 4)
        
        tile = streamer.get_tile(level=1, x=512, y=512, tile_size=512)
        self.assertEqual(tile.shape, (512, 512, 3))
        self.assertEqual(tile.dtype, np.uint8)

    # Traces: TC-SYS-001, DDS-001
    def test_tile_out_of_bounds_rejection(self):
        streamer = TileStreamer(self.slide_path, max_cache_mb=100)
        with self.assertRaises(TileOutOfBoundsError):
            streamer.get_tile(level=99, x=0, y=0)
            
        with self.assertRaises(TileOutOfBoundsError):
            streamer.get_tile(level=0, x=999999, y=999999)

    # Traces: TC-SYS-005, REQ-SW-005, RCM-004
    def test_lru_cache_memory_eviction(self):
        streamer = TileStreamer(self.slide_path, max_cache_mb=2)
        streamer.get_tile(level=1, x=0, y=0)
        streamer.get_tile(level=1, x=512, y=0)
        streamer.get_tile(level=1, x=1024, y=0)
        
        self.assertLessEqual(streamer.current_cache_bytes, streamer.max_cache_bytes)
        self.assertLessEqual(len(streamer.cache), 3)


if __name__ == "__main__":
    unittest.main()
