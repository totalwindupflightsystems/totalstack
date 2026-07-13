---
id: "@specs/aws/ec2/describe_aws_network_performance_metric_subscriptions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeAwsNetworkPerformanceMetricSubscriptions"
---

# DescribeAwsNetworkPerformanceMetricSubscriptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_aws_network_performance_metric_subscriptions
> **spec:implements:** @kind:operation DescribeAwsNetworkPerformanceMetricSubscriptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeAwsNetworkPerformanceMetricSubscriptions.spec.md

Describes the current Infrastructure Performance metric subscriptions.

## Input Shape: DescribeAwsNetworkPerformanceMetricSubscriptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |

## Output Shape: DescribeAwsNetworkPerformanceMetricSubscriptionsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **Subscriptions** (list[Any  # complex shape]): Describes the current Infrastructure Performance subscriptions.

## Implementation

```speclang
def describe_aws_network_performance_metric_subscriptions(store, request: dict) -> dict:
    """Describes the current Infrastructure Performance metric subscriptions."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
