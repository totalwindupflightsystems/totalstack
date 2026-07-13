---
id: "@specs/aws/ec2/create_vpc_peering_connection"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVpcPeeringConnection"
---

# CreateVpcPeeringConnection

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_vpc_peering_connection
> **spec:implements:** @kind:operation CreateVpcPeeringConnection
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVpcPeeringConnection.spec.md

Requests a VPC peering connection between two VPCs: a requester VPC that you own and an accepter VPC with which to create the connection. The accepter VPC can belong to another Amazon Web Services account and can be in a different Region to the requester VPC. The requester VPC and accepter VPC cannot have overlapping CIDR blocks. Limitations and rules apply to a VPC peering connection. For more information, see the VPC peering limitations in the VPC Peering Guide . The owner of the accepter VPC must accept the peering request to activate the peering connection. The VPC peering connection request expires after 7 days, after which it cannot be accepted or rejected. If you create a VPC peering connection request between VPCs with overlapping CIDR blocks, the VPC peering connection has a status of failed .

## Input Shape: CreateVpcPeeringConnectionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PeerOwnerId | str |  | The Amazon Web Services account ID of the owner of the accepter VPC. Default: Your Amazon Web Services account ID |
| PeerRegion | str |  | The Region code for the accepter VPC, if the accepter VPC is located in a Region other than the Region in which you make |
| PeerVpcId | str |  | The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the peering connection. |
| VpcId | Any  # complex shape | ✓ | The ID of the requester VPC. You must specify this parameter in the request. |

## Output Shape: CreateVpcPeeringConnectionResult

- **VpcPeeringConnection** (Any  # complex shape): Information about the VPC peering connection.

## Implementation

```speclang
def create_vpc_peering_connection(store, request: dict) -> dict:
    """Requests a VPC peering connection between two VPCs: a requester VPC that you own and an accepter VPC with which to create the connection. The accepter VPC can belong to another Amazon Web Services acc"""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    if store.vpc_peering_connections(vpc_id):
        raise ResourceInUseException(f"Resource vpc_id already exists")

    record = {
        "PeerRegion": peer_region,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
        "VpcId": vpc_id,
        "PeerVpcId": peer_vpc_id,
        "PeerOwnerId": peer_owner_id,
    }

    store.vpc_peering_connections(vpc_id, record)

    return {
        "VpcPeeringConnection": record.get("VpcPeeringConnection", {}),
    }
```
