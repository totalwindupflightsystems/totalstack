---
id: "@specs/aws/ec2/move_capacity_reservation_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_MoveCapacityReservationInstances"
---

# MoveCapacityReservationInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/move_capacity_reservation_instances
> **spec:implements:** @kind:operation MoveCapacityReservationInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_MoveCapacityReservationInstances.spec.md

Move available capacity from a source Capacity Reservation to a destination Capacity Reservation. The source Capacity Reservation and the destination Capacity Reservation must be active , owned by your Amazon Web Services account, and share the following: Instance type Platform Availability Zone Tenancy Placement group Capacity Reservation end time - At specific time or Manually .

## Input Shape: MoveCapacityReservationInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DestinationCapacityReservationId | Any  # complex shape | ✓ | The ID of the Capacity Reservation that you want to move capacity into. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceCount | int | ✓ | The number of instances that you want to move from the source Capacity Reservation. |
| SourceCapacityReservationId | Any  # complex shape | ✓ | The ID of the Capacity Reservation from which you want to move capacity. |

## Output Shape: MoveCapacityReservationInstancesResult

- **DestinationCapacityReservation** (Any  # complex shape): Information about the destination Capacity Reservation.
- **InstanceCount** (int): The number of instances that were moved from the source Capacity Reservation to the destination Capacity Reservation.
- **SourceCapacityReservation** (Any  # complex shape): Information about the source Capacity Reservation.

## Implementation

```speclang
def move_capacity_reservation_instances(store, request: dict) -> dict:
    """Move available capacity from a source Capacity Reservation to a destination Capacity Reservation. The source Capacity Reservation and the destination Capacity Reservation must be active , owned by you"""
    destination_capacity_reservation_id = request.get("DestinationCapacityReservationId", "").strip() if isinstance(request.get("DestinationCapacityReservationId"), str) else request.get("DestinationCapacityReservationId")
    if not destination_capacity_reservation_id:
        raise ValidationException("DestinationCapacityReservationId is required")
    instance_count = request.get("InstanceCount", "").strip() if isinstance(request.get("InstanceCount"), str) else request.get("InstanceCount")
    if not instance_count:
        raise ValidationException("InstanceCount is required")
    source_capacity_reservation_id = request.get("SourceCapacityReservationId", "").strip() if isinstance(request.get("SourceCapacityReservationId"), str) else request.get("SourceCapacityReservationId")
    if not source_capacity_reservation_id:
        raise ValidationException("SourceCapacityReservationId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("MoveCapacityReservationInstances", request)
```
