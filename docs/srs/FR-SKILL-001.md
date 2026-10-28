# Software Requirement: FR-SKILL-001

> **Requirement ID**: `FR-SKILL-001`  
> **Title**: 13 Modular Antigravity Skills & YAML Frontmatter Compliance  
> **Category**: Antigravity Skills Ecosystem (`[SKILL]`)  
> **Safety Class**: Class B (IEC 62304)  
> **Parent Standard**: Antigravity Customization Specification (Skills Guide)  
> **Version**: 1.0.0 | **Status**: Approved  
> **1:1 Mapped Test Case**: `docs/tests/TC-FR-SKILL-001.md`  

---

## 1. Description & Technical Rationale
The framework shall package all lifecycle stage instructions into 13 discrete Antigravity Skills located under `.agents/skills/<skill-name>/SKILL.md`. Each skill must strictly conform to Antigravity frontmatter parsing rules to enable progressive disclosure and prevent context window exhaustion.

## 2. Detailed Functional Specifications
1. The framework shall provide exactly 13 modular skills:
   - `samd-orchestrator`, `samd-user-needs`, `samd-clinical-sota`, `samd-regulatory-strategy`, `samd-srs`, `samd-risk-mgmt`, `samd-cybersecurity`, `samd-arch-design`, `samd-detailed-design`, `samd-implementation`, `samd-vnv-testing`, `samd-dhf-audit`, `samd-maintenance`.
2. Each `SKILL.md` must begin with a valid YAML frontmatter block enclosed by `---`:
   ```yaml
   ---
   name: <skill-name>
   description: <third-person actionable description>
   ---
   ```
3. The `name` field must match the directory name, containing only lowercase alphanumeric characters and hyphens (`[a-z0-9\-]+`).
4. The `description` field must be non-empty and exceed 20 characters in length.

## 3. Inputs, Processing & Outputs
- **Inputs**: Skill directory path and markdown content.
- **Processing**: YAML frontmatter syntax validation, regex pattern matching on name and description.
- **Outputs**: Valid Antigravity skill registered in workspace index.
