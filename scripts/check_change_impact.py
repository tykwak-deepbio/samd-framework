#!/usr/bin/env python3
"""
check_change_impact.py

Automated Change Impact Analysis (CIA) & Cascading Invalidation Tool.
Enforces ISO 13485:2016 Clause 7.3.9 (Control of Design Changes) and IEC 62304 Clause 8.

Principle of Cascading Invalidation:
If an upstream artifact (e.g., User Needs, SRS, Architecture) is modified,
all downstream approvals in the V-model dependency tree are automatically REVOKED
and must undergo sequential re-verification and re-approval.

Usage:
    python3 scripts/check_change_impact.py [dhf_directory] [--baseline-file .baseline.json] [--modified DHF-04-SRS.md]
"""

import os
import sys
import hashlib
import json
import re
from typing import Dict, List, Set


# IEC 62304 V-Model Downstream Dependency Map (ISO 13485 Cl 7.3.9 & IEC 62304 Cl 8)
VMODEL_DEPENDENCIES = {
    "DHF-00": ["DHF-01", "DHF-02", "DHF-03", "DHF-04", "DHF-05A", "DHF-07", "DHF-08", "DHF-09", "DHF-10", "DHF-11", "DHF-12", "DHF-13"],
    "DHF-01": ["DHF-04", "DHF-05B", "DHF-07", "DHF-08", "DHF-09", "DHF-10", "DHF-11", "DHF-12"],
    "DHF-02": ["DHF-04", "DHF-09", "DHF-10", "DHF-11", "DHF-15"],
    "DHF-03": ["DHF-04", "DHF-07", "DHF-10", "DHF-11"],
    "DHF-04": ["DHF-05B", "DHF-06", "DHF-07", "DHF-08", "DHF-09", "DHF-10", "DHF-11", "DHF-12", "DHF-14"],
    "DHF-05A": ["DHF-05B", "DHF-05C", "DHF-11"],
    "DHF-05B": ["DHF-05C", "DHF-07", "DHF-08", "DHF-09", "DHF-10", "DHF-11", "DHF-14", "DHF-15"],
    "DHF-05C": ["DHF-11", "DHF-13", "DHF-15"],
    "DHF-06": ["DHF-07", "DHF-08", "DHF-09", "DHF-10", "DHF-11", "DHF-13"],
    "DHF-07": ["DHF-08", "DHF-09", "DHF-10", "DHF-11"],
    "DHF-08": ["DHF-09", "DHF-10", "DHF-11"],
    "DHF-09": ["DHF-10", "DHF-11", "DHF-13", "DHF-15"],
    "DHF-10": ["DHF-11"],
    "DHF-11": ["DHF-13"],
    "DHF-12": ["DHF-09", "DHF-10", "DHF-11", "DHF-14"],
    "DHF-13": ["DHF-05C", "DHF-11"],
    "DHF-14": ["DHF-11"],
    "DHF-15": ["DHF-11"],
}


def calculate_sha256(filepath: str) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def get_doc_id(filename: str) -> str:
    m = re.match(r"(DHF-\w+)", filename)
    return m.group(1) if m else filename


def find_downstream_impacts(modified_doc_ids: Set[str]) -> Set[str]:
    invalidated: Set[str] = set()
    queue = list(modified_doc_ids)
    visited: Set[str] = set(modified_doc_ids)

    while queue:
        curr = queue.pop(0)
        # Find all keys matching prefix (e.g. DHF-05 matches DHF-05A/B/C)
        for key, deps in VMODEL_DEPENDENCIES.items():
            if curr.startswith(key):
                for dep in deps:
                    if dep not in visited:
                        visited.add(dep)
                        invalidated.add(dep)
                        queue.append(dep)
    return invalidated


def run_change_impact_analysis(dhf_dir: str, explicit_modified: List[str] = None) -> int:
    print("=" * 80)
    print("  SaMD Cascading Invalidation & Change Impact Analysis (ISO 13485 / IEC 62304)")
    print(f"  Target DHF Directory: {dhf_dir}")
    print("=" * 80)

    if not os.path.isdir(dhf_dir):
        print(f"[ERROR] Directory not found: {dhf_dir}")
        return 1

    baseline_file = os.path.join(dhf_dir, ".dhf_baseline.json")
    all_files = sorted([f for f in os.listdir(dhf_dir) if f.endswith(".md") and not f.startswith(".")])

    modified_files = set()
    if explicit_modified:
        for em in explicit_modified:
            modified_files.add(os.path.basename(em))

    # Compare against saved baseline if exists
    if os.path.exists(baseline_file):
        with open(baseline_file, "r", encoding="utf-8") as f:
            baseline_data = json.load(f)

        for fname in all_files:
            fpath = os.path.join(dhf_dir, fname)
            curr_hash = calculate_sha256(fpath)
            if fname not in baseline_data or baseline_data[fname] != curr_hash:
                modified_files.add(fname)
    else:
        # Check document status inside files
        for fname in all_files:
            fpath = os.path.join(dhf_dir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            if "Draft" in content or "In-Review" in content:
                # Upstream document is in draft/review state
                modified_files.add(fname)

    if not modified_files:
        print("\n[OK] No upstream modifications detected since approved baseline.")
        print("--> Gate Review Status: All current approvals remain VALID.")
        print("=" * 80)
        return 0

    print(f"\n[!] Detected {len(modified_files)} Modified Upstream Document(s):")
    modified_ids = set()
    for mf in sorted(modified_files):
        doc_id = get_doc_id(mf)
        modified_ids.add(doc_id)
        print(f"  - [{doc_id}] {mf}")

    # Compute cascading invalidation
    invalidated_ids = find_downstream_impacts(modified_ids)

    print("\n" + "-" * 80)
    print("  [CASCADING INVALIDATION REPORT] Downstream Approvals Revoked:")
    print("-" * 80)
    if invalidated_ids:
        for inv in sorted(invalidated_ids):
            # Find matching filenames
            matched = [f for f in all_files if inv in f]
            matched_str = f" ({', '.join(matched)})" if matched else ""
            print(f"  [X] {inv:<12} --> STATUS: INVALIDATED (APPROVAL REVOKED){matched_str}")
    else:
        print("  (No downstream artifacts impacted)")

    print("\n" + "=" * 80)
    print("--> REGULATORY VERDICT: CODE 2 (CASCADING DOWNSTREAM INVALIDATION DETECTED)")
    print("    Required Actions: Perform sequential re-verification and re-approval down the V-model.")
    print("=" * 80)
    return 2


def save_current_as_baseline(dhf_dir: str):
    baseline_file = os.path.join(dhf_dir, ".dhf_baseline.json")
    all_files = sorted([f for f in os.listdir(dhf_dir) if f.endswith(".md") and not f.startswith(".")])
    data = {}
    for fname in all_files:
        fpath = os.path.join(dhf_dir, fname)
        data[fname] = calculate_sha256(fpath)

    with open(baseline_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Saved baseline hashes for {len(data)} documents into {baseline_file}")


if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "dhf"
    if "--save-baseline" in sys.argv:
        save_current_as_baseline(target_dir)
        sys.exit(0)

    explicit_mods = []
    if "--modified" in sys.argv:
        idx = sys.argv.index("--modified")
        if idx + 1 < len(sys.argv):
            explicit_mods.append(sys.argv[idx + 1])

    exit_code = run_change_impact_analysis(target_dir, explicit_mods)
    sys.exit(exit_code)
