---
name: stack-react-typescript
description: Stack-specific code review and implementation guardrails for React + TypeScript projects, aligned with docs/stack-rules and the general review checklists.
---

# React + TypeScript Stack

Use this skill when reviewing or writing React + TypeScript code (components, hooks, data fetching, routing, state management).

## When to Use
- Reviewing React components, hooks, or context/state management
- Checking TypeScript strictness, prop typing, and API contracts
- Validating UI correctness, accessibility, and performance
- Hardening data fetching, error boundaries, and testing strategy

## Review Workflow
1. Map the scope: component/service, state source (context/store/query), routing, and data dependencies.
2. Apply the general checklists in `docs/review/` (code-conventions, readability, reliability, security, performance, testing).
3. Enforce stack rules from `docs/stack-rules/react-typescript-rules.md` with focus on TypeScript strictness, hooks hygiene, state/data flows, and a11y/performance.
4. Validate test coverage for critical paths (rendering, hooks, async flows) and align fixtures with typed contracts.
5. Report findings with severity, location, impact, and reference to the relevant rule/checklist section.

## Stack Guardrails
- **TypeScript strict**: Avoid `any`, type props/state, prefer inference for locals, explicit return types for public APIs; see `docs/stack-rules/react-typescript-rules.md#typescript-strict`.
- **Components & hooks**: Keep components pure, memoize derived values, stable deps for hooks, split concerns into smaller components/custom hooks.
- **State and data**: Single source of truth, typed server/client boundaries, consistent loading/error states, avoid stale closures in async callbacks.
- **Rendering & a11y**: Stable keys, semantic HTML, ARIA for inputs/lists, keyboard support, meaningful empty/loading UI.
- **Performance**: `React.memo`/`useMemo`/`useCallback` where needed, avoid inline object/array props in hot paths, debounce/throttle expensive handlers.
- **Testing**: React Testing Library for behavior, mock HTTP at boundary, cover hooks edge cases, snapshot only for stable UI.

## Issue Report Pattern
- **Severity | Area**: Finding title
- **Evidence**: file:line with short snippet/description
- **Impact**: User/system risk
- **Fix**: Direct action linked to rule (e.g., `docs/stack-rules/react-typescript-rules.md#typescript-strict`)

## References
- Stack rules: `docs/stack-rules/react-typescript-rules.md`
- Cheat sheet: `docs/stack-rules/concise/react-typescript-concise.md`
- Examples: `docs/stack-rules/examples-only/react-typescript-examples.md`
- General reviews: `docs/review/`
