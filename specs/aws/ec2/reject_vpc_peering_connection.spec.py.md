---
id: "@specs/aws/ec2/reject_vpc_peering_connection"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RejectVpcPeeringConnection"
---

# RejectVpcPeeringConnection

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/reject_vpc_peering_connection
> **spec:implements:** @kind:operation RejectVpcPeeringConnection
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RejectVpcPeeringConnection.spec.md

Rejects a VPC peering connection request. The VPC peering connection must be in the pending-acceptance state. Use the DescribeVpcPeeringConnections request to view your outstanding VPC peering connection requests. To delete an active VPC peering connection, or to delete a VPC peering connection request that you initiated, use DeleteVpcPeeringConnection .

## Input Shape: RejectVpcPeeringConnectionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpcPeeringConnectionId | Any  # complex shape | ✓ | The ID of the VPC peering connection. |

## Output Shape: RejectVpcPeeringConnectionResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def reject_vpc_peering_connection(store, request: dict) -> dict:
    """Rejects a VPC peering connection request. The VPC peering connection must be in the pending-acceptance state. Use the DescribeVpcPeeringConnections request to view your outstanding VPC peering connect"""
    vpc_peering_connection_id = request.get("VpcPeeringConnectionId", "").strip() if isinstance(request.get("VpcPeeringConnectionId"), str) else request.get("VpcPeeringConnectionId")
    if not vpc_peering_connection_id:
        raise ValidationException("VpcPeeringConnectionId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RejectVpcPeeringConnection", request)
```
