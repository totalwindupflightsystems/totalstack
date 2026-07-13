---
id: "@specs/aws/cloudformation/describe_organizations_access"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeOrganizationsAccess"
---

# DescribeOrganizationsAccess

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_organizations_access
> **spec:implements:** @kind:operation DescribeOrganizationsAccess
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeOrganizationsAccess.spec.md

Retrieves information about the account's OrganizationAccess status. This API can be called either by the management account or the delegated administrator by using the CallAs parameter. This API can also be called without the CallAs parameter by the management account.

## Input Shape: DescribeOrganizationsAccessInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |

## Output Shape: DescribeOrganizationsAccessOutput

- **Status** (Any  # complex shape): Presents the status of the OrganizationAccess .

## Errors
- **InvalidOperationException**: The specified operation isn't valid.
- **OperationNotFoundException**: The specified ID refers to an operation that doesn't exist.

## Implementation

```speclang
def describe_organizations_access(store, request: dict) -> dict:
    """Retrieves information about the account's OrganizationAccess status. This API can be called either by the management account or the delegated administrator by using the CallAs parameter. This API can """

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
