---
id: "@specs/aws/ec2/describe_network_insights_paths"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeNetworkInsightsPaths"
---

# DescribeNetworkInsightsPaths

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_network_insights_paths
> **spec:implements:** @kind:operation DescribeNetworkInsightsPaths
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeNetworkInsightsPaths.spec.md

Describes one or more of your paths.

## Input Shape: DescribeNetworkInsightsPathsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. The following are the possible values: destination - The ID of the resource. filter-at-source.source-addres |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NetworkInsightsPathIds | list[Any  # complex shape] |  | The IDs of the paths. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeNetworkInsightsPathsResult

- **NetworkInsightsPaths** (list[Any  # complex shape]): Information about the paths.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_network_insights_paths(store, request: dict) -> dict:
    """Describes one or more of your paths."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
