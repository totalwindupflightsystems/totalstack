---
id: "@specs/aws/ec2/describe_nat_gateways"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeNatGateways"
---

# DescribeNatGateways

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_nat_gateways
> **spec:implements:** @kind:operation DescribeNatGateways
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeNatGateways.spec.md

Describes your NAT gateways. The default is to describe all your NAT gateways. Alternatively, you can specify specific NAT gateway IDs or filter the results to include only the NAT gateways that match specific criteria.

## Input Shape: DescribeNatGatewaysRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filter | list[Any  # complex shape] |  | The filters. nat-gateway-id - The ID of the NAT gateway. state - The state of the NAT gateway ( pending | failed | avail |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NatGatewayIds | list[Any  # complex shape] |  | The IDs of the NAT gateways. |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeNatGatewaysResult

- **NatGateways** (list[Any  # complex shape]): Information about the NAT gateways.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_nat_gateways(store, request: dict) -> dict:
    """Describes your NAT gateways. The default is to describe all your NAT gateways. Alternatively, you can specify specific NAT gateway IDs or filter the results to include only the NAT gateways that match"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
