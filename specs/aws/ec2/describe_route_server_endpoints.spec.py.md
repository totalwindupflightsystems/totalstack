---
id: "@specs/aws/ec2/describe_route_server_endpoints"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeRouteServerEndpoints"
---

# DescribeRouteServerEndpoints

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_route_server_endpoints
> **spec:implements:** @kind:operation DescribeRouteServerEndpoints
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeRouteServerEndpoints.spec.md

Describes one or more route server endpoints. A route server endpoint is an Amazon Web Services-managed component inside a subnet that facilitates BGP (Border Gateway Protocol) connections between your route server and your BGP peers. For more information see Dynamic routing in your VPC with VPC Route Server in the Amazon VPC User Guide .

## Input Shape: DescribeRouteServerEndpointsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters to apply to the describe request. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. |
| NextToken | str |  | The token for the next page of results. |
| RouteServerEndpointIds | list[Any  # complex shape] |  | The IDs of the route server endpoints to describe. |

## Output Shape: DescribeRouteServerEndpointsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **RouteServerEndpoints** (list[Any  # complex shape]): Information about the described route server endpoints.

## Implementation

```speclang
def describe_route_server_endpoints(store, request: dict) -> dict:
    """Describes one or more route server endpoints. A route server endpoint is an Amazon Web Services-managed component inside a subnet that facilitates BGP (Border Gateway Protocol) connections between you"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
