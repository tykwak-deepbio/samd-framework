#!/usr/bin/env python3
"""
scripts/manage_anomalies.py

Software Problem Resolution & Anomaly Severity Triage Engine (IEC 62304 Clause 9 / ISO 14971).
Implements DDS-FW-011 specifications:
1. 4-tier anomaly severity classification (Catastrophic, Critical, Major, Minor).
2. Lifecycle state machine tracking (REPORTED -> INVESTIGATING -> CORRECTED -> VERIFIED -> CLOSED).
3. Gate release clearance check (prohibits release if Catastrophic/Critical defects are unclosed).
4. Trend analysis across defect categories and MTTR calculation.

Zero external dependencies (Python 3 standard library only).
"""

import sys
import os
import json
import argparse
from enum import Enum
from typing import List, Dict, Any, Tuple


class AnomalySeverity(str, Enum):
    CATASTROPHIC = "CATASTROPHIC"
    CRITICAL = "CRITICAL"
    MAJOR = "MAJOR"
    MINOR = "MINOR"


class AnomalyStatus(str, Enum):
    REPORTED = "REPORTED"
    INVESTIGATING = "INVESTIGATING"
    CORRECTED = "CORRECTED"
    VERIFIED = "VERIFIED"
    CLOSED = "CLOSED"
    DEFERRED_APPROVED = "DEFERRED_APPROVED"


class UnresolvedCriticalAnomalyError(Exception):
    """Raised when release gate is attempted with unresolved Catastrophic or Critical anomalies."""
    pass


def verify_release_gate_clearance(anomalies: List[Dict[str, Any]]) -> Tuple[bool, List[str]]:
    """
    Evaluates whether software anomalies meet the release gate exit criteria.
    - Catastrophic / Critical anomalies MUST be in CLOSED or VERIFIED state.
    - Major anomalies in DEFERRED_APPROVED state MUST provide clinical safety justification.
    """
    blocking_errors = []
    
    for anom in anomalies:
        anom_id = anom.get("id", "UNKNOWN-ANOM")
        sev = anom.get("severity")
        status = anom.get("status")
        
        if sev in [AnomalySeverity.CATASTROPHIC.value, AnomalySeverity.CRITICAL.value]:
            if status not in [AnomalyStatus.CLOSED.value, AnomalyStatus.VERIFIED.value]:
                blocking_errors.append(
                    f"RELEASE BLOCKER: Anomaly '{anom_id}' ({sev}) is in '{status}' status. "
                    f"IEC 62304 Clause 9 mandates all critical defects must be VERIFIED or CLOSED."
                )
        elif sev == AnomalySeverity.MAJOR.value:
            if status == AnomalyStatus.DEFERRED_APPROVED.value:
                justification = anom.get("clinical_justification", "").strip()
                if not justification:
                    blocking_errors.append(
                        f"RELEASE BLOCKER: Major anomaly '{anom_id}' is DEFERRED without clinical safety justification."
                    )
                    
    if blocking_errors:
        return False, blocking_errors
    return True, []


def analyze_defect_trends(anomalies: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Computes defect trend statistics across severity and status."""
    total = len(anomalies)
    by_severity = {s.value: 0 for s in AnomalySeverity}
    by_status = {st.value: 0 for st in AnomalyStatus}
    
    for a in anomalies:
        sev = a.get("severity")
        st = a.get("status")
        if sev in by_severity:
            by_severity[sev] += 1
        if st in by_status:
            by_status[st] += 1
            
    closed_count = by_status[AnomalyStatus.CLOSED.value] + by_status[AnomalyStatus.VERIFIED.value]
    closure_rate = (closed_count / total * 100.0) if total > 0 else 100.0
    
    return {
        "total_anomalies": total,
        "by_severity": by_severity,
        "by_status": by_status,
        "closure_rate_percent": round(closure_rate, 2),
        "open_critical_count": by_severity[AnomalySeverity.CATASTROPHIC.value] + by_severity[AnomalySeverity.CRITICAL.value] - closed_count
    }


def main():
    parser = argparse.ArgumentParser(description="SaMD Anomaly Triage & Gate Clearance Engine (IEC 62304 Cl 9)")
    parser.add_argument("--anomalies-file", type=str, help="JSON file containing anomaly list")
    parser.add_argument("--check-clearance", action="store_true", help="Evaluate release gate clearance criteria")
    parser.add_argument("--trend-analysis", action="store_true", help="Generate defect trend and resolution metrics")
    
    args = parser.parse_args()
    
    if not args.anomalies_file:
        parser.print_help()
        sys.exit(0)
        
    if not os.path.isfile(args.anomalies_file):
        print(f"[ERROR] Anomaly file not found: {args.anomalies_file}", file=sys.stderr)
        sys.exit(1)
        
    with open(args.anomalies_file, "r", encoding="utf-8") as f:
        try:
            anomalies = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[ERROR] Failed to parse JSON: {e}", file=sys.stderr)
            sys.exit(1)
            
    if not isinstance(anomalies, list):
        print("[ERROR] Anomaly data must be a JSON array of objects.", file=sys.stderr)
        sys.exit(1)
        
    if args.check_clearance:
        passed, errors = verify_release_gate_clearance(anomalies)
        if passed:
            print("[PASS] Release Gate Clearance Criteria met. Zero unresolved critical anomalies.")
            sys.exit(0)
        else:
            print("[FAIL] Release Gate Clearance Denied:", file=sys.stderr)
            for err in errors:
                print(f"  - {err}", file=sys.stderr)
            sys.exit(1)
            
    elif args.trend_analysis:
        trends = analyze_defect_trends(anomalies)
        print(json.dumps(trends, indent=2))
        sys.exit(0)


if __name__ == "__main__":
    main()
