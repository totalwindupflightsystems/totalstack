---
id: "@specs/aws/ec2/accept_address_transfer"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AcceptAddressTransfer"
---

# AcceptAddressTransfer

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/accept_address_transfer
> **spec:implements:** @kind:operation AcceptAddressTransfer
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AcceptAddressTransfer.spec.md

Accepts an Elastic IP address transfer. For more information, see Accept a transferred Elastic IP address in the Amazon VPC User Guide .

## Input Shape: AcceptAddressTransferRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Address | str | ✓ | The Elastic IP address you are accepting for transfer. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | tag :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag |

## Output Shape: AcceptAddressTransferResult

- **AddressTransfer** (Any  # complex shape): An Elastic IP address transfer.

## Implementation

```speclang
def accept_address_transfer(store, request: dict) -> dict:
    """Accepts an Elastic IP address transfer. For more information, see Accept a transferred Elastic IP address in the Amazon VPC User Guide ."""
    address = request.get("Address", "").strip() if isinstance(request.get("Address"), str) else request.get("Address")
    if not address:
        raise ValidationException("Address is required")

    if store.accept_address_transfers(address):
        raise ResourceInUseException(f"Resource address already exists")

    record = {
        "Address": address,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.accept_address_transfers(address, record)

    return {
        "AddressTransfer": record.get("AddressTransfer", {}),
    }
```
