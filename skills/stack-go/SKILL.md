---
name: stack-go
description: Go stack skill for reviewing services, CLIs, and libraries using stack rules and general review checklists.
---

# Go Stack

Use this skill for Go services, CLIs, and libraries (concurrency, HTTP, persistence).

## When to Use
- Reviewing Go packages, handlers, and goroutine-based workflows
- Checking error handling, context propagation, and concurrency safety
- Validating interface design, struct layout, and API contracts
- Ensuring tests cover success/error paths and race conditions

## Review Workflow
1. Understand scope: package role, concurrency model, context boundaries, IO dependencies.
2. Apply general checklists in `docs/review/` (conventions, readability, reliability, security, performance, testing).
3. Enforce stack rules from `docs/stack-rules/go-rules.md` focusing on error handling, context usage, goroutines/channels, interfaces, and DB/HTTP patterns.
4. Check resource handling (timeouts, cancellations, defers), logging, and configuration (env vars, flags).
5. Validate tests (table tests, fakes/mocks) and race-safety; report findings with severity, evidence, and rule reference.

## Stack Guardrails
- **Error handling**: Always handle errors, wrap with context `%w`, no panics in library code; see `docs/stack-rules/go-rules.md#error-handling`.
- **Context propagation**: Accept/pass `context.Context`, honor deadlines/cancellation, avoid storing contexts in structs.
- **Concurrency**: Avoid shared mutable state without sync primitives, prefer channels or immutability, clean up goroutines, use WaitGroup responsibly.
- **Interfaces & structs**: Small interfaces for behavior, zero-value safe structs, avoid stuttering names, capitalize exported APIs with docs.
- **I/O & DB**: Parameterized queries, close resources with `defer`, handle `rows.Err()`, manage connection pools and timeouts.
- **Testing**: Table-driven tests, check error cases, use `t.Helper()`, race detector for concurrency-prone code.

## Issue Report Pattern
- **Severity | Area**: Finding title
- **Evidence**: file:line + brief snippet
- **Impact**: Behavior/performance/reliability risk
- **Fix**: Action + reference (e.g., `docs/stack-rules/go-rules.md#error-handling`)

## References
- Stack rules: `docs/stack-rules/go-rules.md`
- Cheat sheet: `docs/stack-rules/concise/go-concise.md`
- Examples: `docs/stack-rules/examples-only/go-examples.md`
- General reviews: `docs/review/`
