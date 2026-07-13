---
id: "@specs/aws/ec2/describe_vpc_classic_link"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcClassicLink"
---

# DescribeVpcClassicLink

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_classic_link
> **spec:implements:** @kind:operation DescribeVpcClassicLink
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcClassicLink.spec.md

This action is deprecated. Describes the ClassicLink status of the specified VPCs.

## Input Shape: DescribeVpcClassicLinkRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. is-classic-link-enabled - Whether the VPC is enabled for ClassicLink ( true | false ). tag - The key/value  |
| VpcIds | list[Any  # complex shape] |  | The VPCs for which you want to describe the ClassicLink status. |

## Output Shape: DescribeVpcClassicLinkResult

- **Vpcs** (list[Any  # complex shape]): The ClassicLink status of the VPCs.

## Implementation

```speclang
def describe_vpc_classic_link(store, request: dict) -> dict:
    """This action is deprecated. Describes the ClassicLink status of the specified VPCs."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
