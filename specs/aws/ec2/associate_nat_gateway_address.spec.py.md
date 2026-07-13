---
id: "@specs/aws/ec2/associate_nat_gateway_address"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateNatGatewayAddress"
---

# AssociateNatGatewayAddress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_nat_gateway_address
> **spec:implements:** @kind:operation AssociateNatGatewayAddress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateNatGatewayAddress.spec.md

Associates Elastic IP addresses (EIPs) and private IPv4 addresses with a public NAT gateway. For more information, see Work with NAT gateways in the Amazon VPC User Guide . By default, you can associate up to 2 Elastic IP addresses per public NAT gateway. You can increase the limit by requesting a quota adjustment. For more information, see Elastic IP address quotas in the Amazon VPC User Guide . When you associate an EIP or secondary EIPs with a public NAT gateway, the network border group of the EIPs must match the network border group of the Availability Zone (AZ) that the public NAT gateway is in. If it's not the same, the EIP will fail to associate. You can see the network border group for the subnet's AZ by viewing the details of the subnet. Similarly, you can view the network border group of an EIP by viewing the details of the EIP address. For more information about network border groups and EIPs, see Allocate an Elastic IP address in the Amazon VPC User Guide .

## Input Shape: AssociateNatGatewayAddressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationIds | list[Any  # complex shape] | ✓ | The allocation IDs of EIPs that you want to associate with your NAT gateway. |
| AvailabilityZone | Any  # complex shape |  | For regional NAT gateways only: The Availability Zone where you want to associate an Elastic IP address (EIP). The regio |
| AvailabilityZoneId | Any  # complex shape |  | For regional NAT gateways only: The ID of the Availability Zone where you want to associate an Elastic IP address (EIP). |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NatGatewayId | Any  # complex shape | ✓ | The ID of the NAT gateway. |
| PrivateIpAddresses | list[str] |  | The private IPv4 addresses that you want to assign to the NAT gateway. |

## Output Shape: AssociateNatGatewayAddressResult

- **NatGatewayAddresses** (list[Any  # complex shape]): The IP addresses.
- **NatGatewayId** (Any  # complex shape): The ID of the NAT gateway.

## Implementation

```speclang
def associate_nat_gateway_address(store, request: dict) -> dict:
    """Associates Elastic IP addresses (EIPs) and private IPv4 addresses with a public NAT gateway. For more information, see Work with NAT gateways in the Amazon VPC User Guide . By default, you can associa"""
    allocation_ids = request.get("AllocationIds", "").strip() if isinstance(request.get("AllocationIds"), str) else request.get("AllocationIds")
    if not allocation_ids:
        raise ValidationException("AllocationIds is required")
    nat_gateway_id = request.get("NatGatewayId", "").strip() if isinstance(request.get("NatGatewayId"), str) else request.get("NatGatewayId")
    if not nat_gateway_id:
        raise ValidationException("NatGatewayId is required")

    if store.associate_nat_gateway_addresss(allocation_ids):
        raise ResourceInUseException(f"Resource allocation_ids already exists")

    record = {
        "NatGatewayId": nat_gateway_id,
        "AllocationIds": allocation_ids,
        "PrivateIpAddresses": private_ip_addresses,
        "DryRun": dry_run,
        "AvailabilityZone": availability_zone,
        "AvailabilityZoneId": availability_zone_id,
    }

    store.associate_nat_gateway_addresss(allocation_ids, record)

    return {
        "NatGatewayId": record.get("NatGatewayId", {}),
        "NatGatewayAddresses": record.get("NatGatewayAddresses", {}),
    }
```
