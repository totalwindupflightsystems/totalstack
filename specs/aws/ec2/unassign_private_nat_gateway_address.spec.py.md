---
id: "@specs/aws/ec2/unassign_private_nat_gateway_address"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_UnassignPrivateNatGatewayAddress"
---

# UnassignPrivateNatGatewayAddress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/unassign_private_nat_gateway_address
> **spec:implements:** @kind:operation UnassignPrivateNatGatewayAddress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_UnassignPrivateNatGatewayAddress.spec.md

Unassigns secondary private IPv4 addresses from a private NAT gateway. You cannot unassign your primary private IP. For more information, see Edit secondary IP address associations in the Amazon VPC User Guide . While unassigning is in progress, you cannot assign/unassign additional IP addresses while the connections are being drained. You are, however, allowed to delete the NAT gateway. A private IP address will only be released at the end of MaxDrainDurationSeconds. The private IP addresses stay associated and support the existing connections, but do not support any new connections (new connections are distributed across the remaining assigned private IP address). After the existing connections drain out, the private IP addresses are released.

## Input Shape: UnassignPrivateNatGatewayAddressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxDrainDurationSeconds | Any  # complex shape |  | The maximum amount of time to wait (in seconds) before forcibly releasing the IP addresses if connections are still in p |
| NatGatewayId | Any  # complex shape | ✓ | The ID of the NAT gateway. |
| PrivateIpAddresses | list[str] | ✓ | The private IPv4 addresses you want to unassign. |

## Output Shape: UnassignPrivateNatGatewayAddressResult

- **NatGatewayAddresses** (list[Any  # complex shape]): Information about the NAT gateway IP addresses.
- **NatGatewayId** (Any  # complex shape): The ID of the NAT gateway.

## Implementation

```speclang
def unassign_private_nat_gateway_address(store, request: dict) -> dict:
    """Unassigns secondary private IPv4 addresses from a private NAT gateway. You cannot unassign your primary private IP. For more information, see Edit secondary IP address associations in the Amazon VPC U"""
    nat_gateway_id = request.get("NatGatewayId", "").strip() if isinstance(request.get("NatGatewayId"), str) else request.get("NatGatewayId")
    if not nat_gateway_id:
        raise ValidationException("NatGatewayId is required")
    private_ip_addresses = request.get("PrivateIpAddresses", "").strip() if isinstance(request.get("PrivateIpAddresses"), str) else request.get("PrivateIpAddresses")
    if not private_ip_addresses:
        raise ValidationException("PrivateIpAddresses is required")

    if store.unassign_private_nat_gateway_addresss(nat_gateway_id):
        raise ResourceInUseException(f"Resource nat_gateway_id already exists")

    record = {
        "NatGatewayId": nat_gateway_id,
        "PrivateIpAddresses": private_ip_addresses,
        "MaxDrainDurationSeconds": max_drain_duration_seconds,
        "DryRun": dry_run,
    }

    store.unassign_private_nat_gateway_addresss(nat_gateway_id, record)

    return {
        "NatGatewayId": nat_gateway_id,
        "NatGatewayAddresses": record.get("NatGatewayAddresses", {}),
    }
```
