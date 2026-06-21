---
id: "@specs/aws/lightsail/get_container_service_metric_data"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetContainerServiceMetricData"
---

# GetContainerServiceMetricData

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_container_service_metric_data
> **spec:implements:** @kind:operation GetContainerServiceMetricData
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetContainerServiceMetricData.spec.md

Returns the data points of a specific metric of your Amazon Lightsail container service. Metrics report the utilization of your resources. Monitor and collect metric data regularly to maintain the reliability, availability, and performance of your resources.

## Input Shape: GetContainerServiceMetricDataRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| endTime | Any  # complex shape | ✓ | The end time of the time period. |
| metricName | Any  # complex shape | ✓ | The metric for which you want to return information. Valid container service metric names are listed below, along with t |
| period | Any  # complex shape | ✓ | The granularity, in seconds, of the returned data points. All container service metric data is available in 5-minute (30 |
| serviceName | Any  # complex shape | ✓ | The name of the container service for which to get metric data. |
| startTime | Any  # complex shape | ✓ | The start time of the time period. |
| statistics | list[Any  # complex shape] | ✓ | The statistic for the metric. The following statistics are available: Minimum - The lowest value observed during the spe |

## Output Shape: GetContainerServiceMetricDataResult

- **metricData** (list[Any  # complex shape]): An array of objects that describe the metric data returned.
- **metricName** (Any  # complex shape): The name of the metric returned.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_container_service_metric_data(store, request: dict) -> dict:
    """Returns the data points of a specific metric of your Amazon Lightsail container service. Metrics report the utilization of your resources. Monitor and collect metric data regularly to maintain the rel"""
    end_time = request.get("endTime", "").strip() if isinstance(request.get("endTime"), str) else request.get("endTime")
    if not end_time:
        raise ValidationException("endTime is required")
    metric_name = request.get("metricName", "").strip() if isinstance(request.get("metricName"), str) else request.get("metricName")
    if not metric_name:
        raise ValidationException("metricName is required")
    period = request.get("period", "").strip() if isinstance(request.get("period"), str) else request.get("period")
    if not period:
        raise ValidationException("period is required")
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")
    start_time = request.get("startTime", "").strip() if isinstance(request.get("startTime"), str) else request.get("startTime")
    if not start_time:
        raise ValidationException("startTime is required")
    statistics = request.get("statistics", "").strip() if isinstance(request.get("statistics"), str) else request.get("statistics")
    if not statistics:
        raise ValidationException("statistics is required")

    resource = store.container_service_metric_datas(metric_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource metric_name not found")
    return {"metricName": metric_name, **resource}
```
