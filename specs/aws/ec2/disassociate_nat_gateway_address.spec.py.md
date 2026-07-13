---
id: "@specs/aws/ec2/disassociate_nat_gateway_address"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateNatGatewayAddress"
---

# DisassociateNatGatewayAddress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_nat_gateway_address
> **spec:implements:** @kind:operation DisassociateNatGatewayAddress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateNatGatewayAddress.spec.md

Disassociates secondary Elastic IP addresses (EIPs) from a public NAT gateway. You cannot disassociate your primary EIP. For more information, see Edit secondary IP address associations in the Amazon VPC User Guide . While disassociating is in progress, you cannot associate/disassociate additional EIPs while the connections are being drained. You are, however, allowed to delete the NAT gateway. An EIP is released only at the end of MaxDrainDurationSeconds. It stays associated and supports the existing connections but does not support any new connections (new connections are distributed across the remaining associated EIPs). As the existing connections drain out, the EIPs (and the corresponding private IP addresses mapped to them) are released.

## Input Shape: DisassociateNatGatewayAddressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationIds | list[Any  # complex shape] | ✓ | The association IDs of EIPs that have been associated with the NAT gateway. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxDrainDurationSeconds | Any  # complex shape |  | The maximum amount of time to wait (in seconds) before forcibly releasing the IP addresses if connections are still in p |
| NatGatewayId | Any  # complex shape | ✓ | The ID of the NAT gateway. |

## Output Shape: DisassociateNatGatewayAddressResult

- **NatGatewayAddresses** (list[Any  # complex shape]): Information about the NAT gateway IP addresses.
- **NatGatewayId** (Any  # complex shape): The ID of the NAT gateway.

## Implementation

```speclang
def disassociate_nat_gateway_address(store, request: dict) -> dict:
    """Disassociates secondary Elastic IP addresses (EIPs) from a public NAT gateway. You cannot disassociate your primary EIP. For more information, see Edit secondary IP address associations in the Amazon """
    association_ids = request.get("AssociationIds", "").strip() if isinstance(request.get("AssociationIds"), str) else request.get("AssociationIds")
    if not association_ids:
        raise ValidationException("AssociationIds is required")
    nat_gateway_id = request.get("NatGatewayId", "").strip() if isinstance(request.get("NatGatewayId"), str) else request.get("NatGatewayId")
    if not nat_gateway_id:
        raise ValidationException("NatGatewayId is required")

    if store.disassociate_nat_gateway_addresss(nat_gateway_id):
        raise ResourceInUseException(f"Resource nat_gateway_id already exists")

    record = {
        "NatGatewayId": nat_gateway_id,
        "AssociationIds": association_ids,
        "MaxDrainDurationSeconds": max_drain_duration_seconds,
        "DryRun": dry_run,
    }

    store.disassociate_nat_gateway_addresss(nat_gateway_id, record)

    return {
        "NatGatewayId": nat_gateway_id,
        "NatGatewayAddresses": record.get("NatGatewayAddresses", {}),
    }
```
