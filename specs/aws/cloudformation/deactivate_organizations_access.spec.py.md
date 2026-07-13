---
id: "@specs/aws/cloudformation/deactivate_organizations_access"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DeactivateOrganizationsAccess"
---

# DeactivateOrganizationsAccess

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/deactivate_organizations_access
> **spec:implements:** @kind:operation DeactivateOrganizationsAccess
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DeactivateOrganizationsAccess.spec.md

Deactivates trusted access with Organizations. If trusted access is deactivated, the management account does not have permissions to create and manage service-managed StackSets for your organization.

## Input Shape: DeactivateOrganizationsAccessInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: DeactivateOrganizationsAccessOutput


## Errors
- **InvalidOperationException**: The specified operation isn't valid.
- **OperationNotFoundException**: The specified ID refers to an operation that doesn't exist.

## Implementation

```speclang
def deactivate_organizations_access(store, request: dict) -> dict:
    """Deactivates trusted access with Organizations. If trusted access is deactivated, the management account does not have permissions to create and manage service-managed StackSets for your organization."""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DeactivateOrganizationsAccess", request)
```
