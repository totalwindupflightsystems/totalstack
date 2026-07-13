---
id: "@specs/aws/ec2/create_instance_event_window"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateInstanceEventWindow"
---

# CreateInstanceEventWindow

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_instance_event_window
> **spec:implements:** @kind:operation CreateInstanceEventWindow
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateInstanceEventWindow.spec.md

Creates an event window in which scheduled events for the associated Amazon EC2 instances can run. You can define either a set of time ranges or a cron expression when creating the event window, but not both. All event window times are in UTC. You can create up to 200 event windows per Amazon Web Services Region. When you create the event window, targets (instance IDs, Dedicated Host IDs, or tags) are not yet associated with it. To ensure that the event window can be used, you must associate one or more targets with it by using the AssociateInstanceEventWindow API. Event windows are applicable only for scheduled events that stop, reboot, or terminate instances. Event windows are not applicable for: Expedited scheduled events and network maintenance events. Unscheduled maintenance such as AutoRecovery and unplanned reboots. For more information, see Define event windows for scheduled events in the Amazon EC2 User Guide .

## Input Shape: CreateInstanceEventWindowRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CronExpression | Any  # complex shape |  | The cron expression for the event window, for example, * 0-4,20-23 * * 1,5 . If you specify a cron expression, you can't |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Name | str |  | The name of the event window. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the event window. |
| TimeRanges | Any  # complex shape |  | The time range for the event window. If you specify a time range, you can't specify a cron expression. |

## Output Shape: CreateInstanceEventWindowResult

- **InstanceEventWindow** (Any  # complex shape): Information about the event window.

## Implementation

```speclang
def create_instance_event_window(store, request: dict) -> dict:
    """Creates an event window in which scheduled events for the associated Amazon EC2 instances can run. You can define either a set of time ranges or a cron expression when creating the event window, but n"""


    record = {
        "DryRun": dry_run,
        "Name": name,
        "TimeRanges": time_ranges,
        "CronExpression": cron_expression,
        "TagSpecifications": tag_specifications,
    }

    store.instance_event_windows(record)

    return {
        "InstanceEventWindow": record.get("InstanceEventWindow", {}),
    }
```
