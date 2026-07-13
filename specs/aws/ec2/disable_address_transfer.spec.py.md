---
id: "@specs/aws/ec2/disable_address_transfer"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableAddressTransfer"
---

# DisableAddressTransfer

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_address_transfer
> **spec:implements:** @kind:operation DisableAddressTransfer
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableAddressTransfer.spec.md

Disables Elastic IP address transfer. For more information, see Transfer Elastic IP addresses in the Amazon VPC User Guide .

## Input Shape: DisableAddressTransferRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationId | Any  # complex shape | ✓ | The allocation ID of an Elastic IP address. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DisableAddressTransferResult

- **AddressTransfer** (Any  # complex shape): An Elastic IP address transfer.

## Implementation

```speclang
def disable_address_transfer(store, request: dict) -> dict:
    """Disables Elastic IP address transfer. For more information, see Transfer Elastic IP addresses in the Amazon VPC User Guide ."""
    allocation_id = request.get("AllocationId", "").strip() if isinstance(request.get("AllocationId"), str) else request.get("AllocationId")
    if not allocation_id:
        raise ValidationException("AllocationId is required")

    if store.disable_address_transfers(allocation_id):
        raise ResourceInUseException(f"Resource allocation_id already exists")

    record = {
        "AllocationId": allocation_id,
        "DryRun": dry_run,
    }

    store.disable_address_transfers(allocation_id, record)

    return {
        "AddressTransfer": record.get("AddressTransfer", {}),
    }
```
