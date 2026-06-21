# spec:trace: aws/lightsail/get_container_service_metric_data.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-container-service-metric-data
# spec:generated: DO NOT EDIT — edit the spec instead

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
        raise ResourceNotFoundException("Resource metric_name not found")
    return {"metricName": metric_name, **resource}

