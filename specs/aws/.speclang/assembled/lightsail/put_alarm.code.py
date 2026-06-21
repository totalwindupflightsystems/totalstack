# spec:trace: aws/lightsail/put_alarm.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/put-alarm
# spec:generated: DO NOT EDIT — edit the spec instead

def put_alarm(store, request: dict) -> dict:
    """Creates or updates an alarm, and associates it with the specified metric. An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify yo"""
    alarm_name = request.get("alarmName", "").strip() if isinstance(request.get("alarmName"), str) else request.get("alarmName")
    if not alarm_name:
        raise ValidationException("alarmName is required")
    comparison_operator = request.get("comparisonOperator", "").strip() if isinstance(request.get("comparisonOperator"), str) else request.get("comparisonOperator")
    if not comparison_operator:
        raise ValidationException("comparisonOperator is required")
    evaluation_periods = request.get("evaluationPeriods", "").strip() if isinstance(request.get("evaluationPeriods"), str) else request.get("evaluationPeriods")
    if not evaluation_periods:
        raise ValidationException("evaluationPeriods is required")
    metric_name = request.get("metricName", "").strip() if isinstance(request.get("metricName"), str) else request.get("metricName")
    if not metric_name:
        raise ValidationException("metricName is required")
    monitored_resource_name = request.get("monitoredResourceName", "").strip() if isinstance(request.get("monitoredResourceName"), str) else request.get("monitoredResourceName")
    if not monitored_resource_name:
        raise ValidationException("monitoredResourceName is required")
    threshold = request.get("threshold", "").strip() if isinstance(request.get("threshold"), str) else request.get("threshold")
    if not threshold:
        raise ValidationException("threshold is required")

    if store.alarms(metric_name):
        raise ResourceInUseException("Resource metric_name already exists")

    record = {
        "alarmName": alarm_name,
        "metricName": metric_name,
        "monitoredResourceName": monitored_resource_name,
        "comparisonOperator": comparison_operator,
        "threshold": threshold,
        "evaluationPeriods": evaluation_periods,
        "datapointsToAlarm": datapoints_to_alarm,
        "treatMissingData": treat_missing_data,
        "contactProtocols": contact_protocols,
        "notificationTriggers": notification_triggers,
        "notificationEnabled": notification_enabled,
    }

    store.alarms(metric_name, record)

    return {
        "operations": record.get("operations", {}),
    }

