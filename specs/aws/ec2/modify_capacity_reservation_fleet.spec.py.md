---
id: "@specs/aws/ec2/modify_capacity_reservation_fleet"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyCapacityReservationFleet"
---

# ModifyCapacityReservationFleet

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_capacity_reservation_fleet
> **spec:implements:** @kind:operation ModifyCapacityReservationFleet
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyCapacityReservationFleet.spec.md

Modifies a Capacity Reservation Fleet. When you modify the total target capacity of a Capacity Reservation Fleet, the Fleet automatically creates new Capacity Reservations, or modifies or cancels existing Capacity Reservations in the Fleet to meet the new total target capacity. When you modify the end date for the Fleet, the end dates for all of the individual Capacity Reservations in the Fleet are updated accordingly.

## Input Shape: ModifyCapacityReservationFleetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationFleetId | Any  # complex shape | ✓ | The ID of the Capacity Reservation Fleet to modify. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EndDate | Any  # complex shape |  | The date and time at which the Capacity Reservation Fleet expires. When the Capacity Reservation Fleet expires, its stat |
| RemoveEndDate | bool |  | Indicates whether to remove the end date from the Capacity Reservation Fleet. If you remove the end date, the Capacity R |
| TotalTargetCapacity | int |  | The total number of capacity units to be reserved by the Capacity Reservation Fleet. This value, together with the insta |

## Output Shape: ModifyCapacityReservationFleetResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def modify_capacity_reservation_fleet(store, request: dict) -> dict:
    """Modifies a Capacity Reservation Fleet. When you modify the total target capacity of a Capacity Reservation Fleet, the Fleet automatically creates new Capacity Reservations, or modifies or cancels exis"""
    capacity_reservation_fleet_id = request.get("CapacityReservationFleetId", "").strip() if isinstance(request.get("CapacityReservationFleetId"), str) else request.get("CapacityReservationFleetId")
    if not capacity_reservation_fleet_id:
        raise ValidationException("CapacityReservationFleetId is required")

    resource = store.capacity_reservation_fleets(capacity_reservation_fleet_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource capacity_reservation_fleet_id not found")

    # Update mutable fields
    if "TotalTargetCapacity" in request:
        resource["TotalTargetCapacity"] = total_target_capacity
    if "EndDate" in request:
        resource["EndDate"] = end_date
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "RemoveEndDate" in request:
        resource["RemoveEndDate"] = remove_end_date

    store.capacity_reservation_fleets(capacity_reservation_fleet_id, resource)
    return resource
```
