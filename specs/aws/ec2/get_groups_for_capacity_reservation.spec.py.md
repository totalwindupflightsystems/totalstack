---
id: "@specs/aws/ec2/get_groups_for_capacity_reservation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetGroupsForCapacityReservation"
---

# GetGroupsForCapacityReservation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_groups_for_capacity_reservation
> **spec:implements:** @kind:operation GetGroupsForCapacityReservation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetGroupsForCapacityReservation.spec.md

Lists the resource groups to which a Capacity Reservation has been added.

## Input Shape: GetGroupsForCapacityReservationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationId | Any  # complex shape | ✓ | The ID of the Capacity Reservation. If you specify a Capacity Reservation that is shared with you, the operation returns |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to use to retrieve the next page of results. |

## Output Shape: GetGroupsForCapacityReservationResult

- **CapacityReservationGroups** (Any  # complex shape): Information about the resource groups to which the Capacity Reservation has been added.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_groups_for_capacity_reservation(store, request: dict) -> dict:
    """Lists the resource groups to which a Capacity Reservation has been added."""
    capacity_reservation_id = request.get("CapacityReservationId", "").strip() if isinstance(request.get("CapacityReservationId"), str) else request.get("CapacityReservationId")
    if not capacity_reservation_id:
        raise ValidationException("CapacityReservationId is required")

    resource = store.groups_for_capacity_reservations(capacity_reservation_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource capacity_reservation_id not found")
    return {"CapacityReservationId": capacity_reservation_id, **resource}
```
