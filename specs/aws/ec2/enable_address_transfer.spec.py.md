---
id: "@specs/aws/ec2/enable_address_transfer"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableAddressTransfer"
---

# EnableAddressTransfer

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_address_transfer
> **spec:implements:** @kind:operation EnableAddressTransfer
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableAddressTransfer.spec.md

Enables Elastic IP address transfer. For more information, see Transfer Elastic IP addresses in the Amazon VPC User Guide .

## Input Shape: EnableAddressTransferRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationId | Any  # complex shape | ✓ | The allocation ID of an Elastic IP address. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransferAccountId | str | ✓ | The ID of the account that you want to transfer the Elastic IP address to. |

## Output Shape: EnableAddressTransferResult

- **AddressTransfer** (Any  # complex shape): An Elastic IP address transfer.

## Implementation

```speclang
def enable_address_transfer(store, request: dict) -> dict:
    """Enables Elastic IP address transfer. For more information, see Transfer Elastic IP addresses in the Amazon VPC User Guide ."""
    allocation_id = request.get("AllocationId", "").strip() if isinstance(request.get("AllocationId"), str) else request.get("AllocationId")
    if not allocation_id:
        raise ValidationException("AllocationId is required")
    transfer_account_id = request.get("TransferAccountId", "").strip() if isinstance(request.get("TransferAccountId"), str) else request.get("TransferAccountId")
    if not transfer_account_id:
        raise ValidationException("TransferAccountId is required")

    if store.enable_address_transfers(allocation_id):
        raise ResourceInUseException(f"Resource allocation_id already exists")

    record = {
        "AllocationId": allocation_id,
        "TransferAccountId": transfer_account_id,
        "DryRun": dry_run,
    }

    store.enable_address_transfers(allocation_id, record)

    return {
        "AddressTransfer": record.get("AddressTransfer", {}),
    }
```
