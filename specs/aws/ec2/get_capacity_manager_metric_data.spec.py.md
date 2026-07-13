---
id: "@specs/aws/ec2/get_capacity_manager_metric_data"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetCapacityManagerMetricData"
---

# GetCapacityManagerMetricData

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_capacity_manager_metric_data
> **spec:implements:** @kind:operation GetCapacityManagerMetricData
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetCapacityManagerMetricData.spec.md

Retrieves capacity usage metrics for your EC2 resources. Returns time-series data for metrics like unused capacity, utilization rates, and costs across On-Demand, Spot, and Capacity Reservations. Data can be grouped and filtered by various dimensions such as region, account, and instance family.

## Input Shape: GetCapacityManagerMetricDataRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EndTime | Any  # complex shape | ✓ | The end time for the metric data query, in ISO 8601 format. If the end time is beyond the latest ingested data, it will  |
| FilterBy | Any  # complex shape |  | Conditions to filter the metric data. Each filter specifies a dimension, comparison operator ('equals', 'in'), and value |
| GroupBy | Any  # complex shape |  | The dimensions by which to group the metric data. This determines how the data is aggregated and returned. |
| MaxResults | Any  # complex shape |  | The maximum number of data points to return. Valid range is 1 to 100,000. Use with NextToken for pagination of large res |
| MetricNames | Any  # complex shape | ✓ | The names of the metrics to retrieve. Maximum of 10 metrics per request. |
| NextToken | Any  # complex shape |  | The token for the next page of results. Use this value in a subsequent call to retrieve additional data points. |
| Period | Any  # complex shape | ✓ | The granularity, in seconds, of the returned data points. |
| StartTime | Any  # complex shape | ✓ | The start time for the metric data query, in ISO 8601 format. The time range (end time - start time) must be a multiple  |

## Output Shape: GetCapacityManagerMetricDataResult

- **MetricDataResults** (Any  # complex shape): The metric data points returned by the query. Each result contains dimension values, timestamp, and metric values with t
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_capacity_manager_metric_data(store, request: dict) -> dict:
    """Retrieves capacity usage metrics for your EC2 resources. Returns time-series data for metrics like unused capacity, utilization rates, and costs across On-Demand, Spot, and Capacity Reservations. Data"""
    end_time = request.get("EndTime", "").strip() if isinstance(request.get("EndTime"), str) else request.get("EndTime")
    if not end_time:
        raise ValidationException("EndTime is required")
    metric_names = request.get("MetricNames", "").strip() if isinstance(request.get("MetricNames"), str) else request.get("MetricNames")
    if not metric_names:
        raise ValidationException("MetricNames is required")
    period = request.get("Period", "").strip() if isinstance(request.get("Period"), str) else request.get("Period")
    if not period:
        raise ValidationException("Period is required")
    start_time = request.get("StartTime", "").strip() if isinstance(request.get("StartTime"), str) else request.get("StartTime")
    if not start_time:
        raise ValidationException("StartTime is required")

    resource = store.capacity_manager_metric_datas(metric_names)
    if not resource:
        raise ResourceNotFoundException(f"Resource metric_names not found")
    return {"MetricNames": metric_names, **resource}
```
