---
id: "@specs/aws/ec2/describe_network_insights_analyses"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeNetworkInsightsAnalyses"
---

# DescribeNetworkInsightsAnalyses

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_network_insights_analyses
> **spec:implements:** @kind:operation DescribeNetworkInsightsAnalyses
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeNetworkInsightsAnalyses.spec.md

Describes one or more of your network insights analyses.

## Input Shape: DescribeNetworkInsightsAnalysesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AnalysisEndTime | Any  # complex shape |  | The time when the network insights analyses ended. |
| AnalysisStartTime | Any  # complex shape |  | The time when the network insights analyses started. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. The following are the possible values: path-found - A Boolean value that indicates whether a feasible path  |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NetworkInsightsAnalysisIds | list[Any  # complex shape] |  | The ID of the network insights analyses. You must specify either analysis IDs or a path ID. |
| NetworkInsightsPathId | Any  # complex shape |  | The ID of the path. You must specify either a path ID or analysis IDs. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeNetworkInsightsAnalysesResult

- **NetworkInsightsAnalyses** (list[Any  # complex shape]): Information about the network insights analyses.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_network_insights_analyses(store, request: dict) -> dict:
    """Describes one or more of your network insights analyses."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
