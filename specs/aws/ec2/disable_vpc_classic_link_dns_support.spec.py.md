---
id: "@specs/aws/ec2/disable_vpc_classic_link_dns_support"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableVpcClassicLinkDnsSupport"
---

# DisableVpcClassicLinkDnsSupport

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_vpc_classic_link_dns_support
> **spec:implements:** @kind:operation DisableVpcClassicLinkDnsSupport
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableVpcClassicLinkDnsSupport.spec.md

This action is deprecated. Disables ClassicLink DNS support for a VPC. If disabled, DNS hostnames resolve to public IP addresses when addressed between a linked EC2-Classic instance and instances in the VPC to which it's linked. You must specify a VPC ID in the request.

## Input Shape: DisableVpcClassicLinkDnsSupportRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| VpcId | Any  # complex shape |  | The ID of the VPC. |

## Output Shape: DisableVpcClassicLinkDnsSupportResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def disable_vpc_classic_link_dns_support(store, request: dict) -> dict:
    """This action is deprecated. Disables ClassicLink DNS support for a VPC. If disabled, DNS hostnames resolve to public IP addresses when addressed between a linked EC2-Classic instance and instances in t"""

```
