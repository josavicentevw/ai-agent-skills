# 🚀 Quick Start - AI Agent Skills

Get up and running with Agent Skills in minutes.

## ⚡ Fast Install

### Option 1: Claude Code (easiest)

```bash
# Copy a skill to your local Claude skills directory
cp -r skills/code-analysis ~/.claude/skills/
```

Use Claude Code normally; it will load the skills automatically.

### Option 2: Claude.ai (web)

1. Package the skill you need:
   ```bash
   ./package-skills.sh code-analysis
   ```
2. Open [Claude.ai](https://claude.ai) → Settings → Features → Upload Skill.
3. Upload `packaged-skills/code-analysis.zip` (or any packaged skill) and start chatting.

### Option 3: Claude API (programmatic)

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

# 1) Upload the skill
with open("packaged-skills/code-analysis.zip", "rb") as f:
    skill = client.skills.create(file=f, name="code-analysis")

# 2) Use it in a conversation
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    container={"type": "code_execution_container", "skill_ids": [skill.id]},
    messages=[{"role": "user", "content": "Review this React component for performance issues"}]
)
print(response.content[0].text)
```

---

## 🎯 Available Skills

| Skill | Use it for |
|-------|------------|
| `code-analysis` | Code reviews, code smells, metrics |
| `documentation` | READMEs, API docs, architecture docs |
| `testing` | Unit/integration/E2E tests, TDD |
| `architecture` | System design, patterns, scalability |
| `refactoring` | Modernization, technical debt, patterns |
| `devsecops` | Secure pipelines, SAST/DAST/SCA, container/IaC checks |
| `ux-ui-design` | Research, flows, wireframes, visual systems, accessibility |
| `README writer` | Fast, high-quality README creation |
| `product-owner` | User stories, backlog, prioritization |
| `engineering-manager` | 1:1s, performance reviews, hiring |
| `human-resources` | Recruiting, onboarding, engagement |
| `marketing` | Campaigns, content, SEO |
| `communications` | Internal/external comms, crisis comms |

---

## 💡 Quick Examples

### Analyze code
```bash
User: "Analyze main.py and list code smells"
Claude (with code-analysis): returns findings + fixes
```

### Generate docs
```bash
User: "Create a README for this API with install, usage, and examples"
Claude (with documentation): returns a structured README
```

### Create tests
```bash
User: "Write unit and integration tests for UserService"
Claude (with testing): returns pytest/JUnit/Jest examples with edge cases
```

---

## 🔧 Handy Commands

```bash
# Package all skills
./package-skills.sh

# Package a specific skill
./package-skills.sh devsecops

# Inspect structure
cat STRUCTURE.md
```

---

## 📚 Learn More

- **Full Usage Guide:** `USAGE_GUIDE.md`
- **Project Structure:** `STRUCTURE.md`
- **Contributing:** `CONTRIBUTING.md`
- **Examples:** `examples/`
- **Official Docs:** [Anthropic Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
