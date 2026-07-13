---
id: "@specs/aws/ec2/monitor_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_MonitorInstances"
---

# MonitorInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/monitor_instances
> **spec:implements:** @kind:operation MonitorInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_MonitorInstances.spec.md

Enables detailed monitoring for a running instance. Otherwise, basic monitoring is enabled. For more information, see Monitor your instances using CloudWatch in the Amazon EC2 User Guide . To disable detailed monitoring, see UnmonitorInstances .

## Input Shape: MonitorInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceIds | list[Any  # complex shape] | ✓ | The IDs of the instances. |

## Output Shape: MonitorInstancesResult

- **InstanceMonitorings** (list[Any  # complex shape]): The monitoring information.

## Implementation

```speclang
def monitor_instances(store, request: dict) -> dict:
    """Enables detailed monitoring for a running instance. Otherwise, basic monitoring is enabled. For more information, see Monitor your instances using CloudWatch in the Amazon EC2 User Guide . To disable """
    instance_ids = request.get("InstanceIds", "").strip() if isinstance(request.get("InstanceIds"), str) else request.get("InstanceIds")
    if not instance_ids:
        raise ValidationException("InstanceIds is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("MonitorInstances", request)
```
