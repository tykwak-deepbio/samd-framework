"""
Cybersecurity & Privacy Tests for De-Identifier Subsystem.
Verifies compliance with ISO 27799:2016, IEC 81001-5-1, and FDA Cybersecurity Guidance.

Traces:
- TC-SEC-001 (Verification of DICOM PHI scrubbing)
- TC-SEC-002 (Verification of TLS 1.3 protocol enforcement)
"""

import unittest
from src.security.deidentifier import sanitize_metadata, verify_tls_compliance


class TestDeidentifier(unittest.TestCase):

    # Traces: TC-SEC-001, REQ-SW-010, SEC-CTL-002
    def test_phi_tag_scrubbing(self):
        raw_header = {
            "PatientName": "Doe^John",
            "PatientID": "12345678",
            "PatientBirthDate": "19800101",
            "PixelSpacing": [0.25, 0.25],
            "Magnification": "40x",
            "TotalLevels": 4,
        }
        
        cleaned = sanitize_metadata(raw_header)
        
        # Assert PHI tags are sanitized
        self.assertEqual(cleaned["PatientName"], "[DE-IDENTIFIED]")
        self.assertEqual(cleaned["PatientID"], "[DE-IDENTIFIED]")
        self.assertEqual(cleaned["PatientBirthDate"], "[DE-IDENTIFIED]")
        
        # Assert clinical imaging technical tags remain intact
        self.assertEqual(cleaned["PixelSpacing"], [0.25, 0.25])
        self.assertEqual(cleaned["Magnification"], "40x")
        self.assertEqual(cleaned["TotalLevels"], 4)

    # Traces: TC-SEC-002, REQ-SW-011, SEC-CTL-001
    def test_tls_compliance(self):
        # Compliant cipher and protocol
        self.assertTrue(verify_tls_compliance("TLSv1.3", "TLS_AES_256_GCM_SHA384"))
        
        # Non-compliant deprecated SSL/TLS protocols
        self.assertFalse(verify_tls_compliance("TLSv1.2", "TLS_AES_256_GCM_SHA384"))
        self.assertFalse(verify_tls_compliance("TLSv1.0", "TLS_RSA_WITH_AES_128_CBC_SHA"))


if __name__ == "__main__":
    unittest.main()
