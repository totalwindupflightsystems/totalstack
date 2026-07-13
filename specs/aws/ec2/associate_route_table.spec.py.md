---
id: "@specs/aws/ec2/associate_route_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateRouteTable"
---

# AssociateRouteTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_route_table
> **spec:implements:** @kind:operation AssociateRouteTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateRouteTable.spec.md

Associates a subnet in your VPC or an internet gateway or virtual private gateway attached to your VPC with a route table in your VPC. This association causes traffic from the subnet or gateway to be routed according to the routes in the route table. The action returns an association ID, which you need in order to disassociate the route table later. A route table can be associated with multiple subnets. For more information, see Route tables in the Amazon VPC User Guide .

## Input Shape: AssociateRouteTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GatewayId | Any  # complex shape |  | The ID of the internet gateway or virtual private gateway. |
| PublicIpv4Pool | Any  # complex shape |  | The ID of a public IPv4 pool. A public IPv4 pool is a pool of IPv4 addresses that you've brought to Amazon Web Services  |
| RouteTableId | Any  # complex shape | ✓ | The ID of the route table. |
| SubnetId | Any  # complex shape |  | The ID of the subnet. |

## Output Shape: AssociateRouteTableResult

- **AssociationId** (str): The route table association ID. This ID is required for disassociating the route table.
- **AssociationState** (Any  # complex shape): The state of the association.

## Implementation

```speclang
def associate_route_table(store, request: dict) -> dict:
    """Associates a subnet in your VPC or an internet gateway or virtual private gateway attached to your VPC with a route table in your VPC. This association causes traffic from the subnet or gateway to be """
    route_table_id = request.get("RouteTableId", "").strip() if isinstance(request.get("RouteTableId"), str) else request.get("RouteTableId")
    if not route_table_id:
        raise ValidationException("RouteTableId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateRouteTable", request)
```
