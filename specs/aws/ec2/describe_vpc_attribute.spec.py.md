---
id: "@specs/aws/ec2/describe_vpc_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpcAttribute"
---

# DescribeVpcAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpc_attribute
> **spec:implements:** @kind:operation DescribeVpcAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpcAttribute.spec.md

Describes the specified attribute of the specified VPC. You can specify only one attribute at a time.

## Input Shape: DescribeVpcAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape | ✓ | The VPC attribute. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Output Shape: DescribeVpcAttributeResult

- **EnableDnsHostnames** (Any  # complex shape): Indicates whether the instances launched in the VPC get DNS hostnames. If this attribute is true , instances in the VPC 
- **EnableDnsSupport** (Any  # complex shape): Indicates whether DNS resolution is enabled for the VPC. If this attribute is true , the Amazon DNS server resolves DNS 
- **EnableNetworkAddressUsageMetrics** (Any  # complex shape): Indicates whether Network Address Usage metrics are enabled for your VPC.
- **VpcId** (str): The ID of the VPC.

## Implementation

```speclang
def describe_vpc_attribute(store, request: dict) -> dict:
    """Describes the specified attribute of the specified VPC. You can specify only one attribute at a time."""
    attribute = request.get("Attribute", "").strip() if isinstance(request.get("Attribute"), str) else request.get("Attribute")
    if not attribute:
        raise ValidationException("Attribute is required")
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    resource = store.vpc_attributes(vpc_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpc_id not found")
    return {"VpcId": vpc_id, **resource}
```
