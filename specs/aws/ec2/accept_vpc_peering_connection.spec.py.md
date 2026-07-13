---
id: "@specs/aws/ec2/accept_vpc_peering_connection"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AcceptVpcPeeringConnection"
---

# AcceptVpcPeeringConnection

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/accept_vpc_peering_connection
> **spec:implements:** @kind:operation AcceptVpcPeeringConnection
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AcceptVpcPeeringConnection.spec.md

Accept a VPC peering connection request. To accept a request, the VPC peering connection must be in the pending-acceptance state, and you must be the owner of the peer VPC. Use DescribeVpcPeeringConnections to view your outstanding VPC peering connection requests. For an inter-Region VPC peering connection request, you must accept the VPC peering connection in the Region of the accepter VPC.

## Input Shape: AcceptVpcPeeringConnectionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpcPeeringConnectionId | Any  # complex shape | ✓ | The ID of the VPC peering connection. You must specify this parameter in the request. |

## Output Shape: AcceptVpcPeeringConnectionResult

- **VpcPeeringConnection** (Any  # complex shape): Information about the VPC peering connection.

## Implementation

```speclang
def accept_vpc_peering_connection(store, request: dict) -> dict:
    """Accept a VPC peering connection request. To accept a request, the VPC peering connection must be in the pending-acceptance state, and you must be the owner of the peer VPC. Use DescribeVpcPeeringConne"""
    vpc_peering_connection_id = request.get("VpcPeeringConnectionId", "").strip() if isinstance(request.get("VpcPeeringConnectionId"), str) else request.get("VpcPeeringConnectionId")
    if not vpc_peering_connection_id:
        raise ValidationException("VpcPeeringConnectionId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AcceptVpcPeeringConnection", request)
```
