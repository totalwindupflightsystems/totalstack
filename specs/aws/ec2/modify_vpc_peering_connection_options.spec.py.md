---
id: "@specs/aws/ec2/modify_vpc_peering_connection_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpcPeeringConnectionOptions"
---

# ModifyVpcPeeringConnectionOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpc_peering_connection_options
> **spec:implements:** @kind:operation ModifyVpcPeeringConnectionOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpcPeeringConnectionOptions.spec.md

Modifies the VPC peering connection options on one side of a VPC peering connection. If the peered VPCs are in the same Amazon Web Services account, you can enable DNS resolution for queries from the local VPC. This ensures that queries from the local VPC resolve to private IP addresses in the peer VPC. This option is not available if the peered VPCs are in different Amazon Web Services accounts or different Regions. For peered VPCs in different Amazon Web Services accounts, each Amazon Web Services account owner must initiate a separate request to modify the peering connection options. For inter-region peering connections, you must use the Region for the requester VPC to modify the requester VPC peering options and the Region for the accepter VPC to modify the accepter VPC peering options. To verify which VPCs are the accepter and the requester for a VPC peering connection, use the DescribeVpcPeeringConnections command.

## Input Shape: ModifyVpcPeeringConnectionOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AccepterPeeringConnectionOptions | Any  # complex shape |  | The VPC peering connection options for the accepter VPC. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| RequesterPeeringConnectionOptions | Any  # complex shape |  | The VPC peering connection options for the requester VPC. |
| VpcPeeringConnectionId | Any  # complex shape | ✓ | The ID of the VPC peering connection. |

## Output Shape: ModifyVpcPeeringConnectionOptionsResult

- **AccepterPeeringConnectionOptions** (Any  # complex shape): Information about the VPC peering connection options for the accepter VPC.
- **RequesterPeeringConnectionOptions** (Any  # complex shape): Information about the VPC peering connection options for the requester VPC.

## Implementation

```speclang
def modify_vpc_peering_connection_options(store, request: dict) -> dict:
    """Modifies the VPC peering connection options on one side of a VPC peering connection. If the peered VPCs are in the same Amazon Web Services account, you can enable DNS resolution for queries from the """
    vpc_peering_connection_id = request.get("VpcPeeringConnectionId", "").strip() if isinstance(request.get("VpcPeeringConnectionId"), str) else request.get("VpcPeeringConnectionId")
    if not vpc_peering_connection_id:
        raise ValidationException("VpcPeeringConnectionId is required")

    resource = store.vpc_peering_connection_optionss(vpc_peering_connection_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpc_peering_connection_id not found")

    # Update mutable fields
    if "AccepterPeeringConnectionOptions" in request:
        resource["AccepterPeeringConnectionOptions"] = accepter_peering_connection_options
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "RequesterPeeringConnectionOptions" in request:
        resource["RequesterPeeringConnectionOptions"] = requester_peering_connection_options

    store.vpc_peering_connection_optionss(vpc_peering_connection_id, resource)
    return resource
```
