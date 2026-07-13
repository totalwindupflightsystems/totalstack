---
id: "@specs/aws/iam/untag_user"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UntagUser"
---

# UntagUser

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/untag_user
> **spec:implements:** @kind:operation UntagUser
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UntagUser.spec.md

Removes the specified tags from the user. For more information about tagging, see Tagging IAM resources in the IAM User Guide .

## Input Shape: UntagUserRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| TagKeys | Any  # complex shape | ✓ | A list of key names as a simple array of strings. The tags with matching keys are removed from the specified user. |
| UserName | Any  # complex shape | ✓ | The name of the IAM user from which you want to remove tags. This parameter allows (through its regex pattern ) a string |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def untag_user(store, request: dict) -> dict:
    """Removes the specified tags from the user. For more information about tagging, see Tagging IAM resources in the IAM User Guide ."""
    tag_keys = request.get("TagKeys", "").strip() if isinstance(request.get("TagKeys"), str) else request.get("TagKeys")
    if not tag_keys:
        raise ValidationException("TagKeys is required")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
