---
id: "@specs/aws/ec2/describe_route_server_peers"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeRouteServerPeers"
---

# DescribeRouteServerPeers

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_route_server_peers
> **spec:implements:** @kind:operation DescribeRouteServerPeers
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeRouteServerPeers.spec.md

Describes one or more route server peers. A route server peer is a session between a route server endpoint and the device deployed in Amazon Web Services (such as a firewall appliance or other network security function running on an EC2 instance). The device must meet these requirements: Have an elastic network interface in the VPC Support BGP (Border Gateway Protocol) Can initiate BGP sessions For more information see Dynamic routing in your VPC with VPC Route Server in the Amazon VPC User Guide .

## Input Shape: DescribeRouteServerPeersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters to apply to the describe request. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. |
| NextToken | str |  | The token for the next page of results. |
| RouteServerPeerIds | list[Any  # complex shape] |  | The IDs of the route server peers to describe. |

## Output Shape: DescribeRouteServerPeersResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **RouteServerPeers** (list[Any  # complex shape]): Information about the described route server peers.

## Implementation

```speclang
def describe_route_server_peers(store, request: dict) -> dict:
    """Describes one or more route server peers. A route server peer is a session between a route server endpoint and the device deployed in Amazon Web Services (such as a firewall appliance or other network"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
