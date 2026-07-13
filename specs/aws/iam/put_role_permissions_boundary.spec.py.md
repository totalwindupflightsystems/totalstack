---
id: "@specs/aws/iam/put_role_permissions_boundary"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_PutRolePermissionsBoundary"
---

# PutRolePermissionsBoundary

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/put_role_permissions_boundary
> **spec:implements:** @kind:operation PutRolePermissionsBoundary
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_PutRolePermissionsBoundary.spec.md

Adds or updates the policy that is specified as the IAM role's permissions boundary. You can use an Amazon Web Services managed policy or a customer managed policy to set the boundary for a role. Use the boundary to control the maximum permissions that the role can have. Setting a permissions boundary is an advanced feature that can affect the permissions for the role. You cannot set the boundary for a service-linked role. Policies used as permissions boundaries do not provide permissions. You must also attach a permissions policy to the role. To learn how the effective permissions for a role are evaluated, see IAM JSON policy evaluation logic in the IAM User Guide.

## Input Shape: PutRolePermissionsBoundaryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PermissionsBoundary | Any  # complex shape | ✓ | The ARN of the managed policy that is used to set the permissions boundary for the role. A permissions boundary policy d |
| RoleName | Any  # complex shape | ✓ | The name (friendly name, not ARN) of the IAM role for which you want to set the permissions boundary. |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **UnmodifiableEntityException**: The request was rejected because service-linked roles are protected Amazon Web Services resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf
- **PolicyNotAttachableException**: The request failed because Amazon Web Services service role policies can only be attached to the service-linked role for that service.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def put_role_permissions_boundary(store, request: dict) -> dict:
    """Adds or updates the policy that is specified as the IAM role's permissions boundary. You can use an Amazon Web Services managed policy or a customer managed policy to set the boundary for a role. Use """
    permissions_boundary = request.get("PermissionsBoundary", "").strip() if isinstance(request.get("PermissionsBoundary"), str) else request.get("PermissionsBoundary")
    if not permissions_boundary:
        raise ValidationException("PermissionsBoundary is required")
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    if store.role_permissions_boundarys(role_name):
        raise ResourceInUseException(f"Resource role_name already exists")

    record = {
        "RoleName": role_name,
        "PermissionsBoundary": permissions_boundary,
    }

    store.role_permissions_boundarys(role_name, record)

    return {
    }
```
