---
id: "@specs/aws/ec2/describe_reserved_instances_listings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeReservedInstancesListings"
---

# DescribeReservedInstancesListings

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_reserved_instances_listings
> **spec:implements:** @kind:operation DescribeReservedInstancesListings
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeReservedInstancesListings.spec.md

Describes your account's Reserved Instance listings in the Reserved Instance Marketplace. The Reserved Instance Marketplace matches sellers who want to resell Reserved Instance capacity that they no longer need with buyers who want to purchase additional capacity. Reserved Instances bought and sold through the Reserved Instance Marketplace work like any other Reserved Instances. As a seller, you choose to list some or all of your Reserved Instances, and you specify the upfront price to receive for them. Your Reserved Instances are then listed in the Reserved Instance Marketplace and are available for purchase. As a buyer, you specify the configuration of the Reserved Instance to purchase, and the Marketplace matches what you're searching for with what's available. The Marketplace first sells the lowest priced Reserved Instances to you, and continues to sell available Reserved Instance listings to you until your demand is met. You are charged based on the total price of all of the listings that you purchase. For more information, see Sell in the Reserved Instance Marketplace in the Amazon EC2 User Guide . The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeReservedInstancesListingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Filters | list[Any  # complex shape] |  | One or more filters. reserved-instances-id - The ID of the Reserved Instances. reserved-instances-listing-id - The ID of |
| ReservedInstancesId | Any  # complex shape |  | One or more Reserved Instance IDs. |
| ReservedInstancesListingId | Any  # complex shape |  | One or more Reserved Instance listing IDs. |

## Output Shape: DescribeReservedInstancesListingsResult

- **ReservedInstancesListings** (list[Any  # complex shape]): Information about the Reserved Instance listing.

## Implementation

```speclang
def describe_reserved_instances_listings(store, request: dict) -> dict:
    """Describes your account's Reserved Instance listings in the Reserved Instance Marketplace. The Reserved Instance Marketplace matches sellers who want to resell Reserved Instance capacity that they no l"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
