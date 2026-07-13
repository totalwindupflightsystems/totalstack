---
id: "@specs/aws/ec2/disassociate_security_group_vpc"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateSecurityGroupVpc"
---

# DisassociateSecurityGroupVpc

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_security_group_vpc
> **spec:implements:** @kind:operation DisassociateSecurityGroupVpc
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateSecurityGroupVpc.spec.md

Disassociates a security group from a VPC. You cannot disassociate the security group if any Elastic network interfaces in the associated VPC are still associated with the security group. Note that the disassociation is asynchronous and you can check the status of the request with DescribeSecurityGroupVpcAssociations .

## Input Shape: DisassociateSecurityGroupVpcRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GroupId | Any  # complex shape | ✓ | A security group ID. |
| VpcId | str | ✓ | A VPC ID. |

## Output Shape: DisassociateSecurityGroupVpcResult

- **State** (Any  # complex shape): The state of the disassociation.

## Implementation

```speclang
def disassociate_security_group_vpc(store, request: dict) -> dict:
    """Disassociates a security group from a VPC. You cannot disassociate the security group if any Elastic network interfaces in the associated VPC are still associated with the security group. Note that th"""
    group_id = request.get("GroupId", "").strip() if isinstance(request.get("GroupId"), str) else request.get("GroupId")
    if not group_id:
        raise ValidationException("GroupId is required")
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DisassociateSecurityGroupVpc", request)
```
