---
id: "@specs/aws/ec2/purchase_capacity_block_extension"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_PurchaseCapacityBlockExtension"
---

# PurchaseCapacityBlockExtension

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/purchase_capacity_block_extension
> **spec:implements:** @kind:operation PurchaseCapacityBlockExtension
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_PurchaseCapacityBlockExtension.spec.md

Purchase the Capacity Block extension for use with your account. You must specify the ID of the Capacity Block extension offering you are purchasing.

## Input Shape: PurchaseCapacityBlockExtensionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityBlockExtensionOfferingId | Any  # complex shape | ✓ | The ID of the Capacity Block extension offering to purchase. |
| CapacityReservationId | Any  # complex shape | ✓ | The ID of the Capacity reservation to be extended. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: PurchaseCapacityBlockExtensionResult

- **CapacityBlockExtensions** (Any  # complex shape): The purchased Capacity Block extensions.

## Implementation

```speclang
def purchase_capacity_block_extension(store, request: dict) -> dict:
    """Purchase the Capacity Block extension for use with your account. You must specify the ID of the Capacity Block extension offering you are purchasing."""
    capacity_block_extension_offering_id = request.get("CapacityBlockExtensionOfferingId", "").strip() if isinstance(request.get("CapacityBlockExtensionOfferingId"), str) else request.get("CapacityBlockExtensionOfferingId")
    if not capacity_block_extension_offering_id:
        raise ValidationException("CapacityBlockExtensionOfferingId is required")
    capacity_reservation_id = request.get("CapacityReservationId", "").strip() if isinstance(request.get("CapacityReservationId"), str) else request.get("CapacityReservationId")
    if not capacity_reservation_id:
        raise ValidationException("CapacityReservationId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("PurchaseCapacityBlockExtension", request)
```
