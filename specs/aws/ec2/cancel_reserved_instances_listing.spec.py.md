---
id: "@specs/aws/ec2/cancel_reserved_instances_listing"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CancelReservedInstancesListing"
---

# CancelReservedInstancesListing

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/cancel_reserved_instances_listing
> **spec:implements:** @kind:operation CancelReservedInstancesListing
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CancelReservedInstancesListing.spec.md

Cancels the specified Reserved Instance listing in the Reserved Instance Marketplace. For more information, see Sell in the Reserved Instance Marketplace in the Amazon EC2 User Guide .

## Input Shape: CancelReservedInstancesListingRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ReservedInstancesListingId | Any  # complex shape | ✓ | The ID of the Reserved Instance listing. |

## Output Shape: CancelReservedInstancesListingResult

- **ReservedInstancesListings** (list[Any  # complex shape]): The Reserved Instance listing.

## Implementation

```speclang
def cancel_reserved_instances_listing(store, request: dict) -> dict:
    """Cancels the specified Reserved Instance listing in the Reserved Instance Marketplace. For more information, see Sell in the Reserved Instance Marketplace in the Amazon EC2 User Guide ."""
    reserved_instances_listing_id = request.get("ReservedInstancesListingId", "").strip() if isinstance(request.get("ReservedInstancesListingId"), str) else request.get("ReservedInstancesListingId")

    if not store.reserved_instances_listings(reserved_instances_listing_id):
        raise ResourceNotFoundException(f"Resource reserved_instances_listing_id not found")
    store.delete_reserved_instances_listings(reserved_instances_listing_id)
    return {}
```
