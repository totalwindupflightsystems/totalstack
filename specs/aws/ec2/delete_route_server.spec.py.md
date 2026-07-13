---
id: "@specs/aws/ec2/delete_route_server"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteRouteServer"
---

# DeleteRouteServer

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_route_server
> **spec:implements:** @kind:operation DeleteRouteServer
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteRouteServer.spec.md

Deletes the specified route server. Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With this feature, VPC Route Server dynamically updates VPC and internet gateway route tables with your preferred IPv4 or IPv6 routes to achieve routing fault tolerance for those workloads. This enables you to automatically reroute traffic within a VPC, which increases the manageability of VPC routing and interoperability with third-party workloads. Route server supports the follow route table types: VPC route tables not associated with subnets Subnet route tables Internet gateway route tables Route server does not support route tables associated with virtual private gateways. To propagate routes into a transit gateway route table, use Transit Gateway Connect . For more information see Dynamic routing in your VPC with VPC Route Server in the Amazon VPC User Guide .

## Input Shape: DeleteRouteServerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| RouteServerId | Any  # complex shape | ✓ | The ID of the route server to delete. |

## Output Shape: DeleteRouteServerResult

- **RouteServer** (Any  # complex shape): Information about the deleted route server.

## Implementation

```speclang
def delete_route_server(store, request: dict) -> dict:
    """Deletes the specified route server. Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With this feature, VPC Route Serv"""
    route_server_id = request.get("RouteServerId", "").strip() if isinstance(request.get("RouteServerId"), str) else request.get("RouteServerId")

    if not store.route_servers(route_server_id):
        raise ResourceNotFoundException(f"Resource route_server_id not found")
    store.delete_route_servers(route_server_id)
    return {}
```
