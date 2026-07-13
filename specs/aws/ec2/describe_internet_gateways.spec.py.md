---
id: "@specs/aws/ec2/describe_internet_gateways"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeInternetGateways"
---

# DescribeInternetGateways

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_internet_gateways
> **spec:implements:** @kind:operation DescribeInternetGateways
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeInternetGateways.spec.md

Describes your internet gateways. The default is to describe all your internet gateways. Alternatively, you can specify specific internet gateway IDs or filter the results to include only the internet gateways that match specific criteria.

## Input Shape: DescribeInternetGatewaysRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. attachment.state - The current state of the attachment between the gateway and the VPC ( available ). Prese |
| InternetGatewayIds | list[Any  # complex shape] |  | The IDs of the internet gateways. Default: Describes all your internet gateways. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeInternetGatewaysResult

- **InternetGateways** (list[Any  # complex shape]): Information about the internet gateways.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_internet_gateways(store, request: dict) -> dict:
    """Describes your internet gateways. The default is to describe all your internet gateways. Alternatively, you can specify specific internet gateway IDs or filter the results to include only the internet"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
