# SaMD Multi-Agent Engineering Framework for Antigravity

[![Compliance](https://img.shields.io/badge/Standards-IEC%2062304%20%7C%20ISO%2014971%20%7C%20ISO%2013485-blue.svg)](#standards--regulatory-compliance)
[![Cybersecurity](https://img.shields.io/badge/Security-IEC%2081001--5--1%20%7C%20FDA%202023%20%7C%20ISO%2027799-green.svg)](#cybersecurity--sbom-compliance)
[![Regulatory Scope](https://img.shields.io/badge/Regulatory-MFDS%20%7C%20FDA%20510(k)%20%7C%20EU%20IVDR%2FCE-orange.svg)](#regulatory-jurisdictions)

An enterprise-grade, multi-agent development framework built for **Google Antigravity** to automate, govern, and audit the complete software lifecycle of **AI/ML-enabled Software as a Medical Device (SaMD)**.

This framework enforces the **IEC 62304 Software V-Model**, **ISO 14971 continuous risk management**, and **ISO 13485 Clause 7.3 design controls**, producing audit-ready **Design History File (DHF)** evidence with 100% bidirectional traceability.

---

## 1. Standards & Regulatory Compliance Matrix

| Standard / Regulation | Scope / Clause | Framework Implementation & Artifacts |
| :--- | :--- | :--- |
| **ISO 13485:2016** | Clause 7.3 Design and Development & DHF (7.3.7) | `DHF-00-DDP` through `DHF-11-AUDIT`, `scripts/generate_dhf_index.py` |
| **IEC 62304:2006+AMD1:2015** | Clauses 5.1 - 5.8, Clause 7, Clause 9 (Safety Class B/C) | Full V-Model: `DHF-04-SRS`, `DHF-07-SDS`, `DHF-08-DDS`, `DHF-09-VNV`, `DHF-10-RTM` |
| **ISO 14971:2019 / TR 24971**| Clauses 4 - 9 (Risk Management Lifecycle) | Continuous parallel track: `DHF-05A-RMP`, `DHF-05B-FMEA`, `DHF-05C-RMR` |
| **IEC 62366-1:2015+AMD1:2020**| Usability Engineering Process | User profiles (`DHF-01`), safety UI indicators (`DHF-08`), summative usability test (`TC-USE`) |
| **ISO/IEC 27001 & ISO 27799** | Health Informatics & Information Security | De-identification filter (`src/security/`), TLS 1.3 enforcement, RBAC |
| **IEC 81001-5-1 / FDA 2023** | Health Software Cybersecurity in Lifecycle | STRIDE threat modeling, CycloneDX SBOM, vulnerability management (`DHF-06`) |
| **South Korea MFDS** | 의료기기/체외진단의료기기 인허가 및 AI 가이드라인 | 기술문서 심사 양식, 소프트웨어 유효성확인(V&V) 성적서, AI 성능지표 검증 |
| **US FDA CDRH** | 21 CFR 864.3700 / 892, 510(k), GMLP, PCCP | 510(k) software documentation levels, predetermined change control plan (PCCP) |
| **EU IVDR (2017/746)** | Annex I GSPR, Annex II/III Technical Dossier, Annex XIII PER | SOTA clinical literature evaluation (`DHF-02`), diagnostic concordance ($\kappa$) |

---

## 2. V-Model & Parallel Lifecycle Architecture

```
                  [V-Model Decomposition & Design]                   [V-Model Integration & Verification]
  Phase 1: User Needs (Intended Use) ────────────── Gate 1 ──────► Phase 11: Final DHF Audit & RTM
           │                                                                 ▲
  Phase 2: Clinical SOTA & Lit. Review ──────────── Gate 2                   │
           │                                                                 │
  Phase 3: Regulatory Strategy & Profile ────────── Gate 3                   │
           │                                                                 │
  Phase 4: Software Requirements (SRS) ──────────── Gate 4 ──────► Phase 10: Independent V&V Testing
           │                                                                 ▲
  Phase 7: System & SW Architecture (SDS) ───────── Gate 6 ──────► Phase 10: Integration Testing
           │                                                                 ▲
  Phase 8: Detailed SW Design (DDS) ─────────────── Gate 7 ──────► Phase 9: Unit Verification
           │                                                                 ▲
           └────────────────► Phase 9: Implementation (Vertex) ──────────────┘

  [Continuous Parallel Track]:
  - Phase 5: Risk Management (ISO 14971: RMP -> PHA -> FMEA -> RCM -> RMR)
  - Phase 6: Cybersecurity & SBOM (IEC 81001-5-1, FDA: Threat Model -> SBOM -> CVE Mgmt)
```

---

## 3. Framework Repository Structure

```
samd-framework/
├── README.md                                 # Framework overview and quick-start guide
├── AGENTS.md                                 # Project rules enforcing regulatory invariants
├── .agents/
│   ├── rules/AGENTS.md                       # Antigravity hierarchical rule mirror
│   ├── plugins/samd-framework/               # Antigravity shareable plugin bundle
│   └── skills/                               # 12 Antigravity on-demand skills
│       ├── samd-orchestrator/SKILL.md        # Master lifecycle & gate review coordinator
│       ├── samd-user-needs/SKILL.md          # Phase 1: User needs & intended use discovery
│       ├── samd-clinical-sota/SKILL.md       # Phase 2: Systematic literature & SOTA review
│       ├── samd-regulatory-strategy/SKILL.md # Phase 3: Global classification & standard mapping
│       ├── samd-srs/SKILL.md                 # Phase 4: IEC 62304 software requirements
│       ├── samd-risk-mgmt/SKILL.md           # Phase 5: ISO 14971 continuous risk management
│       ├── samd-cybersecurity/SKILL.md       # Phase 6: Threat modeling, SBOM, vulnerability
│       ├── samd-arch-design/SKILL.md         # Phase 7: Architectural design & SOUP isolation
│       ├── samd-detailed-design/SKILL.md     # Phase 8: Detailed unit design & algorithms
│       ├── samd-implementation/SKILL.md      # Phase 9: Regulated coding & defensive checks
│       ├── samd-vnv-testing/SKILL.md         # Phase 10: Independent V&V and AI validation
│       └── samd-dhf-audit/SKILL.md           # Phase 11: Traceability matrix & DHF audit
├── agents/                                   # 12 Subagent persona and prompt specifications
│   ├── 00-samd-orchestrator-agent.md
│   ├── 01-user-needs-agent.md
│   ├── 02-clinical-sota-agent.md
│   ├── 03-regulatory-affairs-agent.md
│   ├── 04-srs-analyst-agent.md
│   ├── 05-risk-management-agent.md
│   ├── 06-cybersecurity-agent.md
│   ├── 07-system-architect-agent.md
│   ├── 08-detailed-design-agent.md
│   ├── 09-software-developer-agent.md
│   ├── 10-vnv-test-engineer-agent.md
│   └── 11-dhf-lead-auditor-agent.md
├── templates/                                # 14 Global English DHF Templates with Korean Guidance
│   ├── DHF-00-Design-and-Development-Plan-DDP.md
│   ├── DHF-01-Intended-Use-and-URD.md
│   ├── DHF-02-Clinical-Literature-and-SOTA.md
│   ├── DHF-03-Regulatory-Strategy-and-Clearance-Profile.md
│   ├── DHF-04-Software-Requirements-Specification-SRS.md
│   ├── DHF-05A-Risk-Management-Plan-RMP.md
│   ├── DHF-05B-Hazard-Analysis-and-FMEA-Matrix.md
│   ├── DHF-05C-Risk-Management-Report-RMR.md
│   ├── DHF-06-Cybersecurity-Threat-Model-and-SBOM.md
│   ├── DHF-07-Software-Architectural-Design-Specification-SDS.md
│   ├── DHF-08-Software-Detailed-Design-Specification-DDS.md
│   ├── DHF-09-Software-Verification-and-Validation-Report.md
│   ├── DHF-10-Traceability-Matrix-RTM.md
│   └── DHF-11-DHF-Index-and-Quality-Audit-Report.md
├── workflows/                                # Detailed stage execution guides
│   ├── 00-v-model-lifecycle-workflow.md
│   ├── 01-requirements-and-clinical-workflow.md
│   ├── 02-risk-and-cybersecurity-parallel-workflow.md
│   ├── 03-design-and-implementation-workflow.md
│   ├── 04-independent-vnv-workflow.md
│   └── 05-dhf-audit-and-submission-workflow.md
├── scripts/                                  # Automated regulatory audit tools
│   ├── validate_traceability.py              # Bidirectional traceability & orphan checker
│   └── generate_dhf_index.py                 # SHA-256 DHF Master Index generator
└── examples/
    └── wsi-tissue-viewer-samd/               # Reference Project: "PathoView-AI" WSI Viewer
        ├── dhf/                              # Complete, validated 14 DHF documents
        ├── src/                              # Regulated source code with docstring tags
        └── tests/                            # Unit, system, AI, and security tests (100% PASS)
```

---

## 4. Traceability & Identifier Standards

All artifacts MUST adhere to persistent, verifiable identifiers to maintain traceability across the Design History File:

| Tag Prefix | Description | Example | Target DHF Document |
| :--- | :--- | :--- | :--- |
| `USER-REQ-xxx` | Clinical / End-User Requirements | `USER-REQ-001` | `DHF-01-URD` |
| `CLIN-REQ-xxx` | SOTA Clinical Performance Baselines | `CLIN-REQ-001` | `DHF-02-SOTA` |
| `REG-REQ-xxx` | Regional Regulatory Mandates | `REG-REQ-001` | `DHF-03-REG` |
| `REQ-SW-xxx` | IEC 62304 Software Requirements | `REQ-SW-001` | `DHF-04-SRS` |
| `RSK-xxx` | Hazards / Hazardous Situations | `RSK-001` | `DHF-05B-FMEA` |
| `RCM-xxx` | Risk Control Measures | `RCM-001` | `DHF-05B-FMEA` |
| `SEC-THR-xxx` | STRIDE Cybersecurity Threats | `SEC-THR-001` | `DHF-06-CYBER` |
| `SEC-CTL-xxx` | Cybersecurity Controls | `SEC-CTL-001` | `DHF-06-CYBER` |
| `ARCH-xxx` | High-Level Architecture Components | `ARCH-001` | `DHF-07-SDS` |
| `SOUP-xxx` | Software of Unknown Provenance | `SOUP-001` | `DHF-06` / `DHF-07` |
| `DDS-xxx` | Software Detailed Design Units | `DDS-001` | `DHF-08-DDS` |
| `TC-xxx` | Verification Test Protocols (`TC-SYS-`, `TC-AI-`, etc.) | `TC-SYS-001` | `DHF-09-VNV` |
| `VERIF-xxx` | Objective Verification Evidence Records | `VERIF-001` | `DHF-09-VNV` |

---

## 5. Quick-Start Guide: Applying to a New SaMD Project

### Step 1: Copy Framework Assets into Target Project
In your new medical device repository, mount or copy the framework files:
```bash
# In target project workspace:
cp -r /path/to/samd-framework/.agents .
cp -r /path/to/samd-framework/templates .
cp -r /path/to/samd-framework/scripts .
cp /path/to/samd-framework/AGENTS.md .
mkdir -p dhf src tests
```

### Step 2: Launch the Orchestrator in Antigravity
Inside Antigravity, invoke the master orchestrator skill:
```text
/samd-orchestrator
"Initiate SaMD development for [Device Name] following the IEC 62304 V-model."
```

### Step 3: Execute Lifecycle Stages Progressively
The orchestrator will prompt and guide you through each stage gate:
1. **Phase 1 (User Needs)**: Invoke `/samd-user-needs` -> Answer structured clinical Q&A -> Generates `dhf/DHF-01-Intended-Use-and-URD.md`.
2. **Phase 2 (Clinical SOTA)**: Invoke `/samd-clinical-sota` -> Generates `dhf/DHF-02-Clinical-Literature-and-SOTA.md`.
3. **Phase 3 (Regulatory Strategy)**: Invoke `/samd-regulatory-strategy` -> Generates `dhf/DHF-03-Regulatory-Strategy-and-Clearance-Profile.md`.
4. **Phase 4 (SRS)**: Invoke `/samd-srs` -> Decomposes into `REQ-SW-xxx` -> Generates `dhf/DHF-04-Software-Requirements-Specification-SRS.md`.
5. **Phase 5 & 6 (Parallel Risk & Cyber)**: Invoke `/samd-risk-mgmt` and `/samd-cybersecurity` -> Generates `DHF-05A/B/C` and `DHF-06`.
6. **Phase 7 & 8 (Architecture & Detailed Design)**: Invoke `/samd-arch-design` and `/samd-detailed-design` -> Generates `DHF-07` and `DHF-08`.
7. **Phase 9 (Coding & Unit Verification)**: Invoke `/samd-implementation` -> Implements code in `src/` and unit tests in `tests/`.
8. **Phase 10 (Independent V&V)**: Invoke `/samd-vnv-testing` -> Generates `dhf/DHF-09-Software-Verification-and-Validation-Report.md`.
9. **Phase 11 (Audit & Sign-Off)**: Invoke `/samd-dhf-audit` -> Generates `dhf/DHF-10-Traceability-Matrix-RTM.md` and `dhf/DHF-11-DHF-Index-and-Quality-Audit-Report.md`.

---

## 6. Automated Validation & Verification Commands

### 1. Bidirectional Traceability Verification
Run the traceability checker to verify zero broken links and zero orphan requirements:
```bash
python3 scripts/validate_traceability.py dhf/
```
*Exit Code: 0 on 100% compliance; 1 on missing links or orphaned items.*

### 2. Cryptographic DHF Master Index Generation
Compute SHA-256 signatures and update document control indices:
```bash
python3 scripts/generate_dhf_index.py dhf/
```

### 3. Run Unit and Verification Tests
```bash
PYTHONPATH=. python3 -m unittest discover -s tests -v
```

---

## 7. Reference Project: "PathoView-AI"

A complete, working reference project is included under `examples/wsi-tissue-viewer-samd/`:
- **Clinical Modality**: Digital Pathology Whole Slide Imaging (WSI).
- **Core AI/ML Features**:
  1. Multiresolution pyramidal tile streaming & LRU caching (`TileStreamer`).
  2. Stain deconvolution and background illumination normalization (`MacenkoNormalizer`).
  3. AI-driven tissue region detection with confidence monitoring and alert banners (`TissueSegmenter`).
  4. DICOM PHI scrubbing filter (`sanitize_metadata`).
- **Pre-verified DHF Files**: All 14 DHF markdown documents are included, verified with 100% pass rate in `examples/wsi-tissue-viewer-samd/dhf/`.
- **Pre-verified Tests**: 10 automated unit, system, and AI validation tests in `examples/wsi-tissue-viewer-samd/tests/`.
