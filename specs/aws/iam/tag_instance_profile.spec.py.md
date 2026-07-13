---
id: "@specs/aws/iam/tag_instance_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_TagInstanceProfile"
---

# TagInstanceProfile

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/tag_instance_profile
> **spec:implements:** @kind:operation TagInstanceProfile
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_TagInstanceProfile.spec.md

Adds one or more tags to an IAM instance profile. If a tag with the same key name already exists, then that tag is overwritten with the new value. Each tag consists of a key name and an associated value. By assigning tags to your resources, you can do the following: Administrative grouping and discovery - Attach tags to resources to aid in organization and search. For example, you could search for all resources with the key name Project and the value MyImportantProject . Or search for all resources with the key name Cost Center and the value 41200 . Access control - Include tags in IAM user-based and resource-based policies. You can use tags to restrict access to only an IAM instance profile that has a specified tag attached. For examples of policies that show how to use tags to control access, see Control access using IAM tags in the IAM User Guide . If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created. For more information about tagging, see Tagging IAM resources in the IAM User Guide . Amazon Web Services always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.

## Input Shape: TagInstanceProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| InstanceProfileName | Any  # complex shape | ✓ | The name of the IAM instance profile to which you want to add tags. This parameter allows (through its regex pattern ) a |
| Tags | Any  # complex shape | ✓ | The list of tags that you want to attach to the IAM instance profile. Each tag consists of a key name and an associated  |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def tag_instance_profile(store, request: dict) -> dict:
    """Adds one or more tags to an IAM instance profile. If a tag with the same key name already exists, then that tag is overwritten with the new value. Each tag consists of a key name and an associated val"""
    instance_profile_name = request.get("InstanceProfileName", "").strip() if isinstance(request.get("InstanceProfileName"), str) else request.get("InstanceProfileName")
    if not instance_profile_name:
        raise ValidationException("InstanceProfileName is required")
    tags = request.get("Tags", "").strip() if isinstance(request.get("Tags"), str) else request.get("Tags")
    if not tags:
        raise ValidationException("Tags is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
