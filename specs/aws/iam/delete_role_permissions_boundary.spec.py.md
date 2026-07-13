---
id: "@specs/aws/iam/delete_role_permissions_boundary"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteRolePermissionsBoundary"
---

# DeleteRolePermissionsBoundary

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_role_permissions_boundary
> **spec:implements:** @kind:operation DeleteRolePermissionsBoundary
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteRolePermissionsBoundary.spec.md

Deletes the permissions boundary for the specified IAM role. You cannot set the boundary for a service-linked role. Deleting the permissions boundary for a role might increase its permissions. For example, it might allow anyone who assumes the role to perform all the actions granted in its permissions policies.

## Input Shape: DeleteRolePermissionsBoundaryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| RoleName | Any  # complex shape | ✓ | The name (friendly name, not ARN) of the IAM role from which you want to remove the permissions boundary. |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **UnmodifiableEntityException**: The request was rejected because service-linked roles are protected Amazon Web Services resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_role_permissions_boundary(store, request: dict) -> dict:
    """Deletes the permissions boundary for the specified IAM role. You cannot set the boundary for a service-linked role. Deleting the permissions boundary for a role might increase its permissions. For exa"""
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")

    if not store.role_permissions_boundarys(role_name):
        raise ResourceNotFoundException(f"Resource role_name not found")
    store.delete_role_permissions_boundarys(role_name)
    return {}
```
