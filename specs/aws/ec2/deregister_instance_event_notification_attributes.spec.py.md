---
id: "@specs/aws/ec2/deregister_instance_event_notification_attributes"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeregisterInstanceEventNotificationAttributes"
---

# DeregisterInstanceEventNotificationAttributes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/deregister_instance_event_notification_attributes
> **spec:implements:** @kind:operation DeregisterInstanceEventNotificationAttributes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeregisterInstanceEventNotificationAttributes.spec.md

Deregisters tag keys to prevent tags that have the specified tag keys from being included in scheduled event notifications for resources in the Region.

## Input Shape: DeregisterInstanceEventNotificationAttributesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceTagAttribute | Any  # complex shape | ✓ | Information about the tag keys to deregister. |

## Output Shape: DeregisterInstanceEventNotificationAttributesResult

- **InstanceTagAttribute** (Any  # complex shape): The resulting set of tag keys.

## Implementation

```speclang
def deregister_instance_event_notification_attributes(store, request: dict) -> dict:
    """Deregisters tag keys to prevent tags that have the specified tag keys from being included in scheduled event notifications for resources in the Region."""
    instance_tag_attribute = request.get("InstanceTagAttribute", "").strip() if isinstance(request.get("InstanceTagAttribute"), str) else request.get("InstanceTagAttribute")

    if store.deregister_instance_event_notification_attributess(instance_tag_attribute):
        raise ResourceInUseException(f"Resource instance_tag_attribute already exists")

    record = {
        "DryRun": dry_run,
        "InstanceTagAttribute": instance_tag_attribute,
    }

    store.deregister_instance_event_notification_attributess(instance_tag_attribute, record)

    return {
        "InstanceTagAttribute": instance_tag_attribute,
    }
```
