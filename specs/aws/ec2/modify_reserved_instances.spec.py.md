---
id: "@specs/aws/ec2/modify_reserved_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyReservedInstances"
---

# ModifyReservedInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_reserved_instances
> **spec:implements:** @kind:operation ModifyReservedInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyReservedInstances.spec.md

Modifies the configuration of your Reserved Instances, such as the Availability Zone, instance count, or instance type. The Reserved Instances to be modified must be identical, except for Availability Zone, network platform, and instance type. For more information, see Modify Reserved Instances in the Amazon EC2 User Guide .

## Input Shape: ModifyReservedInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive token you provide to ensure idempotency of your modification request. For more information, see |
| ReservedInstancesIds | list[Any  # complex shape] | ✓ | The IDs of the Reserved Instances to modify. |
| TargetConfigurations | list[Any  # complex shape] | ✓ | The configuration settings for the Reserved Instances to modify. |

## Output Shape: ModifyReservedInstancesResult

- **ReservedInstancesModificationId** (str): The ID for the modification.

## Implementation

```speclang
def modify_reserved_instances(store, request: dict) -> dict:
    """Modifies the configuration of your Reserved Instances, such as the Availability Zone, instance count, or instance type. The Reserved Instances to be modified must be identical, except for Availability"""
    reserved_instances_ids = request.get("ReservedInstancesIds", "").strip() if isinstance(request.get("ReservedInstancesIds"), str) else request.get("ReservedInstancesIds")
    if not reserved_instances_ids:
        raise ValidationException("ReservedInstancesIds is required")
    target_configurations = request.get("TargetConfigurations", "").strip() if isinstance(request.get("TargetConfigurations"), str) else request.get("TargetConfigurations")
    if not target_configurations:
        raise ValidationException("TargetConfigurations is required")

    resource = store.reserved_instancess(reserved_instances_ids)
    if not resource:
        raise ResourceNotFoundException(f"Resource reserved_instances_ids not found")

    # Update mutable fields
    if "ClientToken" in request:
        resource["ClientToken"] = client_token

    store.reserved_instancess(reserved_instances_ids, resource)
    return resource
```
