---
id: "@specs/aws/ec2/create_interruptible_capacity_reservation_allocation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateInterruptibleCapacityReservationAllocation"
---

# CreateInterruptibleCapacityReservationAllocation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_interruptible_capacity_reservation_allocation
> **spec:implements:** @kind:operation CreateInterruptibleCapacityReservationAllocation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateInterruptibleCapacityReservationAllocation.spec.md

Creates an interruptible Capacity Reservation by specifying the number of unused instances you want to allocate from your source reservation. This helps you make unused capacity available for other workloads within your account while maintaining control to reclaim it.

## Input Shape: CreateInterruptibleCapacityReservationAllocationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationId | Any  # complex shape | ✓ | The ID of the source Capacity Reservation from which to create the interruptible Capacity Reservation. Your Capacity Res |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceCount | int | ✓ | The number of instances to allocate from your source reservation. You can only allocate available instances (also called |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the interruptible Capacity Reservation during creation. |

## Output Shape: CreateInterruptibleCapacityReservationAllocationResult

- **InterruptionType** (Any  # complex shape): The type of interruption applied to the interruptible reservation.
- **SourceCapacityReservationId** (Any  # complex shape): The ID of the source Capacity Reservation from which the interruptible Capacity Reservation was created.
- **Status** (Any  # complex shape): The current status of the allocation request (creating, active, updating).
- **TargetInstanceCount** (int): The number of instances allocated to the interruptible reservation.

## Implementation

```speclang
def create_interruptible_capacity_reservation_allocation(store, request: dict) -> dict:
    """Creates an interruptible Capacity Reservation by specifying the number of unused instances you want to allocate from your source reservation. This helps you make unused capacity available for other wo"""
    capacity_reservation_id = request.get("CapacityReservationId", "").strip() if isinstance(request.get("CapacityReservationId"), str) else request.get("CapacityReservationId")
    if not capacity_reservation_id:
        raise ValidationException("CapacityReservationId is required")
    instance_count = request.get("InstanceCount", "").strip() if isinstance(request.get("InstanceCount"), str) else request.get("InstanceCount")
    if not instance_count:
        raise ValidationException("InstanceCount is required")

    if store.interruptible_capacity_reservation_allocations(capacity_reservation_id):
        raise ResourceInUseException(f"Resource capacity_reservation_id already exists")

    record = {
        "CapacityReservationId": capacity_reservation_id,
        "InstanceCount": instance_count,
        "ClientToken": client_token,
        "DryRun": dry_run,
        "TagSpecifications": tag_specifications,
    }

    store.interruptible_capacity_reservation_allocations(capacity_reservation_id, record)

    return {
        "SourceCapacityReservationId": record.get("SourceCapacityReservationId", {}),
        "TargetInstanceCount": record.get("TargetInstanceCount", {}),
        "Status": record.get("Status", {}),
        "InterruptionType": record.get("InterruptionType", {}),
    }
```
