---
name: stack-angular
description: Stack-specific guardrails for reviewing and implementing Angular + TypeScript code using the Angular rules and general review checklists.
---

# Angular Stack

Use this skill for Angular components, services, modules, and NgRx/RxJS flows.

## When to Use
- Reviewing Angular components, modules, and change detection strategies
- Validating RxJS usage, async flows, and HTTP/error handling
- Checking forms, validation, and template binding safety
- Ensuring testability and maintainability across modules

## Review Workflow
1. Understand context: module boundaries, DI graph, routing, and state source (services, NgRx, signals).
2. Run general checklists in `docs/review/` (conventions, readability, reliability, security, performance, testing).
3. Apply stack rules from `docs/stack-rules/angular-rules.md` covering strict typing, templates, DI, RxJS, change detection, and performance.
4. Verify template safety (inputs/outputs, async pipe usage, trackBy, a11y) and HTTP concerns (interceptors, errors, retries).
5. Confirm unit/integration tests exist for components, services, and observables; report findings with severity, location, and rule reference.

## Stack Guardrails
- **TypeScript strict**: No `any`, typed inputs/outputs, prefer readonly where possible; see `docs/stack-rules/angular-rules.md#typescript-strict`.
- **Templates & change detection**: Use `OnPush` when viable, `trackBy` on `*ngFor`, async pipe over manual subscribe, avoid heavy logic in templates.
- **Dependency injection**: Providers scoped correctly, avoid service singletons for request data, inject HttpClient/interceptors for cross-cutting concerns.
- **RxJS**: Strong typing on observables, unsubscribe via async pipe/takeUntil, handle errors, avoid nested subscribes; compose with operators.
- **Forms & validation**: Use typed forms, validation at control/group, surface errors in UI, sanitize/escape user input.
- **Testing**: Isolated component tests with TestBed, marbles for observables, verify change detection scenarios and DI configuration.

## Issue Report Pattern
- **Severity | Area**: Finding title
- **Evidence**: file:line + brief snippet
- **Impact**: User/system risk
- **Fix**: Action + reference (e.g., `docs/stack-rules/angular-rules.md#typescript-strict`)

## References
- Stack rules: `docs/stack-rules/angular-rules.md`
- Cheat sheet: `docs/stack-rules/concise/angular-concise.md`
- Examples: `docs/stack-rules/examples-only/angular-examples.md`
- General reviews: `docs/review/`
