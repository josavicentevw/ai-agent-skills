---
name: stack-scala
description: Scala stack skill for reviewing services and libraries with stack rules plus general review checklists.
---

# Scala Stack

Use this skill for Scala services, functional codebases, and library reviews.

## When to Use
- Reviewing services using Future/IO/ZIO/Cats Effect or Akka/Play
- Checking type safety, Option/Either usage, and collection patterns
- Validating error handling, immutability, and concurrency semantics
- Ensuring test coverage for async/streaming code

## Review Workflow
1. Map runtime/context: effect system (Future/IO), streaming libs, typelevel vs standard collections.
2. Apply general checklists in `docs/review/` (conventions, readability, reliability, security, performance, testing).
3. Enforce stack rules from `docs/stack-rules/scala-rules.md` focusing on Option/Either/Try, collections, implicits/givens, for-comprehensions, and concurrency.
4. Check immutability, pattern matching exhaustiveness, and safe resource handling (bracket/using).
5. Confirm tests for success/failure branches, async timing, and lawfulness where applicable; report findings with severity, evidence, and rule reference.

## Stack Guardrails
- **Null avoidance**: Prefer `Option`/`Either`/`Try`, avoid `null`/`get`, use pattern matching; see `docs/stack-rules/scala-rules.md#option-types`.
- **Collections**: Favor immutable collections, avoid unsafe head/tail, leverage `map/flatMap` over manual loops.
- **Control flow**: for-comprehensions for sequencing, guard against partial functions, exhaustive pattern matches with sealed traits.
- **Concurrency & effects**: Correct execution contexts, avoid blocking in async paths, manage resource lifecycles, handle failures explicitly.
- **Type safety**: Precise types for domain models, avoid implicit conversions unless necessary, prefer givens/typeclasses for extension.
- **Testing**: Property tests where useful, async test support for Futures/IO, fixtures for streaming pipelines.

## Issue Report Pattern
- **Severity | Area**: Finding title
- **Evidence**: file:line + short snippet
- **Impact**: Behavior/performance/reliability risk
- **Fix**: Action + reference (e.g., `docs/stack-rules/scala-rules.md#option-types`)

## References
- Stack rules: `docs/stack-rules/scala-rules.md`
- Cheat sheet: `docs/stack-rules/concise/scala-concise.md`
- Examples: `docs/stack-rules/examples-only/scala-examples.md`
- General reviews: `docs/review/`
