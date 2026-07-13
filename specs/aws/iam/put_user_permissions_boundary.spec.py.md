---
id: "@specs/aws/iam/put_user_permissions_boundary"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_PutUserPermissionsBoundary"
---

# PutUserPermissionsBoundary

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/put_user_permissions_boundary
> **spec:implements:** @kind:operation PutUserPermissionsBoundary
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_PutUserPermissionsBoundary.spec.md

Adds or updates the policy that is specified as the IAM user's permissions boundary. You can use an Amazon Web Services managed policy or a customer managed policy to set the boundary for a user. Use the boundary to control the maximum permissions that the user can have. Setting a permissions boundary is an advanced feature that can affect the permissions for the user. Policies that are used as permissions boundaries do not provide permissions. You must also attach a permissions policy to the user. To learn how the effective permissions for a user are evaluated, see IAM JSON policy evaluation logic in the IAM User Guide.

## Input Shape: PutUserPermissionsBoundaryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PermissionsBoundary | Any  # complex shape | ✓ | The ARN of the managed policy that is used to set the permissions boundary for the user. A permissions boundary policy d |
| UserName | Any  # complex shape | ✓ | The name (friendly name, not ARN) of the IAM user for which you want to set the permissions boundary. |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **PolicyNotAttachableException**: The request failed because Amazon Web Services service role policies can only be attached to the service-linked role for that service.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def put_user_permissions_boundary(store, request: dict) -> dict:
    """Adds or updates the policy that is specified as the IAM user's permissions boundary. You can use an Amazon Web Services managed policy or a customer managed policy to set the boundary for a user. Use """
    permissions_boundary = request.get("PermissionsBoundary", "").strip() if isinstance(request.get("PermissionsBoundary"), str) else request.get("PermissionsBoundary")
    if not permissions_boundary:
        raise ValidationException("PermissionsBoundary is required")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    if store.user_permissions_boundarys(user_name):
        raise ResourceInUseException(f"Resource user_name already exists")

    record = {
        "UserName": user_name,
        "PermissionsBoundary": permissions_boundary,
    }

    store.user_permissions_boundarys(user_name, record)

    return {
    }
```
