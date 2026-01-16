# AI Agent Skills - Usage Guide

This guide shows how to install, package, and use the skills across GitHub Copilot, Claude Code, Claude API, and Claude.ai.

## Contents
- [Quick Start](#quick-start)
- [GitHub Copilot (VS Code)](#github-copilot-vs-code)
- [Claude Code](#claude-code)
- [Claude API](#claude-api)
- [Claude.ai](#claudeai)
- [Packaging Skills](#packaging-skills)
- [Choosing the Right Skill](#choosing-the-right-skill)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)

## Quick Start

```bash
# Copy skills locally (Copilot or Claude Code)
mkdir -p .github/skills
cp -r skills/code-analysis .github/skills/
cp -r skills/stack-react-typescript .github/skills/   # stack guardrail (optional)

# Package for Claude.ai / Claude API
./package-skills.sh code-analysis
```

See `QUICKSTART.md` for a 5-minute walkthrough.

## GitHub Copilot (VS Code)
- Copy skills into `.github/skills` in your repo or workspace.
- Enable: Settings → `chat.useAgentSkills` → ✅.
- Copilot Chat will auto-load relevant skills based on the prompt.
- Suggested set for engineers: `code-analysis`, `testing`, `documentation`, plus stack guardrails (e.g., `stack-react-typescript`).

## Claude Code
- Copy skills into `~/.claude/skills/`:
  ```bash
  cp -r skills/code-analysis ~/.claude/skills/
  cp -r skills/stack-python ~/.claude/skills/
  ```
- Claude Code will discover them automatically.

## Claude API
1) Package the skill (creates ZIPs in `packaged-skills/`):
```bash
./package-skills.sh stack-react-typescript
```
2) Upload and use:
```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")
with open("packaged-skills/stack-react-typescript.zip", "rb") as f:
    skill = client.skills.create(file=f, name="stack-react-typescript")

resp = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    container={"type": "code_execution_container", "skill_ids": [skill.id]},
    messages=[{"role": "user", "content": "Review this React component for a11y and performance"}]
)
print(resp.content[0].text)
```

## Claude.ai
1. Package a skill: `./package-skills.sh code-analysis`  
2. In Claude.ai: Settings → Features → Upload Skill → choose the ZIP.  
3. Start a chat; Claude will load the uploaded skill when relevant.

## Packaging Skills

- Package all skills: `./package-skills.sh`
- Package one: `./package-skills.sh stack-go`
- Output directory: `packaged-skills/`
- ZIPs exclude `*.DS_Store`, `__pycache__`, `.git`.

## Choosing the Right Skill

- **General engineering**: `code-analysis`, `testing`, `documentation`, `architecture`, `refactoring`
- **Stack guardrails**:
  - React + TypeScript: `stack-react-typescript`
  - Angular: `stack-angular`
  - Python: `stack-python`
  - Java: `stack-java`
  - Kotlin: `stack-kotlin`
  - Go: `stack-go`
  - Scala: `stack-scala`
- **Leadership/operations**: `product-owner`, `engineering-manager`, `human-resources`, `marketing`, `communications`

Tip: Combine a general skill with a stack guardrail for precise reviews (e.g., `code-analysis` + `stack-go`).

## Examples

### Code review (React + TS)
- Prompt: “Analyze `UserCard.tsx`, flag key issues, and reference stack rules.”
- Skills: `code-analysis`, `stack-react-typescript`

### Test generation
- Prompt: “Write unit and integration tests for `UserService`.”
- Skills: `testing`

### Documentation
- Prompt: “Create a README with install, usage, and troubleshooting for this API.”
- Skills: `documentation`

### Architecture
- Prompt: “Propose an event-driven architecture for order processing.”
- Skills: `architecture`

### Refactoring
- Prompt: “Refactor this legacy Python module to reduce complexity and add type hints.”
- Skills: `refactoring`, `stack-python`

## Troubleshooting
- **Skill not loading**: Confirm the skill directory/ZIP is present and frontmatter (`name`, `description`) exists in `SKILL.md`.
- **Wrong skill chosen**: Include the skill name in the prompt (“Use the `stack-angular` skill for this review.”).
- **Packaging errors**: Ensure `package-skills.sh` is executable (`chmod +x package-skills.sh`) and run from repo root.
- **Claude API errors**: Verify the ZIP path and that the `skill_ids` array includes the uploaded skill ID.

## References
- `docs/review/` – General checklists (code conventions, readability, reliability, security, performance, testing)
- `docs/stack-rules/` – Stack-specific rules, concise cheat sheets, and examples
- `skills/` – All available skills (core, stack, and non-technical)
- Official Agent Skills docs: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
