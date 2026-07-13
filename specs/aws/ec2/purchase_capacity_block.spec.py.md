---
id: "@specs/aws/ec2/purchase_capacity_block"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_PurchaseCapacityBlock"
---

# PurchaseCapacityBlock

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/purchase_capacity_block
> **spec:implements:** @kind:operation PurchaseCapacityBlock
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_PurchaseCapacityBlock.spec.md

Purchase the Capacity Block for use with your account. With Capacity Blocks you ensure GPU capacity is available for machine learning (ML) workloads. You must specify the ID of the Capacity Block offering you are purchasing.

## Input Shape: PurchaseCapacityBlockRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityBlockOfferingId | Any  # complex shape | ✓ | The ID of the Capacity Block offering. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstancePlatform | Any  # complex shape | ✓ | The type of operating system for which to reserve capacity. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the Capacity Block during launch. |

## Output Shape: PurchaseCapacityBlockResult

- **CapacityBlocks** (Any  # complex shape): The Capacity Block.
- **CapacityReservation** (Any  # complex shape): The Capacity Reservation.

## Implementation

```speclang
def purchase_capacity_block(store, request: dict) -> dict:
    """Purchase the Capacity Block for use with your account. With Capacity Blocks you ensure GPU capacity is available for machine learning (ML) workloads. You must specify the ID of the Capacity Block offe"""
    capacity_block_offering_id = request.get("CapacityBlockOfferingId", "").strip() if isinstance(request.get("CapacityBlockOfferingId"), str) else request.get("CapacityBlockOfferingId")
    if not capacity_block_offering_id:
        raise ValidationException("CapacityBlockOfferingId is required")
    instance_platform = request.get("InstancePlatform", "").strip() if isinstance(request.get("InstancePlatform"), str) else request.get("InstancePlatform")
    if not instance_platform:
        raise ValidationException("InstancePlatform is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("PurchaseCapacityBlock", request)
```
