---
id: "@specs/aws/ec2/delete_spot_datafeed_subscription"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteSpotDatafeedSubscription"
---

# DeleteSpotDatafeedSubscription

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_spot_datafeed_subscription
> **spec:implements:** @kind:operation DeleteSpotDatafeedSubscription
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteSpotDatafeedSubscription.spec.md

Deletes the data feed for Spot Instances.

## Input Shape: DeleteSpotDatafeedSubscriptionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Implementation

```speclang
def delete_spot_datafeed_subscription(store, request: dict) -> dict:
    """Deletes the data feed for Spot Instances."""

    return {}
```
