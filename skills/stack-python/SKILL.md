---
name: stack-python
description: Python stack skill for reviewing services, APIs, and libraries with rules from docs/stack-rules and the general review checklists.
---

# Python Stack

Use this skill for FastAPI/Django services, libraries, scripts, and data pipelines.

## When to Use
- Reviewing API handlers, services, background tasks, or data pipelines
- Checking typing, validation, error handling, and logging
- Assessing async/await usage, ORM patterns, and performance
- Verifying testing strategy with pytest/unit frameworks

## Review Workflow
1. Capture context: framework (FastAPI/Django/CLI), sync vs async, database/IO boundaries.
2. Apply general checklists in `docs/review/` (conventions, readability, reliability, security, performance, testing).
3. Enforce stack rules from `docs/stack-rules/python-rules.md` focusing on typing, validation, error handling, async, and persistence.
4. Review configuration and security (settings separation, secrets management, logging, dependency versions).
5. Ensure pytest/coverage for critical paths and data validation; report issues with severity, location, impact, and rule reference.

## Stack Guardrails
- **Typing**: Function/class annotations, avoid `Any`, use `Optional` and generics, type-check in CI; see `docs/stack-rules/python-rules.md#type-hints`.
- **Validation & data models**: Pydantic/dataclasses for external data, strict field validation, explicit schemas for API I/O.
- **Error handling & logging**: Domain exceptions, structured logging, never swallow exceptions, return meaningful HTTP errors.
- **Async & IO**: Use async where IO-bound, avoid blocking calls in async paths, leverage connection pooling, timeouts, and context managers.
- **ORM/DB**: Prevent N+1 queries, transactions for multi-step writes, migrations/versioning, parameterized queries only.
- **Testing**: pytest fixtures/factories, fast unit tests for pure logic, integration tests for DB/external calls, coverage on edge cases.

## Issue Report Pattern
- **Severity | Area**: Finding title
- **Evidence**: file:line + short snippet
- **Impact**: Behavior/performance/security risk
- **Fix**: Action + reference (e.g., `docs/stack-rules/python-rules.md#type-hints`)

## References
- Stack rules: `docs/stack-rules/python-rules.md`
- Cheat sheet: `docs/stack-rules/concise/python-concise.md`
- Examples: `docs/stack-rules/examples-only/python-examples.md`
- General reviews: `docs/review/`
