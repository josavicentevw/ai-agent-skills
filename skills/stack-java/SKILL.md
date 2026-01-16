---
name: stack-java
description: Java (Spring) stack skill for code reviews and implementation guidance using stack rules plus general review checklists.
---

# Java Stack

Use this skill for Java services, Spring Boot apps, libraries, and integrations.

## When to Use
- Reviewing Spring controllers/services/repositories or library code
- Checking null safety, immutability, and API contracts
- Validating JPA/transaction patterns, exception handling, and logging
- Ensuring test coverage (JUnit/Mockito) and performance considerations

## Review Workflow
1. Identify context: web/API layer, service boundaries, data sources, threading model.
2. Run general checklists in `docs/review/` (conventions, readability, reliability, security, performance, testing).
3. Apply stack rules from `docs/stack-rules/java-rules.md` covering null-safety/Optional, streams, DI, JPA/Hibernate, logging, and immutability.
4. Validate API contracts (DTOs vs entities), transaction scopes, error handling, and configuration (profiles, env vars).
5. Confirm tests for service/repo layers and boundary behaviors; report findings with severity, evidence, impact, and rule reference.

## Stack Guardrails
- **Null safety**: Use `Optional` for nullable returns, never return `null` Optional, leverage nullability annotations; see `docs/stack-rules/java-rules.md#null-safety`.
- **Dependency injection**: Prefer constructor injection, avoid field injection/statics, keep beans scoped appropriately, no hidden side effects.
- **Data & transactions**: DTOs for I/O, entities not leaked, transactional boundaries at service layer, lazy loading managed (fetch joins, batch).
- **Error handling & logging**: Custom exceptions per domain, global handlers, structured logging with context, avoid swallowing exceptions.
- **Streams & collections**: Use streams judiciously, avoid side effects, prefer immutability for inputs/outputs.
- **Testing**: JUnit 5 + Mockito, slice tests for controllers/repos, test transaction behaviors and error paths.

## Issue Report Pattern
- **Severity | Area**: Finding title
- **Evidence**: file:line + brief snippet
- **Impact**: Reliability/performance/security risk
- **Fix**: Action + reference (e.g., `docs/stack-rules/java-rules.md#null-safety`)

## References
- Stack rules: `docs/stack-rules/java-rules.md`
- Cheat sheet: `docs/stack-rules/concise/java-concise.md`
- Examples: `docs/stack-rules/examples-only/java-examples.md`
- General reviews: `docs/review/`
