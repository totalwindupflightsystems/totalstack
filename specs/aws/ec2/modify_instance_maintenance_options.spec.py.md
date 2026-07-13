---
id: "@specs/aws/ec2/modify_instance_maintenance_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyInstanceMaintenanceOptions"
---

# ModifyInstanceMaintenanceOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_instance_maintenance_options
> **spec:implements:** @kind:operation ModifyInstanceMaintenanceOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyInstanceMaintenanceOptions.spec.md

Modifies the recovery behavior of your instance to disable simplified automatic recovery or set the recovery behavior to default. The default configuration will not enable simplified automatic recovery for an unsupported instance type. For more information, see Simplified automatic recovery . Modifies the reboot migration behavior during a user-initiated reboot of an instance that has a pending system-reboot event. For more information, see Enable or disable reboot migration .

## Input Shape: ModifyInstanceMaintenanceOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AutoRecovery | Any  # complex shape |  | Disables the automatic recovery behavior of your instance or sets it to default. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |
| RebootMigration | Any  # complex shape |  | Specifies whether to attempt reboot migration during a user-initiated reboot of an instance that has a scheduled system- |

## Output Shape: ModifyInstanceMaintenanceOptionsResult

- **AutoRecovery** (Any  # complex shape): Provides information on the current automatic recovery behavior of your instance.
- **InstanceId** (str): The ID of the instance.
- **RebootMigration** (Any  # complex shape): Specifies whether to attempt reboot migration during a user-initiated reboot of an instance that has a scheduled system-

## Implementation

```speclang
def modify_instance_maintenance_options(store, request: dict) -> dict:
    """Modifies the recovery behavior of your instance to disable simplified automatic recovery or set the recovery behavior to default. The default configuration will not enable simplified automatic recover"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.instance_maintenance_optionss(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")

    # Update mutable fields
    if "AutoRecovery" in request:
        resource["AutoRecovery"] = auto_recovery
    if "RebootMigration" in request:
        resource["RebootMigration"] = reboot_migration
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.instance_maintenance_optionss(instance_id, resource)
    return resource
```
