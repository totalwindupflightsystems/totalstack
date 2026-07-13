---
id: "@specs/aws/ec2/delete_instance_event_window"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteInstanceEventWindow"
---

# DeleteInstanceEventWindow

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_instance_event_window
> **spec:implements:** @kind:operation DeleteInstanceEventWindow
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteInstanceEventWindow.spec.md

Deletes the specified event window. For more information, see Define event windows for scheduled events in the Amazon EC2 User Guide .

## Input Shape: DeleteInstanceEventWindowRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ForceDelete | bool |  | Specify true to force delete the event window. Use the force delete parameter if the event window is currently associate |
| InstanceEventWindowId | Any  # complex shape | ✓ | The ID of the event window. |

## Output Shape: DeleteInstanceEventWindowResult

- **InstanceEventWindowState** (Any  # complex shape): The state of the event window.

## Implementation

```speclang
def delete_instance_event_window(store, request: dict) -> dict:
    """Deletes the specified event window. For more information, see Define event windows for scheduled events in the Amazon EC2 User Guide ."""
    instance_event_window_id = request.get("InstanceEventWindowId", "").strip() if isinstance(request.get("InstanceEventWindowId"), str) else request.get("InstanceEventWindowId")

    if not store.instance_event_windows(instance_event_window_id):
        raise ResourceNotFoundException(f"Resource instance_event_window_id not found")
    store.delete_instance_event_windows(instance_event_window_id)
    return {}
```
