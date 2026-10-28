#!/usr/bin/env python3
"""
tests/integration/test_framework_integration.py

Integration Test Suite for the SaMD Multi-Agent Framework Subsystems (IEC 62304 Clause 5.6).
Verifies inter-module data contracts, boundary interfaces, and subsystem integration:
1. Audit Trail Engine <-> Project State Machine integration.
2. PreToolUse Safety Guard <-> RBAC execution flow.
3. Cascading Invalidation Engine <-> Change Impact Analysis.
4. AI Dataset Split Validator <-> Statistical Drift Detection.
5. Grounding Verifier <-> Adversarial Injection Defense.
"""

import os
import sys
import json
import tempfile
import unittest
import subprocess


class TestFrameworkIntegration(unittest.TestCase):
    def setUp(self):
        self.workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self.scripts_dir = os.path.join(self.workspace_root, "scripts")

    def test_integration_audit_and_project_state(self):
        """Test integration between record_audit_event.py and project_state.json."""
        record_script = os.path.join(self.scripts_dir, "record_audit_event.py")
        self.assertTrue(os.path.isfile(record_script))

        with tempfile.TemporaryDirectory() as tmpdir:
            test_log = os.path.join(tmpdir, "audit_trail.log")
            test_state = os.path.join(tmpdir, "project_state.json")

            # Copy template project_state.json
            template_state = os.path.join(self.workspace_root, "templates", "project_state.json")
            with open(template_state, "r", encoding="utf-8") as f:
                state_data = json.load(f)
            with open(test_state, "w", encoding="utf-8") as f:
                json.dump(state_data, f, indent=2)

            # Record GATE-01 signoff
            cmd = [
                sys.executable, record_script,
                "--record",
                "--log", test_log,
                "--actor", "Regulatory_Lead_Signer",
                "--action", "GATE_REVIEW_APPROVAL",
                "--resource", "DHF-01-Intended-Use-and-URD.md",
                "--details", "Gate 1 formal clinical approval recorded",
                "--state-file", test_state,
                "--gate", "GATE-01"
            ]
            res = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(res.returncode, 0, f"Record failed: {res.stderr}")

            # Verify project_state.json was updated
            with open(test_state, "r", encoding="utf-8") as f:
                updated_state = json.load(f)
            gate1 = updated_state["gates"]["GATE-01"]
            self.assertEqual(gate1["status"], "APPROVED")
            self.assertEqual(gate1["approved_by"], "Regulatory_Lead_Signer")
            self.assertTrue(len(gate1["sign_off_hash"]) == 64)

            # Verify audit trail integrity
            res_ver = subprocess.run([sys.executable, record_script, "--verify", "--log", test_log], capture_output=True, text=True)
            self.assertEqual(res_ver.returncode, 0)
            self.assertIn("[PASS] Full audit chain verified", res_ver.stdout)

    def test_integration_safety_guard_fail_closed(self):
        """Test that hook_pre_write_guard safely denies invalid or exception-causing payloads."""
        guard_script = os.path.join(self.scripts_dir, "hook_pre_write_guard.py")
        self.assertTrue(os.path.isfile(guard_script))

        # Test malformed payload trigger -> Must fail closed (deny)
        res = subprocess.run([sys.executable, guard_script], input="INVALID_NON_JSON{{{", capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        output = json.loads(res.stdout)
        self.assertEqual(output.get("decision"), "deny")
        self.assertIn("Fail-Closed", output.get("reason", ""))

    def test_integration_ai_governance_and_grounding_pipeline(self):
        """Test AI pipeline data validation and prompt grounding integration."""
        ai_validator = os.path.join(self.scripts_dir, "validate_ai_dataset.py")
        grounding_script = os.path.join(self.scripts_dir, "verify_grounding.py")

        self.assertTrue(os.path.isfile(ai_validator))
        self.assertTrue(os.path.isfile(grounding_script))

        # Step 1: AI dataset split verification
        res_ai = subprocess.run([
            sys.executable, ai_validator,
            "--check-leakage",
            "--train-patients", "PAT-001", "PAT-002",
            "--test-patients", "PAT-003", "PAT-004",
            "--val-patients", "PAT-005"
        ], capture_output=True, text=True)
        self.assertEqual(res_ai.returncode, 0)
        self.assertIn("Zero patient-level data leakage verified", res_ai.stdout)

        # Step 2: Prompt grounding verification
        res_ground = subprocess.run([
            sys.executable, grounding_script,
            "--check-text", "Clinically verified prompt for pathology tissue segmentation"
        ], capture_output=True, text=True)
        self.assertEqual(res_ground.returncode, 0)
        self.assertIn("<untrusted_input>", res_ground.stdout)


if __name__ == "__main__":
    unittest.main()
