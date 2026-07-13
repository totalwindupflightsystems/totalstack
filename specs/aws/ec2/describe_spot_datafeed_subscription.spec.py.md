---
id: "@specs/aws/ec2/describe_spot_datafeed_subscription"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSpotDatafeedSubscription"
---

# DescribeSpotDatafeedSubscription

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_spot_datafeed_subscription
> **spec:implements:** @kind:operation DescribeSpotDatafeedSubscription
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSpotDatafeedSubscription.spec.md

Describes the data feed for Spot Instances. For more information, see Spot Instance data feed in the Amazon EC2 User Guide .

## Input Shape: DescribeSpotDatafeedSubscriptionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DescribeSpotDatafeedSubscriptionResult

- **SpotDatafeedSubscription** (Any  # complex shape): The Spot Instance data feed subscription.

## Implementation

```speclang
def describe_spot_datafeed_subscription(store, request: dict) -> dict:
    """Describes the data feed for Spot Instances. For more information, see Spot Instance data feed in the Amazon EC2 User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
