---
id: "@specs/aws/ec2/get_route_server_propagations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetRouteServerPropagations"
---

# GetRouteServerPropagations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_route_server_propagations
> **spec:implements:** @kind:operation GetRouteServerPropagations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetRouteServerPropagations.spec.md

Gets information about the route propagations for the specified route server. When enabled, route server propagation installs the routes in the FIB on the route table you've specified. Route server supports IPv4 and IPv6 route propagation. Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With this feature, VPC Route Server dynamically updates VPC and internet gateway route tables with your preferred IPv4 or IPv6 routes to achieve routing fault tolerance for those workloads. This enables you to automatically reroute traffic within a VPC, which increases the manageability of VPC routing and interoperability with third-party workloads. Route server supports the follow route table types: VPC route tables not associated with subnets Subnet route tables Internet gateway route tables Route server does not support route tables associated with virtual private gateways. To propagate routes into a transit gateway route table, use Transit Gateway Connect .

## Input Shape: GetRouteServerPropagationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| RouteServerId | Any  # complex shape | ✓ | The ID of the route server for which to get propagation information. |
| RouteTableId | Any  # complex shape |  | The ID of the route table for which to get propagation information. |

## Output Shape: GetRouteServerPropagationsResult

- **RouteServerPropagations** (list[Any  # complex shape]): Information about the route propagations for the specified route server.

## Implementation

```speclang
def get_route_server_propagations(store, request: dict) -> dict:
    """Gets information about the route propagations for the specified route server. When enabled, route server propagation installs the routes in the FIB on the route table you've specified. Route server su"""
    route_server_id = request.get("RouteServerId", "").strip() if isinstance(request.get("RouteServerId"), str) else request.get("RouteServerId")
    if not route_server_id:
        raise ValidationException("RouteServerId is required")

    resource = store.route_server_propagationss(route_server_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource route_server_id not found")
    return {"RouteServerId": route_server_id, **resource}
```
