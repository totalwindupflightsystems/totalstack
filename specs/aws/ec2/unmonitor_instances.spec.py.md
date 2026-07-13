---
id: "@specs/aws/ec2/unmonitor_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_UnmonitorInstances"
---

# UnmonitorInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/unmonitor_instances
> **spec:implements:** @kind:operation UnmonitorInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_UnmonitorInstances.spec.md

Disables detailed monitoring for a running instance. For more information, see Monitoring your instances and volumes in the Amazon EC2 User Guide .

## Input Shape: UnmonitorInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceIds | list[Any  # complex shape] | ✓ | The IDs of the instances. |

## Output Shape: UnmonitorInstancesResult

- **InstanceMonitorings** (list[Any  # complex shape]): The monitoring information.

## Implementation

```speclang
def unmonitor_instances(store, request: dict) -> dict:
    """Disables detailed monitoring for a running instance. For more information, see Monitoring your instances and volumes in the Amazon EC2 User Guide ."""
    instance_ids = request.get("InstanceIds", "").strip() if isinstance(request.get("InstanceIds"), str) else request.get("InstanceIds")
    if not instance_ids:
        raise ValidationException("InstanceIds is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("UnmonitorInstances", request)
```
