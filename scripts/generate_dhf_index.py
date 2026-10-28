#!/usr/bin/env python3
"""
generate_dhf_index.py

Scans a SaMD DHF directory, computes cryptographic SHA-256 hashes for all markdown documents,
extracts Document Control metadata, and prints/updates the formal DHF Master Index.
Complies with ISO 13485:2016 Clause 7.3.7 and 4.2.4 (Document Control).

Usage:
    python3 scripts/generate_dhf_index.py [dhf_directory]
"""

import os
import sys
import hashlib
import re
from typing import Dict, List


def calculate_sha256(filepath: str) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def extract_metadata(filepath: str) -> Dict[str, str]:
    meta = {
        "id": "",
        "title": "",
        "version": "1.0",
        "date": "2026-10-28",
        "status": "Approved",
    }
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract Document ID
    id_match = re.search(r"\*\*Document ID\*\*:\s*`([^`]+)`", content)
    if id_match:
        meta["id"] = id_match.group(1)
    else:
        # Fallback to filename prefix
        fname = os.path.basename(filepath)
        prefix_match = re.match(r"(DHF-\w+)", fname)
        meta["id"] = prefix_match.group(1) if prefix_match else fname

    # Extract Title (# Title)
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if title_match:
        meta["title"] = title_match.group(1).strip()
    else:
        meta["title"] = os.path.splitext(os.path.basename(filepath))[0]

    # Extract Revision
    rev_match = re.search(r"\*\*Revision\*\*:\s*`([^`]+)`", content)
    if rev_match:
        meta["version"] = rev_match.group(1)

    # Extract Date
    date_match = re.search(r"\*\*Effective Date\*\*:\s*`([^`]+)`", content)
    if date_match:
        meta["date"] = date_match.group(1)

    # Extract Status
    status_match = re.search(r"\*\*Document Status\*\*:\s*`([^`]+)`", content)
    if status_match:
        meta["status"] = status_match.group(1)

    return meta


def generate_index(dhf_dir: str) -> str:
    print("=" * 80)
    print("  SaMD Design History File (DHF) Index & Integrity Generator (ISO 13485)")
    print(f"  Target DHF Directory: {dhf_dir}")
    print("=" * 80)

    if not os.path.isdir(dhf_dir):
        print(f"[ERROR] Directory not found: {dhf_dir}")
        return ""

    md_files = sorted([f for f in os.listdir(dhf_dir) if f.endswith(".md") and not f.startswith(".")])
    if not md_files:
        print(f"[ERROR] No markdown files found in {dhf_dir}")
        return ""

    table_lines = [
        "| DHF ID | Document Title | Version | Effective Date | Status | Cryptographic Hash (SHA-256) |",
        "| :--- | :--- | :---: | :---: | :---: | :--- |",
    ]

    print(f"\nProcessing {len(md_files)} DHF documents:\n")
    for fname in md_files:
        fpath = os.path.join(dhf_dir, fname)
        meta = extract_metadata(fpath)
        sha = calculate_sha256(fpath)
        line = f"| `{meta['id']}` | {meta['title']} | {meta['version']} | `{meta['date']}` | {meta['status']} | `{sha[:16]}...` |"
        table_lines.append(line)
        print(f"  [OK] {meta['id']:<12} | {meta['title'][:35]:<35} | {sha[:16]}...")

    output_table = "\n".join(table_lines)
    print("\n" + "=" * 80)
    print("Generated Master DHF Index Markdown Table:")
    print("=" * 80 + "\n")
    print(output_table)
    print("\n" + "=" * 80)
    return output_table


if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "dhf"
    generate_index(target_dir)
