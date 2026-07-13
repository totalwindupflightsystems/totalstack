---
id: "@specs/aws/ec2/associate_instance_event_window"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateInstanceEventWindow"
---

# AssociateInstanceEventWindow

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_instance_event_window
> **spec:implements:** @kind:operation AssociateInstanceEventWindow
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateInstanceEventWindow.spec.md

Associates one or more targets with an event window. Only one type of target (instance IDs, Dedicated Host IDs, or tags) can be specified with an event window. For more information, see Define event windows for scheduled events in the Amazon EC2 User Guide .

## Input Shape: AssociateInstanceEventWindowRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationTarget | Any  # complex shape | ✓ | One or more targets associated with the specified event window. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceEventWindowId | Any  # complex shape | ✓ | The ID of the event window. |

## Output Shape: AssociateInstanceEventWindowResult

- **InstanceEventWindow** (Any  # complex shape): Information about the event window.

## Implementation

```speclang
def associate_instance_event_window(store, request: dict) -> dict:
    """Associates one or more targets with an event window. Only one type of target (instance IDs, Dedicated Host IDs, or tags) can be specified with an event window. For more information, see Define event w"""
    association_target = request.get("AssociationTarget", "").strip() if isinstance(request.get("AssociationTarget"), str) else request.get("AssociationTarget")
    if not association_target:
        raise ValidationException("AssociationTarget is required")
    instance_event_window_id = request.get("InstanceEventWindowId", "").strip() if isinstance(request.get("InstanceEventWindowId"), str) else request.get("InstanceEventWindowId")
    if not instance_event_window_id:
        raise ValidationException("InstanceEventWindowId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateInstanceEventWindow", request)
```
