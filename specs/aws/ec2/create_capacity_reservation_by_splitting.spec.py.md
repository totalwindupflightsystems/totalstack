---
id: "@specs/aws/ec2/create_capacity_reservation_by_splitting"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateCapacityReservationBySplitting"
---

# CreateCapacityReservationBySplitting

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_capacity_reservation_by_splitting
> **spec:implements:** @kind:operation CreateCapacityReservationBySplitting
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateCapacityReservationBySplitting.spec.md

Create a new Capacity Reservation by splitting the capacity of the source Capacity Reservation. The new Capacity Reservation will have the same attributes as the source Capacity Reservation except for tags. The source Capacity Reservation must be active and owned by your Amazon Web Services account.

## Input Shape: CreateCapacityReservationBySplittingRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceCount | int | ✓ | The number of instances to split from the source Capacity Reservation. |
| SourceCapacityReservationId | Any  # complex shape | ✓ | The ID of the Capacity Reservation from which you want to split the capacity. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the new Capacity Reservation. |

## Output Shape: CreateCapacityReservationBySplittingResult

- **DestinationCapacityReservation** (Any  # complex shape): Information about the destination Capacity Reservation.
- **InstanceCount** (int): The number of instances in the new Capacity Reservation. The number of instances in the source Capacity Reservation was 
- **SourceCapacityReservation** (Any  # complex shape): Information about the source Capacity Reservation.

## Implementation

```speclang
def create_capacity_reservation_by_splitting(store, request: dict) -> dict:
    """Create a new Capacity Reservation by splitting the capacity of the source Capacity Reservation. The new Capacity Reservation will have the same attributes as the source Capacity Reservation except for"""
    instance_count = request.get("InstanceCount", "").strip() if isinstance(request.get("InstanceCount"), str) else request.get("InstanceCount")
    if not instance_count:
        raise ValidationException("InstanceCount is required")
    source_capacity_reservation_id = request.get("SourceCapacityReservationId", "").strip() if isinstance(request.get("SourceCapacityReservationId"), str) else request.get("SourceCapacityReservationId")
    if not source_capacity_reservation_id:
        raise ValidationException("SourceCapacityReservationId is required")

    if store.capacity_reservation_by_splittings(source_capacity_reservation_id):
        raise ResourceInUseException(f"Resource source_capacity_reservation_id already exists")

    record = {
        "DryRun": dry_run,
        "ClientToken": client_token,
        "SourceCapacityReservationId": source_capacity_reservation_id,
        "InstanceCount": instance_count,
        "TagSpecifications": tag_specifications,
    }

    store.capacity_reservation_by_splittings(source_capacity_reservation_id, record)

    return {
        "SourceCapacityReservation": record.get("SourceCapacityReservation", {}),
        "DestinationCapacityReservation": record.get("DestinationCapacityReservation", {}),
        "InstanceCount": record.get("InstanceCount", {}),
    }
```
