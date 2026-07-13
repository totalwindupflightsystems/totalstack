---
id: "@specs/aws/ec2/modify_instance_event_window"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyInstanceEventWindow"
---

# ModifyInstanceEventWindow

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_instance_event_window
> **spec:implements:** @kind:operation ModifyInstanceEventWindow
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyInstanceEventWindow.spec.md

Modifies the specified event window. You can define either a set of time ranges or a cron expression when modifying the event window, but not both. To modify the targets associated with the event window, use the AssociateInstanceEventWindow and DisassociateInstanceEventWindow API. If Amazon Web Services has already scheduled an event, modifying an event window won't change the time of the scheduled event. For more information, see Define event windows for scheduled events in the Amazon EC2 User Guide .

## Input Shape: ModifyInstanceEventWindowRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CronExpression | Any  # complex shape |  | The cron expression of the event window, for example, * 0-4,20-23 * * 1,5 . Constraints: Only hour and day of the week v |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceEventWindowId | Any  # complex shape | ✓ | The ID of the event window. |
| Name | str |  | The name of the event window. |
| TimeRanges | Any  # complex shape |  | The time ranges of the event window. |

## Output Shape: ModifyInstanceEventWindowResult

- **InstanceEventWindow** (Any  # complex shape): Information about the event window.

## Implementation

```speclang
def modify_instance_event_window(store, request: dict) -> dict:
    """Modifies the specified event window. You can define either a set of time ranges or a cron expression when modifying the event window, but not both. To modify the targets associated with the event wind"""
    instance_event_window_id = request.get("InstanceEventWindowId", "").strip() if isinstance(request.get("InstanceEventWindowId"), str) else request.get("InstanceEventWindowId")
    if not instance_event_window_id:
        raise ValidationException("InstanceEventWindowId is required")

    resource = store.instance_event_windows(instance_event_window_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_event_window_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "Name" in request:
        resource["Name"] = name
    if "TimeRanges" in request:
        resource["TimeRanges"] = time_ranges
    if "CronExpression" in request:
        resource["CronExpression"] = cron_expression

    store.instance_event_windows(instance_event_window_id, resource)
    return resource
```
