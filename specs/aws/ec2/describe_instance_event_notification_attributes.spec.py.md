---
id: "@specs/aws/ec2/describe_instance_event_notification_attributes"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeInstanceEventNotificationAttributes"
---

# DescribeInstanceEventNotificationAttributes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_instance_event_notification_attributes
> **spec:implements:** @kind:operation DescribeInstanceEventNotificationAttributes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeInstanceEventNotificationAttributes.spec.md

Describes the tag keys that are registered to appear in scheduled event notifications for resources in the current Region.

## Input Shape: DescribeInstanceEventNotificationAttributesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DescribeInstanceEventNotificationAttributesResult

- **InstanceTagAttribute** (Any  # complex shape): Information about the registered tag keys.

## Implementation

```speclang
def describe_instance_event_notification_attributes(store, request: dict) -> dict:
    """Describes the tag keys that are registered to appear in scheduled event notifications for resources in the current Region."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
