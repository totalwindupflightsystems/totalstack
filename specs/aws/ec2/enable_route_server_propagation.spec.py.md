---
id: "@specs/aws/ec2/enable_route_server_propagation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableRouteServerPropagation"
---

# EnableRouteServerPropagation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_route_server_propagation
> **spec:implements:** @kind:operation EnableRouteServerPropagation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableRouteServerPropagation.spec.md

Defines which route tables the route server can update with routes. When enabled, route server propagation installs the routes in the FIB on the route table you've specified. Route server supports IPv4 and IPv6 route propagation. For more information see Dynamic routing in your VPC with VPC Route Server in the Amazon VPC User Guide .

## Input Shape: EnableRouteServerPropagationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| RouteServerId | Any  # complex shape | ✓ | The ID of the route server for which to enable propagation. |
| RouteTableId | Any  # complex shape | ✓ | The ID of the route table to which route server will propagate routes. |

## Output Shape: EnableRouteServerPropagationResult

- **RouteServerPropagation** (Any  # complex shape): Information about the enabled route server propagation.

## Implementation

```speclang
def enable_route_server_propagation(store, request: dict) -> dict:
    """Defines which route tables the route server can update with routes. When enabled, route server propagation installs the routes in the FIB on the route table you've specified. Route server supports IPv"""
    route_server_id = request.get("RouteServerId", "").strip() if isinstance(request.get("RouteServerId"), str) else request.get("RouteServerId")
    if not route_server_id:
        raise ValidationException("RouteServerId is required")
    route_table_id = request.get("RouteTableId", "").strip() if isinstance(request.get("RouteTableId"), str) else request.get("RouteTableId")
    if not route_table_id:
        raise ValidationException("RouteTableId is required")

    resource = store.enable_route_server_propagations(route_server_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource route_server_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_route_server_propagations(route_server_id, resource)
    return resource
```
