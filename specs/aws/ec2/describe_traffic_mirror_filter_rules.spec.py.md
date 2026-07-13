---
id: "@specs/aws/ec2/describe_traffic_mirror_filter_rules"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeTrafficMirrorFilterRules"
---

# DescribeTrafficMirrorFilterRules

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_traffic_mirror_filter_rules
> **spec:implements:** @kind:operation DescribeTrafficMirrorFilterRules
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeTrafficMirrorFilterRules.spec.md

Describe traffic mirror filters that determine the traffic that is mirrored.

## Input Shape: DescribeTrafficMirrorFilterRulesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | Traffic mirror filters. traffic-mirror-filter-rule-id : The ID of the Traffic Mirror rule. traffic-mirror-filter-id : Th |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| TrafficMirrorFilterId | Any  # complex shape |  | Traffic filter ID. |
| TrafficMirrorFilterRuleIds | list[Any  # complex shape] |  | Traffic filter rule IDs. |

## Output Shape: DescribeTrafficMirrorFilterRulesResult

- **NextToken** (str): The token to use to retrieve the next page of results. The value is null when there are no more results to return.
- **TrafficMirrorFilterRules** (Any  # complex shape): Traffic mirror rules.

## Implementation

```speclang
def describe_traffic_mirror_filter_rules(store, request: dict) -> dict:
    """Describe traffic mirror filters that determine the traffic that is mirrored."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
