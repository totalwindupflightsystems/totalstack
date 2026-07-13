---
id: "@specs/aws/ec2/describe_traffic_mirror_targets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeTrafficMirrorTargets"
---

# DescribeTrafficMirrorTargets

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_traffic_mirror_targets
> **spec:implements:** @kind:operation DescribeTrafficMirrorTargets
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeTrafficMirrorTargets.spec.md

Information about one or more Traffic Mirror targets.

## Input Shape: DescribeTrafficMirrorTargetsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. The possible values are: description : The Traffic Mirror target description. network-interface-id  |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| TrafficMirrorTargetIds | list[Any  # complex shape] |  | The ID of the Traffic Mirror targets. |

## Output Shape: DescribeTrafficMirrorTargetsResult

- **NextToken** (str): The token to use to retrieve the next page of results. The value is null when there are no more results to return.
- **TrafficMirrorTargets** (Any  # complex shape): Information about one or more Traffic Mirror targets.

## Implementation

```speclang
def describe_traffic_mirror_targets(store, request: dict) -> dict:
    """Information about one or more Traffic Mirror targets."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
