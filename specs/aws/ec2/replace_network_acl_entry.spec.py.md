---
id: "@specs/aws/ec2/replace_network_acl_entry"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ReplaceNetworkAclEntry"
---

# ReplaceNetworkAclEntry

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/replace_network_acl_entry
> **spec:implements:** @kind:operation ReplaceNetworkAclEntry
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ReplaceNetworkAclEntry.spec.md

Replaces an entry (rule) in a network ACL. For more information, see Network ACLs in the Amazon VPC User Guide .

## Input Shape: ReplaceNetworkAclEntryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CidrBlock | str |  | The IPv4 network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ). |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Egress | bool | ✓ | Indicates whether to replace the egress rule. Default: If no value is specified, we replace the ingress rule. |
| IcmpTypeCode | Any  # complex shape |  | ICMP protocol: The ICMP or ICMPv6 type and code. Required if specifying protocol 1 (ICMP) or protocol 58 (ICMPv6) with a |
| Ipv6CidrBlock | str |  | The IPv6 network range to allow or deny, in CIDR notation (for example 2001:bd8:1234:1a00::/64 ). |
| NetworkAclId | Any  # complex shape | ✓ | The ID of the ACL. |
| PortRange | Any  # complex shape |  | TCP or UDP protocols: The range of ports the rule applies to. Required if specifying protocol 6 (TCP) or 17 (UDP). |
| Protocol | str | ✓ | The protocol number. A value of "-1" means all protocols. If you specify "-1" or a protocol number other than "6" (TCP), |
| RuleAction | Any  # complex shape | ✓ | Indicates whether to allow or deny the traffic that matches the rule. |
| RuleNumber | int | ✓ | The rule number of the entry to replace. |

## Implementation

```speclang
def replace_network_acl_entry(store, request: dict) -> dict:
    """Replaces an entry (rule) in a network ACL. For more information, see Network ACLs in the Amazon VPC User Guide ."""
    egress = request.get("Egress", "").strip() if isinstance(request.get("Egress"), str) else request.get("Egress")
    if not egress:
        raise ValidationException("Egress is required")
    network_acl_id = request.get("NetworkAclId", "").strip() if isinstance(request.get("NetworkAclId"), str) else request.get("NetworkAclId")
    if not network_acl_id:
        raise ValidationException("NetworkAclId is required")
    protocol = request.get("Protocol", "").strip() if isinstance(request.get("Protocol"), str) else request.get("Protocol")
    if not protocol:
        raise ValidationException("Protocol is required")
    rule_action = request.get("RuleAction", "").strip() if isinstance(request.get("RuleAction"), str) else request.get("RuleAction")
    if not rule_action:
        raise ValidationException("RuleAction is required")
    rule_number = request.get("RuleNumber", "").strip() if isinstance(request.get("RuleNumber"), str) else request.get("RuleNumber")
    if not rule_number:
        raise ValidationException("RuleNumber is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ReplaceNetworkAclEntry", request)
```
