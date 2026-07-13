---
id: "@specs/aws/ec2/revoke_security_group_egress"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RevokeSecurityGroupEgress"
---

# RevokeSecurityGroupEgress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/revoke_security_group_egress
> **spec:implements:** @kind:operation RevokeSecurityGroupEgress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RevokeSecurityGroupEgress.spec.md

Removes the specified outbound (egress) rules from the specified security group. You can specify rules using either rule IDs or security group rule properties. If you use rule properties, the values that you specify (for example, ports) must match the existing rule's values exactly. Each rule has a protocol, from and to ports, and destination (CIDR range, security group, or prefix list). For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code. If the security group rule has a description, you do not need to specify the description to revoke the rule. For a default VPC, if the values you specify do not match the existing rule's values, no error is returned, and the output describes the security group rules that were not revoked. Amazon Web Services recommends that you describe the security group to verify that the rules were removed. Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.

## Input Shape: RevokeSecurityGroupEgressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CidrIp | str |  | Not supported. Use a set of IP permissions to specify the CIDR. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FromPort | int |  | Not supported. Use a set of IP permissions to specify the port. |
| GroupId | Any  # complex shape | ✓ | The ID of the security group. |
| IpPermissions | list[Any  # complex shape] |  | The sets of IP permissions. You can't specify a destination security group and a CIDR IP address range in the same set o |
| IpProtocol | str |  | Not supported. Use a set of IP permissions to specify the protocol name or number. |
| SecurityGroupRuleIds | list[str] |  | The IDs of the security group rules. |
| SourceSecurityGroupName | str |  | Not supported. Use a set of IP permissions to specify a destination security group. |
| SourceSecurityGroupOwnerId | str |  | Not supported. Use a set of IP permissions to specify a destination security group. |
| ToPort | int |  | Not supported. Use a set of IP permissions to specify the port. |

## Output Shape: RevokeSecurityGroupEgressResult

- **Return** (bool): Returns true if the request succeeds; otherwise, returns an error.
- **RevokedSecurityGroupRules** (list[Any  # complex shape]): Details about the revoked security group rules.
- **UnknownIpPermissions** (list[Any  # complex shape]): The outbound rules that were unknown to the service. In some cases, unknownIpPermissionSet might be in a different forma

## Implementation

```speclang
def revoke_security_group_egress(store, request: dict) -> dict:
    """Removes the specified outbound (egress) rules from the specified security group. You can specify rules using either rule IDs or security group rule properties. If you use rule properties, the values t"""
    group_id = request.get("GroupId", "").strip() if isinstance(request.get("GroupId"), str) else request.get("GroupId")
    if not group_id:
        raise ValidationException("GroupId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RevokeSecurityGroupEgress", request)
```
