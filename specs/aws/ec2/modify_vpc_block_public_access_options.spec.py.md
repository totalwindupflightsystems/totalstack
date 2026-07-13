---
id: "@specs/aws/ec2/modify_vpc_block_public_access_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpcBlockPublicAccessOptions"
---

# ModifyVpcBlockPublicAccessOptions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpc_block_public_access_options
> **spec:implements:** @kind:operation ModifyVpcBlockPublicAccessOptions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpcBlockPublicAccessOptions.spec.md

Modify VPC Block Public Access (BPA) options. VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. To learn more about VPC BPA, see Block public access to VPCs and subnets in the Amazon VPC User Guide .

## Input Shape: ModifyVpcBlockPublicAccessOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InternetGatewayBlockMode | Any  # complex shape | ✓ | The mode of VPC BPA. off : VPC BPA is not enabled and traffic is allowed to and from internet gateways and egress-only i |

## Output Shape: ModifyVpcBlockPublicAccessOptionsResult

- **VpcBlockPublicAccessOptions** (Any  # complex shape): Details related to the VPC Block Public Access (BPA) options.

## Implementation

```speclang
def modify_vpc_block_public_access_options(store, request: dict) -> dict:
    """Modify VPC Block Public Access (BPA) options. VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet"""
    internet_gateway_block_mode = request.get("InternetGatewayBlockMode", "").strip() if isinstance(request.get("InternetGatewayBlockMode"), str) else request.get("InternetGatewayBlockMode")
    if not internet_gateway_block_mode:
        raise ValidationException("InternetGatewayBlockMode is required")

    resource = store.vpc_block_public_access_optionss(internet_gateway_block_mode)
    if not resource:
        raise ResourceNotFoundException(f"Resource internet_gateway_block_mode not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.vpc_block_public_access_optionss(internet_gateway_block_mode, resource)
    return resource
```
