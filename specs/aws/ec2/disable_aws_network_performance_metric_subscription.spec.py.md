---
id: "@specs/aws/ec2/disable_aws_network_performance_metric_subscription"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableAwsNetworkPerformanceMetricSubscription"
---

# DisableAwsNetworkPerformanceMetricSubscription

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_aws_network_performance_metric_subscription
> **spec:implements:** @kind:operation DisableAwsNetworkPerformanceMetricSubscription
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableAwsNetworkPerformanceMetricSubscription.spec.md

Disables Infrastructure Performance metric subscriptions.

## Input Shape: DisableAwsNetworkPerformanceMetricSubscriptionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Destination | str |  | The target Region or Availability Zone that the metric subscription is disabled for. For example, eu-north-1 . |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Metric | Any  # complex shape |  | The metric used for the disabled subscription. |
| Source | str |  | The source Region or Availability Zone that the metric subscription is disabled for. For example, us-east-1 . |
| Statistic | Any  # complex shape |  | The statistic used for the disabled subscription. |

## Output Shape: DisableAwsNetworkPerformanceMetricSubscriptionResult

- **Output** (bool): Indicates whether the unsubscribe action was successful.

## Implementation

```speclang
def disable_aws_network_performance_metric_subscription(store, request: dict) -> dict:
    """Disables Infrastructure Performance metric subscriptions."""

```
