---
id: "@specs/aws/ec2/delete_traffic_mirror_filter_rule"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTrafficMirrorFilterRule"
---

# DeleteTrafficMirrorFilterRule

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_traffic_mirror_filter_rule
> **spec:implements:** @kind:operation DeleteTrafficMirrorFilterRule
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTrafficMirrorFilterRule.spec.md

Deletes the specified Traffic Mirror rule.

## Input Shape: DeleteTrafficMirrorFilterRuleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TrafficMirrorFilterRuleId | Any  # complex shape | ✓ | The ID of the Traffic Mirror rule. |

## Output Shape: DeleteTrafficMirrorFilterRuleResult

- **TrafficMirrorFilterRuleId** (str): The ID of the deleted Traffic Mirror rule.

## Implementation

```speclang
def delete_traffic_mirror_filter_rule(store, request: dict) -> dict:
    """Deletes the specified Traffic Mirror rule."""
    traffic_mirror_filter_rule_id = request.get("TrafficMirrorFilterRuleId", "").strip() if isinstance(request.get("TrafficMirrorFilterRuleId"), str) else request.get("TrafficMirrorFilterRuleId")

    if not store.traffic_mirror_filter_rules(traffic_mirror_filter_rule_id):
        raise ResourceNotFoundException(f"Resource traffic_mirror_filter_rule_id not found")
    store.delete_traffic_mirror_filter_rules(traffic_mirror_filter_rule_id)
    return {}
```
