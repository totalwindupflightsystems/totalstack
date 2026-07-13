---
id: "@specs/aws/ec2/disable_instance_sql_ha_standby_detections"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableInstanceSqlHaStandbyDetections"
---

# DisableInstanceSqlHaStandbyDetections

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_instance_sql_ha_standby_detections
> **spec:implements:** @kind:operation DisableInstanceSqlHaStandbyDetections
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableInstanceSqlHaStandbyDetections.spec.md

Disable Amazon EC2 instances running in an SQL Server High Availability cluster from SQL Server High Availability instance standby detection monitoring. Once disabled, Amazon Web Services no longer monitors the metadata for the instances to determine whether they are active or standby nodes in the SQL Server High Availability cluster.

## Input Shape: DisableInstanceSqlHaStandbyDetectionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceIds | list[Any  # complex shape] | ✓ | The IDs of the instances to disable from SQL Server High Availability standby detection monitoring. |

## Output Shape: DisableInstanceSqlHaStandbyDetectionsResult

- **Instances** (list[Any  # complex shape]): Information about the instances that were disabled from SQL Server High Availability standby detection monitoring.

## Implementation

```speclang
def disable_instance_sql_ha_standby_detections(store, request: dict) -> dict:
    """Disable Amazon EC2 instances running in an SQL Server High Availability cluster from SQL Server High Availability instance standby detection monitoring. Once disabled, Amazon Web Services no longer mo"""
    instance_ids = request.get("InstanceIds", "").strip() if isinstance(request.get("InstanceIds"), str) else request.get("InstanceIds")
    if not instance_ids:
        raise ValidationException("InstanceIds is required")

    resource = store.disable_instance_sql_ha_standby_detectionss(instance_ids)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_ids not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.disable_instance_sql_ha_standby_detectionss(instance_ids, resource)
    return resource
```
