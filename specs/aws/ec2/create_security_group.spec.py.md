---
id: "@specs/aws/ec2/create_security_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateSecurityGroup"
---

# CreateSecurityGroup

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_security_group
> **spec:implements:** @kind:operation CreateSecurityGroup
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateSecurityGroup.spec.md

Creates a security group. A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. For more information, see Amazon EC2 security groups in the Amazon EC2 User Guide and Security groups for your VPC in the Amazon VPC User Guide . When you create a security group, you specify a friendly name of your choice. You can't have two security groups for the same VPC with the same name. You have a default security group for use in your VPC. If you don't specify a security group when you launch an instance, the instance is launched into the appropriate default security group. A default security group includes a default rule that grants instances unrestricted network access to each other. You can add or remove rules from your security groups using AuthorizeSecurityGroupIngress , AuthorizeSecurityGroupEgress , RevokeSecurityGroupIngress , and RevokeSecurityGroupEgress . For more information about VPC security group limits, see Amazon VPC Limits .

## Input Shape: CreateSecurityGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | str | ✓ | A description for the security group. Constraints: Up to 255 characters in length Valid characters: a-z, A-Z, 0-9, space |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GroupName | str | ✓ | The name of the security group. Names are case-insensitive and must be unique within the VPC. Constraints: Up to 255 cha |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the security group. |
| VpcId | Any  # complex shape |  | The ID of the VPC. Required for a nondefault VPC. |

## Output Shape: CreateSecurityGroupResult

- **GroupId** (str): The ID of the security group.
- **SecurityGroupArn** (str): The security group ARN.
- **Tags** (list[Any  # complex shape]): The tags assigned to the security group.

## Implementation

```speclang
def create_security_group(store, request: dict) -> dict:
    """Creates a security group. A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. For more information, see Amazon EC2 security groups in the Amazon EC2 """
    description = request.get("Description", "").strip() if isinstance(request.get("Description"), str) else request.get("Description")
    if not description:
        raise ValidationException("Description is required")
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")
    if not group_name:
        raise ValidationException("GroupName is required")

    if store.security_groups(group_name):
        raise ResourceInUseException(f"Resource group_name already exists")

    record = {
        "Description": description,
        "GroupName": group_name,
        "VpcId": vpc_id,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.security_groups(group_name, record)

    return {
        "GroupId": record.get("GroupId", {}),
        "Tags": record.get("Tags", {}),
        "SecurityGroupArn": record.get("SecurityGroupArn", {}),
    }
```
