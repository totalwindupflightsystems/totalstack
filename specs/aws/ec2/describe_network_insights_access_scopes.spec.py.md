---
id: "@specs/aws/ec2/describe_network_insights_access_scopes"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeNetworkInsightsAccessScopes"
---

# DescribeNetworkInsightsAccessScopes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_network_insights_access_scopes
> **spec:implements:** @kind:operation DescribeNetworkInsightsAccessScopes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeNetworkInsightsAccessScopes.spec.md

Describes the specified Network Access Scopes.

## Input Shape: DescribeNetworkInsightsAccessScopesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | There are no supported filters. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NetworkInsightsAccessScopeIds | list[Any  # complex shape] |  | The IDs of the Network Access Scopes. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeNetworkInsightsAccessScopesResult

- **NetworkInsightsAccessScopes** (list[Any  # complex shape]): The Network Access Scopes.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_network_insights_access_scopes(store, request: dict) -> dict:
    """Describes the specified Network Access Scopes."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
