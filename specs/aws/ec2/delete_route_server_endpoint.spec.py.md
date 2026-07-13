---
id: "@specs/aws/ec2/delete_route_server_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteRouteServerEndpoint"
---

# DeleteRouteServerEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_route_server_endpoint
> **spec:implements:** @kind:operation DeleteRouteServerEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteRouteServerEndpoint.spec.md

Deletes the specified route server endpoint. A route server endpoint is an Amazon Web Services-managed component inside a subnet that facilitates BGP (Border Gateway Protocol) connections between your route server and your BGP peers.

## Input Shape: DeleteRouteServerEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| RouteServerEndpointId | Any  # complex shape | ✓ | The ID of the route server endpoint to delete. |

## Output Shape: DeleteRouteServerEndpointResult

- **RouteServerEndpoint** (Any  # complex shape): Information about the deleted route server endpoint.

## Implementation

```speclang
def delete_route_server_endpoint(store, request: dict) -> dict:
    """Deletes the specified route server endpoint. A route server endpoint is an Amazon Web Services-managed component inside a subnet that facilitates BGP (Border Gateway Protocol) connections between your"""
    route_server_endpoint_id = request.get("RouteServerEndpointId", "").strip() if isinstance(request.get("RouteServerEndpointId"), str) else request.get("RouteServerEndpointId")

    if not store.route_server_endpoints(route_server_endpoint_id):
        raise ResourceNotFoundException(f"Resource route_server_endpoint_id not found")
    store.delete_route_server_endpoints(route_server_endpoint_id)
    return {}
```
