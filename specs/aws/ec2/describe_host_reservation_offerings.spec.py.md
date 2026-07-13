---
id: "@specs/aws/ec2/describe_host_reservation_offerings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeHostReservationOfferings"
---

# DescribeHostReservationOfferings

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_host_reservation_offerings
> **spec:implements:** @kind:operation DescribeHostReservationOfferings
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeHostReservationOfferings.spec.md

Describes the Dedicated Host reservations that are available to purchase. The results describe all of the Dedicated Host reservation offerings, including offerings that might not match the instance family and Region of your Dedicated Hosts. When purchasing an offering, ensure that the instance family and Region of the offering matches that of the Dedicated Hosts with which it is to be associated. For more information about supported instance types, see Dedicated Hosts in the Amazon EC2 User Guide .

## Input Shape: DescribeHostReservationOfferingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Filter | list[Any  # complex shape] |  | The filters. instance-family - The instance family of the offering (for example, m4 ). payment-option - The payment opti |
| MaxDuration | int |  | This is the maximum duration of the reservation to purchase, specified in seconds. Reservations are available in one-yea |
| MaxResults | Any  # complex shape |  | The maximum number of results to return for the request in a single page. The remaining results can be seen by sending a |
| MinDuration | int |  | This is the minimum duration of the reservation you'd like to purchase, specified in seconds. Reservations are available |
| NextToken | str |  | The token to use to retrieve the next page of results. |
| OfferingId | Any  # complex shape |  | The ID of the reservation offering. |

## Output Shape: DescribeHostReservationOfferingsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **OfferingSet** (Any  # complex shape): Information about the offerings.

## Implementation

```speclang
def describe_host_reservation_offerings(store, request: dict) -> dict:
    """Describes the Dedicated Host reservations that are available to purchase. The results describe all of the Dedicated Host reservation offerings, including offerings that might not match the instance fa"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
