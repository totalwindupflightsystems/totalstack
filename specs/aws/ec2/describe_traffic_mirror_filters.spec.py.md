---
id: "@specs/aws/ec2/describe_traffic_mirror_filters"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeTrafficMirrorFilters"
---

# DescribeTrafficMirrorFilters

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_traffic_mirror_filters
> **spec:implements:** @kind:operation DescribeTrafficMirrorFilters
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeTrafficMirrorFilters.spec.md

Describes one or more Traffic Mirror filters.

## Input Shape: DescribeTrafficMirrorFiltersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. The possible values are: description : The Traffic Mirror filter description. traffic-mirror-filter |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| TrafficMirrorFilterIds | list[Any  # complex shape] |  | The ID of the Traffic Mirror filter. |

## Output Shape: DescribeTrafficMirrorFiltersResult

- **NextToken** (str): The token to use to retrieve the next page of results. The value is null when there are no more results to return.
- **TrafficMirrorFilters** (Any  # complex shape): Information about one or more Traffic Mirror filters.

## Implementation

```speclang
def describe_traffic_mirror_filters(store, request: dict) -> dict:
    """Describes one or more Traffic Mirror filters."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
