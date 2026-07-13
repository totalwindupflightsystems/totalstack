---
id: "@specs/aws/ec2/enable_vpc_classic_link_dns_support"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableVpcClassicLinkDnsSupport"
---

# EnableVpcClassicLinkDnsSupport

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_vpc_classic_link_dns_support
> **spec:implements:** @kind:operation EnableVpcClassicLinkDnsSupport
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableVpcClassicLinkDnsSupport.spec.md

This action is deprecated. Enables a VPC to support DNS hostname resolution for ClassicLink. If enabled, the DNS hostname of a linked EC2-Classic instance resolves to its private IP address when addressed from an instance in the VPC to which it's linked. Similarly, the DNS hostname of an instance in a VPC resolves to its private IP address when addressed from a linked EC2-Classic instance. You must specify a VPC ID in the request.

## Input Shape: EnableVpcClassicLinkDnsSupportRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| VpcId | Any  # complex shape |  | The ID of the VPC. |

## Output Shape: EnableVpcClassicLinkDnsSupportResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def enable_vpc_classic_link_dns_support(store, request: dict) -> dict:
    """This action is deprecated. Enables a VPC to support DNS hostname resolution for ClassicLink. If enabled, the DNS hostname of a linked EC2-Classic instance resolves to its private IP address when addre"""

```
