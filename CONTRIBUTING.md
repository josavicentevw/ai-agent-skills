# Contributing to AI Agent Skills

Thank you for your interest in contributing! This document provides guidelines for contributing new skills or improving existing ones.

## How to Contribute

### 1. Fork and Clone

```bash
git clone https://github.com/yourusername/ai-agent-skills.git
cd ai-agent-skills
```

### 2. Create a Branch

```bash
git checkout -b feature/your-skill-name
```

### 3. Create or Modify a Skill

Follow the [Skill Structure](#skill-structure) guidelines below.

### 4. Test Your Skill

- Test the skill with Claude Code, API, or Claude.ai
- Verify all examples work as expected
- Check that descriptions are clear and accurate

### 5. Submit a Pull Request

- Provide a clear description of changes
- Reference any related issues
- Include examples of the skill in action

## Skill Structure

Every skill must follow this structure:

```
skill-name/
├── SKILL.md           # Main skill file (REQUIRED)
├── EXAMPLES.md        # Usage examples (recommended)
├── REFERENCE.md       # Detailed reference (optional)
├── scripts/           # Helper scripts (optional)
│   └── helper.py
└── templates/         # Templates and resources (optional)
    └── template.json
```

### SKILL.md Requirements

The `SKILL.md` file must include:

1. **YAML Frontmatter** (required):
```yaml
---
name: skill-name
description: Clear description of what the skill does and when to use it
---
```

2. **Title and Introduction**
3. **Quick Start** section
4. **Core Capabilities** section
5. **Examples** or reference to EXAMPLES.md
6. **Best Practices**
7. **When to Use** section

### Naming Conventions

- **Skill names**: lowercase with hyphens (e.g., `code-analysis`)
- **File names**: UPPERCASE for documentation (e.g., `SKILL.md`, `EXAMPLES.md`)
- **Directories**: lowercase (e.g., `scripts/`, `templates/`)

### Description Guidelines

The description in the frontmatter should:
- Be clear and concise (under 1024 characters)
- Explain **what** the skill does
- Explain **when** to use it
- Use keywords Claude can match against user requests

**Good example:**
```yaml
description: Analyze code quality, detect code smells, identify bugs, and provide improvement recommendations. Use when reviewing code, checking quality, analyzing complexity, or when user mentions code review, refactoring suggestions, or quality assessment.
```

**Bad example:**
```yaml
description: A tool for code.
```

## Content Guidelines

### 1. Be Specific and Actionable

✅ **Good:**
```markdown
Calculate cyclomatic complexity using this formula:
CC = E - N + 2P
where E = edges, N = nodes, P = connected components
```

❌ **Bad:**
```markdown
Calculate complexity somehow.
```

### 2. Include Examples

Every capability should have concrete code examples:

```python
# Example: Detect long methods
def check_method_length(function_node):
    """Flag methods longer than 50 lines."""
    line_count = function_node.end_lineno - function_node.lineno
    if line_count > 50:
        return f"Method too long: {line_count} lines"
```

### 3. Provide Context

Explain **why**, not just **what**:

```markdown
## Why Extract Method?

Long methods are hard to:
- Understand at a glance
- Test in isolation
- Reuse in other contexts
- Debug when issues arise
```

### 4. Use Clear Structure

- Use headers to organize content
- Use lists for steps or options
- Use code blocks with language tags
- Use tables for comparisons

### 5. Cross-Reference Appropriately

```markdown
For detailed examples, see [EXAMPLES.md](EXAMPLES.md).
For helper scripts, see [scripts/analyze.py](scripts/analyze.py).
```

## Code Guidelines

### Python Scripts

```python
"""
Brief description of what the script does.
"""

import standard_library
import third_party
import local_modules

# Use type hints
def function_name(param: str) -> int:
    """
    Clear docstring explaining:
    - What the function does
    - Parameters
    - Return value
    - Exceptions raised
    """
    pass

# Include main guard
if __name__ == "__main__":
    main()
```

### JavaScript/TypeScript

```javascript
/**
 * Brief description
 * 
 * @param {string} param - Description
 * @returns {number} Description
 */
function functionName(param) {
    // Implementation
}
```

## Testing Your Skill

### Local Testing with Claude Code

1. Copy skill to `.claude/skills/`:
```bash
cp -r skills/your-skill ~/.claude/skills/
```

2. Test with Claude Code

### Testing with Claude API

```python
import anthropic

client = anthropic.Anthropic()

# Upload skill
with open("your-skill.zip", "rb") as f:
    skill = client.skills.create(file=f, name="your-skill")

# Test in conversation
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    tools=[{"type": "code_execution_2025_08_25"}],
    container={
        "type": "code_execution_container",
        "skill_ids": [skill.id]
    },
    messages=[{"role": "user", "content": "Test the skill"}],
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
        "files-api-2025-04-14"
    ]
)
```

## Skill Ideas

Looking for ideas? Consider creating skills for:

- **Domain-specific**: Medical coding, legal document analysis, financial modeling
- **Frameworks**: React, Django, Spring Boot best practices
- **DevOps**: CI/CD pipelines, infrastructure as code, monitoring
- **Data Science**: Data cleaning, visualization, ML workflows
- **Security**: Security audits, penetration testing, compliance
- **Content**: Technical writing, API documentation, blogging

## Questions?

- Open an issue for questions
- Check existing skills for examples
- Review [Anthropic's documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

## Code of Conduct

- Be respectful and constructive
- Focus on helping others
- Follow best practices
- Keep skills professional and appropriate

Thank you for contributing! 🎉
