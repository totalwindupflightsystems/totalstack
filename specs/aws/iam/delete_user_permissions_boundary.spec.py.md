---
id: "@specs/aws/iam/delete_user_permissions_boundary"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteUserPermissionsBoundary"
---

# DeleteUserPermissionsBoundary

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_user_permissions_boundary
> **spec:implements:** @kind:operation DeleteUserPermissionsBoundary
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteUserPermissionsBoundary.spec.md

Deletes the permissions boundary for the specified IAM user. Deleting the permissions boundary for a user might increase its permissions by allowing the user to perform all the actions granted in its permissions policies.

## Input Shape: DeleteUserPermissionsBoundaryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| UserName | Any  # complex shape | ✓ | The name (friendly name, not ARN) of the IAM user from which you want to remove the permissions boundary. |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_user_permissions_boundary(store, request: dict) -> dict:
    """Deletes the permissions boundary for the specified IAM user. Deleting the permissions boundary for a user might increase its permissions by allowing the user to perform all the actions granted in its """
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")

    if not store.user_permissions_boundarys(user_name):
        raise ResourceNotFoundException(f"Resource user_name not found")
    store.delete_user_permissions_boundarys(user_name)
    return {}
```
