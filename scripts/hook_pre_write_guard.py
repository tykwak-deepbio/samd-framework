#!/usr/bin/env python3
"""
hook_pre_write_guard.py

Antigravity PreToolUse Lifecycle Hook for SaMD Technical RBAC & Integrity Enforcement.
Enforces IEC 62304 Clause 5.6.2 / 5.7.2 (Independence of Verification) and ISO 13485 Cl 7.3.5.

Technical Controls:
1. Intercepts 'write_to_file' and 'replace_file_content' targeting 'src/'.
2. Intercepts 'run_command' to inspect shell write redirections ('>', '>>', 'tee', 'mv', 'cp', 'rm', 'sed -i') targeting 'src/'.
3. Detects attempts by Independent V&V / Lead Auditor personas to modify production code under 'src/'.
4. Returns JSON decision 'deny' if a persona boundary violation is detected.
5. Emits JSON decision 'allow' for authorized operations.
6. Fail-Closed: returns 'deny' upon any unhandled exception or malformed payload.

Input: JSON on stdin (from Antigravity PreToolUse hook)
Output: JSON on stdout: {"decision": "allow"|"deny", "reason": "..."}
"""

import sys
import json
import re

AUDITOR_VNV_PERSONAS = [
    "vnv-test-engineer-agent",
    "vnv_tester",
    "samd_vnv_tester",
    "dhf-lead-auditor-agent",
    "dhf_auditor",
    "samd_dhf_auditor",
    "samd_srs_auditor"
]

PROTECTED_PATHS = [
    "src/",
    "/src/"
]

BASH_WRITE_PATTERNS = [
    r">\s*src/",
    r">>\s*src/",
    r"tee\s+(?:-\w+\s+)*src/",
    r"mv\s+.*?\s+src/",
    r"cp\s+.*?\s+src/",
    r"rm\s+(?:-\w+\s+)*src/",
    r"sed\s+(?:-i\w*\s+).*?src/",
]


def evaluate_pre_tool_use(payload: dict) -> dict:
    tool_call = payload.get("toolCall", {})
    tool_name = tool_call.get("name", "")
    tool_args = tool_call.get("args", {})

    caller_context = json.dumps(payload).lower()
    is_vnv_auditor = any(p in caller_context for p in AUDITOR_VNV_PERSONAS)

    # 1. File write tools (write_to_file, replace_file_content)
    if tool_name in ["write_to_file", "replace_file_content"]:
        target_file = tool_args.get("TargetFile", "")
        if not target_file:
            return {"decision": "allow", "reason": "No target file specified"}

        normalized_path = target_file.replace("\\", "/")
        is_protected_src = any(p in normalized_path for p in PROTECTED_PATHS) or normalized_path.startswith("src/")

        if is_protected_src and is_vnv_auditor:
            return {
                "decision": "deny",
                "reason": (
                    f"IEC 62304 Clause 5.6.2 / 5.7.2 Violation: "
                    f"Independent V&V and Quality Auditor agents are strictly prohibited from "
                    f"modifying production source code ('{target_file}'). "
                    f"Technical RBAC write protection enforced by hook_pre_write_guard.py."
                )
            }

    # 2. Shell execution tool (run_command)
    elif tool_name == "run_command":
        cmd_line = tool_args.get("CommandLine", "")
        if is_vnv_auditor and cmd_line:
            for pattern in BASH_WRITE_PATTERNS:
                if re.search(pattern, cmd_line):
                    return {
                        "decision": "deny",
                        "reason": (
                            f"IEC 62304 Clause 5.6.2 / 5.7.2 Violation: "
                            f"Independent V&V and Quality Auditor agents are strictly prohibited from "
                            f"executing shell commands that modify production source code under 'src/' ('{cmd_line}'). "
                            f"Shell write interception enforced by hook_pre_write_guard.py."
                        )
                    }

    return {
        "decision": "allow",
        "reason": "SaMD Pre-write RBAC and safety guard verified."
    }


def main():
    try:
        raw_input = sys.stdin.read()
        if not raw_input.strip():
            print(json.dumps({"decision": "allow", "reason": "Empty input"}))
            return
        payload = json.loads(raw_input)
        result = evaluate_pre_tool_use(payload)
        print(json.dumps(result))
    except Exception as e:
        # Fail-Closed safety interlock for medical device software (IEC 62304 / ISO 14971 RCM-FW-015)
        print(json.dumps({"decision": "deny", "reason": f"Hook execution failure (Fail-Closed safety interlock active): {e}"}))


if __name__ == "__main__":
    main()
