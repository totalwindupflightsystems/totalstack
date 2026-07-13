---
id: "@specs/aws/ec2/describe_route_servers"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeRouteServers"
---

# DescribeRouteServers

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_route_servers
> **spec:implements:** @kind:operation DescribeRouteServers
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeRouteServers.spec.md

Describes one or more route servers. Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With this feature, VPC Route Server dynamically updates VPC and internet gateway route tables with your preferred IPv4 or IPv6 routes to achieve routing fault tolerance for those workloads. This enables you to automatically reroute traffic within a VPC, which increases the manageability of VPC routing and interoperability with third-party workloads. Route server supports the follow route table types: VPC route tables not associated with subnets Subnet route tables Internet gateway route tables Route server does not support route tables associated with virtual private gateways. To propagate routes into a transit gateway route table, use Transit Gateway Connect . For more information see Dynamic routing in your VPC with VPC Route Server in the Amazon VPC User Guide .

## Input Shape: DescribeRouteServersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters to apply to the describe request. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. |
| NextToken | str |  | The token for the next page of results. |
| RouteServerIds | list[Any  # complex shape] |  | The IDs of the route servers to describe. |

## Output Shape: DescribeRouteServersResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **RouteServers** (list[Any  # complex shape]): Information about the described route servers.

## Implementation

```speclang
def describe_route_servers(store, request: dict) -> dict:
    """Describes one or more route servers. Amazon VPC Route Server simplifies routing for traffic between workloads that are deployed within a VPC and its internet gateways. With this feature, VPC Route Ser"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
