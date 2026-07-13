---
id: "@specs/aws/ec2/describe_vpc_endpoints"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcEndpoints"
---

# DescribeVpcEndpoints

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_endpoints
> **spec:implements:** @kind:operation DescribeVpcEndpoints
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcEndpoints.spec.md

Describes your VPC endpoints. The default is to describe all your VPC endpoints. Alternatively, you can specify specific VPC endpoint IDs or filter the results to include only the VPC endpoints that match specific criteria.

## Input Shape: DescribeVpcEndpointsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. ip-address-type - The IP address type ( ipv4 | ipv6 ). service-name - The name of the service. service-regi |
| MaxResults | int |  | The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent |
| NextToken | str |  | The token for the next set of items to return. (You received this token from a prior call.) |
| VpcEndpointIds | list[Any  # complex shape] |  | The IDs of the VPC endpoints. |

## Output Shape: DescribeVpcEndpointsResult

- **NextToken** (str): The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
- **VpcEndpoints** (Any  # complex shape): Information about the VPC endpoints.

## Implementation

```speclang
def describe_vpc_endpoints(store, request: dict) -> dict:
    """Describes your VPC endpoints. The default is to describe all your VPC endpoints. Alternatively, you can specify specific VPC endpoint IDs or filter the results to include only the VPC endpoints that m"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
