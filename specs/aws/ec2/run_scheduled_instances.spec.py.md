---
id: "@specs/aws/ec2/run_scheduled_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RunScheduledInstances"
---

# RunScheduledInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/run_scheduled_instances
> **spec:implements:** @kind:operation RunScheduledInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RunScheduledInstances.spec.md

Launches the specified Scheduled Instances. Before you can launch a Scheduled Instance, you must purchase it and obtain an identifier using PurchaseScheduledInstances . You must launch a Scheduled Instance during its scheduled time period. You can't stop or reboot a Scheduled Instance, but you can terminate it as needed. If you terminate a Scheduled Instance before the current scheduled time period ends, you can launch it again after a few minutes.

## Input Shape: RunScheduledInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see Ensuring Idempo |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceCount | int |  | The number of instances. Default: 1 |
| LaunchSpecification | Any  # complex shape | ✓ | The launch specification. You must match the instance type, Availability Zone, network, and platform of the schedule tha |
| ScheduledInstanceId | Any  # complex shape | ✓ | The Scheduled Instance ID. |

## Output Shape: RunScheduledInstancesResult

- **InstanceIdSet** (Any  # complex shape): The IDs of the newly launched instances.

## Implementation

```speclang
def run_scheduled_instances(store, request: dict) -> dict:
    """Launches the specified Scheduled Instances. Before you can launch a Scheduled Instance, you must purchase it and obtain an identifier using PurchaseScheduledInstances . You must launch a Scheduled Ins"""
    launch_specification = request.get("LaunchSpecification", "").strip() if isinstance(request.get("LaunchSpecification"), str) else request.get("LaunchSpecification")
    if not launch_specification:
        raise ValidationException("LaunchSpecification is required")
    scheduled_instance_id = request.get("ScheduledInstanceId", "").strip() if isinstance(request.get("ScheduledInstanceId"), str) else request.get("ScheduledInstanceId")
    if not scheduled_instance_id:
        raise ValidationException("ScheduledInstanceId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RunScheduledInstances", request)
```
