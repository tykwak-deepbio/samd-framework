#!/usr/bin/env python3
"""
verify_grounding.py

SaMD LLM Grounding Verifier & Prompt Guard (DDS-FW-009 / IEC 62304 Cl 5.3).
Provides deterministic evaluation of:
1. Prompt Injection & Adversarial Jailbreak Detection (Regex signature matching).
2. Untrusted User Input Tag Encapsulation (<untrusted_input> boundaries).
3. PubMed / MeSH Scientific Citation Verification (PMID/DOI regex format validation).
4. Deterministic Temperature Clamping Verification (temperature = 0.0 greedy decoding).

Zero External Dependencies: Python 3 Standard Library only.
"""

import os
import sys
import re
import json
import argparse
from typing import Tuple, List, Dict, Any

# 7 Critical Prompt Injection Signatures (OWASP LLM Top 10 / STRIDE SEC-THR-004)
INJECTION_SIGNATURES = [
    r"ignore\s+(?:all\s+)?previous\s+instructions",
    r"disregard\s+(?:all\s+)?prior\s+prompts",
    r"you\s+are\s+now\s+an\s+unrestricted",
    r"jailbreak\s+mode",
    r"system\s*:\s*override",
    r"bypass\s+(?:safety|medical)\s+(?:guardrails|guidelines)",
    r"<script[\s\S]*?>[\s\S]*?<\/script>",
]


class PromptInjectionSecurityException(Exception):
    """Raised when an adversarial prompt injection pattern is detected."""
    pass


def sanitize_untrusted_input(text: str) -> str:
    """
    Scans input for adversarial injection patterns.
    If detected, raises PromptInjectionSecurityException.
    Otherwise, encapsulates in XML boundary tags for defensive prompt grounding.
    """
    for pattern in INJECTION_SIGNATURES:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            raise PromptInjectionSecurityException(
                f"Security violation: Adversarial injection pattern detected: '{match.group(0)}'"
            )
            
    # Encapsulate in boundary tags
    return f"<untrusted_input>\n{text.strip()}\n</untrusted_input>"


def verify_pubmed_citations(content: str) -> Tuple[bool, Dict[str, Any]]:
    """
    Scans markdown text for valid PMID or DOI clinical literature citations.
    Conforms to FR-LLM-001 (Grounding on Clinical SOTA).
    """
    pmid_pattern = r"(?:PMID:\s*|PubMed\s*(?:ID)?:\s*)(\d{7,9})"
    doi_pattern = r"(?:doi:\s*|https?:\/\/doi\.org\/)(10\.\d{4,9}\/[-._;()\/:A-Z0-9]+)"
    
    pmids = re.findall(pmid_pattern, content, re.IGNORECASE)
    dois = re.findall(doi_pattern, content, re.IGNORECASE)
    
    total_valid = len(pmids) + len(dois)
    report = {
        "valid_citations_count": total_valid,
        "pmids_found": list(set(pmids)),
        "dois_found": list(set(dois)),
        "grounding_status": "PASS" if total_valid > 0 else "NO_VERIFIED_CITATIONS"
    }
    
    if total_valid == 0:
        return False, report
    return True, report


def verify_temperature_clamp(temperature: float, max_allowed: float = 0.0) -> bool:
    """
    Verifies that model generation temperature is clamped to deterministic threshold.
    Conforms to IEC 62304 reproducibility and FR-LLM-003 deterministic standard (T = 0.0).
    """
    if temperature < 0.0 or temperature > max_allowed:
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description="SaMD LLM Grounding Verifier & Prompt Guard (DDS-FW-009)")
    parser.add_argument("--check-text", type=str, help="Text string to scan for prompt injection")
    parser.add_argument("--check-file", type=str, help="File path to scan for prompt injection")
    parser.add_argument("--verify-citations", type=str, help="Markdown file path to verify PMID/DOI citations")
    parser.add_argument("--check-temp", type=float, help="Check if temperature meets deterministic clamp (T = 0.0)")
    
    args = parser.parse_args()
    
    if args.check_text is not None:
        try:
            sanitized = sanitize_untrusted_input(args.check_text)
            print("[PASS] No prompt injection signatures detected.")
            print(sanitized)
            sys.exit(0)
        except PromptInjectionSecurityException as e:
            print(f"[SECURITY ALERT] {e}", file=sys.stderr)
            sys.exit(1)
            
    elif args.check_file:
        if not os.path.isfile(args.check_file):
            print(f"[ERROR] File not found: {args.check_file}", file=sys.stderr)
            sys.exit(1)
        with open(args.check_file, "r", encoding="utf-8") as f:
            content = f.read()
        try:
            sanitized = sanitize_untrusted_input(content)
            print(f"[PASS] File '{args.check_file}' passed prompt injection scan.")
            sys.exit(0)
        except PromptInjectionSecurityException as e:
            print(f"[SECURITY ALERT in {args.check_file}] {e}", file=sys.stderr)
            sys.exit(1)
            
    elif args.verify_citations:
        if not os.path.isfile(args.verify_citations):
            print(f"[ERROR] File not found: {args.verify_citations}", file=sys.stderr)
            sys.exit(1)
        with open(args.verify_citations, "r", encoding="utf-8") as f:
            content = f.read()
        passed, report = verify_pubmed_citations(content)
        print(json.dumps(report, indent=2))
        if passed:
            print(f"[PASS] Valid clinical citations found in '{args.verify_citations}'.")
            sys.exit(0)
        else:
            print(f"[FAIL] No valid PMIDs or DOIs found in '{args.verify_citations}'.", file=sys.stderr)
            sys.exit(1)
            
    elif args.check_temp is not None:
        is_clamped = verify_temperature_clamp(args.check_temp, max_allowed=0.0)
        if is_clamped:
            print(f"[PASS] Temperature {args.check_temp} satisfies deterministic greedy decoding (T = 0.0).")
            sys.exit(0)
        else:
            print(f"[FAIL] Temperature {args.check_temp} exceeds deterministic limit (> 0.0).", file=sys.stderr)
            sys.exit(1)
            
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
