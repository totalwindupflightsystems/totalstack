---
id: "@specs/aws/ec2/describe_vpc_endpoint_connections"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcEndpointConnections"
---

# DescribeVpcEndpointConnections

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_endpoint_connections
> **spec:implements:** @kind:operation DescribeVpcEndpointConnections
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcEndpointConnections.spec.md

Describes the VPC endpoint connections to your VPC endpoint services, including any endpoints that are pending your acceptance.

## Input Shape: DescribeVpcEndpointConnectionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. ip-address-type - The IP address type ( ipv4 | ipv6 ). service-id - The ID of the service. vpc-endpoint-own |
| MaxResults | int |  | The maximum number of results to return for the request in a single page. The remaining results of the initial request c |
| NextToken | str |  | The token to retrieve the next page of results. |

## Output Shape: DescribeVpcEndpointConnectionsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **VpcEndpointConnections** (Any  # complex shape): Information about the VPC endpoint connections.

## Implementation

```speclang
def describe_vpc_endpoint_connections(store, request: dict) -> dict:
    """Describes the VPC endpoint connections to your VPC endpoint services, including any endpoints that are pending your acceptance."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
