---
id: "@specs/aws/ec2/get_capacity_reservation_usage"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetCapacityReservationUsage"
---

# GetCapacityReservationUsage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_capacity_reservation_usage
> **spec:implements:** @kind:operation GetCapacityReservationUsage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetCapacityReservationUsage.spec.md

Gets usage information about a Capacity Reservation. If the Capacity Reservation is shared, it shows usage information for the Capacity Reservation owner and each Amazon Web Services account that is currently using the shared capacity. If the Capacity Reservation is not shared, it shows only the Capacity Reservation owner's usage.

## Input Shape: GetCapacityReservationUsageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationId | Any  # complex shape | ✓ | The ID of the Capacity Reservation. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to use to retrieve the next page of results. |

## Output Shape: GetCapacityReservationUsageResult

- **AvailableInstanceCount** (int): The remaining capacity. Indicates the number of instances that can be launched in the Capacity Reservation.
- **CapacityReservationId** (str): The ID of the Capacity Reservation.
- **InstanceType** (str): The type of instance for which the Capacity Reservation reserves capacity.
- **InstanceUsages** (Any  # complex shape): Information about the Capacity Reservation usage.
- **Interruptible** (bool): Indicates whether the Capacity Reservation is interruptible, meaning instances may be terminated when the owner reclaims
- **InterruptibleCapacityAllocation** (Any  # complex shape): Information about the capacity allocated to the interruptible Capacity Reservation, including instance counts and alloca
- **InterruptionInfo** (Any  # complex shape): Details about the interruption configuration and source reservation for interruptible Capacity Reservations.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **State** (Any  # complex shape): The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states: active - Th
- **TotalInstanceCount** (int): The number of instances for which the Capacity Reservation reserves capacity.

## Implementation

```speclang
def get_capacity_reservation_usage(store, request: dict) -> dict:
    """Gets usage information about a Capacity Reservation. If the Capacity Reservation is shared, it shows usage information for the Capacity Reservation owner and each Amazon Web Services account that is c"""
    capacity_reservation_id = request.get("CapacityReservationId", "").strip() if isinstance(request.get("CapacityReservationId"), str) else request.get("CapacityReservationId")
    if not capacity_reservation_id:
        raise ValidationException("CapacityReservationId is required")

    resource = store.capacity_reservation_usages(capacity_reservation_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource capacity_reservation_id not found")
    return {"CapacityReservationId": capacity_reservation_id, **resource}
```
