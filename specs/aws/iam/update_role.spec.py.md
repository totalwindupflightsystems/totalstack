---
id: "@specs/aws/iam/update_role"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateRole"
---

# UpdateRole

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_role
> **spec:implements:** @kind:operation UpdateRole
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateRole.spec.md

Updates the description or maximum session duration setting of a role.

## Input Shape: UpdateRoleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | Any  # complex shape |  | The new description that you want to apply to the specified role. |
| MaxSessionDuration | Any  # complex shape |  | The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for |
| RoleName | Any  # complex shape | ✓ | The name of the role that you want to modify. |

## Output Shape: UpdateRoleResponse


## Errors
- **UnmodifiableEntityException**: The request was rejected because service-linked roles are protected Amazon Web Services resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def update_role(store, request: dict) -> dict:
    """Updates the description or maximum session duration setting of a role."""
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    resource = store.roles(role_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource role_name not found")

    # Update mutable fields
    if "Description" in request:
        resource["Description"] = description
    if "MaxSessionDuration" in request:
        resource["MaxSessionDuration"] = max_session_duration

    store.roles(role_name, resource)
    return resource
```
