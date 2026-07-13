---
id: "@specs/aws/ec2/update_security_group_rule_descriptions_ingress"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_UpdateSecurityGroupRuleDescriptionsIngress"
---

# UpdateSecurityGroupRuleDescriptionsIngress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/update_security_group_rule_descriptions_ingress
> **spec:implements:** @kind:operation UpdateSecurityGroupRuleDescriptionsIngress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_UpdateSecurityGroupRuleDescriptionsIngress.spec.md

Updates the description of an ingress (inbound) security group rule. You can replace an existing description, or add a description to a rule that did not have one previously. You can remove a description for a security group rule by omitting the description parameter in the request.

## Input Shape: UpdateSecurityGroupRuleDescriptionsIngressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GroupId | Any  # complex shape |  | The ID of the security group. You must specify either the security group ID or the security group name in the request. F |
| GroupName | Any  # complex shape |  | [Default VPC] The name of the security group. You must specify either the security group ID or the security group name.  |
| IpPermissions | list[Any  # complex shape] |  | The IP permissions for the security group rule. You must specify either IP permissions or a description. |
| SecurityGroupRuleDescriptions | list[Any  # complex shape] |  | The description for the ingress security group rules. You must specify either a description or IP permissions. |

## Output Shape: UpdateSecurityGroupRuleDescriptionsIngressResult

- **Return** (bool): Returns true if the request succeeds; otherwise, returns an error.

## Implementation

```speclang
def update_security_group_rule_descriptions_ingress(store, request: dict) -> dict:
    """Updates the description of an ingress (inbound) security group rule. You can replace an existing description, or add a description to a rule that did not have one previously. You can remove a descript"""

```
