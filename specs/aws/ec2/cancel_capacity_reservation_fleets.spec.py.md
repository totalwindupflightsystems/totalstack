---
id: "@specs/aws/ec2/cancel_capacity_reservation_fleets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CancelCapacityReservationFleets"
---

# CancelCapacityReservationFleets

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/cancel_capacity_reservation_fleets
> **spec:implements:** @kind:operation CancelCapacityReservationFleets
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CancelCapacityReservationFleets.spec.md

Cancels one or more Capacity Reservation Fleets. When you cancel a Capacity Reservation Fleet, the following happens: The Capacity Reservation Fleet's status changes to cancelled . The individual Capacity Reservations in the Fleet are cancelled. Instances running in the Capacity Reservations at the time of cancelling the Fleet continue to run in shared capacity. The Fleet stops creating new Capacity Reservations.

## Input Shape: CancelCapacityReservationFleetsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationFleetIds | Any  # complex shape | ✓ | The IDs of the Capacity Reservation Fleets to cancel. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: CancelCapacityReservationFleetsResult

- **FailedFleetCancellations** (Any  # complex shape): Information about the Capacity Reservation Fleets that could not be cancelled.
- **SuccessfulFleetCancellations** (Any  # complex shape): Information about the Capacity Reservation Fleets that were successfully cancelled.

## Implementation

```speclang
def cancel_capacity_reservation_fleets(store, request: dict) -> dict:
    """Cancels one or more Capacity Reservation Fleets. When you cancel a Capacity Reservation Fleet, the following happens: The Capacity Reservation Fleet's status changes to cancelled . The individual Capa"""
    capacity_reservation_fleet_ids = request.get("CapacityReservationFleetIds", "").strip() if isinstance(request.get("CapacityReservationFleetIds"), str) else request.get("CapacityReservationFleetIds")

    if not store.capacity_reservation_fleetss(capacity_reservation_fleet_ids):
        raise ResourceNotFoundException(f"Resource capacity_reservation_fleet_ids not found")
    store.delete_capacity_reservation_fleetss(capacity_reservation_fleet_ids)
    return {}
```
