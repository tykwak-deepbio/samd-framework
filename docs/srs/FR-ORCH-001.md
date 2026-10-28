# Software Requirement: FR-ORCH-001

> **Requirement ID**: `FR-ORCH-001`  
> **Title**: 12-Phase IEC 62304 V-Model Lifecycle & Gate Review Administration  
> **Category**: Orchestration & Lifecycle Governance (`[ORCH]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006+AMD1:2015 Clause 5.1 & Clause 6, ISO 13485:2016 Clause 7.3.2  
> **Version**: 1.1.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-ORCH-001.md`  

---

## 1. Description & Clinical/Regulatory Rationale
The SaMD Multi-Agent Framework shall provide a master orchestrator agent and skill that manages the 12 discrete phases of the IEC 62304 Software Life Cycle V-Model. Each phase transition shall be governed by formal Gate Exit Criteria to prevent premature implementation without verified design inputs.

## 2. Detailed Functional Specifications
1. The framework shall define and sequence Phases 1 through 12:
   - Phase 1: User Needs & Intended Use (`DHF-01`)
   - Phase 2: Clinical Literature & SOTA Benchmark (`DHF-02`)
   - Phase 3: Regulatory Affairs & Classification Strategy (`DHF-03`)
   - Phase 4: Software Requirements Specification (`DHF-04`)
   - Phase 5: Continuous Risk Management (`DHF-05A/B/C`)
   - Phase 6: Cybersecurity Threat Modeling & SBOM (`DHF-06`)
   - Phase 7: System & Software Architecture Design (`DHF-07`)
   - Phase 8: Detailed Software Design (`DHF-08`)
   - Phase 9: Software Implementation & Unit Verification (Code & Unit Tests)
   - Phase 10: Independent Verification & Validation (`DHF-09`)
   - Phase 11: Traceability Matrix & DHF Quality Audit (`DHF-10`, `DHF-11`)
   - Phase 12: Post-Market Maintenance, Continuous Monitoring & Anomaly Resolution (`DHF-13`, Gate 11/12)
2. The orchestrator skill (`.agents/skills/samd-orchestrator/SKILL.md`) and agent (`agents/00-samd-orchestrator-agent.md`) shall expose formal checklists for each gate.
3. The orchestrator shall prohibit advancing to Phase $N+1$ until Gate $N$ deliverables exist and meet verification thresholds.

## 3. Inputs, Processing & Outputs
- **Inputs**: Current project phase, active DHF documents.
- **Processing**: Verification of phase entry/exit criteria against gate checklists.
- **Outputs**: Phase advancement clearance or blocking defect report.
