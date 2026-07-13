---
id: "@specs/aws/ec2/modify_instance_event_start_time"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyInstanceEventStartTime"
---

# ModifyInstanceEventStartTime

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_instance_event_start_time
> **spec:implements:** @kind:operation ModifyInstanceEventStartTime
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyInstanceEventStartTime.spec.md

Modifies the start time for a scheduled Amazon EC2 instance event.

## Input Shape: ModifyInstanceEventStartTimeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceEventId | str | ✓ | The ID of the event whose date and time you are modifying. |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance with the scheduled event. |
| NotBefore | Any  # complex shape | ✓ | The new date and time when the event will take place. |

## Output Shape: ModifyInstanceEventStartTimeResult

- **Event** (Any  # complex shape): Information about the event.

## Implementation

```speclang
def modify_instance_event_start_time(store, request: dict) -> dict:
    """Modifies the start time for a scheduled Amazon EC2 instance event."""
    instance_event_id = request.get("InstanceEventId", "").strip() if isinstance(request.get("InstanceEventId"), str) else request.get("InstanceEventId")
    if not instance_event_id:
        raise ValidationException("InstanceEventId is required")
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")
    not_before = request.get("NotBefore", "").strip() if isinstance(request.get("NotBefore"), str) else request.get("NotBefore")
    if not not_before:
        raise ValidationException("NotBefore is required")

    if store.instance_event_start_times(instance_id):
        raise ResourceInUseException(f"Resource instance_id already exists")

    record = {
        "DryRun": dry_run,
        "InstanceId": instance_id,
        "InstanceEventId": instance_event_id,
        "NotBefore": not_before,
    }

    store.instance_event_start_times(instance_id, record)

    return {
        "Event": record.get("Event", {}),
    }
```
