---
id: "@specs/aws/ec2/enable_aws_network_performance_metric_subscription"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableAwsNetworkPerformanceMetricSubscription"
---

# EnableAwsNetworkPerformanceMetricSubscription

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_aws_network_performance_metric_subscription
> **spec:implements:** @kind:operation EnableAwsNetworkPerformanceMetricSubscription
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableAwsNetworkPerformanceMetricSubscription.spec.md

Enables Infrastructure Performance subscriptions.

## Input Shape: EnableAwsNetworkPerformanceMetricSubscriptionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Destination | str |  | The target Region (like us-east-2 ) or Availability Zone ID (like use2-az2 ) that the metric subscription is enabled for |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Metric | Any  # complex shape |  | The metric used for the enabled subscription. |
| Source | str |  | The source Region (like us-east-1 ) or Availability Zone ID (like use1-az1 ) that the metric subscription is enabled for |
| Statistic | Any  # complex shape |  | The statistic used for the enabled subscription. |

## Output Shape: EnableAwsNetworkPerformanceMetricSubscriptionResult

- **Output** (bool): Indicates whether the subscribe action was successful.

## Implementation

```speclang
def enable_aws_network_performance_metric_subscription(store, request: dict) -> dict:
    """Enables Infrastructure Performance subscriptions."""

```
