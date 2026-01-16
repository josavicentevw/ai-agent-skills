---
name: stack-kotlin
description: Kotlin stack skill for code reviews and implementation guidance (Spring/Ktor/Coroutines) using stack rules and general review checklists.
---

# Kotlin Stack

Use this skill for Kotlin services, Spring Boot/Ktor apps, and coroutine-based libraries.

## When to Use
- Reviewing coroutine-based services, controllers, repositories, and flows
- Checking null safety, data classes/sealed hierarchies, and API contracts
- Validating exception handling, logging, and dependency injection
- Ensuring tests cover suspend functions, flows, and edge cases

## Review Workflow
1. Map context: framework, sync vs suspend, data sources, and concurrency model (flows/channels).
2. Apply general checklists in `docs/review/` (conventions, readability, reliability, security, performance, testing).
3. Enforce stack rules from `docs/stack-rules/java-kotlin-rules.md` focusing on null safety, coroutines/Flow, DI, collections, and logging/error handling.
4. Check immutability (data classes, val), sealed hierarchies for domain states, and safe operator usage (`?.`, `?:`, no unchecked `!!`).
5. Validate tests (JUnit/Kotest/MockK) for suspend functions, flows, and repository behaviors; report issues with severity, evidence, and rule reference.

## Stack Guardrails
- **Null safety**: Prefer nullable types + safe calls, avoid `!!`, use `let/run/apply/also`; see `docs/stack-rules/java-kotlin-rules.md#null-safety`.
- **Coroutines & Flow**: Propagate cancellation, use structured concurrency, specify dispatchers, avoid blocking calls, collect with lifecycle awareness.
- **Data modeling**: Data classes for values, sealed classes for states/errors, extension functions for readability not side effects.
- **Dependency injection**: Constructor injection, immutable dependencies, avoid global singletons for mutable state.
- **Error handling & logging**: Domain-specific exceptions/results, wrap errors with context, structured logging, avoid silent failures.
- **Testing**: `runTest`/`TestScope` for coroutines, turbine/marbles for Flow, MockK for collaborators, verify dispatcher usage.

## Issue Report Pattern
- **Severity | Area**: Finding title
- **Evidence**: file:line + short snippet
- **Impact**: Behavior/performance/security risk
- **Fix**: Action + reference (e.g., `docs/stack-rules/java-kotlin-rules.md#null-safety`)

## References
- Stack rules: `docs/stack-rules/java-kotlin-rules.md`
- Cheat sheet: `docs/stack-rules/concise/java-kotlin-concise.md`
- Examples: `docs/stack-rules/examples-only/java-kotlin-examples.md`
- General reviews: `docs/review/`
