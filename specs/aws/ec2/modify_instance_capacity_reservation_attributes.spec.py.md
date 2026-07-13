---
id: "@specs/aws/ec2/modify_instance_capacity_reservation_attributes"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyInstanceCapacityReservationAttributes"
---

# ModifyInstanceCapacityReservationAttributes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_instance_capacity_reservation_attributes
> **spec:implements:** @kind:operation ModifyInstanceCapacityReservationAttributes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyInstanceCapacityReservationAttributes.spec.md

Modifies the Capacity Reservation settings for a stopped instance. Use this action to configure an instance to target a specific Capacity Reservation, run in any open Capacity Reservation with matching attributes, run in On-Demand Instance capacity, or only run in a Capacity Reservation.

## Input Shape: ModifyInstanceCapacityReservationAttributesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationSpecification | Any  # complex shape | ✓ | Information about the Capacity Reservation targeting option. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance to be modified. |

## Output Shape: ModifyInstanceCapacityReservationAttributesResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def modify_instance_capacity_reservation_attributes(store, request: dict) -> dict:
    """Modifies the Capacity Reservation settings for a stopped instance. Use this action to configure an instance to target a specific Capacity Reservation, run in any open Capacity Reservation with matchin"""
    capacity_reservation_specification = request.get("CapacityReservationSpecification", "").strip() if isinstance(request.get("CapacityReservationSpecification"), str) else request.get("CapacityReservationSpecification")
    if not capacity_reservation_specification:
        raise ValidationException("CapacityReservationSpecification is required")
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.instance_capacity_reservation_attributess(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.instance_capacity_reservation_attributess(instance_id, resource)
    return resource
```
