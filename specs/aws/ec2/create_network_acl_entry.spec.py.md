---
id: "@specs/aws/ec2/create_network_acl_entry"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateNetworkAclEntry"
---

# CreateNetworkAclEntry

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_network_acl_entry
> **spec:implements:** @kind:operation CreateNetworkAclEntry
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateNetworkAclEntry.spec.md

Creates an entry (a rule) in a network ACL with the specified rule number. Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the ACL, we process the entries in the ACL according to the rule numbers, in ascending order. Each network ACL has a set of ingress rules and a separate set of egress rules. We recommend that you leave room between the rule numbers (for example, 100, 110, 120, ...), and not number them one right after the other (for example, 101, 102, 103, ...). This makes it easier to add a rule between existing ones without having to renumber the rules. After you add an entry, you can't modify it; you must either replace it, or create an entry and delete the old one. For more information about network ACLs, see Network ACLs in the Amazon VPC User Guide .

## Input Shape: CreateNetworkAclEntryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CidrBlock | str |  | The IPv4 network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ). We modify the specified CIDR blo |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Egress | bool | ✓ | Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). |
| IcmpTypeCode | Any  # complex shape |  | ICMP protocol: The ICMP or ICMPv6 type and code. Required if specifying protocol 1 (ICMP) or protocol 58 (ICMPv6) with a |
| Ipv6CidrBlock | str |  | The IPv6 network range to allow or deny, in CIDR notation (for example 2001:db8:1234:1a00::/64 ). |
| NetworkAclId | Any  # complex shape | ✓ | The ID of the network ACL. |
| PortRange | Any  # complex shape |  | TCP or UDP protocols: The range of ports the rule applies to. Required if specifying protocol 6 (TCP) or 17 (UDP). |
| Protocol | str | ✓ | The protocol number. A value of "-1" means all protocols. If you specify "-1" or a protocol number other than "6" (TCP), |
| RuleAction | Any  # complex shape | ✓ | Indicates whether to allow or deny the traffic that matches the rule. |
| RuleNumber | int | ✓ | The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number. Constrain |

## Implementation

```speclang
def create_network_acl_entry(store, request: dict) -> dict:
    """Creates an entry (a rule) in a network ACL with the specified rule number. Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a """
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

    if store.network_acl_entrys(network_acl_id):
        raise ResourceInUseException(f"Resource network_acl_id already exists")

    record = {
        "DryRun": dry_run,
        "NetworkAclId": network_acl_id,
        "RuleNumber": rule_number,
        "Protocol": protocol,
        "RuleAction": rule_action,
        "Egress": egress,
        "CidrBlock": cidr_block,
        "Ipv6CidrBlock": ipv6_cidr_block,
        "IcmpTypeCode": icmp_type_code,
        "PortRange": port_range,
    }

    store.network_acl_entrys(network_acl_id, record)

    return {
    }
```
