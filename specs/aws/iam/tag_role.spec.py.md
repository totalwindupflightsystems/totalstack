---
id: "@specs/aws/iam/tag_role"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_TagRole"
---

# TagRole

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/tag_role
> **spec:implements:** @kind:operation TagRole
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_TagRole.spec.md

Adds one or more tags to an IAM role. The role can be a regular role or a service-linked role. If a tag with the same key name already exists, then that tag is overwritten with the new value. A tag consists of a key name and an associated value. By assigning tags to your resources, you can do the following: Administrative grouping and discovery - Attach tags to resources to aid in organization and search. For example, you could search for all resources with the key name Project and the value MyImportantProject . Or search for all resources with the key name Cost Center and the value 41200 . Access control - Include tags in IAM user-based and resource-based policies. You can use tags to restrict access to only an IAM role that has a specified tag attached. You can also restrict access to only those resources that have a certain tag attached. For examples of policies that show how to use tags to control access, see Control access using IAM tags in the IAM User Guide . Cost allocation - Use tags to help track which individuals and teams are using which Amazon Web Services resources. If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created. For more information about tagging, see Tagging IAM resources in the IAM User Guide . Amazon Web Services always interprets the tag Value as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code. For more information about tagging, see Tagging IAM identities in the IAM User Guide .

## Input Shape: TagRoleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| RoleName | Any  # complex shape | ✓ | The name of the IAM role to which you want to add tags. This parameter accepts (through its regex pattern ) a string of  |
| Tags | Any  # complex shape | ✓ | The list of tags that you want to attach to the IAM role. Each tag consists of a key name and an associated value. |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def tag_role(store, request: dict) -> dict:
    """Adds one or more tags to an IAM role. The role can be a regular role or a service-linked role. If a tag with the same key name already exists, then that tag is overwritten with the new value. A tag co"""
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")
    tags = request.get("Tags", "").strip() if isinstance(request.get("Tags"), str) else request.get("Tags")
    if not tags:
        raise ValidationException("Tags is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
