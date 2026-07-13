---
id: "@specs/aws/ec2/describe_vpc_classic_link_dns_support"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcClassicLinkDnsSupport"
---

# DescribeVpcClassicLinkDnsSupport

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_classic_link_dns_support
> **spec:implements:** @kind:operation DescribeVpcClassicLinkDnsSupport
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcClassicLinkDnsSupport.spec.md

This action is deprecated. Describes the ClassicLink DNS support status of one or more VPCs. If enabled, the DNS hostname of a linked EC2-Classic instance resolves to its private IP address when addressed from an instance in the VPC to which it's linked. Similarly, the DNS hostname of an instance in a VPC resolves to its private IP address when addressed from a linked EC2-Classic instance.

## Input Shape: DescribeVpcClassicLinkDnsSupportRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| VpcIds | list[Any  # complex shape] |  | The IDs of the VPCs. |

## Output Shape: DescribeVpcClassicLinkDnsSupportResult

- **NextToken** (Any  # complex shape): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **Vpcs** (list[Any  # complex shape]): Information about the ClassicLink DNS support status of the VPCs.

## Implementation

```speclang
def describe_vpc_classic_link_dns_support(store, request: dict) -> dict:
    """This action is deprecated. Describes the ClassicLink DNS support status of one or more VPCs. If enabled, the DNS hostname of a linked EC2-Classic instance resolves to its private IP address when addre"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
