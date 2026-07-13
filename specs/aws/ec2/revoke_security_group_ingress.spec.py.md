---
id: "@specs/aws/ec2/revoke_security_group_ingress"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RevokeSecurityGroupIngress"
---

# RevokeSecurityGroupIngress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/revoke_security_group_ingress
> **spec:implements:** @kind:operation RevokeSecurityGroupIngress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RevokeSecurityGroupIngress.spec.md

Removes the specified inbound (ingress) rules from a security group. You can specify rules using either rule IDs or security group rule properties. If you use rule properties, the values that you specify (for example, ports) must match the existing rule's values exactly. Each rule has a protocol, from and to ports, and source (CIDR range, security group, or prefix list). For the TCP and UDP protocols, you must also specify the destination port or range of ports. For the ICMP protocol, you must also specify the ICMP type and code. If the security group rule has a description, you do not need to specify the description to revoke the rule. For a default VPC, if the values you specify do not match the existing rule's values, no error is returned, and the output describes the security group rules that were not revoked. For a non-default VPC, if the values you specify do not match the existing rule's values, an InvalidPermission.NotFound client error is returned, and no rules are revoked. Amazon Web Services recommends that you describe the security group to verify that the rules were removed. Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.

## Input Shape: RevokeSecurityGroupIngressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CidrIp | str |  | The CIDR IP address range. You can't specify this parameter when specifying a source security group. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FromPort | int |  | If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP, this is the ICMP type or -1 |
| GroupId | Any  # complex shape |  | The ID of the security group. |
| GroupName | Any  # complex shape |  | [Default VPC] The name of the security group. You must specify either the security group ID or the security group name i |
| IpPermissions | list[Any  # complex shape] |  | The sets of IP permissions. You can't specify a source security group and a CIDR IP address range in the same set of per |
| IpProtocol | str |  | The IP protocol name ( tcp , udp , icmp ) or number (see Protocol Numbers ). Use -1 to specify all. |
| SecurityGroupRuleIds | list[str] |  | The IDs of the security group rules. |
| SourceSecurityGroupName | str |  | [Default VPC] The name of the source security group. You can't specify this parameter in combination with the following  |
| SourceSecurityGroupOwnerId | str |  | Not supported. |
| ToPort | int |  | If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP, this is the ICMP code or -1 ( |

## Output Shape: RevokeSecurityGroupIngressResult

- **Return** (bool): Returns true if the request succeeds; otherwise, returns an error.
- **RevokedSecurityGroupRules** (list[Any  # complex shape]): Details about the revoked security group rules.
- **UnknownIpPermissions** (list[Any  # complex shape]): The inbound rules that were unknown to the service. In some cases, unknownIpPermissionSet might be in a different format

## Implementation

```speclang
def revoke_security_group_ingress(store, request: dict) -> dict:
    """Removes the specified inbound (ingress) rules from a security group. You can specify rules using either rule IDs or security group rule properties. If you use rule properties, the values that you spec"""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RevokeSecurityGroupIngress", request)
```
