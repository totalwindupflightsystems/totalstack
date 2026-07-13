---
id: "@specs/aws/ec2/create_capacity_reservation_fleet"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateCapacityReservationFleet"
---

# CreateCapacityReservationFleet

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_capacity_reservation_fleet
> **spec:implements:** @kind:operation CreateCapacityReservationFleet
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateCapacityReservationFleet.spec.md

Creates a Capacity Reservation Fleet. For more information, see Create a Capacity Reservation Fleet in the Amazon EC2 User Guide .

## Input Shape: CreateCapacityReservationFleetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationStrategy | str |  | The strategy used by the Capacity Reservation Fleet to determine which of the specified instance types to use. Currently |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EndDate | Any  # complex shape |  | The date and time at which the Capacity Reservation Fleet expires. When the Capacity Reservation Fleet expires, its stat |
| InstanceMatchCriteria | Any  # complex shape |  | Indicates the type of instance launches that the Capacity Reservation Fleet accepts. All Capacity Reservations in the Fl |
| InstanceTypeSpecifications | list[Any  # complex shape] | ✓ | Information about the instance types for which to reserve the capacity. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the Capacity Reservation Fleet. The tags are automatically assigned to the Capacity Reservations i |
| Tenancy | Any  # complex shape |  | Indicates the tenancy of the Capacity Reservation Fleet. All Capacity Reservations in the Fleet inherit this tenancy. Th |
| TotalTargetCapacity | int | ✓ | The total number of capacity units to be reserved by the Capacity Reservation Fleet. This value, together with the insta |

## Output Shape: CreateCapacityReservationFleetResult

- **AllocationStrategy** (str): The allocation strategy used by the Capacity Reservation Fleet.
- **CapacityReservationFleetId** (Any  # complex shape): The ID of the Capacity Reservation Fleet.
- **CreateTime** (Any  # complex shape): The date and time at which the Capacity Reservation Fleet was created.
- **EndDate** (Any  # complex shape): The date and time at which the Capacity Reservation Fleet expires.
- **FleetCapacityReservations** (Any  # complex shape): Information about the individual Capacity Reservations in the Capacity Reservation Fleet.
- **InstanceMatchCriteria** (Any  # complex shape): The instance matching criteria for the Capacity Reservation Fleet.
- **State** (Any  # complex shape): The status of the Capacity Reservation Fleet.
- **Tags** (list[Any  # complex shape]): The tags assigned to the Capacity Reservation Fleet.
- **Tenancy** (Any  # complex shape): Indicates the tenancy of Capacity Reservation Fleet.
- **TotalFulfilledCapacity** (float): The requested capacity units that have been successfully reserved.
- **TotalTargetCapacity** (int): The total number of capacity units for which the Capacity Reservation Fleet reserves capacity.

## Implementation

```speclang
def create_capacity_reservation_fleet(store, request: dict) -> dict:
    """Creates a Capacity Reservation Fleet. For more information, see Create a Capacity Reservation Fleet in the Amazon EC2 User Guide ."""
    instance_type_specifications = request.get("InstanceTypeSpecifications", "").strip() if isinstance(request.get("InstanceTypeSpecifications"), str) else request.get("InstanceTypeSpecifications")
    if not instance_type_specifications:
        raise ValidationException("InstanceTypeSpecifications is required")
    total_target_capacity = request.get("TotalTargetCapacity", "").strip() if isinstance(request.get("TotalTargetCapacity"), str) else request.get("TotalTargetCapacity")
    if not total_target_capacity:
        raise ValidationException("TotalTargetCapacity is required")

    if store.capacity_reservation_fleets(instance_type_specifications):
        raise ResourceInUseException(f"Resource instance_type_specifications already exists")

    record = {
        "AllocationStrategy": allocation_strategy,
        "ClientToken": client_token,
        "InstanceTypeSpecifications": instance_type_specifications,
        "Tenancy": tenancy,
        "TotalTargetCapacity": total_target_capacity,
        "EndDate": end_date,
        "InstanceMatchCriteria": instance_match_criteria,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.capacity_reservation_fleets(instance_type_specifications, record)

    return {
        "CapacityReservationFleetId": record.get("CapacityReservationFleetId", {}),
        "State": record.get("State", {}),
        "TotalTargetCapacity": record.get("TotalTargetCapacity", {}),
        "TotalFulfilledCapacity": record.get("TotalFulfilledCapacity", {}),
        "InstanceMatchCriteria": record.get("InstanceMatchCriteria", {}),
        "AllocationStrategy": record.get("AllocationStrategy", {}),
        "CreateTime": record.get("CreateTime", {}),
        "EndDate": record.get("EndDate", {}),
        "Tenancy": record.get("Tenancy", {}),
        "FleetCapacityReservations": record.get("FleetCapacityReservations", {}),
        "Tags": record.get("Tags", {}),
    }
```
