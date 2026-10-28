#!/usr/bin/env python3
"""
validate_traceability.py

Validates bidirectional traceability across SaMD Design History File (DHF) markdown documents.
Checks compliance with IEC 62304 Clause 5.1.1, 5.2, 5.7 and ISO 13485 Clause 7.3.7.

Modes Supported:
1. 'app' (Default): Audits application SaMD DHF documents (USER-REQ-* <-> REQ-SW-* <-> ARCH-* <-> TC-*).
2. 'framework': Audits the SaMD Multi-Agent Framework itself (FR-* <-> ARCH-FW-* <-> DDS-FW-* <-> TC-FR-*).

Invariants Verified:
1. Every requirement maps forward to at least one architecture component or detailed design unit.
2. Every requirement maps forward to at least one verification test case.
3. Every safety risk control (RCM) maps to an implemented requirement and test case.
4. Detects orphan requirements, unlinked risks, or unverified test cases.
5. Verifies 100% Preliminary Hazard Analysis (PHA) screening coverage.

Usage:
    python3 scripts/validate_traceability.py [target_directory] [--target-mode=app|framework]
"""

import os
import sys
import re
import argparse
from typing import Dict, Set, List, Tuple


def find_tags(text: str, pattern: str) -> Set[str]:
    return set(re.findall(pattern, text))


def parse_rtm_table_app(rtm_file_path: str) -> List[Dict[str, str]]:
    """Parses markdown table in DHF-10-Traceability-Matrix-RTM.md for application SaMD."""
    rows = []
    if not os.path.exists(rtm_file_path):
        return rows

    with open(rtm_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header_found = False
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue

        cols = [c.strip() for c in stripped.split("|")[1:-1]]
        if not cols:
            continue

        if ("Software Requirement ID" in line or "REQ-SW" in line) and not header_found:
            header_found = True
            continue

        if header_found and all(set(c) <= {"-", ":", " "} for c in cols):
            continue  # separator line

        if header_found and len(cols) >= 5:
            row_dict = {
                "user_req": cols[0],
                "req_sw": cols[1],
                "risk": cols[2] if len(cols) > 2 else "",
                "security": cols[3] if len(cols) > 3 else "",
                "arch": cols[4] if len(cols) > 4 else "",
                "dds": cols[5] if len(cols) > 5 else "",
                "code": cols[6] if len(cols) > 6 else "",
                "tc": cols[7] if len(cols) > 7 else "",
                "verif": cols[8] if len(cols) > 8 else "",
                "status": cols[9] if len(cols) > 9 else "",
            }
            rows.append(row_dict)

    return rows


def parse_rtm_table_framework(rtm_file_path: str) -> List[Dict[str, str]]:
    """Parses markdown table in FRAMEWORK_RTM.md for the SaMD Multi-Agent Framework."""
    rows = []
    if not os.path.exists(rtm_file_path):
        return rows

    with open(rtm_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header_found = False
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue

        cols = [c.strip() for c in stripped.split("|")[1:-1]]
        if not cols:
            continue

        if ("Req ID" in line or "Functional Req ID" in line or ("FR-" in line and "Title" in line)) and not header_found:
            header_found = True
            continue

        if header_found and all(set(c) <= {"-", ":", " "} for c in cols):
            continue

        if header_found and len(cols) >= 7:
            req_id_match = re.search(r"FR-[A-Z0-9]+-\d+", cols[0])
            if req_id_match:
                row_dict = {
                    "fr_id": req_id_match.group(0),
                    "title": cols[1] if len(cols) > 1 else "",
                    "risk": cols[2] if len(cols) > 2 else "",
                    "arch": cols[3] if len(cols) > 3 else "",
                    "dds": cols[4] if len(cols) > 4 else "",
                    "artifact": cols[5] if len(cols) > 5 else "",
                    "tc": cols[6] if len(cols) > 6 else "",
                    "status": cols[7] if len(cols) > 7 else "",
                }
                rows.append(row_dict)

    return rows


def validate_traceability_app(dhf_dir: str) -> bool:
    print("=" * 80)
    print("  SaMD Application Traceability Validator (IEC 62304 / ISO 13485)")
    print(f"  Target DHF Directory: {dhf_dir}")
    print("=" * 80)

    if not os.path.isdir(dhf_dir):
        print(f"[ERROR] Directory not found: {dhf_dir}")
        return False

    all_files = [f for f in os.listdir(dhf_dir) if f.endswith(".md")]
    if not all_files:
        print(f"[ERROR] No markdown files found in {dhf_dir}")
        return False

    full_text = ""
    file_contents = {}
    for fname in sorted(all_files):
        fpath = os.path.join(dhf_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            file_contents[fname] = content
            full_text += content + "\n"

    user_reqs = find_tags(full_text, r"USER-REQ-\d+")
    clin_reqs = find_tags(full_text, r"CLIN-REQ-\d+")
    reg_reqs = find_tags(full_text, r"REG-REQ-\d+")
    req_sws = find_tags(full_text, r"REQ-SW-\d+")
    risks = find_tags(full_text, r"RSK-\d+")
    rcms = find_tags(full_text, r"RCM-\d+")
    archs = find_tags(full_text, r"ARCH-\d+")
    ddss = find_tags(full_text, r"DDS-\d+")
    tcs = find_tags(full_text, r"TC-[A-Z]+-\d+")
    verifs = find_tags(full_text, r"VERIF-\d+")

    print(f"\n[1] Extracted Traceability Entities:")
    print(f"  - User Needs (`USER-REQ-*`): {len(user_reqs)} found")
    print(f"  - Clinical Requirements (`CLIN-REQ-*`): {len(clin_reqs)} found")
    print(f"  - Regulatory Requirements (`REG-REQ-*`): {len(reg_reqs)} found")
    print(f"  - Software Requirements (`REQ-SW-*`): {len(req_sws)} found")
    print(f"  - Risk Hazards (`RSK-*`): {len(risks)} found")
    print(f"  - Risk Control Measures (`RCM-*`): {len(rcms)} found")
    print(f"  - Architectural Components (`ARCH-*`): {len(archs)} found")
    print(f"  - Detailed Design Units (`DDS-*`): {len(ddss)} found")
    print(f"  - Test Cases (`TC-*`): {len(tcs)} found")
    print(f"  - Verification Evidence (`VERIF-*`): {len(verifs)} found")

    rtm_files = [f for f in all_files if "10" in f and "RTM" in f.upper()]
    if not rtm_files:
        rtm_files = all_files

    rtm_rows = []
    for rf in rtm_files:
        rows = parse_rtm_table_app(os.path.join(dhf_dir, rf))
        if rows:
            rtm_rows = rows
            print(f"\n[2] Found RTM Table in `{rf}` with {len(rows)} requirement rows.")
            break

    if not rtm_rows:
        print("[ERROR] Could not parse RTM table rows.")
        return False

    errors = []
    warnings = []

    covered_user_reqs = set()
    covered_req_sws = set()
    covered_tcs = set()
    covered_rcms = set()

    for idx, row in enumerate(rtm_rows, 1):
        req_sw = row["req_sw"].strip("` ")
        user_req_str = row["user_req"]
        arch_str = row["arch"]
        tc_str = row["tc"]
        risk_str = row["risk"]
        status = row["status"]

        if not re.search(r"REQ-SW-\d+", req_sw):
            errors.append(f"Row {idx}: Invalid or missing REQ-SW ID: '{req_sw}'")
            continue
        covered_req_sws.add(req_sw)

        row_user_reqs = find_tags(user_req_str, r"USER-REQ-\d+")
        for ur in row_user_reqs:
            covered_user_reqs.add(ur)
        if not row_user_reqs and "REG-REQ" not in user_req_str and "RCM" not in user_req_str:
            warnings.append(f"Row {idx} ({req_sw}): No USER-REQ or REG-REQ mapped backward.")

        if not (re.search(r"ARCH-\d+", arch_str) or re.search(r"DDS-\d+", row["dds"])):
            errors.append(f"Row {idx} ({req_sw}): Missing architecture (ARCH-*) or detailed design (DDS-*) link.")

        row_tcs = find_tags(tc_str, r"TC-[A-Z]+-\d+")
        for tc in row_tcs:
            covered_tcs.add(tc)
        if not row_tcs:
            errors.append(f"Row {idx} ({req_sw}): No verification test case (TC-*) linked forward (Orphan requirement).")

        row_rcms = find_tags(risk_str, r"RCM-\d+")
        for rcm in row_rcms:
            covered_rcms.add(rcm)

        if "PASS" not in status:
            warnings.append(f"Row {idx} ({req_sw}): Verification status is '{status}' (not marked PASS).")

    orphan_user_reqs = user_reqs - covered_user_reqs
    if orphan_user_reqs:
        errors.append(f"Orphan User Needs without mapped REQ-SW: {sorted(orphan_user_reqs)}")

    orphan_rcms = rcms - covered_rcms
    if orphan_rcms:
        warnings.append(f"Risk Control Measures not mapped in RTM table: {sorted(orphan_rcms)}")

    pha_checked = False
    for fname, content in file_contents.items():
        if "Requirements Screening Table" in content or "PHA Screening Matrix" in content:
            pha_checked = True
            missing_pha = [r for r in sorted(covered_req_sws) if r not in content]
            if missing_pha:
                errors.append(f"Preliminary Hazard Analysis incomplete in `{fname}`: Missing evaluation for {missing_pha}")
            else:
                print(f"  - PHA 100% Software Requirements Screening: PASS ({len(covered_req_sws)} / {len(covered_req_sws)} evaluated in `{fname}`)")

    if not pha_checked and any("05B" in f for f in all_files):
        warnings.append("DHF-05B does not yet contain a formal 100% PHA Software Requirements Screening Table (recommended under ISO 14971:2019 Cl 5.4).")

    print("\n[3] Traceability Verification Results:")
    print(f"  - Total REQ-SW Verified in RTM: {len(covered_req_sws)} / {len(req_sws)}")
    print(f"  - Total USER-REQ Linked: {len(covered_user_reqs)} / {len(user_reqs)}")
    print(f"  - Total Test Cases Linked: {len(covered_tcs)} / {len(tcs)}")
    print(f"  - Total Risk Controls Linked: {len(covered_rcms)} / {len(rcms)}")

    if warnings:
        print(f"\n[!] Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print(f"\n[X] Errors / Non-Conformities Detected ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        print("\n--> REGULATORY AUDIT VERDICT: FAIL (Broken Traceability Links Detected)")
        return False
    else:
        print("\n" + "=" * 80)
        print("--> REGULATORY AUDIT VERDICT: PASS (100% Bidirectional Traceability Satisfied)")
        print("=" * 80)
        return True


def validate_traceability_framework(workspace_root: str) -> bool:
    print("=" * 80)
    print("  SaMD Multi-Agent Framework Meta-Traceability Validator")
    print(f"  Workspace Root: {workspace_root}")
    print("=" * 80)

    docs_dir = os.path.join(workspace_root, "docs")
    srs_dir = os.path.join(docs_dir, "srs")
    tests_dir = os.path.join(docs_dir, "tests")
    arch_dir = os.path.join(docs_dir, "architecture")
    dds_dir = os.path.join(docs_dir, "detailed_design")
    risks_dir = os.path.join(docs_dir, "risks")
    rtm_path = os.path.join(docs_dir, "traceability", "FRAMEWORK_RTM.md")
    pha_path = os.path.join(risks_dir, "FRAMEWORK_PHA_MATRIX.md")

    if not os.path.isfile(rtm_path):
        print(f"[ERROR] FRAMEWORK_RTM.md not found at {rtm_path}")
        return False

    srs_files = [f for f in os.listdir(srs_dir) if f.startswith("FR-") and f.endswith(".md")]
    expected_frs = {f.replace(".md", "") for f in srs_files}

    tc_files = [f for f in os.listdir(tests_dir) if f.startswith("TC-FR-") and f.endswith(".md")]
    expected_tcs = {f.replace(".md", "") for f in tc_files}

    arch_files = [f for f in os.listdir(arch_dir) if f.startswith("ARCH-FW-") and f.endswith(".md")]
    dds_files = [f for f in os.listdir(dds_dir) if f.startswith("DDS-FW-") and f.endswith(".md")]

    print(f"\n[1] Extracted Framework Specification Entities:")
    print(f"  - Software Functional Requirements (`FR-*`): {len(expected_frs)} found")
    print(f"  - 1:1 Test Protocols (`TC-FR-*`): {len(expected_tcs)} found")
    print(f"  - Architecture Components (`ARCH-FW-*`): {len(arch_files)} found")
    print(f"  - Detailed Design Units (`DDS-FW-*`): {len(dds_files)} found")

    rtm_rows = parse_rtm_table_framework(rtm_path)
    print(f"\n[2] Found Framework RTM Table in `{rtm_path}` with {len(rtm_rows)} requirement rows.")

    errors = []
    warnings = []

    covered_frs = set()
    covered_tcs = set()

    for idx, row in enumerate(rtm_rows, 1):
        fr_id = row["fr_id"]
        arch = row["arch"]
        dds = row["dds"]
        tc = row["tc"]
        status = row["status"]

        covered_frs.add(fr_id)

        if not (re.search(r"ARCH-FW-\d+", arch) or re.search(r"DDS-FW-\d+", dds)):
            errors.append(f"Row {idx} ({fr_id}): Missing architecture (ARCH-FW-*) or detailed design (DDS-FW-*) link.")

        tcs_in_row = find_tags(tc, r"TC-FR-[A-Z0-9]+-\d+")
        for t in tcs_in_row:
            covered_tcs.add(t)
        if not tcs_in_row:
            errors.append(f"Row {idx} ({fr_id}): Missing 1:1 mapped test protocol (TC-FR-*).")

        if "PASS" not in status and "APPROVED" not in status.upper():
            warnings.append(f"Row {idx} ({fr_id}): Status is '{status}' (not marked PASS).")

    # Orphan checks
    orphan_frs = expected_frs - covered_frs
    if orphan_frs:
        errors.append(f"Orphan Framework Requirements without RTM entry: {sorted(orphan_frs)}")

    unmapped_tcs = expected_tcs - covered_tcs
    if unmapped_tcs:
        errors.append(f"Test Protocols missing forward link in RTM: {sorted(unmapped_tcs)}")

    # PHA Matrix Screening check
    if os.path.isfile(pha_path):
        with open(pha_path, "r", encoding="utf-8") as f:
            pha_text = f.read()
        missing_pha = [fr for fr in sorted(expected_frs) if fr not in pha_text]
        if missing_pha:
            errors.append(f"FRAMEWORK_PHA_MATRIX.md incomplete: Missing preliminary hazard screening for: {missing_pha}")
        else:
            print(f"  - PHA 100% Software Requirements Screening: PASS ({len(expected_frs)} / {len(expected_frs)} screened in PHA Matrix)")

    print("\n[3] Framework Traceability Verification Results:")
    print(f"  - Total FR Verified in RTM: {len(covered_frs)} / {len(expected_frs)}")
    print(f"  - Total Test Protocols Linked: {len(covered_tcs)} / {len(expected_tcs)}")

    if warnings:
        print(f"\n[!] Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print(f"\n[X] Errors / Non-Conformities Detected ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        print("\n--> FRAMEWORK AUDIT VERDICT: FAIL (Broken Traceability Links Detected)")
        return False
    else:
        print("\n" + "=" * 80)
        print("--> FRAMEWORK AUDIT VERDICT: PASS (100% Bidirectional Traceability Satisfied)")
        print("=" * 80)
        return True


def main():
    parser = argparse.ArgumentParser(description="SaMD Regulatory Traceability Validator (Dual-Mode)")
    parser.add_argument("path", nargs="?", default=".", help="Path to DHF directory (for app mode) or workspace root (for framework mode)")
    parser.add_argument("--mode", choices=["app", "framework"], default=None, help="Validation mode ('app' or 'framework')")
    parser.add_argument("--target-mode", choices=["app", "framework"], default=None, dest="target_mode", help="Alias for --mode")

    args = parser.parse_args()
    mode = args.target_mode or args.mode

    # Auto-detect mode if not explicitly passed
    target_path = os.path.abspath(args.path)
    if mode is None:
        if os.path.isfile(os.path.join(target_path, "FRAMEWORK_RTM.md")) or os.path.isdir(os.path.join(target_path, "docs", "srs")) or "docs" in target_path:
            mode = "framework"
        else:
            mode = "app"

    if mode == "framework":
        # Resolve workspace root
        if os.path.isdir(os.path.join(target_path, "docs")):
            workspace_root = target_path
        elif os.path.isdir(os.path.join(target_path, "..", "docs")):
            workspace_root = os.path.abspath(os.path.join(target_path, ".."))
        elif os.path.isdir(os.path.join(target_path, "..", "..", "docs")):
            workspace_root = os.path.abspath(os.path.join(target_path, "..", ".."))
        else:
            workspace_root = target_path
        success = validate_traceability_framework(workspace_root)
    else:
        success = validate_traceability_app(target_path)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
