---
id: "@specs/aws/ec2/create_spot_datafeed_subscription"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateSpotDatafeedSubscription"
---

# CreateSpotDatafeedSubscription

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_spot_datafeed_subscription
> **spec:implements:** @kind:operation CreateSpotDatafeedSubscription
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateSpotDatafeedSubscription.spec.md

Creates a data feed for Spot Instances, enabling you to view Spot Instance usage logs. You can create one data feed per Amazon Web Services account. For more information, see Spot Instance data feed in the Amazon EC2 User Guide .

## Input Shape: CreateSpotDatafeedSubscriptionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Bucket | str | ✓ | The name of the Amazon S3 bucket in which to store the Spot Instance data feed. For more information about bucket names, |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Prefix | str |  | The prefix for the data feed file names. |

## Output Shape: CreateSpotDatafeedSubscriptionResult

- **SpotDatafeedSubscription** (Any  # complex shape): The Spot Instance data feed subscription.

## Implementation

```speclang
def create_spot_datafeed_subscription(store, request: dict) -> dict:
    """Creates a data feed for Spot Instances, enabling you to view Spot Instance usage logs. You can create one data feed per Amazon Web Services account. For more information, see Spot Instance data feed i"""
    bucket = request.get("Bucket", "").strip() if isinstance(request.get("Bucket"), str) else request.get("Bucket")
    if not bucket:
        raise ValidationException("Bucket is required")

    if store.spot_datafeed_subscriptions(bucket):
        raise ResourceInUseException(f"Resource bucket already exists")

    record = {
        "DryRun": dry_run,
        "Bucket": bucket,
        "Prefix": prefix,
    }

    store.spot_datafeed_subscriptions(bucket, record)

    return {
        "SpotDatafeedSubscription": record.get("SpotDatafeedSubscription", {}),
    }
```
