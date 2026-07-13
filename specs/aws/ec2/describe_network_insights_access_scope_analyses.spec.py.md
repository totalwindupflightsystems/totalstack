---
id: "@specs/aws/ec2/describe_network_insights_access_scope_analyses"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeNetworkInsightsAccessScopeAnalyses"
---

# DescribeNetworkInsightsAccessScopeAnalyses

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_network_insights_access_scope_analyses
> **spec:implements:** @kind:operation DescribeNetworkInsightsAccessScopeAnalyses
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeNetworkInsightsAccessScopeAnalyses.spec.md

Describes the specified Network Access Scope analyses.

## Input Shape: DescribeNetworkInsightsAccessScopeAnalysesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AnalysisStartTimeBegin | Any  # complex shape |  | Filters the results based on the start time. The analysis must have started on or after this time. |
| AnalysisStartTimeEnd | Any  # complex shape |  | Filters the results based on the start time. The analysis must have started on or before this time. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | There are no supported filters. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NetworkInsightsAccessScopeAnalysisIds | list[Any  # complex shape] |  | The IDs of the Network Access Scope analyses. |
| NetworkInsightsAccessScopeId | Any  # complex shape |  | The ID of the Network Access Scope. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeNetworkInsightsAccessScopeAnalysesResult

- **NetworkInsightsAccessScopeAnalyses** (list[Any  # complex shape]): The Network Access Scope analyses.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_network_insights_access_scope_analyses(store, request: dict) -> dict:
    """Describes the specified Network Access Scope analyses."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
