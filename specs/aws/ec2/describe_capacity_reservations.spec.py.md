---
id: "@specs/aws/ec2/describe_capacity_reservations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCapacityReservations"
---

# DescribeCapacityReservations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_capacity_reservations
> **spec:implements:** @kind:operation DescribeCapacityReservations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCapacityReservations.spec.md

Describes one or more of your Capacity Reservations. The results describe only the Capacity Reservations in the Amazon Web Services Region that you're currently using.

## Input Shape: DescribeCapacityReservationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationIds | Any  # complex shape |  | The ID of the Capacity Reservation. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. instance-type - The type of instance for which the Capacity Reservation reserves capacity. owner-id |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to use to retrieve the next page of results. |

## Output Shape: DescribeCapacityReservationsResult

- **CapacityReservations** (Any  # complex shape): Information about the Capacity Reservations.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_capacity_reservations(store, request: dict) -> dict:
    """Describes one or more of your Capacity Reservations. The results describe only the Capacity Reservations in the Amazon Web Services Region that you're currently using."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
