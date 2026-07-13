---
id: "@specs/aws/iam/untag_instance_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UntagInstanceProfile"
---

# UntagInstanceProfile

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/untag_instance_profile
> **spec:implements:** @kind:operation UntagInstanceProfile
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UntagInstanceProfile.spec.md

Removes the specified tags from the IAM instance profile. For more information about tagging, see Tagging IAM resources in the IAM User Guide .

## Input Shape: UntagInstanceProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| InstanceProfileName | Any  # complex shape | ✓ | The name of the IAM instance profile from which you want to remove tags. This parameter allows (through its regex patter |
| TagKeys | Any  # complex shape | ✓ | A list of key names as a simple array of strings. The tags with matching keys are removed from the specified instance pr |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def untag_instance_profile(store, request: dict) -> dict:
    """Removes the specified tags from the IAM instance profile. For more information about tagging, see Tagging IAM resources in the IAM User Guide ."""
    instance_profile_name = request.get("InstanceProfileName", "").strip() if isinstance(request.get("InstanceProfileName"), str) else request.get("InstanceProfileName")
    if not instance_profile_name:
        raise ValidationException("InstanceProfileName is required")
    tag_keys = request.get("TagKeys", "").strip() if isinstance(request.get("TagKeys"), str) else request.get("TagKeys")
    if not tag_keys:
        raise ValidationException("TagKeys is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
