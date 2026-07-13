---
id: "@specs/aws/iam/list_groups"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ListGroups"
---

# ListGroups

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/list_groups
> **spec:implements:** @kind:operation ListGroups
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ListGroups.spec.md

Lists the IAM groups that have the specified path prefix. You can paginate the results using the MaxItems and Marker parameters.

## Input Shape: ListGroupsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | Any  # complex shape |  | Use this parameter only when paginating results and only after you receive a response indicating that the results are tr |
| MaxItems | Any  # complex shape |  | Use this only when paginating results to indicate the maximum number of items you want in the response. If additional it |
| PathPrefix | Any  # complex shape |  | The path prefix for filtering the results. For example, the prefix /division_abc/subdivision_xyz/ gets all groups whose  |

## Output Shape: ListGroupsResponse

- **Groups** (Any  # complex shape): A list of groups.
- **IsTruncated** (Any  # complex shape): A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent 
- **Marker** (Any  # complex shape): When IsTruncated is true , this element is present and contains the value to use for the Marker parameter in a subsequen

## Errors
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def list_groups(store, request: dict) -> dict:
    """Lists the IAM groups that have the specified path prefix. You can paginate the results using the MaxItems and Marker parameters."""

    items = store.list_groupss()
    return {"Groups": list(items.values())}
```
