---
id: "@specs/aws/ec2/delete_vpc_peering_connection"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVpcPeeringConnection"
---

# DeleteVpcPeeringConnection

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_vpc_peering_connection
> **spec:implements:** @kind:operation DeleteVpcPeeringConnection
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVpcPeeringConnection.spec.md

Deletes a VPC peering connection. Either the owner of the requester VPC or the owner of the accepter VPC can delete the VPC peering connection if it's in the active state. The owner of the requester VPC can delete a VPC peering connection in the pending-acceptance state. You cannot delete a VPC peering connection that's in the failed or rejected state.

## Input Shape: DeleteVpcPeeringConnectionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpcPeeringConnectionId | Any  # complex shape | ✓ | The ID of the VPC peering connection. |

## Output Shape: DeleteVpcPeeringConnectionResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def delete_vpc_peering_connection(store, request: dict) -> dict:
    """Deletes a VPC peering connection. Either the owner of the requester VPC or the owner of the accepter VPC can delete the VPC peering connection if it's in the active state. The owner of the requester V"""
    vpc_peering_connection_id = request.get("VpcPeeringConnectionId", "").strip() if isinstance(request.get("VpcPeeringConnectionId"), str) else request.get("VpcPeeringConnectionId")

    if not store.vpc_peering_connections(vpc_peering_connection_id):
        raise ResourceNotFoundException(f"Resource vpc_peering_connection_id not found")
    store.delete_vpc_peering_connections(vpc_peering_connection_id)
    return {}
```
