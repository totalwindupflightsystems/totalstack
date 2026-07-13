---
id: "@specs/aws/ec2/purchase_reserved_instances_offering"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_PurchaseReservedInstancesOffering"
---

# PurchaseReservedInstancesOffering

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/purchase_reserved_instances_offering
> **spec:implements:** @kind:operation PurchaseReservedInstancesOffering
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_PurchaseReservedInstancesOffering.spec.md

Purchases a Reserved Instance for use with your account. With Reserved Instances, you pay a lower hourly rate compared to On-Demand instance pricing. Use DescribeReservedInstancesOfferings to get a list of Reserved Instance offerings that match your specifications. After you've purchased a Reserved Instance, you can check for your new Reserved Instance with DescribeReservedInstances . To queue a purchase for a future date and time, specify a purchase time. If you do not specify a purchase time, the default is the current time. For more information, see Reserved Instances and Sell in the Reserved Instance Marketplace in the Amazon EC2 User Guide .

## Input Shape: PurchaseReservedInstancesOfferingRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceCount | int | ✓ | The number of Reserved Instances to purchase. |
| LimitPrice | Any  # complex shape |  | Specified for Reserved Instance Marketplace offerings to limit the total order and ensure that the Reserved Instances ar |
| PurchaseTime | Any  # complex shape |  | The time at which to purchase the Reserved Instance, in UTC format (for example, YYYY - MM - DD T HH : MM : SS Z). |
| ReservedInstancesOfferingId | Any  # complex shape | ✓ | The ID of the Reserved Instance offering to purchase. |

## Output Shape: PurchaseReservedInstancesOfferingResult

- **ReservedInstancesId** (str): The IDs of the purchased Reserved Instances. If your purchase crosses into a discounted pricing tier, the final Reserved

## Implementation

```speclang
def purchase_reserved_instances_offering(store, request: dict) -> dict:
    """Purchases a Reserved Instance for use with your account. With Reserved Instances, you pay a lower hourly rate compared to On-Demand instance pricing. Use DescribeReservedInstancesOfferings to get a li"""
    instance_count = request.get("InstanceCount", "").strip() if isinstance(request.get("InstanceCount"), str) else request.get("InstanceCount")
    if not instance_count:
        raise ValidationException("InstanceCount is required")
    reserved_instances_offering_id = request.get("ReservedInstancesOfferingId", "").strip() if isinstance(request.get("ReservedInstancesOfferingId"), str) else request.get("ReservedInstancesOfferingId")
    if not reserved_instances_offering_id:
        raise ValidationException("ReservedInstancesOfferingId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("PurchaseReservedInstancesOffering", request)
```
