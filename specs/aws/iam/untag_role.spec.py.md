---
id: "@specs/aws/iam/untag_role"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UntagRole"
---

# UntagRole

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/untag_role
> **spec:implements:** @kind:operation UntagRole
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UntagRole.spec.md

Removes the specified tags from the role. For more information about tagging, see Tagging IAM resources in the IAM User Guide .

## Input Shape: UntagRoleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| RoleName | Any  # complex shape | ✓ | The name of the IAM role from which you want to remove tags. This parameter accepts (through its regex pattern ) a strin |
| TagKeys | Any  # complex shape | ✓ | A list of key names as a simple array of strings. The tags with matching keys are removed from the specified role. |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def untag_role(store, request: dict) -> dict:
    """Removes the specified tags from the role. For more information about tagging, see Tagging IAM resources in the IAM User Guide ."""
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")
    tag_keys = request.get("TagKeys", "").strip() if isinstance(request.get("TagKeys"), str) else request.get("TagKeys")
    if not tag_keys:
        raise ValidationException("TagKeys is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
