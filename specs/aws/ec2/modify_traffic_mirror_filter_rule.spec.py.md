---
id: "@specs/aws/ec2/modify_traffic_mirror_filter_rule"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyTrafficMirrorFilterRule"
---

# ModifyTrafficMirrorFilterRule

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_traffic_mirror_filter_rule
> **spec:implements:** @kind:operation ModifyTrafficMirrorFilterRule
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyTrafficMirrorFilterRule.spec.md

Modifies the specified Traffic Mirror rule. DestinationCidrBlock and SourceCidrBlock must both be an IPv4 range or an IPv6 range.

## Input Shape: ModifyTrafficMirrorFilterRuleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | str |  | The description to assign to the Traffic Mirror rule. |
| DestinationCidrBlock | str |  | The destination CIDR block to assign to the Traffic Mirror rule. |
| DestinationPortRange | Any  # complex shape |  | The destination ports that are associated with the Traffic Mirror rule. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Protocol | int |  | The protocol, for example TCP, to assign to the Traffic Mirror rule. |
| RemoveFields | list[Any  # complex shape] |  | The properties that you want to remove from the Traffic Mirror filter rule. When you remove a property from a Traffic Mi |
| RuleAction | Any  # complex shape |  | The action to assign to the rule. |
| RuleNumber | int |  | The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The |
| SourceCidrBlock | str |  | The source CIDR block to assign to the Traffic Mirror rule. |
| SourcePortRange | Any  # complex shape |  | The port range to assign to the Traffic Mirror rule. |
| TrafficDirection | Any  # complex shape |  | The type of traffic to assign to the rule. |
| TrafficMirrorFilterRuleId | Any  # complex shape | ✓ | The ID of the Traffic Mirror rule. |

## Output Shape: ModifyTrafficMirrorFilterRuleResult

- **TrafficMirrorFilterRule** (Any  # complex shape): Tags are not returned for ModifyTrafficMirrorFilterRule. A Traffic Mirror rule.

## Implementation

```speclang
def modify_traffic_mirror_filter_rule(store, request: dict) -> dict:
    """Modifies the specified Traffic Mirror rule. DestinationCidrBlock and SourceCidrBlock must both be an IPv4 range or an IPv6 range."""
    traffic_mirror_filter_rule_id = request.get("TrafficMirrorFilterRuleId", "").strip() if isinstance(request.get("TrafficMirrorFilterRuleId"), str) else request.get("TrafficMirrorFilterRuleId")
    if not traffic_mirror_filter_rule_id:
        raise ValidationException("TrafficMirrorFilterRuleId is required")

    resource = store.traffic_mirror_filter_rules(traffic_mirror_filter_rule_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource traffic_mirror_filter_rule_id not found")

    # Update mutable fields
    if "TrafficDirection" in request:
        resource["TrafficDirection"] = traffic_direction
    if "RuleNumber" in request:
        resource["RuleNumber"] = rule_number
    if "RuleAction" in request:
        resource["RuleAction"] = rule_action
    if "DestinationPortRange" in request:
        resource["DestinationPortRange"] = destination_port_range
    if "SourcePortRange" in request:
        resource["SourcePortRange"] = source_port_range
    if "Protocol" in request:
        resource["Protocol"] = protocol
    if "DestinationCidrBlock" in request:
        resource["DestinationCidrBlock"] = destination_cidr_block
    if "SourceCidrBlock" in request:
        resource["SourceCidrBlock"] = source_cidr_block
    if "Description" in request:
        resource["Description"] = description
    if "RemoveFields" in request:
        resource["RemoveFields"] = remove_fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.traffic_mirror_filter_rules(traffic_mirror_filter_rule_id, resource)
    return resource
```
