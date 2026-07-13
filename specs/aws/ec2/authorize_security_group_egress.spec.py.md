---
id: "@specs/aws/ec2/authorize_security_group_egress"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AuthorizeSecurityGroupEgress"
---

# AuthorizeSecurityGroupEgress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/authorize_security_group_egress
> **spec:implements:** @kind:operation AuthorizeSecurityGroupEgress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AuthorizeSecurityGroupEgress.spec.md

Adds the specified outbound (egress) rules to a security group. An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address ranges, the IP address ranges specified by a prefix list, or the instances that are associated with a source security group. For more information, see Security group rules . You must specify exactly one of the following destinations: an IPv4 or IPv6 address range, a prefix list, or a security group. You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP type and code. Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur. For examples of rules that you can add to security groups for specific access scenarios, see Security group rules for different use cases in the Amazon EC2 User Guide . For information about security group quotas, see Amazon VPC quotas in the Amazon VPC User Guide .

## Input Shape: AuthorizeSecurityGroupEgressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CidrIp | str |  | Not supported. Use IP permissions instead. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FromPort | int |  | Not supported. Use IP permissions instead. |
| GroupId | Any  # complex shape | ✓ | The ID of the security group. |
| IpPermissions | list[Any  # complex shape] |  | The permissions for the security group rules. |
| IpProtocol | str |  | Not supported. Use IP permissions instead. |
| SourceSecurityGroupName | str |  | Not supported. Use IP permissions instead. |
| SourceSecurityGroupOwnerId | str |  | Not supported. Use IP permissions instead. |
| TagSpecifications | list[Any  # complex shape] |  | The tags applied to the security group rule. |
| ToPort | int |  | Not supported. Use IP permissions instead. |

## Output Shape: AuthorizeSecurityGroupEgressResult

- **Return** (bool): Returns true if the request succeeds; otherwise, returns an error.
- **SecurityGroupRules** (list[Any  # complex shape]): Information about the outbound (egress) security group rules that were added.

## Implementation

```speclang
def authorize_security_group_egress(store, request: dict) -> dict:
    """Adds the specified outbound (egress) rules to a security group. An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 address ranges, the IP address ranges specified by a pr"""
    group_id = request.get("GroupId", "").strip() if isinstance(request.get("GroupId"), str) else request.get("GroupId")
    if not group_id:
        raise ValidationException("GroupId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AuthorizeSecurityGroupEgress", request)
```
