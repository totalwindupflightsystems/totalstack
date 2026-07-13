---
id: "@specs/aws/ec2/describe_capacity_reservation_fleets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCapacityReservationFleets"
---

# DescribeCapacityReservationFleets

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_capacity_reservation_fleets
> **spec:implements:** @kind:operation DescribeCapacityReservationFleets
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCapacityReservationFleets.spec.md

Describes one or more Capacity Reservation Fleets.

## Input Shape: DescribeCapacityReservationFleetsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationFleetIds | Any  # complex shape |  | The IDs of the Capacity Reservation Fleets to describe. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. state - The state of the Fleet ( submitted | modifying | active | partially_fulfilled | expiring |  |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to use to retrieve the next page of results. |

## Output Shape: DescribeCapacityReservationFleetsResult

- **CapacityReservationFleets** (Any  # complex shape): Information about the Capacity Reservation Fleets.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_capacity_reservation_fleets(store, request: dict) -> dict:
    """Describes one or more Capacity Reservation Fleets."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
