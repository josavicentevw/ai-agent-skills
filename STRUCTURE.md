# AI Agent Skills Project Structure

```
ai-agent-skills/
│
├── README.md                # Project overview and feature list
├── QUICKSTART.md            # Fast setup for all platforms
├── USAGE_GUIDE.md           # Detailed usage guide
├── STRUCTURE.md             # This file (structure + contents)
├── CONTRIBUTING.md          # Contribution guidelines
├── LICENSE                  # MIT License
├── package-skills.sh        # Script to package skills as ZIPs
│
├── docs/
│   ├── review/              # General review checklists (quality, security, testing, etc.)
│   └── stack-rules/         # Stack-specific rules, cheat sheets, and examples
│
├── examples/                # Usage samples
│   └── api_example.py
│
└── skills/                  # All available skills
    ├── code-analysis/       # Core code review skill (+ EXAMPLES, stack examples)
    ├── documentation/
    ├── testing/
    ├── architecture/
    ├── refactoring/
    ├── product-owner/
    ├── engineering-manager/
    ├── human-resources/
    ├── marketing/
    ├── communications/
    ├── stack-react-typescript/  # React + TS guardrails
    ├── stack-angular/           # Angular guardrails
    ├── stack-python/            # Python guardrails
    ├── stack-java/              # Java (Spring) guardrails
    ├── stack-kotlin/            # Kotlin guardrails
    ├── stack-go/                # Go guardrails
    └── stack-scala/             # Scala guardrails
```

## Key Skills (Core)
- `code-analysis`: Code quality reviews, smells, metrics, stack references
- `documentation`: Technical docs (README, API docs, ADRs)
- `testing`: Unit/integration/E2E strategies and examples
- `architecture`: System design, patterns, scalability
- `refactoring`: Modernization, technical debt reduction

## Stack-Specific Guardrails
- React + TypeScript (`stack-react-typescript`)
- Angular (`stack-angular`)
- Python (`stack-python`)
- Java (`stack-java`)
- Kotlin (`stack-kotlin`)
- Go (`stack-go`)
- Scala (`stack-scala`)

## Non-Technical Skills
- Product Owner, Engineering Manager, Human Resources, Marketing, Communications

## How to Package and Use
- Package all skills: `./package-skills.sh`
- Package one skill: `./package-skills.sh stack-react-typescript`
- Copy to Claude Code: `cp -r skills/<skill-name> ~/.claude/skills/`
- Upload to Claude.ai: use ZIPs from `packaged-skills/`
