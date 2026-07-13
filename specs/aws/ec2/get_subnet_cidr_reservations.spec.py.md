---
id: "@specs/aws/ec2/get_subnet_cidr_reservations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetSubnetCidrReservations"
---

# GetSubnetCidrReservations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_subnet_cidr_reservations
> **spec:implements:** @kind:operation GetSubnetCidrReservations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetSubnetCidrReservations.spec.md

Gets information about the subnet CIDR reservations.

## Input Shape: GetSubnetCidrReservationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. reservationType - The type of reservation ( prefix | explicit ). subnet-id - The ID of the subnet.  |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| SubnetId | Any  # complex shape | ✓ | The ID of the subnet. |

## Output Shape: GetSubnetCidrReservationsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **SubnetIpv4CidrReservations** (list[Any  # complex shape]): Information about the IPv4 subnet CIDR reservations.
- **SubnetIpv6CidrReservations** (list[Any  # complex shape]): Information about the IPv6 subnet CIDR reservations.

## Implementation

```speclang
def get_subnet_cidr_reservations(store, request: dict) -> dict:
    """Gets information about the subnet CIDR reservations."""
    subnet_id = request.get("SubnetId", "").strip() if isinstance(request.get("SubnetId"), str) else request.get("SubnetId")
    if not subnet_id:
        raise ValidationException("SubnetId is required")

    resource = store.subnet_cidr_reservationss(subnet_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource subnet_id not found")
    return {"SubnetId": subnet_id, **resource}
```
