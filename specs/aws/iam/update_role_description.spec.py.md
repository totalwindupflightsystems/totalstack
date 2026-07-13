---
id: "@specs/aws/iam/update_role_description"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateRoleDescription"
---

# UpdateRoleDescription

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_role_description
> **spec:implements:** @kind:operation UpdateRoleDescription
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateRoleDescription.spec.md

Use UpdateRole instead. Modifies only the description of a role. This operation performs the same function as the Description parameter in the UpdateRole operation.

## Input Shape: UpdateRoleDescriptionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | Any  # complex shape | ✓ | The new description that you want to apply to the specified role. |
| RoleName | Any  # complex shape | ✓ | The name of the role that you want to modify. |

## Output Shape: UpdateRoleDescriptionResponse

- **Role** (Any  # complex shape): A structure that contains details about the modified role.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **UnmodifiableEntityException**: The request was rejected because service-linked roles are protected Amazon Web Services resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def update_role_description(store, request: dict) -> dict:
    """Use UpdateRole instead. Modifies only the description of a role. This operation performs the same function as the Description parameter in the UpdateRole operation."""
    description = request.get("Description", "").strip() if isinstance(request.get("Description"), str) else request.get("Description")
    if not description:
        raise ValidationException("Description is required")
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    resource = store.role_descriptions(role_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource role_name not found")

    # Update mutable fields

    store.role_descriptions(role_name, resource)
    return resource
```
