---
id: "@specs/aws/ec2/modify_security_group_rules"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifySecurityGroupRules"
---

# ModifySecurityGroupRules

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_security_group_rules
> **spec:implements:** @kind:operation ModifySecurityGroupRules
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifySecurityGroupRules.spec.md

Modifies the rules of a security group.

## Input Shape: ModifySecurityGroupRulesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GroupId | Any  # complex shape | ✓ | The ID of the security group. |
| SecurityGroupRules | list[Any  # complex shape] | ✓ | Information about the security group properties to update. |

## Output Shape: ModifySecurityGroupRulesResult

- **Return** (bool): Returns true if the request succeeds; otherwise, returns an error.

## Implementation

```speclang
def modify_security_group_rules(store, request: dict) -> dict:
    """Modifies the rules of a security group."""
    group_id = request.get("GroupId", "").strip() if isinstance(request.get("GroupId"), str) else request.get("GroupId")
    if not group_id:
        raise ValidationException("GroupId is required")
    security_group_rules = request.get("SecurityGroupRules", "").strip() if isinstance(request.get("SecurityGroupRules"), str) else request.get("SecurityGroupRules")
    if not security_group_rules:
        raise ValidationException("SecurityGroupRules is required")

    resource = store.security_group_ruless(group_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource group_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.security_group_ruless(group_id, resource)
    return resource
```
