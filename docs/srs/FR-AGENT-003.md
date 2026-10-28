# Software Requirement: FR-AGENT-003

> **Requirement ID**: `FR-AGENT-003`  
> **Title**: Subagent Role-Based Access Control (RBAC) & Read-Only Sandbox Isolation  
> **Category**: Subagent Architecture (`[AGENT]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: IEC 62304:2006 Clause 5.6.2 & 5.7.2, ISO 13485:2016 Clause 7.3.6  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-AGENT-003.md`  
> **Allocated Architecture**: `docs/architecture/ARCH-FW-002.md`, `docs/architecture/ARCH-FW-009.md`  
> **Allocated Detailed Design**: `docs/detailed_design/DDS-FW-006.md`  

---

## 1. Description & Technical Rationale
To guarantee the technical independence of verification under IEC 62304 Clause 5.6/5.7, the framework shall enforce role-based access control (RBAC) on subagents, programmatically revoking filesystem write permissions on production code (`src/`) for testing and audit agents.

## 2. Detailed Functional Specifications
1. **Agent Permission Profiles**:
   - `software-developer-agent`: Read/Write access to `src/`, `tests/unit/`.
   - `vnv-test-engineer-agent`: Read-Only access to `src/`, Write access to `tests/integration/`, `tests/system/`, and `DHF-09`.
   - `dhf-lead-auditor-agent`: Read-Only access to all source and test directories; Write access restricted strictly to `DHF-10` and `DHF-11`.
2. **Enforcement Mechanism**:
   - When launching `vnv-test-engineer-agent` or `dhf-lead-auditor-agent` via `invoke_subagent`, write tools shall either be disabled (`enable_write_tools = false`) or sandboxed with OS-level read-only file mounts.
3. **Tamper Prevention**:
   - Any write attempt by a verification agent to `src/` triggers an immediate security error and audit log flag.

## 3. Inputs, Processing & Outputs
- **Inputs**: Agent role definition, subagent launch payload.
- **Processing**: Tool filter application, filesystem access permission check.
- **Outputs**: Sandboxed subagent execution context, permission boundary logs.
