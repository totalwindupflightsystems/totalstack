---
id: "@specs/aws/iam/list_role_tags"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListRoleTags"
---

# ListRoleTags

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_role_tags
> **spec:implements:** @kind:operation ListRoleTags
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListRoleTags.spec.md

Lists the tags that are attached to the specified role. The returned list of tags is sorted by tag key. For more information about tagging, see Tagging IAM resources in the IAM User Guide .

## Input Shape: ListRoleTagsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| RoleName | Any  # complex shape | ✓ | The name of the IAM role for which you want to see the list of tags. This parameter accepts (through its regex pattern ) |

## Output Shape: ListRoleTagsResponse

- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen
- **Tags** (Any  # complex shape): The list of tags that are currently attached to the role. Each tag consists of a key name and an associated value. If no

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_role_tags(store, request: dict) -> dict:
    """Lists the tags that are attached to the specified role. The returned list of tags is sorted by tag key. For more information about tagging, see Tagging IAM resources in the IAM User Guide ."""
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    items = store.list_role_tagss()
    return {"Tags": list(items.values())}
```
