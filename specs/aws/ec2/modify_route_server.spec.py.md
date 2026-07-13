---
id: "@specs/aws/ec2/modify_route_server"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyRouteServer"
---

# ModifyRouteServer

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_route_server
> **spec:implements:** @kind:operation ModifyRouteServer
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyRouteServer.spec.md

Modifies the configuration of an existing route server. Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With this feature, VPC Route Server dynamically updates VPC and internet gateway route tables with your preferred IPv4 or IPv6 routes to achieve routing fault tolerance for those workloads. This enables you to automatically reroute traffic within a VPC, which increases the manageability of VPC routing and interoperability with third-party workloads. Route server supports the follow route table types: VPC route tables not associated with subnets Subnet route tables Internet gateway route tables Route server does not support route tables associated with virtual private gateways. To propagate routes into a transit gateway route table, use Transit Gateway Connect . For more information see Dynamic routing in your VPC with VPC Route Server in the Amazon VPC User Guide .

## Input Shape: ModifyRouteServerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| PersistRoutes | Any  # complex shape |  | Specifies whether to persist routes after all BGP sessions are terminated. enable: Routes will be persisted in FIB and R |
| PersistRoutesDuration | Any  # complex shape |  | The number of minutes a route server will wait after BGP is re-established to unpersist the routes in the FIB and RIB. V |
| RouteServerId | Any  # complex shape | ✓ | The ID of the route server to modify. |
| SnsNotificationsEnabled | bool |  | Specifies whether to enable SNS notifications for route server events. Enabling SNS notifications persists BGP status ch |

## Output Shape: ModifyRouteServerResult

- **RouteServer** (Any  # complex shape): Information about the modified route server.

## Implementation

```speclang
def modify_route_server(store, request: dict) -> dict:
    """Modifies the configuration of an existing route server. Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With this fea"""
    route_server_id = request.get("RouteServerId", "").strip() if isinstance(request.get("RouteServerId"), str) else request.get("RouteServerId")
    if not route_server_id:
        raise ValidationException("RouteServerId is required")

    resource = store.route_servers(route_server_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource route_server_id not found")

    # Update mutable fields
    if "PersistRoutes" in request:
        resource["PersistRoutes"] = persist_routes
    if "PersistRoutesDuration" in request:
        resource["PersistRoutesDuration"] = persist_routes_duration
    if "SnsNotificationsEnabled" in request:
        resource["SnsNotificationsEnabled"] = sns_notifications_enabled
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.route_servers(route_server_id, resource)
    return resource
```
