# Software Requirement: FR-CM-001

> **Requirement ID**: `FR-CM-001`  
> **Title**: Software Configuration Management & Deterministic Build Reproducibility  
> **Category**: Configuration Management (`[CM]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006 Clause 8 (Software configuration management), ISO 13485:2016 Clause 4.2.4  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-CM-001.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-011.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-005.md`  

---

## 1. Description & Technical Rationale
The framework shall implement configuration management under IEC 62304 Clause 8, uniquely identifying all configuration items (source code, AI model weights, prompts, build toolchains), establishing frozen release baselines, and guaranteeing 100% deterministic build reproducibility.

## 2. Detailed Functional Specifications
1. **Configuration Item Identification (Clause 8.1)**: Uniquely tag configuration items with `CI-xxx` prefixes, encompassing:
   - Source code commits (Git SHA)
   - AI model weights (SHA-256 digest)
   - System prompts and Antigravity skill definitions
   - Dependency lockfiles (`requirements.txt`, `poetry.lock`, Docker digest)
2. **Change Control & Baseline Freezing (Clause 8.2)**:
   - Mandate Change Control Board (CCB) approval for baseline modifications.
   - Prevent unauthorized edits to frozen baseline artifacts.
3. **Configuration Status Accounting (Clause 8.3)**:
   - Archive exact build environments to ensure any released version can be bit-for-bit reproduced throughout the device's commercial lifecycle.

## 3. Inputs, Processing & Outputs
- **Inputs**: Release build assets, model weights, dependency lockfiles.
- **Processing**: Cryptographic hashing, configuration baseline ledger recording.
- **Outputs**: Configuration status accounting report, deterministic build verification record.
