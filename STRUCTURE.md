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
    ├── code-analysis/       # Core code review skill (+ EXAMPLES)
    ├── documentation/
    ├── testing/
    ├── architecture/
    ├── refactoring/
    ├── devsecops/
    ├── ux-ui-design/
    ├── README writer/
    ├── product-owner/
    ├── engineering-manager/
    ├── human-resources/
    ├── marketing/
    └── communications/
```

## Key Skills (Core)
- `code-analysis`: Code quality reviews, smells, metrics
- `documentation`: Technical docs (README, API docs, ADRs)
- `testing`: Unit/integration/E2E strategies and examples
- `architecture`: System design, patterns, scalability
- `refactoring`: Modernization, technical debt reduction
- `devsecops`: Security automation, scanning, and pipeline hardening
- `ux-ui-design`: Research, flows, wireframes, and accessibility
- `README writer`: Quick, high-quality READMEs

## Non-Technical Skills
- Product Owner, Engineering Manager, Human Resources, Marketing, Communications

## How to Package and Use
- Package all skills: `./package-skills.sh`
- Package one skill: `./package-skills.sh devsecops`
- Copy to Claude Code: `cp -r skills/<skill-name> ~/.claude/skills/`
- Upload to Claude.ai: use ZIPs from `packaged-skills/`
