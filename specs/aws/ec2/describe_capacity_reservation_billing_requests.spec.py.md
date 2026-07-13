---
id: "@specs/aws/ec2/describe_capacity_reservation_billing_requests"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCapacityReservationBillingRequests"
---

# DescribeCapacityReservationBillingRequests

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_capacity_reservation_billing_requests
> **spec:implements:** @kind:operation DescribeCapacityReservationBillingRequests
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCapacityReservationBillingRequests.spec.md

Describes a request to assign the billing of the unused capacity of a Capacity Reservation. For more information, see Billing assignment for shared Amazon EC2 Capacity Reservations .

## Input Shape: DescribeCapacityReservationBillingRequestsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationIds | Any  # complex shape |  | The ID of the Capacity Reservation. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. status - The state of the request ( pending | accepted | rejected | cancelled | revoked | expired ) |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to use to retrieve the next page of results. |
| Role | Any  # complex shape | ✓ | Specify one of the following: odcr-owner - If you are the Capacity Reservation owner, specify this value to view request |

## Output Shape: DescribeCapacityReservationBillingRequestsResult

- **CapacityReservationBillingRequests** (Any  # complex shape): Information about the request.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_capacity_reservation_billing_requests(store, request: dict) -> dict:
    """Describes a request to assign the billing of the unused capacity of a Capacity Reservation. For more information, see Billing assignment for shared Amazon EC2 Capacity Reservations ."""
    role = request.get("Role", "").strip() if isinstance(request.get("Role"), str) else request.get("Role")
    if not role:
        raise ValidationException("Role is required")

    resource = store.capacity_reservation_billing_requestss(role)
    if not resource:
        raise ResourceNotFoundException(f"Resource role not found")
    return {"Role": role, **resource}
```
