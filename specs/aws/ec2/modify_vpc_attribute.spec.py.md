---
id: "@specs/aws/ec2/modify_vpc_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpcAttribute"
---

# ModifyVpcAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpc_attribute
> **spec:implements:** @kind:operation ModifyVpcAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpcAttribute.spec.md

Modifies the specified attribute of the specified VPC.

## Input Shape: ModifyVpcAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| EnableDnsHostnames | Any  # complex shape |  | Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostname |
| EnableDnsSupport | Any  # complex shape |  | Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at  |
| EnableNetworkAddressUsageMetrics | Any  # complex shape |  | Indicates whether Network Address Usage metrics are enabled for your VPC. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Implementation

```speclang
def modify_vpc_attribute(store, request: dict) -> dict:
    """Modifies the specified attribute of the specified VPC."""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    resource = store.vpc_attributes(vpc_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpc_id not found")

    # Update mutable fields
    if "EnableDnsHostnames" in request:
        resource["EnableDnsHostnames"] = enable_dns_hostnames
    if "EnableDnsSupport" in request:
        resource["EnableDnsSupport"] = enable_dns_support
    if "EnableNetworkAddressUsageMetrics" in request:
        resource["EnableNetworkAddressUsageMetrics"] = enable_network_address_usage_metrics

    store.vpc_attributes(vpc_id, resource)
    return resource
```
