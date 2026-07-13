---
id: "@specs/aws/ec2/describe_prefix_lists"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribePrefixLists"
---

# DescribePrefixLists

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_prefix_lists
> **spec:implements:** @kind:operation DescribePrefixLists
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribePrefixLists.spec.md

Describes available Amazon Web Services services in a prefix list format, which includes the prefix list name and prefix list ID of the service and the IP address range for the service.

## Input Shape: DescribePrefixListsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. prefix-list-id : The ID of a prefix list. prefix-list-name : The name of a prefix list. |
| MaxResults | int |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| PrefixListIds | list[Any  # complex shape] |  | One or more prefix list IDs. |

## Output Shape: DescribePrefixListsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **PrefixLists** (Any  # complex shape): All available prefix lists.

## Implementation

```speclang
def describe_prefix_lists(store, request: dict) -> dict:
    """Describes available Amazon Web Services services in a prefix list format, which includes the prefix list name and prefix list ID of the service and the IP address range for the service."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
