---
id: "@specs/aws/ec2/describe_managed_prefix_lists"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeManagedPrefixLists"
---

# DescribeManagedPrefixLists

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_managed_prefix_lists
> **spec:implements:** @kind:operation DescribeManagedPrefixLists
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeManagedPrefixLists.spec.md

Describes your managed prefix lists and any Amazon Web Services-managed prefix lists.

## Input Shape: DescribeManagedPrefixListsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. owner-id - The ID of the prefix list owner. prefix-list-id - The ID of the prefix list. prefix-list |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| PrefixListIds | list[str] |  | One or more prefix list IDs. |

## Output Shape: DescribeManagedPrefixListsResult

- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **PrefixLists** (Any  # complex shape): Information about the prefix lists.

## Implementation

```speclang
def describe_managed_prefix_lists(store, request: dict) -> dict:
    """Describes your managed prefix lists and any Amazon Web Services-managed prefix lists."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
