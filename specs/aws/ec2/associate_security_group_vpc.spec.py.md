---
id: "@specs/aws/ec2/associate_security_group_vpc"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateSecurityGroupVpc"
---

# AssociateSecurityGroupVpc

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_security_group_vpc
> **spec:implements:** @kind:operation AssociateSecurityGroupVpc
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateSecurityGroupVpc.spec.md

Associates a security group with another VPC in the same Region. This enables you to use the same security group with network interfaces and instances in the specified VPC. The VPC you want to associate the security group with must be in the same Region. You can associate the security group with another VPC if your account owns the VPC or if the VPC was shared with you. You must own the security group. You cannot use this feature with default security groups. You cannot use this feature with the default VPC.

## Input Shape: AssociateSecurityGroupVpcRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GroupId | Any  # complex shape | ✓ | A security group ID. |
| VpcId | Any  # complex shape | ✓ | A VPC ID. |

## Output Shape: AssociateSecurityGroupVpcResult

- **State** (Any  # complex shape): The state of the association.

## Implementation

```speclang
def associate_security_group_vpc(store, request: dict) -> dict:
    """Associates a security group with another VPC in the same Region. This enables you to use the same security group with network interfaces and instances in the specified VPC. The VPC you want to associa"""
    group_id = request.get("GroupId", "").strip() if isinstance(request.get("GroupId"), str) else request.get("GroupId")
    if not group_id:
        raise ValidationException("GroupId is required")
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateSecurityGroupVpc", request)
```
