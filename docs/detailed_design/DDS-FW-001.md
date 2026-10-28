# Detailed Design Specification: DDS-FW-001

> **Unit Design ID**: `DDS-FW-001`  
> **Title**: YAML Frontmatter Lexer & Skill Contract Validator Unit  
> **Parent Architecture**: `docs/architecture/ARCH-FW-001.md`  
> **Safety Class**: Class B (IEC 62304 Clause 5.4)  
> **Allocated Risk Controls**: `RCM-FW-006`, `RCM-FW-015`  
> **Target Requirement**: `FR-SKILL-001`, `FR-SKILL-002`, `FR-MCP-001`  
> **Implementation Target**: `scripts/test_framework.py` (`test_ts_skill_001_skills_schema`)  
> **Verification Test Protocol**: `docs/tests/TC-FR-SKILL-001.md`, `docs/tests/TC-FR-SKILL-002.md`, `docs/tests/TC-FR-MCP-001.md`  

---

## 1. Detailed Unit Description & Rationale
`DDS-FW-001` specifies the unit algorithm for validating that every skill under `.agents/skills/<name>/SKILL.md` adheres to the Antigravity skill specification: starting with YAML delimiters (`---`), defining a lowercase hyphenated name matching its directory, and providing a substantive description without third-party dependencies.

## 2. Data Structures & Interface Signatures
```python
class SkillMetadata:
    name: str             # regex: ^[a-z0-9\-]+$
    description: str      # len(description) > 20
    filepath: str         # absolute path to SKILL.md
    is_valid: bool        # validation verdict
```

## 3. Algorithmic Pseudocode & Logic
```python
def validate_skill_file(skill_dir: str, expected_name: str) -> bool:
    skill_file = os.path.join(skill_dir, "SKILL.md")
    assert os.path.isfile(skill_file), f"Missing SKILL.md in {skill_dir}"
    
    with open(skill_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    assert content.startswith("---\n"), "File must start with YAML delimiter"
    parts = content.split("---\n", 2)
    assert len(parts) >= 3, "Frontmatter must be closed by ---"
    
    frontmatter = parts[1]
    name_match = re.search(r"^name:\s*([a-z0-9\-]+)$", frontmatter, re.MULTILINE)
    assert name_match is not None, "Missing or invalid 'name' field"
    assert name_match.group(1) == expected_name, f"Name mismatch: {name_match.group(1)} != {expected_name}"
    
    desc_match = re.search(r"description:\s*(.+)", frontmatter, re.DOTALL)
    assert desc_match is not None, "Missing 'description' field"
    assert len(desc_match.group(1).strip()) > 20, "Description too short (< 20 chars)"
    return True
```

## 4. Error Handling & Boundary Conditions
- **Missing File**: Raises explicit assertion error naming the missing path.
- **Short Description**: Rejects descriptions with $\le 20$ characters to guarantee semantic discovery.
- **Malformed Delimiters**: Rejects files lacking leading or closing `---`.

## 5. Safety Invariants & Risk Control Implementation (RCM-FW-006, RCM-FW-015)
- **Safety Invariant 1 (RCM-FW-006 - Context & Frontmatter Integrity)**: Skill definitions must strictly parse with valid YAML frontmatter matching directory name. Unparseable, oversized, or missing skills are immediately rejected, preventing agent context buffer overrun and procedural drift.
- **Safety Invariant 2 (RCM-FW-015 - Extension & Intercept Fail-Closed)**: Any pre-tool-call or hook execution failure must fail closed, raising an immediate synchronous abort rather than permitting untrusted or unvalidated execution.
