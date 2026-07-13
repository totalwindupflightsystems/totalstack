---
id: "@specs/aws/ec2/delete_security_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteSecurityGroup"
---

# DeleteSecurityGroup

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_security_group
> **spec:implements:** @kind:operation DeleteSecurityGroup
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteSecurityGroup.spec.md

Deletes a security group. If you attempt to delete a security group that is associated with an instance or network interface, is referenced by another security group in the same VPC, or has a VPC association, the operation fails with DependencyViolation .

## Input Shape: DeleteSecurityGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GroupId | Any  # complex shape |  | The ID of the security group. |
| GroupName | Any  # complex shape |  | [Default VPC] The name of the security group. You can specify either the security group name or the security group ID. F |

## Output Shape: DeleteSecurityGroupResult

- **GroupId** (Any  # complex shape): The ID of the deleted security group.
- **Return** (bool): Returns true if the request succeeds; otherwise, returns an error.

## Implementation

```speclang
def delete_security_group(store, request: dict) -> dict:
    """Deletes a security group. If you attempt to delete a security group that is associated with an instance or network interface, is referenced by another security group in the same VPC, or has a VPC asso"""

    return {}
```
