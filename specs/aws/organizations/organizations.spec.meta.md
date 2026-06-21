---
id: "@specs/aws/organizations"
version: 1.0.0
target_lang: meta
owned-by: codegen
status: active
---

# AWS Organizations — Meta Spec (WHY)

## Why Organizations Exists

AWS Organizations provides centralized governance and management of multiple AWS accounts within an organization. It allows administrators to:

- Create and manage groups of AWS accounts
- Apply service control policies (SCPs) across accounts
- Simplify billing with consolidated payment
- Delegate administration of AWS services
- Manage account creation and hierarchical structures

## Architecture

The service has four core entities:

1. **Organization** — Top-level container. One per management account. Supports ALL features or CONSOLIDATED_BILLING mode.
2. **Account** — Member accounts. Created, invited, suspended, or closed within the org.
3. **Organizational Unit (OU)** — Nested container for accounts and child OUs. Forms a tree with roots at top.
4. **Policy** — Service Control Policies (SCP), Tag Policies, Backup Policies, and AI Opt-Out Policies. Attached to roots, OUs, or accounts.

## Design Philosophy

- **Tree structure** — OUs form a hierarchy rooted at the organization root. Accounts are leaves.
- **Policy inheritance** — Policies attached at higher levels apply to all descendants.
- **Eventual consistency** — Many operations are asynchronous in real AWS, but the emulator is synchronous.

## Implementation Notes

- TotalStack emulator (v4.14.0 fork): 25 core CRUD handlers + models + integration tests
- Greenfield service — no existing LocalStack provider
- Store: dict-backed, in-memory
- 43 integration tests, 5 E2E tests (skipped until provider wired)
