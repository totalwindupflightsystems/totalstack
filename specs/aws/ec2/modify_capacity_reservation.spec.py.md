---
id: "@specs/aws/ec2/modify_capacity_reservation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyCapacityReservation"
---

# ModifyCapacityReservation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_capacity_reservation
> **spec:implements:** @kind:operation ModifyCapacityReservation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyCapacityReservation.spec.md

Modifies a Capacity Reservation's capacity, instance eligibility, and the conditions under which it is to be released. You can't modify a Capacity Reservation's instance type, EBS optimization, platform, instance store settings, Availability Zone, or tenancy. If you need to modify any of these attributes, we recommend that you cancel the Capacity Reservation, and then create a new one with the required attributes. For more information, see Modify an active Capacity Reservation . The allowed modifications depend on the state of the Capacity Reservation: assessing or scheduled state - You can modify the tags only. pending state - You can't modify the Capacity Reservation in any way. active state but still within the commitment duration - You can't decrease the instance count or set an end date that is within the commitment duration. All other modifications are allowed. active state with no commitment duration or elapsed commitment duration - All modifications are allowed. expired , cancelled , unsupported , or failed state - You can't modify the Capacity Reservation in any way.

## Input Shape: ModifyCapacityReservationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Accept | bool |  | Reserved. Capacity Reservations you have created are accepted by default. |
| AdditionalInfo | str |  | Reserved for future use. |
| CapacityReservationId | Any  # complex shape | ✓ | The ID of the Capacity Reservation. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EndDate | Any  # complex shape |  | The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity  |
| EndDateType | Any  # complex shape |  | Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types |
| InstanceCount | int |  | The number of instances for which to reserve capacity. The number of instances can't be increased or decreased by more t |
| InstanceMatchCriteria | Any  # complex shape |  | The matching criteria (instance eligibility) that you want to use in the modified Capacity Reservation. If you change th |

## Output Shape: ModifyCapacityReservationResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def modify_capacity_reservation(store, request: dict) -> dict:
    """Modifies a Capacity Reservation's capacity, instance eligibility, and the conditions under which it is to be released. You can't modify a Capacity Reservation's instance type, EBS optimization, platfo"""
    capacity_reservation_id = request.get("CapacityReservationId", "").strip() if isinstance(request.get("CapacityReservationId"), str) else request.get("CapacityReservationId")
    if not capacity_reservation_id:
        raise ValidationException("CapacityReservationId is required")

    resource = store.capacity_reservations(capacity_reservation_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource capacity_reservation_id not found")

    # Update mutable fields
    if "InstanceCount" in request:
        resource["InstanceCount"] = instance_count
    if "EndDate" in request:
        resource["EndDate"] = end_date
    if "EndDateType" in request:
        resource["EndDateType"] = end_date_type
    if "Accept" in request:
        resource["Accept"] = accept
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "AdditionalInfo" in request:
        resource["AdditionalInfo"] = additional_info
    if "InstanceMatchCriteria" in request:
        resource["InstanceMatchCriteria"] = instance_match_criteria

    store.capacity_reservations(capacity_reservation_id, resource)
    return resource
```
