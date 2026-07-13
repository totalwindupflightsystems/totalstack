---
id: "@specs/aws/ec2/describe_vpc_block_public_access_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcBlockPublicAccessOptions"
---

# DescribeVpcBlockPublicAccessOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_block_public_access_options
> **spec:implements:** @kind:operation DescribeVpcBlockPublicAccessOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcBlockPublicAccessOptions.spec.md

Describe VPC Block Public Access (BPA) options. VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. To learn more about VPC BPA, see Block public access to VPCs and subnets in the Amazon VPC User Guide .

## Input Shape: DescribeVpcBlockPublicAccessOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DescribeVpcBlockPublicAccessOptionsResult

- **VpcBlockPublicAccessOptions** (Any  # complex shape): Details related to the options.

## Implementation

```speclang
def describe_vpc_block_public_access_options(store, request: dict) -> dict:
    """Describe VPC Block Public Access (BPA) options. VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the intern"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
