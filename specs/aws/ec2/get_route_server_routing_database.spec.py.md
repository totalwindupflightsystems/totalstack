---
id: "@specs/aws/ec2/get_route_server_routing_database"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetRouteServerRoutingDatabase"
---

# GetRouteServerRoutingDatabase

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_route_server_routing_database
> **spec:implements:** @kind:operation GetRouteServerRoutingDatabase
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetRouteServerRoutingDatabase.spec.md

Gets the routing database for the specified route server. The Routing Information Base (RIB) serves as a database that stores all the routing information and network topology data collected by a router or routing system, such as routes learned from BGP peers. The RIB is constantly updated as new routing information is received or existing routes change. This ensures that the route server always has the most current view of the network topology and can make optimal routing decisions. Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With this feature, VPC Route Server dynamically updates VPC and internet gateway route tables with your preferred IPv4 or IPv6 routes to achieve routing fault tolerance for those workloads. This enables you to automatically reroute traffic within a VPC, which increases the manageability of VPC routing and interoperability with third-party workloads. Route server supports the follow route table types: VPC route tables not associated with subnets Subnet route tables Internet gateway route tables Route server does not support route tables associated with virtual private gateways. To propagate routes into a transit gateway route table, use Transit Gateway Connect .

## Input Shape: GetRouteServerRoutingDatabaseRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | Filters to apply to the routing database query. |
| MaxResults | Any  # complex shape |  | The maximum number of routing database entries to return in a single response. |
| NextToken | str |  | The token for the next page of results. |
| RouteServerId | Any  # complex shape | ✓ | The ID of the route server for which to get the routing database. |

## Output Shape: GetRouteServerRoutingDatabaseResult

- **AreRoutesPersisted** (bool): Indicates whether routes are being persisted in the routing database.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **Routes** (list[Any  # complex shape]): The collection of routes in the route server's routing database.

## Implementation

```speclang
def get_route_server_routing_database(store, request: dict) -> dict:
    """Gets the routing database for the specified route server. The Routing Information Base (RIB) serves as a database that stores all the routing information and network topology data collected by a route"""
    route_server_id = request.get("RouteServerId", "").strip() if isinstance(request.get("RouteServerId"), str) else request.get("RouteServerId")
    if not route_server_id:
        raise ValidationException("RouteServerId is required")

    resource = store.route_server_routing_databases(route_server_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource route_server_id not found")
    return {"RouteServerId": route_server_id, **resource}
```
