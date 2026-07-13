---
id: "@specs/aws/ec2/create_route_server"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateRouteServer"
---

# CreateRouteServer

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_route_server
> **spec:implements:** @kind:operation CreateRouteServer
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateRouteServer.spec.md

Creates a new route server to manage dynamic routing in a VPC. Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With this feature, VPC Route Server dynamically updates VPC and internet gateway route tables with your preferred IPv4 or IPv6 routes to achieve routing fault tolerance for those workloads. This enables you to automatically reroute traffic within a VPC, which increases the manageability of VPC routing and interoperability with third-party workloads. Route server supports the follow route table types: VPC route tables not associated with subnets Subnet route tables Internet gateway route tables Route server does not support route tables associated with virtual private gateways. To propagate routes into a transit gateway route table, use Transit Gateway Connect . For more information see Dynamic routing in your VPC with VPC Route Server in the Amazon VPC User Guide .

## Input Shape: CreateRouteServerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AmazonSideAsn | int | ✓ | The private Autonomous System Number (ASN) for the Amazon side of the BGP session. Valid values are from 1 to 4294967295 |
| ClientToken | str |  | Unique, case-sensitive identifier to ensure idempotency of the request. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| PersistRoutes | Any  # complex shape |  | Indicates whether routes should be persisted after all BGP sessions are terminated. |
| PersistRoutesDuration | Any  # complex shape |  | The number of minutes a route server will wait after BGP is re-established to unpersist the routes in the FIB and RIB. V |
| SnsNotificationsEnabled | bool |  | Indicates whether SNS notifications should be enabled for route server events. Enabling SNS notifications persists BGP s |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the route server during creation. |

## Output Shape: CreateRouteServerResult

- **RouteServer** (Any  # complex shape): Information about the created route server.

## Implementation

```speclang
def create_route_server(store, request: dict) -> dict:
    """Creates a new route server to manage dynamic routing in a VPC. Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With t"""
    amazon_side_asn = request.get("AmazonSideAsn", "").strip() if isinstance(request.get("AmazonSideAsn"), str) else request.get("AmazonSideAsn")
    if not amazon_side_asn:
        raise ValidationException("AmazonSideAsn is required")

    if store.route_servers(amazon_side_asn):
        raise ResourceInUseException(f"Resource amazon_side_asn already exists")

    record = {
        "AmazonSideAsn": amazon_side_asn,
        "ClientToken": client_token,
        "DryRun": dry_run,
        "PersistRoutes": persist_routes,
        "PersistRoutesDuration": persist_routes_duration,
        "SnsNotificationsEnabled": sns_notifications_enabled,
        "TagSpecifications": tag_specifications,
    }

    store.route_servers(amazon_side_asn, record)

    return {
        "RouteServer": record.get("RouteServer", {}),
    }
```
