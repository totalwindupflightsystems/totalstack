---
id: "@specs/aws/ec2/describe_capacity_block_extension_offerings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCapacityBlockExtensionOfferings"
---

# DescribeCapacityBlockExtensionOfferings

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_capacity_block_extension_offerings
> **spec:implements:** @kind:operation DescribeCapacityBlockExtensionOfferings
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCapacityBlockExtensionOfferings.spec.md

Describes Capacity Block extension offerings available for purchase in the Amazon Web Services Region that you're currently using.

## Input Shape: DescribeCapacityBlockExtensionOfferingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityBlockExtensionDurationHours | int | ✓ | The duration of the Capacity Block extension offering in hours. |
| CapacityReservationId | Any  # complex shape | ✓ | The ID of the Capacity reservation to be extended. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to use to retrieve the next page of results. |

## Output Shape: DescribeCapacityBlockExtensionOfferingsResult

- **CapacityBlockExtensionOfferings** (Any  # complex shape): The recommended Capacity Block extension offerings for the dates specified.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_capacity_block_extension_offerings(store, request: dict) -> dict:
    """Describes Capacity Block extension offerings available for purchase in the Amazon Web Services Region that you're currently using."""
    capacity_block_extension_duration_hours = request.get("CapacityBlockExtensionDurationHours", "").strip() if isinstance(request.get("CapacityBlockExtensionDurationHours"), str) else request.get("CapacityBlockExtensionDurationHours")
    if not capacity_block_extension_duration_hours:
        raise ValidationException("CapacityBlockExtensionDurationHours is required")
    capacity_reservation_id = request.get("CapacityReservationId", "").strip() if isinstance(request.get("CapacityReservationId"), str) else request.get("CapacityReservationId")
    if not capacity_reservation_id:
        raise ValidationException("CapacityReservationId is required")

    resource = store.capacity_block_extension_offeringss(capacity_reservation_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource capacity_reservation_id not found")
    return {"CapacityReservationId": capacity_reservation_id, **resource}
```
