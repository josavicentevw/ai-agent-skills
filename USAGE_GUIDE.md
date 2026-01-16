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

### Code & Stack
- **React review**: “Analyze `UserCard.tsx`, flag accessibility, performance, and typing issues using the React/TS stack rules.” → Skills: `code-analysis`, `stack-react-typescript`
- **Angular service**: “Review `user.service.ts` for RxJS patterns, DI scope, and error handling.” → Skills: `code-analysis`, `stack-angular`
- **Python service refactor**: “Refactor `billing.py` to lower complexity and add type hints; call out ORM pitfalls.” → Skills: `refactoring`, `stack-python`
- **Go reliability**: “Audit `worker.go` for error handling and context propagation.” → Skills: `code-analysis`, `stack-go`

### Testing & Quality
- **API tests**: “Write unit and integration tests for `UserService` (happy paths + error cases).” → Skills: `testing`
- **Frontend tests**: “Create RTL tests for `LoginForm` covering validation, submit flow, and loading state.” → Skills: `testing`, `stack-react-typescript`
- **Performance sweep**: “Identify hotspots in `order-controller.ts` and propose low-risk optimizations.” → Skills: `code-analysis`, `stack-angular`

### Documentation & Architecture
- **README**: “Create a README with install, usage, env vars, and troubleshooting for this API.” → Skills: `documentation`
- **ADR**: “Draft an ADR comparing SQS vs Kafka for async processing with pros/cons.” → Skills: `architecture`, `documentation`
- **System design**: “Propose an event-driven architecture for order processing with scaling considerations.” → Skills: `architecture`

### Non-Technical (emphasis)
- **Product Owner**: “Write user stories with acceptance criteria for a ‘Saved Carts’ feature; include edge cases and analytics events.” → Skills: `product-owner`
- **Engineering Manager**: “Draft a 6-week plan with milestones and risks to stabilize the checkout service.” → Skills: `engineering-manager`
- **Communications**: “Write an incident postmortem summary email for a 45-minute outage (audience: execs + engineering).” → Skills: `communications`
- **Human Resources**: “Create a 30-60-90 onboarding plan for a senior backend engineer (Java).” → Skills: `human-resources`, `stack-java`
- **Marketing**: “Draft a product launch brief for the new analytics dashboard with key messages and channels.” → Skills: `marketing`

### Combined Skill Patterns
- **Focused review**: “Use the `code-analysis` and `stack-kotlin` skills to review `InvoiceService.kt`, prioritizing null-safety and coroutine correctness.”
- **Docs + PO**: “Summarize the v2 API changes for stakeholders and add acceptance criteria for rollout.” → Skills: `documentation`, `product-owner`
- **Tests + Stack**: “Generate Jest + RTL tests for `CartSummary.tsx` covering discounts and edge cases; follow React/TS rules.” → Skills: `testing`, `stack-react-typescript`
- **Architecture + Comms**: “Propose a migration plan to event-driven invoicing and draft a stakeholder update.” → Skills: `architecture`, `communications`

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
