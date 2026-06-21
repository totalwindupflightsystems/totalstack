---
id: "@specs/aws/lightsail/put_alarm"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_PutAlarm"
---

# PutAlarm

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/put_alarm
> **spec:implements:** @kind:operation PutAlarm
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_PutAlarm.spec.md

Creates or updates an alarm, and associates it with the specified metric. An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see Alarms in Amazon Lightsail . When this action creates an alarm, the alarm state is immediately set to INSUFFICIENT_DATA . The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed. When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm. The alarm is then evaluated with the updated configuration.

## Input Shape: PutAlarmRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| alarmName | Any  # complex shape | ✓ | The name for the alarm. Specify the name of an existing alarm to update, and overwrite the previous configuration of the |
| comparisonOperator | Any  # complex shape | ✓ | The arithmetic operation to use when comparing the specified statistic to the threshold. The specified statistic value i |
| contactProtocols | list[Any  # complex shape] |  | The contact protocols to use for the alarm, such as Email , SMS (text messaging), or both. A notification is sent via th |
| datapointsToAlarm | Any  # complex shape |  | The number of data points that must be not within the specified threshold to trigger the alarm. If you are setting an "M |
| evaluationPeriods | Any  # complex shape | ✓ | The number of most recent periods over which data is compared to the specified threshold. If you are setting an "M out o |
| metricName | Any  # complex shape | ✓ | The name of the metric to associate with the alarm. You can configure up to two alarms per metric. The following metrics |
| monitoredResourceName | Any  # complex shape | ✓ | The name of the Lightsail resource that will be monitored. Instances, load balancers, and relational databases are the o |
| notificationEnabled | Any  # complex shape |  | Indicates whether the alarm is enabled. Notifications are enabled by default if you don't specify this parameter. |
| notificationTriggers | list[Any  # complex shape] |  | The alarm states that trigger a notification. An alarm has the following possible states: ALARM - The metric is outside  |
| threshold | Any  # complex shape | ✓ | The value against which the specified statistic is compared. |
| treatMissingData | Any  # complex shape |  | Sets how this alarm will handle missing data points. An alarm can treat missing data in the following ways: breaching -  |

## Output Shape: PutAlarmResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
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
        raise ResourceInUseException(f"Resource metric_name already exists")

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
```
