---
id: "@specs/aws/ec2/create_nat_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateNatGateway"
---

# CreateNatGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_nat_gateway
> **spec:implements:** @kind:operation CreateNatGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateNatGateway.spec.md

Creates a NAT gateway in the specified subnet. This action creates a network interface in the specified subnet with a private IP address from the IP address range of the subnet. You can create either a public NAT gateway or a private NAT gateway. With a public NAT gateway, internet-bound traffic from a private subnet can be routed to the NAT gateway, so that instances in a private subnet can connect to the internet. With a private NAT gateway, private communication is routed across VPCs and on-premises networks through a transit gateway or virtual private gateway. Common use cases include running large workloads behind a small pool of allowlisted IPv4 addresses, preserving private IPv4 addresses, and communicating between overlapping networks. For more information, see NAT gateways in the Amazon VPC User Guide . When you create a public NAT gateway and assign it an EIP or secondary EIPs, the network border group of the EIPs must match the network border group of the Availability Zone (AZ) that the public NAT gateway is in. If it's not the same, the NAT gateway will fail to launch. You can see the network border group for the subnet's AZ by viewing the details of the subnet. Similarly, you can view the network border group of an EIP by viewing the details of the EIP address. For more information about network border groups and EIPs, see Allocate an Elastic IP address in the Amazon VPC User Guide .

## Input Shape: CreateNatGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationId | Any  # complex shape |  | [Public NAT gateways only] The allocation ID of an Elastic IP address to associate with the NAT gateway. You cannot spec |
| AvailabilityMode | Any  # complex shape |  | Specifies whether to create a zonal (single-AZ) or regional (multi-AZ) NAT gateway. Defaults to zonal . A zonal NAT gate |
| AvailabilityZoneAddresses | Any  # complex shape |  | For regional NAT gateways only: Specifies which Availability Zones you want the NAT gateway to support and the Elastic I |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| ConnectivityType | Any  # complex shape |  | Indicates whether the NAT gateway supports public or private connectivity. The default is public connectivity. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PrivateIpAddress | str |  | The private IPv4 address to assign to the NAT gateway. If you don't provide an address, a private IPv4 address will be a |
| SecondaryAllocationIds | list[Any  # complex shape] |  | Secondary EIP allocation IDs. For more information, see Create a NAT gateway in the Amazon VPC User Guide . |
| SecondaryPrivateIpAddressCount | Any  # complex shape |  | [Private NAT gateway only] The number of secondary private IPv4 addresses you want to assign to the NAT gateway. For mor |
| SecondaryPrivateIpAddresses | list[str] |  | Secondary private IPv4 addresses. For more information about secondary addresses, see Create a NAT gateway in the Amazon |
| SubnetId | Any  # complex shape |  | The ID of the subnet in which to create the NAT gateway. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the NAT gateway. |
| VpcId | Any  # complex shape |  | The ID of the VPC where you want to create a regional NAT gateway. |

## Output Shape: CreateNatGatewayResult

- **ClientToken** (str): Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided
- **NatGateway** (Any  # complex shape): Information about the NAT gateway.

## Implementation

```speclang
def create_nat_gateway(store, request: dict) -> dict:
    """Creates a NAT gateway in the specified subnet. This action creates a network interface in the specified subnet with a private IP address from the IP address range of the subnet. You can create either """


    record = {
        "AvailabilityMode": availability_mode,
        "AllocationId": allocation_id,
        "ClientToken": client_token,
        "DryRun": dry_run,
        "SubnetId": subnet_id,
        "VpcId": vpc_id,
        "AvailabilityZoneAddresses": availability_zone_addresses,
        "TagSpecifications": tag_specifications,
        "ConnectivityType": connectivity_type,
        "PrivateIpAddress": private_ip_address,
        "SecondaryAllocationIds": secondary_allocation_ids,
        "SecondaryPrivateIpAddresses": secondary_private_ip_addresses,
        "SecondaryPrivateIpAddressCount": secondary_private_ip_address_count,
    }

    store.nat_gateways(record)

    return {
        "ClientToken": record.get("ClientToken", {}),
        "NatGateway": record.get("NatGateway", {}),
    }
```
