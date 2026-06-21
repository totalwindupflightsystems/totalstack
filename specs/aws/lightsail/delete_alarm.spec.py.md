---
id: "@specs/aws/lightsail/delete_alarm"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteAlarm"
---

# DeleteAlarm

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_alarm
> **spec:implements:** @kind:operation DeleteAlarm
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteAlarm.spec.md

Deletes an alarm. An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see Alarms in Amazon Lightsail .

## Input Shape: DeleteAlarmRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| alarmName | Any  # complex shape | ✓ | The name of the alarm to delete. |

## Output Shape: DeleteAlarmResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def delete_alarm(store, request: dict) -> dict:
    """Deletes an alarm. An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on """
    alarm_name = request.get("alarmName", "").strip() if isinstance(request.get("alarmName"), str) else request.get("alarmName")

    if not store.alarms(alarm_name):
        raise ResourceNotFoundException(f"Resource alarm_name not found")
    store.delete_alarms(alarm_name)
    return {}
```
