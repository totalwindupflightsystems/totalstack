---
id: "@specs/aws/ec2/enable_instance_sql_ha_standby_detections"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableInstanceSqlHaStandbyDetections"
---

# EnableInstanceSqlHaStandbyDetections

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_instance_sql_ha_standby_detections
> **spec:implements:** @kind:operation EnableInstanceSqlHaStandbyDetections
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableInstanceSqlHaStandbyDetections.spec.md

Enable Amazon EC2 instances running in an SQL Server High Availability cluster for SQL Server High Availability instance standby detection monitoring. Once enabled, Amazon Web Services monitors the metadata for the instances to determine whether they are active or standby nodes in the SQL Server High Availability cluster. If the instances are determined to be standby failover nodes, Amazon Web Services automatically applies SQL Server licensing fee waiver for those instances. To register an instance, it must be running a Windows SQL Server license-included AMI and have the Amazon Web Services Systems Manager agent installed and running. Only Windows Server 2019 and later and SQL Server (Standard and Enterprise editions) 2017 and later are supported. For more information, see Prerequisites for using SQL Server High Availability instance standby detection .

## Input Shape: EnableInstanceSqlHaStandbyDetectionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceIds | list[Any  # complex shape] | ✓ | The IDs of the instances to enable for SQL Server High Availability standby detection monitoring. |
| SqlServerCredentials | Any  # complex shape |  | The ARN of the Secrets Manager secret containing the SQL Server access credentials. The specified secret must contain va |

## Output Shape: EnableInstanceSqlHaStandbyDetectionsResult

- **Instances** (list[Any  # complex shape]): Information about the instances that were enabled for SQL Server High Availability standby detection monitoring.

## Implementation

```speclang
def enable_instance_sql_ha_standby_detections(store, request: dict) -> dict:
    """Enable Amazon EC2 instances running in an SQL Server High Availability cluster for SQL Server High Availability instance standby detection monitoring. Once enabled, Amazon Web Services monitors the me"""
    instance_ids = request.get("InstanceIds", "").strip() if isinstance(request.get("InstanceIds"), str) else request.get("InstanceIds")
    if not instance_ids:
        raise ValidationException("InstanceIds is required")

    resource = store.enable_instance_sql_ha_standby_detectionss(instance_ids)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_ids not found")

    # Update mutable fields
    if "SqlServerCredentials" in request:
        resource["SqlServerCredentials"] = sql_server_credentials
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_instance_sql_ha_standby_detectionss(instance_ids, resource)
    return resource
```
