---
id: "@specs/aws/ec2/register_instance_event_notification_attributes"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RegisterInstanceEventNotificationAttributes"
---

# RegisterInstanceEventNotificationAttributes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/register_instance_event_notification_attributes
> **spec:implements:** @kind:operation RegisterInstanceEventNotificationAttributes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RegisterInstanceEventNotificationAttributes.spec.md

Registers a set of tag keys to include in scheduled event notifications for your resources. To remove tags, use DeregisterInstanceEventNotificationAttributes .

## Input Shape: RegisterInstanceEventNotificationAttributesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceTagAttribute | Any  # complex shape | ✓ | Information about the tag keys to register. |

## Output Shape: RegisterInstanceEventNotificationAttributesResult

- **InstanceTagAttribute** (Any  # complex shape): The resulting set of tag keys.

## Implementation

```speclang
def register_instance_event_notification_attributes(store, request: dict) -> dict:
    """Registers a set of tag keys to include in scheduled event notifications for your resources. To remove tags, use DeregisterInstanceEventNotificationAttributes ."""
    instance_tag_attribute = request.get("InstanceTagAttribute", "").strip() if isinstance(request.get("InstanceTagAttribute"), str) else request.get("InstanceTagAttribute")
    if not instance_tag_attribute:
        raise ValidationException("InstanceTagAttribute is required")

    if store.register_instance_event_notification_attributess(instance_tag_attribute):
        raise ResourceInUseException(f"Resource instance_tag_attribute already exists")

    record = {
        "DryRun": dry_run,
        "InstanceTagAttribute": instance_tag_attribute,
    }

    store.register_instance_event_notification_attributess(instance_tag_attribute, record)

    return {
        "InstanceTagAttribute": instance_tag_attribute,
    }
```
