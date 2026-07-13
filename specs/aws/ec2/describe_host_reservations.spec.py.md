---
id: "@specs/aws/ec2/describe_host_reservations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeHostReservations"
---

# DescribeHostReservations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_host_reservations
> **spec:implements:** @kind:operation DescribeHostReservations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeHostReservations.spec.md

Describes reservations that are associated with Dedicated Hosts in your account.

## Input Shape: DescribeHostReservationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Filter | list[Any  # complex shape] |  | The filters. instance-family - The instance family (for example, m4 ). payment-option - The payment option ( NoUpfront | |
| HostReservationIdSet | Any  # complex shape |  | The host reservation IDs. |
| MaxResults | int |  | The maximum number of results to return for the request in a single page. The remaining results can be seen by sending a |
| NextToken | str |  | The token to use to retrieve the next page of results. |

## Output Shape: DescribeHostReservationsResult

- **HostReservationSet** (Any  # complex shape): Details about the reservation's configuration.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_host_reservations(store, request: dict) -> dict:
    """Describes reservations that are associated with Dedicated Hosts in your account."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
