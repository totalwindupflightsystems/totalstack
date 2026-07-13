---
id: "@specs/aws/ec2/assign_private_nat_gateway_address"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssignPrivateNatGatewayAddress"
---

# AssignPrivateNatGatewayAddress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/assign_private_nat_gateway_address
> **spec:implements:** @kind:operation AssignPrivateNatGatewayAddress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssignPrivateNatGatewayAddress.spec.md

Assigns private IPv4 addresses to a private NAT gateway. For more information, see Work with NAT gateways in the Amazon VPC User Guide .

## Input Shape: AssignPrivateNatGatewayAddressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NatGatewayId | Any  # complex shape | ✓ | The ID of the NAT gateway. |
| PrivateIpAddressCount | Any  # complex shape |  | The number of private IP addresses to assign to the NAT gateway. You can't specify this parameter when also specifying p |
| PrivateIpAddresses | list[str] |  | The private IPv4 addresses you want to assign to the private NAT gateway. |

## Output Shape: AssignPrivateNatGatewayAddressResult

- **NatGatewayAddresses** (list[Any  # complex shape]): NAT gateway IP addresses.
- **NatGatewayId** (Any  # complex shape): The ID of the NAT gateway.

## Implementation

```speclang
def assign_private_nat_gateway_address(store, request: dict) -> dict:
    """Assigns private IPv4 addresses to a private NAT gateway. For more information, see Work with NAT gateways in the Amazon VPC User Guide ."""
    nat_gateway_id = request.get("NatGatewayId", "").strip() if isinstance(request.get("NatGatewayId"), str) else request.get("NatGatewayId")
    if not nat_gateway_id:
        raise ValidationException("NatGatewayId is required")

    if store.assign_private_nat_gateway_addresss(nat_gateway_id):
        raise ResourceInUseException(f"Resource nat_gateway_id already exists")

    record = {
        "NatGatewayId": nat_gateway_id,
        "PrivateIpAddresses": private_ip_addresses,
        "PrivateIpAddressCount": private_ip_address_count,
        "DryRun": dry_run,
    }

    store.assign_private_nat_gateway_addresss(nat_gateway_id, record)

    return {
        "NatGatewayId": nat_gateway_id,
        "NatGatewayAddresses": record.get("NatGatewayAddresses", {}),
    }
```
