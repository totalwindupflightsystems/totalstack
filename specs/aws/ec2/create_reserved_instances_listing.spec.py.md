---
id: "@specs/aws/ec2/create_reserved_instances_listing"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateReservedInstancesListing"
---

# CreateReservedInstancesListing

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_reserved_instances_listing
> **spec:implements:** @kind:operation CreateReservedInstancesListing
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateReservedInstancesListing.spec.md

Creates a listing for Amazon EC2 Standard Reserved Instances to be sold in the Reserved Instance Marketplace. You can submit one Standard Reserved Instance listing at a time. To get a list of your Standard Reserved Instances, you can use the DescribeReservedInstances operation. Only Standard Reserved Instances can be sold in the Reserved Instance Marketplace. Convertible Reserved Instances cannot be sold. The Reserved Instance Marketplace matches sellers who want to resell Standard Reserved Instance capacity that they no longer need with buyers who want to purchase additional capacity. Reserved Instances bought and sold through the Reserved Instance Marketplace work like any other Reserved Instances. To sell your Standard Reserved Instances, you must first register as a seller in the Reserved Instance Marketplace. After completing the registration process, you can create a Reserved Instance Marketplace listing of some or all of your Standard Reserved Instances, and specify the upfront price to receive for them. Your Standard Reserved Instance listings then become available for purchase. To view the details of your Standard Reserved Instance listing, you can use the DescribeReservedInstancesListings operation. For more information, see Sell in the Reserved Instance Marketplace in the Amazon EC2 User Guide .

## Input Shape: CreateReservedInstancesListingRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str | ✓ | Unique, case-sensitive identifier you provide to ensure idempotency of your listings. This helps avoid duplicate listing |
| InstanceCount | int | ✓ | The number of instances that are a part of a Reserved Instance account to be listed in the Reserved Instance Marketplace |
| PriceSchedules | list[Any  # complex shape] | ✓ | A list specifying the price of the Standard Reserved Instance for each month remaining in the Reserved Instance term. |
| ReservedInstancesId | Any  # complex shape | ✓ | The ID of the active Standard Reserved Instance. |

## Output Shape: CreateReservedInstancesListingResult

- **ReservedInstancesListings** (list[Any  # complex shape]): Information about the Standard Reserved Instance listing.

## Implementation

```speclang
def create_reserved_instances_listing(store, request: dict) -> dict:
    """Creates a listing for Amazon EC2 Standard Reserved Instances to be sold in the Reserved Instance Marketplace. You can submit one Standard Reserved Instance listing at a time. To get a list of your Sta"""
    client_token = request.get("ClientToken", "").strip() if isinstance(request.get("ClientToken"), str) else request.get("ClientToken")
    if not client_token:
        raise ValidationException("ClientToken is required")
    instance_count = request.get("InstanceCount", "").strip() if isinstance(request.get("InstanceCount"), str) else request.get("InstanceCount")
    if not instance_count:
        raise ValidationException("InstanceCount is required")
    price_schedules = request.get("PriceSchedules", "").strip() if isinstance(request.get("PriceSchedules"), str) else request.get("PriceSchedules")
    if not price_schedules:
        raise ValidationException("PriceSchedules is required")
    reserved_instances_id = request.get("ReservedInstancesId", "").strip() if isinstance(request.get("ReservedInstancesId"), str) else request.get("ReservedInstancesId")
    if not reserved_instances_id:
        raise ValidationException("ReservedInstancesId is required")

    if store.reserved_instances_listings(reserved_instances_id):
        raise ResourceInUseException(f"Resource reserved_instances_id already exists")

    record = {
        "ReservedInstancesId": reserved_instances_id,
        "InstanceCount": instance_count,
        "PriceSchedules": price_schedules,
        "ClientToken": client_token,
    }

    store.reserved_instances_listings(reserved_instances_id, record)

    return {
        "ReservedInstancesListings": record.get("ReservedInstancesListings", {}),
    }
```
