---
id: "@specs/aws/ec2/get_capacity_manager_metric_dimensions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetCapacityManagerMetricDimensions"
---

# GetCapacityManagerMetricDimensions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_capacity_manager_metric_dimensions
> **spec:implements:** @kind:operation GetCapacityManagerMetricDimensions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetCapacityManagerMetricDimensions.spec.md

Retrieves the available dimension values for capacity metrics within a specified time range. This is useful for discovering what accounts, regions, instance families, and other dimensions have data available for filtering and grouping.

## Input Shape: GetCapacityManagerMetricDimensionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EndTime | Any  # complex shape | ✓ | The end time for the dimension query, in ISO 8601 format. Only dimensions with data in this time range will be returned. |
| FilterBy | Any  # complex shape |  | Conditions to filter which dimension values are returned. Each filter specifies a dimension, comparison operator, and va |
| GroupBy | Any  # complex shape | ✓ | The dimensions to group by when retrieving available dimension values. This determines which dimension combinations are  |
| MaxResults | Any  # complex shape |  | The maximum number of dimension combinations to return. Valid range is 1 to 1000. Use with NextToken for pagination. |
| MetricNames | Any  # complex shape | ✓ | The metric names to use as an additional filter when retrieving dimensions. Only dimensions that have data for these met |
| NextToken | Any  # complex shape |  | The token for the next page of results. Use this value in a subsequent call to retrieve additional dimension values. |
| StartTime | Any  # complex shape | ✓ | The start time for the dimension query, in ISO 8601 format. Only dimensions with data in this time range will be returne |

## Output Shape: GetCapacityManagerMetricDimensionsResult

- **MetricDimensionResults** (Any  # complex shape): The available dimension combinations that have data within the specified time range and filters.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_capacity_manager_metric_dimensions(store, request: dict) -> dict:
    """Retrieves the available dimension values for capacity metrics within a specified time range. This is useful for discovering what accounts, regions, instance families, and other dimensions have data av"""
    end_time = request.get("EndTime", "").strip() if isinstance(request.get("EndTime"), str) else request.get("EndTime")
    if not end_time:
        raise ValidationException("EndTime is required")
    group_by = request.get("GroupBy", "").strip() if isinstance(request.get("GroupBy"), str) else request.get("GroupBy")
    if not group_by:
        raise ValidationException("GroupBy is required")
    metric_names = request.get("MetricNames", "").strip() if isinstance(request.get("MetricNames"), str) else request.get("MetricNames")
    if not metric_names:
        raise ValidationException("MetricNames is required")
    start_time = request.get("StartTime", "").strip() if isinstance(request.get("StartTime"), str) else request.get("StartTime")
    if not start_time:
        raise ValidationException("StartTime is required")

    resource = store.capacity_manager_metric_dimensionss(metric_names)
    if not resource:
        raise ResourceNotFoundException(f"Resource metric_names not found")
    return {"MetricNames": metric_names, **resource}
```
