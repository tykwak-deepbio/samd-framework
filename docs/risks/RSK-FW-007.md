# Risk Analysis: RSK-FW-007

> **Risk ID**: `RSK-FW-007`  
> **Risk Control Measure ID**: `RCM-FW-007`  
> **Title**: Workspace Rule Tampering, Omission, or Exceeding Context Budget  
> **Standard Reference**: ISO 14971:2019 Clause 5.4, ISO 13485:2016 Clause 4.2.4  
> **Target Requirement**: `FR-RULE-001`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-002.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-006.md`  
> **Verification Test Protocol**: `docs/tests/TC-FR-RULE-001.md`  

---

## 1. Hazard, Sequence of Events & Hazardous Situation
- **Hazard**: Silent ignoring of workspace medical rules due to oversized rule files or accidental rule modification.
- **Sequence of Events**:
  1. An agent or developer expands `AGENTS.md` beyond the 24,000-byte budget limit (`defaultRulesBudget`).
  2. The Antigravity runtime silently ignores or drops the oversized rule file.
  3. The agent operates without SaMD engineering constraints (tag prefixes, bidirectional trace mandate).
- **Hazardous Situation**: Agents produce code and documentation violating ISO 13485 / IEC 62304 standards without raising errors.
- **Harm**: Premarket submission rejection, severe audit findings, non-compliant medical device software. (Severity: S3 - Serious, Probability: P3 - Medium $\to$ **Initial Risk: Medium / ALARP**).

## 2. Risk Control Measure: RCM-FW-007
- **Control Measure Description**: The framework enforces **Automated Workspace Rule Budget & Schema Verification**.
  - `AGENTS.md` is maintained under strict conciseness guidelines (< 24,000 bytes, currently ~5.5 KB).
  - An automated test in `scripts/test_framework.py` asserts that `AGENTS.md` exists, is $\le 24,000$ bytes, and contains all 10 mandatory prefix tags (`USER-REQ`, `REQ-SW`, `RSK`, `RCM`, `ARCH`, `DDS`, `TC-`, `VERIF-`).
- **Control Type**: Inherent Verification / Static Rule Gate.

## 3. Residual Risk Evaluation
- **Residual Severity**: S1.
- **Residual Probability**: P1 (Automated test fails build if rule exceeds budget or drops mandatory tags).
- **Residual Risk Level**: **Negligible / Acceptable**.
- **Verification Evidence**: `VERIF-FW-028` via `TC-FR-RULE-001.md`.
## 4. Evaluation of New Hazards Arising from Risk Control Measures (ISO 14971:2019 Cl 7.3 & IEC 62304 Cl 7.2.2)
- **Potential New Hazards Introduced**:
  - Rule file permission lockouts preventing administrative configuration updates or legitimate regulatory adaptations.
  - Multi-file rule duplication causing context token waste or drift.
- **Secondary Risk Mitigations**:
  - Authoritative single canonical root `AGENTS.md` placement eliminating token duplication and drift.
  - Automated rule size and content checker (`test_ts_skill_002_agents_rules`) validating size budget and mandatory tags.
  - Administrative role segregation requiring explicit human approval token to modify rule files.
  - Version-controlled changelog with mandatory regulatory impact analysis for any rule modification.
- **Residual Risk Conclusion**: No unacceptable secondary hazards introduced. Residual risk remains **Acceptable (ALARP satisfied)**.
