---
id: "@specs/aws/ec2/associate_route_server"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateRouteServer"
---

# AssociateRouteServer

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_route_server
> **spec:implements:** @kind:operation AssociateRouteServer
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateRouteServer.spec.md

Associates a route server with a VPC to enable dynamic route updates. A route server association is the connection established between a route server and a VPC. For more information see Dynamic routing in your VPC with VPC Route Server in the Amazon VPC User Guide .

## Input Shape: AssociateRouteServerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| RouteServerId | Any  # complex shape | ✓ | The unique identifier for the route server to be associated. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC to associate with the route server. |

## Output Shape: AssociateRouteServerResult

- **RouteServerAssociation** (Any  # complex shape): Information about the association between the route server and the VPC.

## Implementation

```speclang
def associate_route_server(store, request: dict) -> dict:
    """Associates a route server with a VPC to enable dynamic route updates. A route server association is the connection established between a route server and a VPC. For more information see Dynamic routin"""
    route_server_id = request.get("RouteServerId", "").strip() if isinstance(request.get("RouteServerId"), str) else request.get("RouteServerId")
    if not route_server_id:
        raise ValidationException("RouteServerId is required")
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateRouteServer", request)
```
