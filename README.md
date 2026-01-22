# AI Agent Skills Collection

A collection of professional Agent Skills following Anthropic's best practices to extend Claude's capabilities with specialized expertise.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-14-blue.svg)]()
[![Documentation](https://img.shields.io/badge/Docs-Complete-green.svg)]()

## 🚀 Quick Start

### GitHub Copilot in VS Code (Recommended)

```bash
# 1. Copy skills to your project
mkdir -p .github/skills
cp -r skills/* .github/skills/

# 2. Enable Agent Skills in VS Code
# Settings → chat.useAgentSkills → ✅

# 3. Done! Copilot will use them automatically
```

### Claude API/Code

```bash
# 1. Package the skills you need
./package-skills.sh code-analysis

# 2. Import into Claude according to your platform
# See USAGE_GUIDE.md for complete details
```

📖 **[See Complete Usage Guide →](USAGE_GUIDE.md)**

## 🎯 What are Agent Skills?

**Agent Skills** are modular file system-based resources that provide AI agents (GitHub Copilot, Claude, etc.) with domain-specific expertise: workflows, context, and best practices that transform general-purpose agents into specialists.

**Agent Skills is an open standard** ([agentskills.io](https://agentskills.io/)) natively supported by:
- ✅ GitHub Copilot in VS Code
- ✅ GitHub Copilot CLI
- ✅ GitHub Copilot coding agent
- ✅ Claude API, Claude Code, Claude.ai

## 📋 Available Skills

### 🔧 Technical Skills

#### 1. **Code Analysis** (`code-analysis`)
Analyze and review code with software engineering best practices.
- Code quality analysis for React, Angular, Python, Java, Kotlin
- Stack-specific code smell detection
- Improvement recommendations with concrete examples
- Complexity and maintainability metrics

#### 2. **Documentation** (`documentation`)
Generate and maintain professional technical documentation.
- API documentation (REST, GraphQL, gRPC)
- README files and contribution guides
- System architecture (diagrams, ADRs)
- User guides and onboarding

#### 3. **Testing** (`testing`)
Create and execute comprehensive testing strategies.
- Unit tests (Jest, pytest, JUnit, Kotlin Test)
- Integration tests and E2E
- React Testing Library for components
- Test-driven development (TDD)
- Coverage analysis and improvement

#### 4. **Quality Assurance** (`quality-assurance`)
Plan and execute functional/non-functional testing with strong gates.
- Test strategy, plans, and risk-based coverage
- Functional, regression, and non-functional (perf, security, accessibility)
- Quality gates in CI/CD, flake management, and reporting
- Defect triage, exit criteria, and release readiness

#### 5. **Architecture** (`architecture`)
Design and evaluate software architectures.
- Design patterns (SOLID, DDD, Clean Architecture)
- System architectures (microservices, event-driven)
- Technical diagrams (C4 model, UML)
- Trade-off analysis and architectural decisions

#### 6. **Refactoring** (`refactoring`)
Improve existing code while maintaining its functionality.
- Code modernization for React hooks, Kotlin coroutines
- Pattern implementation (Repository, Factory, Strategy)
- Performance optimization
- Technical debt reduction

#### 7. **DevSecOps** (`devsecops`)
Security automation across code, pipelines, and infrastructure.
- Secure CI/CD (SAST/DAST/SCA), secrets management, SBOMs
- Container/Kubernetes hardening and runtime monitoring
- IaC scanning and cloud posture checks
- Compliance automation and evidence collection

#### 8. **UX/UI Design** (`ux-ui-design`)
Design user-centered, accessible experiences.
- User research, personas, and journey maps
- Information architecture, flows, and wireframes
- Visual systems, prototypes, and interaction patterns
- Accessibility and usability testing

#### 9. **README Writer** (`README writer`)
Produce high-quality README files quickly.
- Installation, usage, and troubleshooting sections
- Feature highlights and configuration matrices
- Examples/snippets tailored to the project
- Contribution, license, and support guidance

### 💼 Non-Technical Skills

#### 10. **Product Owner** (`product-owner`)
Product management, backlog, and stakeholders.
- User stories and acceptance criteria
- Backlog prioritization (MoSCoW, RICE)
- Sprint planning and roadmaps
- Stakeholder communication

#### 11. **Engineering Manager** (`engineering-manager`)
Technical leadership and team management.
- 1-on-1s and career development
- Performance reviews
- Hiring and onboarding
- Team culture building

#### 12. **Human Resources** (`human-resources`)
Talent management and HR operations.
- Recruiting and candidate evaluation
- Employee engagement programs
- HR policies and compliance
- Onboarding (30-60-90 day plans)

#### 13. **Marketing** (`marketing`)
Campaigns, content, and marketing strategy.
- Content marketing (blog posts, case studies)
- SEO strategy and keyword research
- Social media campaigns
- Analytics and performance tracking

#### 14. **Communications** (`communications`)
Internal, external, and crisis communication.
- Internal comms (all-hands, newsletters)
- Press releases and media relations
- Crisis communication plans
- Executive communications

## 🚀 How to Use

### In GitHub Copilot (VS Code)

```bash
# 1. Copy skills to your project (shared with the team)
mkdir -p .github/skills
cp -r skills/code-analysis .github/skills/
cp -r skills/testing .github/skills/

# 2. Enable in VS Code: Settings → chat.useAgentSkills → ✅

# 3. Use Copilot Chat normally - skills activate automatically
```

📖 **[See Complete GitHub Copilot Guide →](USAGE_GUIDE.md)**

### In Claude API

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

# Upload the skill
with open("code-analysis.zip", "rb") as f:
    skill = client.skills.create(
        file=f,
        name="code-analysis"
    )

# Use in a conversation
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    tools=[{"type": "code_execution_2025_08_25"}],
    container={
        "type": "code_execution_container",
        "skill_ids": [skill.id]
    },
    messages=[{
        "role": "user",
        "content": "Analyze the code in main.py"
    }],
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
        "files-api-2025-04-14"
    ]
)
```

### In Claude Code

1. Copy the skill directory to your project:
```bash
cp -r skills/code-analysis .claude/skills/
```

2. Claude will discover and use the skill automatically

### In Claude.ai

1. Compress the skill directory into a ZIP file
2. Go to Settings > Features
3. Upload the ZIP file

## 📁 Skill Structure

```
skill-name/
├── SKILL.md              # Main instructions (required)
├── EXAMPLES.md           # Usage examples (optional)
├── EXAMPLES_STACK.md     # Stack-specific examples (optional)
└── scripts/              # Auxiliary scripts (optional)
    └── analyze.py
```

### Loading Levels

1. **Metadata (always loaded)**: YAML frontmatter with name and description
2. **Instructions (when activated)**: Main content of SKILL.md
3. **Resources (on demand)**: Additional referenced files

## 🛠️ Development

### Creating a New Skill

1. Create a directory with the skill name (lowercase, hyphens)
2. Create `SKILL.md` with frontmatter:
```markdown
---
name: my-skill
description: Clear description of what it does and when to use it
---

# My Skill

## Quick Start
[Basic instructions]

## Workflows
[Step-by-step procedures]

## Examples
[Concrete examples]
```

3. Add additional resources as needed

### Best Practices

- **Clear description**: Include what it does AND when to use it
- **Specific instructions**: Step-by-step, unambiguous
- **Concrete examples**: Real use cases
- **Scripts for deterministic operations**: Reduces token consumption
- **Progressive disclosure**: Only load what's necessary

## 📊 Benefits

✅ **Specialization**: Adapt capabilities for specific tasks
✅ **No repetition**: Create once, use automatically
✅ **Composition**: Combine Skills for complex workflows
✅ **Context efficiency**: Load on demand
✅ **Reusable code**: Executable scripts without consuming tokens

## 🔒 Security

⚠️ **Use only Skills from trusted sources**:
- Your own Skills
- Official Anthropic Skills
- Fully audit third-party skills

Skills can execute code and access files. Treat them like installing software.

## 📚 Documentation

### 📖 Project Guides
- **[🚀 Quick Start](QUICKSTART.md)** - Get started in 5 minutes!
- **[📘 Usage Guide](USAGE_GUIDE.md)** - Detailed usage for each platform
- **[📋 Structure](STRUCTURE.md)** - Project organization
- **[🤝 Contributing](CONTRIBUTING.md)** - How to contribute new skills

### 🔗 Official References
- [Official Agent Skills Documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)
- [Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)

## 📄 License

MIT License - See LICENSE file for details

---

**Note**: This collection follows Anthropic's official specifications for Agent Skills and is compatible with Claude API, Claude Code, and Claude.ai.
