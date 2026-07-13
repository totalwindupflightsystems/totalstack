---
id: "@specs/aws/ec2/update_interruptible_capacity_reservation_allocation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_UpdateInterruptibleCapacityReservationAllocation"
---

# UpdateInterruptibleCapacityReservationAllocation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/update_interruptible_capacity_reservation_allocation
> **spec:implements:** @kind:operation UpdateInterruptibleCapacityReservationAllocation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_UpdateInterruptibleCapacityReservationAllocation.spec.md

Modifies the number of instances allocated to an interruptible reservation, allowing you to add more capacity or reclaim capacity to your source Capacity Reservation.

## Input Shape: UpdateInterruptibleCapacityReservationAllocationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationId | Any  # complex shape | ✓ | The ID of the source Capacity Reservation containing the interruptible allocation to modify. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TargetInstanceCount | int | ✓ | The new number of instances to allocate. Enter a higher number to add more capacity to share, or a lower number to recla |

## Output Shape: UpdateInterruptibleCapacityReservationAllocationResult

- **InstanceCount** (int): The current number of instances allocated to the interruptible reservation.
- **InterruptibleCapacityReservationId** (Any  # complex shape): The ID of the interruptible Capacity Reservation that was modified.
- **InterruptionType** (Any  # complex shape): The interruption type for the interruptible reservation.
- **SourceCapacityReservationId** (Any  # complex shape): The ID of the source Capacity Reservation to which capacity was reclaimed or from which capacity was allocated.
- **Status** (Any  # complex shape): The current status of the allocation (updating during reclamation, active when complete).
- **TargetInstanceCount** (int): The requested number of instances for the interruptible Capacity Reservation.

## Implementation

```speclang
def update_interruptible_capacity_reservation_allocation(store, request: dict) -> dict:
    """Modifies the number of instances allocated to an interruptible reservation, allowing you to add more capacity or reclaim capacity to your source Capacity Reservation."""
    capacity_reservation_id = request.get("CapacityReservationId", "").strip() if isinstance(request.get("CapacityReservationId"), str) else request.get("CapacityReservationId")
    if not capacity_reservation_id:
        raise ValidationException("CapacityReservationId is required")
    target_instance_count = request.get("TargetInstanceCount", "").strip() if isinstance(request.get("TargetInstanceCount"), str) else request.get("TargetInstanceCount")
    if not target_instance_count:
        raise ValidationException("TargetInstanceCount is required")

    resource = store.interruptible_capacity_reservation_allocations(capacity_reservation_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource capacity_reservation_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.interruptible_capacity_reservation_allocations(capacity_reservation_id, resource)
    return resource
```
