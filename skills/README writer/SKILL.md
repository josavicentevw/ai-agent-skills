# AI README Authoring Guide

Use this guide when prompting an AI to draft or refresh a README that follows the SOLO README schema. The goal is a concise, operations-ready document that orients newcomers and on-call engineers without needing tribal knowledge.

## Schema to Follow (in order)
- **Title & Quick Descriptor**: Service name plus a one-line value statement; badges only if already available.
- **TL;DR / Overview**: 3–5 sentences on what the service does, who consumes it, and the core business flow it supports.
- **Key Responsibilities & Use Cases**: Bullet the primary jobs-to-be-done and critical paths; call out constraints or SLAs.
- **Interfaces**: REST/gRPC topics, async queues, cron jobs. Link Swagger/OpenAPI, protobuf specs, and message contracts.
- **Architecture**: High-level system/context view and deployment topology only (Mermaid if available); keep arrows simple and directional; avoid per-endpoint or per-notification flow diagrams.
- **Data Model**: Main aggregates/entities, key fields, and storage tech in prose or a small table; link schemas/migrations; skip ER diagrams unless explicitly requested.
- **Configuration & Secrets**: Required env vars, config sources, feature flags, secrets management location (no secrets inline).
- **Local Development**: Prereqs, how to start dependencies, how to run the app, common bootstrap commands, sample data.
- **Testing**: How to run tests (unit/integration/e2e), coverage commands, and notable fixtures or contracts.
- **Security & Compliance**: AuthN/Z expectations, required roles/scopes, data handling/PII notes, threat surfaces.
- **Observability**: Health/metrics/traces/logging endpoints, dashboards, alerts, and log conventions.
- **Operations & Deployments**: CI/CD entry points, release cadence, runtime profiles, rollback/recovery notes, runbooks.
- **Troubleshooting**: Frequent failure modes with quick checks.
- **References & Ownership**: Links to ADRs, RFCs, upstream docs, and the owning team/contact channel.

## Content Rules
- Write for engineers onboarding or on-call; keep paragraphs short and use bullets when possible.
- Prefer links to canonical sources over duplicating details; keep commands copy-pastable.
- Use tables for env vars/config when the list is long; avoid placeholder secrets.
- Call out what is _required_ vs. _optional_; include defaults where safe.
- Keep diagrams minimal: system/context and deployment only; avoid component-level or sequence/notification flows unless the user explicitly asks for them; ensure arrows read left-to-right or top-down to reduce ambiguity.

## Ask the User Before Drafting
Collect these inputs (links preferred) so the AI can populate the schema accurately:
- Current service name, one-line elevator pitch, and primary business flow it supports.
- API surface: Swagger/OpenAPI URL, gRPC/proto repo paths, and any message/queue contracts.
- Architecture references: existing system/context or deployment diagrams (Mermaid/PlantUML/images) and a short component rundown; confirm if additional diagrams are desired.
- Data and storage: main entities, schemas/migrations, and where canonical definitions live.
- Configuration: required env vars with defaults, feature flags, and where secrets are stored/loaded.
- Local dev: prerequisites, how to start dependencies (Docker Compose, mocks), and seed data locations.
- Testing: commands for unit/integration/e2e, notable fixtures, and coverage expectations.
- Security: required roles/scopes/permissions, auth mechanisms, and PII/data handling constraints.
- Observability: health endpoints, metrics/traces/logging conventions, dashboard/alert links.
- Operations: deployment pipeline entry points, runtime profiles, rollback steps, runbooks, and SLO/SLA targets.
- Ownership and support: responsible team, contact channel, and where to file incidents or tickets.

## Prompt Template (suggested)
```
You are documenting the README for <service>. Follow the SOLO README schema below and keep it concise and actionable.
- Title & Quick Descriptor
- TL;DR / Overview
- Key Responsibilities & Use Cases
- Interfaces (REST/gRPC/queues/cron) with links
- Architecture (system/context + deployment only; keep arrows simple; no per-endpoint flows)
- Data Model (entities + storage)
- Configuration & Secrets
- Local Development
- Testing
- Security & Compliance
- Observability
- Operations & Deployments
- Troubleshooting
- References & Ownership

Use the provided links and details:
<paste user-provided answers/links here>
```
