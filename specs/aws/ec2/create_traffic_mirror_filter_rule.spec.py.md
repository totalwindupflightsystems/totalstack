---
id: "@specs/aws/ec2/create_traffic_mirror_filter_rule"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTrafficMirrorFilterRule"
---

# CreateTrafficMirrorFilterRule

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_traffic_mirror_filter_rule
> **spec:implements:** @kind:operation CreateTrafficMirrorFilterRule
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTrafficMirrorFilterRule.spec.md

Creates a Traffic Mirror filter rule. A Traffic Mirror rule defines the Traffic Mirror source traffic to mirror. You need the Traffic Mirror filter ID when you create the rule.

## Input Shape: CreateTrafficMirrorFilterRuleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| Description | str |  | The description of the Traffic Mirror rule. |
| DestinationCidrBlock | str | ✓ | The destination CIDR block to assign to the Traffic Mirror rule. |
| DestinationPortRange | Any  # complex shape |  | The destination port range. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Protocol | int |  | The protocol, for example UDP, to assign to the Traffic Mirror rule. For information about the protocol value, see Proto |
| RuleAction | Any  # complex shape | ✓ | The action to take on the filtered traffic. |
| RuleNumber | int | ✓ | The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The |
| SourceCidrBlock | str | ✓ | The source CIDR block to assign to the Traffic Mirror rule. |
| SourcePortRange | Any  # complex shape |  | The source port range. |
| TagSpecifications | list[Any  # complex shape] |  | Traffic Mirroring tags specifications. |
| TrafficDirection | Any  # complex shape | ✓ | The type of traffic. |
| TrafficMirrorFilterId | Any  # complex shape | ✓ | The ID of the filter that this rule is associated with. |

## Output Shape: CreateTrafficMirrorFilterRuleResult

- **ClientToken** (str): Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H
- **TrafficMirrorFilterRule** (Any  # complex shape): The Traffic Mirror rule.

## Implementation

```speclang
def create_traffic_mirror_filter_rule(store, request: dict) -> dict:
    """Creates a Traffic Mirror filter rule. A Traffic Mirror rule defines the Traffic Mirror source traffic to mirror. You need the Traffic Mirror filter ID when you create the rule."""
    destination_cidr_block = request.get("DestinationCidrBlock", "").strip() if isinstance(request.get("DestinationCidrBlock"), str) else request.get("DestinationCidrBlock")
    if not destination_cidr_block:
        raise ValidationException("DestinationCidrBlock is required")
    rule_action = request.get("RuleAction", "").strip() if isinstance(request.get("RuleAction"), str) else request.get("RuleAction")
    if not rule_action:
        raise ValidationException("RuleAction is required")
    rule_number = request.get("RuleNumber", "").strip() if isinstance(request.get("RuleNumber"), str) else request.get("RuleNumber")
    if not rule_number:
        raise ValidationException("RuleNumber is required")
    source_cidr_block = request.get("SourceCidrBlock", "").strip() if isinstance(request.get("SourceCidrBlock"), str) else request.get("SourceCidrBlock")
    if not source_cidr_block:
        raise ValidationException("SourceCidrBlock is required")
    traffic_direction = request.get("TrafficDirection", "").strip() if isinstance(request.get("TrafficDirection"), str) else request.get("TrafficDirection")
    if not traffic_direction:
        raise ValidationException("TrafficDirection is required")
    traffic_mirror_filter_id = request.get("TrafficMirrorFilterId", "").strip() if isinstance(request.get("TrafficMirrorFilterId"), str) else request.get("TrafficMirrorFilterId")
    if not traffic_mirror_filter_id:
        raise ValidationException("TrafficMirrorFilterId is required")

    if store.traffic_mirror_filter_rules(destination_cidr_block):
        raise ResourceInUseException(f"Resource destination_cidr_block already exists")

    record = {
        "TrafficMirrorFilterId": traffic_mirror_filter_id,
        "TrafficDirection": traffic_direction,
        "RuleNumber": rule_number,
        "RuleAction": rule_action,
        "DestinationPortRange": destination_port_range,
        "SourcePortRange": source_port_range,
        "Protocol": protocol,
        "DestinationCidrBlock": destination_cidr_block,
        "SourceCidrBlock": source_cidr_block,
        "Description": description,
        "DryRun": dry_run,
        "ClientToken": client_token,
        "TagSpecifications": tag_specifications,
    }

    store.traffic_mirror_filter_rules(destination_cidr_block, record)

    return {
        "TrafficMirrorFilterRule": record.get("TrafficMirrorFilterRule", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
