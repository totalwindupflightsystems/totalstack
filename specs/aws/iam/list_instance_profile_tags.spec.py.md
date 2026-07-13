---
id: "@specs/aws/iam/list_instance_profile_tags"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListInstanceProfileTags"
---

# ListInstanceProfileTags

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_instance_profile_tags
> **spec:implements:** @kind:operation ListInstanceProfileTags
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListInstanceProfileTags.spec.md

Lists the tags that are attached to the specified IAM instance profile. The returned list of tags is sorted by tag key. For more information about tagging, see Tagging IAM resources in the IAM User Guide .

## Input Shape: ListInstanceProfileTagsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| InstanceProfileName | Any  # complex shape | ✓ | The name of the IAM instance profile whose tags you want to see. This parameter allows (through its regex pattern ) a st |
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |

## Output Shape: ListInstanceProfileTagsResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **Tags** (Any  # complex shape): The list of tags that are currently attached to the IAM instance profile. Each tag consists of a key name and an associa

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_instance_profile_tags(store, request: dict) -> dict:
    """Lists the tags that are attached to the specified IAM instance profile. The returned list of tags is sorted by tag key. For more information about tagging, see Tagging IAM resources in the IAM User Gu"""
    instance_profile_name = request.get("InstanceProfileName", "").strip() if isinstance(request.get("InstanceProfileName"), str) else request.get("InstanceProfileName")
    if not instance_profile_name:
        raise ValidationException("InstanceProfileName is required")

    items = store.list_instance_profile_tagss()
    return {"Tags": list(items.values())}
```
