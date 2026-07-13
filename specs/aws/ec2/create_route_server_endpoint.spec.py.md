---
id: "@specs/aws/ec2/create_route_server_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateRouteServerEndpoint"
---

# CreateRouteServerEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_route_server_endpoint
> **spec:implements:** @kind:operation CreateRouteServerEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateRouteServerEndpoint.spec.md

Creates a new endpoint for a route server in a specified subnet. A route server endpoint is an Amazon Web Services-managed component inside a subnet that facilitates BGP (Border Gateway Protocol) connections between your route server and your BGP peers. For more information see Dynamic routing in your VPC with VPC Route Server in the Amazon VPC User Guide .

## Input Shape: CreateRouteServerEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier to ensure idempotency of the request. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| RouteServerId | Any  # complex shape | ✓ | The ID of the route server for which to create an endpoint. |
| SubnetId | Any  # complex shape | ✓ | The ID of the subnet in which to create the route server endpoint. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the route server endpoint during creation. |

## Output Shape: CreateRouteServerEndpointResult

- **RouteServerEndpoint** (Any  # complex shape): Information about the created route server endpoint.

## Implementation

```speclang
def create_route_server_endpoint(store, request: dict) -> dict:
    """Creates a new endpoint for a route server in a specified subnet. A route server endpoint is an Amazon Web Services-managed component inside a subnet that facilitates BGP (Border Gateway Protocol) conn"""
    route_server_id = request.get("RouteServerId", "").strip() if isinstance(request.get("RouteServerId"), str) else request.get("RouteServerId")
    if not route_server_id:
        raise ValidationException("RouteServerId is required")
    subnet_id = request.get("SubnetId", "").strip() if isinstance(request.get("SubnetId"), str) else request.get("SubnetId")
    if not subnet_id:
        raise ValidationException("SubnetId is required")

    if store.route_server_endpoints(route_server_id):
        raise ResourceInUseException(f"Resource route_server_id already exists")

    record = {
        "RouteServerId": route_server_id,
        "SubnetId": subnet_id,
        "ClientToken": client_token,
        "DryRun": dry_run,
        "TagSpecifications": tag_specifications,
    }

    store.route_server_endpoints(route_server_id, record)

    return {
        "RouteServerEndpoint": record.get("RouteServerEndpoint", {}),
    }
```
