---
id: "@specs/aws/lightsail/get_bucket_metric_data"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetBucketMetricData"
---

# GetBucketMetricData

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_bucket_metric_data
> **spec:implements:** @kind:operation GetBucketMetricData
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetBucketMetricData.spec.md

Returns the data points of a specific metric for an Amazon Lightsail bucket. Metrics report the utilization of a bucket. View and collect metric data regularly to monitor the number of objects stored in a bucket (including object versions) and the storage space used by those objects.

## Input Shape: GetBucketMetricDataRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| bucketName | Any  # complex shape | ✓ | The name of the bucket for which to get metric data. |
| endTime | Any  # complex shape | ✓ | The timestamp indicating the latest data to be returned. |
| metricName | Any  # complex shape | ✓ | The metric for which you want to return information. Valid bucket metric names are listed below, along with the most use |
| period | Any  # complex shape | ✓ | The granularity, in seconds, of the returned data points. Bucket storage metrics are reported once per day. Therefore, y |
| startTime | Any  # complex shape | ✓ | The timestamp indicating the earliest data to be returned. |
| statistics | list[Any  # complex shape] | ✓ | The statistic for the metric. The following statistics are available: Minimum - The lowest value observed during the spe |
| unit | Any  # complex shape | ✓ | The unit for the metric data request. Valid units depend on the metric data being requested. For the valid units with ea |

## Output Shape: GetBucketMetricDataResult

- **metricData** (list[Any  # complex shape]): An array of objects that describe the metric data returned.
- **metricName** (Any  # complex shape): The name of the metric returned.

## Errors
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **ServiceException**: A general service exception.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_bucket_metric_data(store, request: dict) -> dict:
    """Returns the data points of a specific metric for an Amazon Lightsail bucket. Metrics report the utilization of a bucket. View and collect metric data regularly to monitor the number of objects stored """
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")
    end_time = request.get("endTime", "").strip() if isinstance(request.get("endTime"), str) else request.get("endTime")
    if not end_time:
        raise ValidationException("endTime is required")
    metric_name = request.get("metricName", "").strip() if isinstance(request.get("metricName"), str) else request.get("metricName")
    if not metric_name:
        raise ValidationException("metricName is required")
    period = request.get("period", "").strip() if isinstance(request.get("period"), str) else request.get("period")
    if not period:
        raise ValidationException("period is required")
    start_time = request.get("startTime", "").strip() if isinstance(request.get("startTime"), str) else request.get("startTime")
    if not start_time:
        raise ValidationException("startTime is required")
    statistics = request.get("statistics", "").strip() if isinstance(request.get("statistics"), str) else request.get("statistics")
    if not statistics:
        raise ValidationException("statistics is required")
    unit = request.get("unit", "").strip() if isinstance(request.get("unit"), str) else request.get("unit")
    if not unit:
        raise ValidationException("unit is required")

    resource = store.bucket_metric_datas(metric_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource metric_name not found")
    return {"metricName": metric_name, **resource}
```
