---
id: "@specs/aws/ec2/cancel_capacity_reservation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CancelCapacityReservation"
---

# CancelCapacityReservation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/cancel_capacity_reservation
> **spec:implements:** @kind:operation CancelCapacityReservation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CancelCapacityReservation.spec.md

Cancels the specified Capacity Reservation, releases the reserved capacity, and changes the Capacity Reservation's state to cancelled . You can cancel a Capacity Reservation that is in the following states: assessing active and there is no commitment duration or the commitment duration has elapsed. You can't cancel a future-dated Capacity Reservation during the commitment duration. You can't modify or cancel a Capacity Block. For more information, see Capacity Blocks for ML . If a future-dated Capacity Reservation enters the delayed state, the commitment duration is waived, and you can cancel it as soon as it enters the active state. Instances running in the reserved capacity continue running until you stop them. Stopped instances that target the Capacity Reservation can no longer launch. Modify these instances to either target a different Capacity Reservation, launch On-Demand Instance capacity, or run in any open Capacity Reservation that has matching attributes and sufficient capacity.

## Input Shape: CancelCapacityReservationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationId | Any  # complex shape | ✓ | The ID of the Capacity Reservation to be cancelled. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: CancelCapacityReservationResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def cancel_capacity_reservation(store, request: dict) -> dict:
    """Cancels the specified Capacity Reservation, releases the reserved capacity, and changes the Capacity Reservation's state to cancelled . You can cancel a Capacity Reservation that is in the following s"""
    capacity_reservation_id = request.get("CapacityReservationId", "").strip() if isinstance(request.get("CapacityReservationId"), str) else request.get("CapacityReservationId")

    if not store.capacity_reservations(capacity_reservation_id):
        raise ResourceNotFoundException(f"Resource capacity_reservation_id not found")
    store.delete_capacity_reservations(capacity_reservation_id)
    return {}
```
