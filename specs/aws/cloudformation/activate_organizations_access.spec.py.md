---
id: "@specs/aws/cloudformation/activate_organizations_access"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ActivateOrganizationsAccess"
---

# ActivateOrganizationsAccess

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/activate_organizations_access
> **spec:implements:** @kind:operation ActivateOrganizationsAccess
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ActivateOrganizationsAccess.spec.md

Activate trusted access with Organizations. With trusted access between StackSets and Organizations activated, the management account has permissions to create and manage StackSets for your organization.

## Input Shape: ActivateOrganizationsAccessInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: ActivateOrganizationsAccessOutput


## Errors
- **InvalidOperationException**: The specified operation isn't valid.
- **OperationNotFoundException**: The specified ID refers to an operation that doesn't exist.

## Implementation

```speclang
def activate_organizations_access(store, request: dict) -> dict:
    """Activate trusted access with Organizations. With trusted access between StackSets and Organizations activated, the management account has permissions to create and manage StackSets for your organizati"""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ActivateOrganizationsAccess", request)
```
