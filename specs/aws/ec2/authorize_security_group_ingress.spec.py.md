---
id: "@specs/aws/ec2/authorize_security_group_ingress"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AuthorizeSecurityGroupIngress"
---

# AuthorizeSecurityGroupIngress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/authorize_security_group_ingress
> **spec:implements:** @kind:operation AuthorizeSecurityGroupIngress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AuthorizeSecurityGroupIngress.spec.md

Adds the specified inbound (ingress) rules to a security group. An inbound rule permits instances to receive traffic from the specified IPv4 or IPv6 address range, the IP address ranges that are specified by a prefix list, or the instances that are associated with a destination security group. For more information, see Security group rules . You must specify exactly one of the following sources: an IPv4 or IPv6 address range, a prefix list, or a security group. You must specify a protocol for each rule (for example, TCP). If the protocol is TCP or UDP, you must also specify a port or port range. If the protocol is ICMP or ICMPv6, you must also specify the ICMP/ICMPv6 type and code. Rule changes are propagated to instances associated with the security group as quickly as possible. However, a small delay might occur. For examples of rules that you can add to security groups for specific access scenarios, see Security group rules for different use cases in the Amazon EC2 User Guide . For more information about security group quotas, see Amazon VPC quotas in the Amazon VPC User Guide .

## Input Shape: AuthorizeSecurityGroupIngressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CidrIp | str |  | The IPv4 address range, in CIDR format. Amazon Web Services canonicalizes IPv4 and IPv6 CIDRs. For example, if you speci |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FromPort | int |  | If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP, this is the ICMP type or -1 |
| GroupId | Any  # complex shape |  | The ID of the security group. |
| GroupName | Any  # complex shape |  | [Default VPC] The name of the security group. For security groups for a default VPC you can specify either the ID or the |
| IpPermissions | list[Any  # complex shape] |  | The permissions for the security group rules. |
| IpProtocol | str |  | The IP protocol name ( tcp , udp , icmp ) or number (see Protocol Numbers ). To specify all protocols, use -1 . To speci |
| SourceSecurityGroupName | str |  | [Default VPC] The name of the source security group. The rule grants full ICMP, UDP, and TCP access. To create a rule wi |
| SourceSecurityGroupOwnerId | str |  | The Amazon Web Services account ID for the source security group, if the source security group is in a different account |
| TagSpecifications | list[Any  # complex shape] |  | The tags applied to the security group rule. |
| ToPort | int |  | If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP, this is the ICMP code or -1 ( |

## Output Shape: AuthorizeSecurityGroupIngressResult

- **Return** (bool): Returns true if the request succeeds; otherwise, returns an error.
- **SecurityGroupRules** (list[Any  # complex shape]): Information about the inbound (ingress) security group rules that were added.

## Implementation

```speclang
def authorize_security_group_ingress(store, request: dict) -> dict:
    """Adds the specified inbound (ingress) rules to a security group. An inbound rule permits instances to receive traffic from the specified IPv4 or IPv6 address range, the IP address ranges that are speci"""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AuthorizeSecurityGroupIngress", request)
```
