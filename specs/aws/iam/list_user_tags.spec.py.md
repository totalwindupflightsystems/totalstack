---
id: "@specs/aws/iam/list_user_tags"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListUserTags"
---

# ListUserTags

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_user_tags
> **spec:implements:** @kind:operation ListUserTags
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListUserTags.spec.md

Lists the tags that are attached to the specified IAM user. The returned list of tags is sorted by tag key. For more information about tagging, see Tagging IAM resources in the IAM User Guide .

## Input Shape: ListUserTagsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| UserName | Any  # complex shape | ✓ | The name of the IAM user whose tags you want to see. This parameter allows (through its regex pattern ) a string of char |

## Output Shape: ListUserTagsResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **Tags** (Any  # complex shape): The list of tags that are currently attached to the user. Each tag consists of a key name and an associated value. If no

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_user_tags(store, request: dict) -> dict:
    """Lists the tags that are attached to the specified IAM user. The returned list of tags is sorted by tag key. For more information about tagging, see Tagging IAM resources in the IAM User Guide ."""
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    items = store.list_user_tagss()
    return {"Tags": list(items.values())}
```
