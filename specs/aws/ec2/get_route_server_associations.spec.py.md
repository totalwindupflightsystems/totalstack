---
id: "@specs/aws/ec2/get_route_server_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetRouteServerAssociations"
---

# GetRouteServerAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_route_server_associations
> **spec:implements:** @kind:operation GetRouteServerAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetRouteServerAssociations.spec.md

Gets information about the associations for the specified route server. A route server association is the connection established between a route server and a VPC. For more information see Dynamic routing in your VPC with VPC Route Server in the Amazon VPC User Guide .

## Input Shape: GetRouteServerAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| RouteServerId | Any  # complex shape | ✓ | The ID of the route server for which to get association information. |

## Output Shape: GetRouteServerAssociationsResult

- **RouteServerAssociations** (list[Any  # complex shape]): Information about the associations for the specified route server.

## Implementation

```speclang
def get_route_server_associations(store, request: dict) -> dict:
    """Gets information about the associations for the specified route server. A route server association is the connection established between a route server and a VPC. For more information see Dynamic rout"""
    route_server_id = request.get("RouteServerId", "").strip() if isinstance(request.get("RouteServerId"), str) else request.get("RouteServerId")
    if not route_server_id:
        raise ValidationException("RouteServerId is required")

    resource = store.route_server_associationss(route_server_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource route_server_id not found")
    return {"RouteServerId": route_server_id, **resource}
```
