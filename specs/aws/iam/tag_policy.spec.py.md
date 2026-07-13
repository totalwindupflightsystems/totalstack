---
id: "@specs/aws/iam/tag_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_TagPolicy"
---

# TagPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/tag_policy
> **spec:implements:** @kind:operation TagPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_TagPolicy.spec.md

Adds one or more tags to an IAM customer managed policy. If a tag with the same key name already exists, then that tag is overwritten with the new value. A tag consists of a key name and an associated value. By assigning tags to your resources, you can do the following: Administrative grouping and discovery - Attach tags to resources to aid in organization and search. For example, you could search for all resources with the key name Project and the value MyImportantProject . Or search for all resources with the key name Cost Center and the value 41200 . Access control - Include tags in IAM user-based and resource-based policies. You can use tags to restrict access to only an IAM customer managed policy that has a specified tag attached. For examples of policies that show how to use tags to control access, see Control access using IAM tags in the IAM User Guide . If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created. For more information about tagging, see Tagging IAM resources in the IAM User Guide . Amazon Web Services always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.

## Input Shape: TagPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyArn | Any  # complex shape | ✓ | The ARN of the IAM customer managed policy to which you want to add tags. This parameter allows (through its regex patte |
| Tags | Any  # complex shape | ✓ | The list of tags that you want to attach to the IAM customer managed policy. Each tag consists of a key name and an asso |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def tag_policy(store, request: dict) -> dict:
    """Adds one or more tags to an IAM customer managed policy. If a tag with the same key name already exists, then that tag is overwritten with the new value. A tag consists of a key name and an associated"""
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")
    if not policy_arn:
        raise ValidationException("PolicyArn is required")
    tags = request.get("Tags", "").strip() if isinstance(request.get("Tags"), str) else request.get("Tags")
    if not tags:
        raise ValidationException("Tags is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
